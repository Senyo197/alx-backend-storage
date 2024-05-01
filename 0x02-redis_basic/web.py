#!/usr/bin/env python3
"""
Allows caching HTTP responses to Redis.

This module provides a decorator `cache_response` that caches the output of
fetched HTTP responses to Redis. It also includes a function `get_page` which
makes HTTP GET requests to the provided URL and returns the response text.
"""

import redis
import requests
from functools import wraps
from typing import Callable


# Initialize Redis connection
redis_store = redis.Redis()


def cache_response(method: Callable) -> Callable:
    """
    Decorator to cache the output of fetched data.

    This decorator caches the output of the provided method
    (which typically fetches data) to Redis for subsequent requests to the
    same URL.

    Args:
        method (Callable): The method to be decorated.

    Returns:
        Callable: The decorated method.
    """
    @wraps(method)
    def invoker(url: str) -> str:
        """
        Wrapper function for caching the output.

        This function first checks if the response for the given URL is already
        cached in Redis. If it is, it returns the cached response.
        Otherwise, it fetches the response using the provided method and
        caches it in Redis for 10 seconds.

        Args:
            url (str): The URL to fetch the data from.

        Returns:
            str: The response text.
        """
        # Increment the count of requests made to this URL
        redis_store.incr(f'count:{url}')

        # Check if the response for this URL is cached
        result = redis_store.get(f'result:{url}')
        if result:
            return result.decode('utf-8')

        # If not cached, fetch the response using the provided method
        result = method(url)

        # Cache the response for 10 seconds
        redis_store.setex(f'result:{url}', 10, result)

        return result
    return invoker


@cache_response
def get_page(url: str) -> str:
    """
    Fetches the response from the specified URL and returns it.

    Args:
        url (str): The URL to fetch the response from.

    Returns:
        str: The response text.
    """
    return requests.get(url).text

#!/usr/bin/env python3
"""Change school topics"""


def update_topics(mongo_collection, name, topics):
    """Python function that changes all topics of a school document based on
    the name
    """
    schools_to_update = {'name': name}
    new_values = {'$set': {'topics': topics}}
    mongo_collection.update_many(
        schools_to_update,
        new_values
    )

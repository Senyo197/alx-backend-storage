#!/usr/bin/env python3
"""
8. List all documents in Python
"""


def list_all(mongo_collection):
    """Python function that lists all documents in a collection"""
    col_documents = mongo_collection.find({})
    return col_documents

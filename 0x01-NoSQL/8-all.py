#!/usr/bin/env python3
"""
Defines a function list_all
"""

from pymongo import MongoClient


def list_all(mongo_collection):
    """
    lists all documents in a collection
    """
    return list(mongo_collection.find())

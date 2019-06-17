import ssl

from pymongo import MongoClient, DESCENDING, ReturnDocument

import json
import sys

from configuration.config import *


class MongoClients:
    """NoodleMongoClient."""

    def __init__(self):
        """Init.

        method is run as soon as an object of a class is instantiated.
        The method is useful to do any initialization you want to do
        with your object
        """
        self.client = MongoClient(MONGO_URL,  ssl_cert_reqs=ssl.CERT_NONE)
        self.database = self.client[DB_NAME]
        self.error=None

    def find_one(self, collectionname, data):
        """Find One."""
        return self.database[collectionname].find_one(data)

    def insert_one(self, collectionname, data):
        """Insert One."""
        try:
            data = json.loads(data)
        except ValueError as err:
            message = err.args[0] + ' - ERROR IN - ' + collectionname
            sys.exit(message)
        return self.database[collectionname].insert_one(
            data)

    def find_all(self, db_name, collection_name, query={}, sort_field="_id",
                 sort_order=DESCENDING):
        db = self.client[db_name]

        if db is None:
            raise ConnectionError(self.error)

        results = []
        db_results = db[collection_name].find(query).sort(sort_field, sort_order)
        results_count = db_results.count()
        for result in db_results:
            results.append(result)
        self.client.close()
        return results, results_count

    def find(self, db_name, collection_name, query={}, offset=0, limit=1, sort_field="_id"):
        db = self.client[db_name]

        if db is None:
            raise ConnectionError(self.error)

        results = []
        db_results = db[collection_name].find(query).sort(sort_field, DESCENDING).skip(int(offset)).limit(int(limit))
        results_count = db_results.count()
        for result in db_results:
            results.append(result)
        self.client.close()
        return results, results_count

    def find_one_and_delete(self, db_name, collection_name, query):
        db = self.client[db_name]
        if db is None:
            raise ConnectionError(self.error)
        return db[collection_name].find_one_and_delete(query, projection={'_id': False})

    def find_one_and_update(self, db_name, collection_name, query, update):
        db = self.client[db_name]
        if db is None:
            raise ConnectionError(self.error)
        return db[collection_name].find_one_and_update(query, update, return_document=ReturnDocument.AFTER)

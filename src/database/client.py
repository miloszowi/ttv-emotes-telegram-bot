from typing import Iterable
from urllib.parse import quote_plus

from config.credentials import (MONGODB_DATABASE, MONGODB_HOSTNAME,
                                MONGODB_PASSWORD, MONGODB_PORT,
                                MONGODB_USERNAME)
from pymongo import MongoClient
from pymongo.database import Database


class Client():
    mongoClient: MongoClient
    database: Database

    def __init__(self) -> None:
        uri = "mongodb://%s:%s@%s:%s/%s?authSource=admin" % (
            MONGODB_USERNAME, quote_plus(MONGODB_PASSWORD),
            MONGODB_HOSTNAME, MONGODB_PORT, MONGODB_DATABASE
        )

        self.mongoClient = MongoClient(uri)
        self.database = self.mongoClient[MONGODB_DATABASE]

    def findMany(self, collection: str, filter: dict) -> dict:
        return self.database.get_collection(collection).find(filter)

    def insertMany(self, collection: str, data: Iterable[dict]) -> None:
        self.database.get_collection(collection).insert_many(data)
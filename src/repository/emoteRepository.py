from typing import Iterable
from database.client import Client
from entity.emote import Emote

class EmoteRepository():
    databaseClient: Client

    def __init__(self) -> None:
        self.databaseClient = Client()

    def searchByCode(self, code: str) -> Iterable[Emote]:
        search = self.databaseClient.findMany(
            Emote.collection,
            { Emote.codeIndex: {'$regex' : code} }
        )

        return [Emote.fromMongoDocument(item) for item in search]

    def insertMany(self, mongoData: dict) -> None:
        self.databaseClient.insertMany(Emote.collection, mongoData)

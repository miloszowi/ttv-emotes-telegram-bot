from typing import Iterable
from database.client import Client
from entity.emote import Emote

class EmoteRepository():
    client: Client

    def __init__(self) -> None:
        self.client = Client()

    def getManyByCode(self, code: str) -> Iterable[Emote]:
        result = []
        search = self.client.findMany(Emote.collection, {Emote.codeIndex: code})

        for item in search[:4]:
            result.append(Emote.fromMongoDocument(item))

        return result

    def insertMany(self, mongoData: dict) -> None:
        self.client.insertMany(Emote.collection, mongoData)

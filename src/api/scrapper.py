import os.path
import sys

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))
)

from repository.emoteRepository import EmoteRepository
import requests
from entity.emote import Emote


class Scrapper():
    emoteRepository: EmoteRepository

    def __init__(self) -> None:
        self.emoteRepository = EmoteRepository()

    def process(self):
        for i in range (0, 10000, 50):
            self.scrape(i, 50)

    def scrape(self, offset: int, limit: int) -> None:
        url = 'https://api.betterttv.net/3/emotes/shared/top?offset={}&limit={}'.format(offset, limit)
        response = requests.get(url).json()

        insert = []
        for emote in response:
            emoteData = emote['emote']
            
            insert.append({
                Emote.ttvIdIndex: emoteData["id"],
                Emote.codeIndex: emoteData["code"].lower(),
                Emote.typeIndex: emoteData['imageType']
            })

        self.emoteRepository.insertMany(insert)

scrapper = Scrapper()

scrapper.process()

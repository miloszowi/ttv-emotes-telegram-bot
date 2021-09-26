from __future__ import annotations


class Emote():
    ttvId: str
    code: str
    type: str

    collection: str = 'emotes'

    ttvIdIndex: str = 'ttv_id'
    codeIndex: str = 'code'
    typeIndex: str = 'type' 

    sourceInterpolationString: str = 'https://cdn.betterttv.net/emote/{}/3x'

    def __init__(self, ttvId: str, code: str, type: str) -> None:
        self.ttvId = ttvId
        self.code = code
        self.type = type

    def getTtvId(self) -> str:
        return self.ttvId    

    def getCode(self) -> str:
        return self.code

    def getType(self) -> str:
        return self.type

    def getSource(self) -> str:
        return self.sourceInterpolationString.format(self.getTtvId())

    @staticmethod
    def fromMongoDocument(mongoDocument: dict) -> Emote:
        return Emote(
            mongoDocument[Emote.ttvIdIndex],
            mongoDocument[Emote.codeIndex],
            mongoDocument[Emote.typeIndex]
        )

from typing import Optional
import uuid
from logging import raiseExceptions

from telegram.inline.inlinequeryresult import InlineQueryResult

from entity.emote import Emote
from repository.emoteRepository import EmoteRepository
from telegram import InlineQueryResultGif, InlineQueryResultPhoto
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.inlinequeryhandler import InlineQueryHandler
from telegram.update import Update

from handler.abstractHandler import AbstractHandler


class EmoteInlineQueryHandler(AbstractHandler):
    botHandler: InlineQueryHandler
    emoteRepository: Emote

    def __init__(self) -> None:
        self.botHandler = InlineQueryHandler(self.handle)
        self.emoteRepository = EmoteRepository()

    def handle(self, update: Update, context: CallbackContext) -> None:
        emotes = self.emoteRepository.getManyByCode(update.inline_query.query.lower())

        possibleEmotes = []
        for idx, emote in enumerate(emotes):
            possibleEmotes.append(
                self.resolveEmote(emote, idx)
            )
        
        update.inline_query.answer(possibleEmotes, cache_time=5)

    def getBotHandler(self) -> InlineQueryHandler:
        return self.botHandler

    def resolveEmote(self, emote: Emote, idx: int) -> Optional[InlineQueryResult]:
        emoteUrl = f'https://cdn.betterttv.net/emote/{emote.getTtvId()}/3x'

        scenarios = {
            'gif' : InlineQueryResultGif(id=idx, gif_url=emoteUrl, thumb_url=emoteUrl),
            'png' : InlineQueryResultPhoto(id=idx, photo_url=emoteUrl, thumb_url=emoteUrl)
        }
        return scenarios.get(emote.getType(), None)
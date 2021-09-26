import logging
from typing import Optional
from uuid import uuid4

from entity.emote import Emote
from repository.emoteRepository import EmoteRepository
from telegram import InlineQueryResultGif, InlineQueryResultPhoto
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.inlinequeryhandler import InlineQueryHandler
from telegram.inline.inlinequeryresult import InlineQueryResult
from telegram.update import Update

from handler.abstractHandler import AbstractHandler


class EmoteInlineQueryHandler(AbstractHandler):
    botHandler: InlineQueryHandler
    emoteRepository: Emote
    logger: logging.Logger

    def __init__(self) -> None:
        self.botHandler = InlineQueryHandler(self.handle)
        self.emoteRepository = EmoteRepository()

    def handle(self, update: Update, context: CallbackContext) -> None:
        emotes = self.emoteRepository.searchByCode(update.inline_query.query.lower())

        update.inline_query.answer(
            [self.resolveEmote(emote) for emote in emotes],
            cache_time = 10
        )

    def getBotHandler(self) -> InlineQueryHandler:
        return self.botHandler

    def resolveEmote(self, emote: Emote) -> Optional[InlineQueryResult]:
        emoteUrl = emote.getSource()
        emoteTempId = uuid4()

        scenarios = {
            'gif' : InlineQueryResultGif(emoteTempId, emoteUrl, emoteUrl),
            'png' : InlineQueryResultPhoto(emoteTempId, emoteUrl, emoteUrl)
        }

        return scenarios.get(emote.getType(), None)

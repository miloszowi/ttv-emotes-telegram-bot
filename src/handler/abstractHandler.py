from abc import abstractmethod

from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.handler import Handler
from telegram.update import Update


class AbstractHandler: 
    def __init__(self) -> None:
        pass

    @abstractmethod
    def getBotHandler(self) -> Handler: raise Exception('getBotHandler method is not implemented')

    @abstractmethod
    def handle(self, update: Update, context: CallbackContext) -> None: raise Exception('handle method is not implemented')

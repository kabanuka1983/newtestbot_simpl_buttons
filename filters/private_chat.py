from aiogram import types
from aiogram.dispatcher.filters import BoundFilter
from aiogram.types import Message


class IsPrivate(BoundFilter):
    async def check(self, message: Message):
        return message.chat.type == types.ChatType.PRIVATE

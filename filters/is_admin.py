from aiogram.dispatcher.filters import BoundFilter
from aiogram import types

from SQL import get_bot_admins


class IsAdmin(BoundFilter):

    async def check(self, message: types.Message):
        res = message.from_user.id in get_bot_admins()
        # print(res)
        return res

from aiogram import types

from filters import IsAdmin
from loader import dp
from SQL import get_bot_password
from SQL import add_new_admin


@dp.message_handler(text=[get_bot_password()], state='*')
async def auth(message: types.Message):
    await message.answer('Добавляем в администраторы')
    res = add_new_admin(username=message.from_user.username, user_id=message.from_user.id)
    if res is not None:
        await message.answer(res)

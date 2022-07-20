from pprint import pprint
from aiogram.dispatcher import FSMContext
from loader import dp, bot
from data.config import admins
from aiogram.types import ContentType, Message
from SQL.new_skillbox_chat import add_new_skillbox_chat
from states import Admin_state


@dp.message_handler(content_types=[ContentType.NEW_CHAT_MEMBERS], state='*')
async def new_members_handler(message: Message, state: FSMContext):
    bot_id = (await bot.get_me()).id
    new_member = message.new_chat_members[0]
    if new_member.id == bot_id:
        if message.from_user.id in admins:
            await add_new_skillbox_chat(chat_id=message.chat.id, name=message.chat.title)
        else:
            await message.answer('Меня добавил не админ, всем пока')
            await bot.leave_chat(message.chat.id)
    else:
        if not new_member.is_bot:
            await message.answer(f"Добро пожаловать, {new_member.mention}")
            await message.answer(await bot.get_chat_members_count(message.chat.id))
        else:
            await message.answer('Кляти бот')

# @dp.message.handler(content_type=['left_chat_member'])
# async def left_member(message: Message):
#      await message.answer('Куда пошел!?')
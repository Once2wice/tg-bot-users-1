from filters import IsAdmin
from keyboards.inline.password import inline_password
from keyboards.inline.filters_admin_comands import yes_no_callback
from aiogram.dispatcher import FSMContext
from aiogram import types
from loader import dp
from states import Admin_state
from SQL import set_bot_password


@dp.callback_query_handler(IsAdmin(), yes_no_callback.filter(answer='Password'), state='*')
async def password(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer('Введите новый пароль', reply_markup=inline_password)
    await Admin_state.password.set()


@dp.message_handler(IsAdmin(), state=Admin_state.password)
async def password(mes: types.Message, state: FSMContext):
    print('Новый пароль', mes.text)
    set_bot_password(mes.text)
    await state.finish()
    await mes.answer('Пароль изменен')


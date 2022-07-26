from aiogram.dispatcher import FSMContext
from keyboards.inline.start_panel import inline_start_panel
from keyboards.inline.filters_admin_comands import yes_no_callback
from filters import IsAdmin
from aiogram import types
from loader import dp


@dp.message_handler(IsAdmin(), commands=['start'], state='*')
async def start_panel(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer('Добро пожаловать, товарищь ГЕНЕРАЛ!\nПанель управление администраторами',
                         reply_markup=inline_start_panel)


@dp.callback_query_handler(IsAdmin(), yes_no_callback.filter(answer='StartPanel'), state='*')
async def start_panel(call: types.CallbackQuery, state: FSMContext):
    await call.message.delete()
    await state.finish()
    await call.message.answer('Панель управление администраторами', reply_markup=inline_start_panel)

from aiogram.dispatcher import FSMContext

from filters import IsAdmin
from keyboards.inline.admin_panel import inline_admin_panel
from keyboards.inline.filters_admin_comands import yes_no_callback
from keyboards.inline.del_admin_panel import inline_dell_admin_panel
from aiogram import types
from loader import dp
from SQL import get_bot_admins, del_admin
from states import Admin_state


@dp.callback_query_handler(IsAdmin(), yes_no_callback.filter(answer='AdminPanel'), state='*')
async def admin_panel(call: types.CallbackQuery, state: FSMContext):
    await call.message.delete()
    await state.reset_data()
    await call.message.answer('Панель управление администраторами', reply_markup=inline_admin_panel)


@dp.callback_query_handler(IsAdmin(), yes_no_callback.filter(answer='ListAdmin'), state='*')
async def admin_panel(call: types.CallbackQuery, state: FSMContext):
    await call.answer()
    result = get_bot_admins(full=True)
    new_string = ''
    for count_users, element in enumerate(result):
        new_string += f"{count_users + 1}. {' - '.join(map(str, element))}\n"
    await call.message.answer(new_string)


@dp.callback_query_handler(IsAdmin(), yes_no_callback.filter(answer='DelAdmin'), state='*')
async def admin_panel(call: types.CallbackQuery, state: FSMContext):
    await Admin_state.del_admin.set()
    await call.message.delete()
    await call.message.answer('Кого вы хотите удалить?', reply_markup=inline_dell_admin_panel)


@dp.callback_query_handler(IsAdmin(), state=Admin_state.del_admin)
async def admin_panel(call: types.CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.delete()
    del_admin(call.data.split(":")[1])
    await call.message.answer('Админ удален')

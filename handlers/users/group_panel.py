from filters import IsAdmin
from keyboards.inline.group_panel import inline_group_panel
from keyboards.inline.get_list_user_group import inline_list_user_group
from keyboards.inline.filters_admin_comands import yes_no_callback
from aiogram import types
from loader import dp
from SQL import get_list_user_group, set_moderator_chat
from states import Admin_state
from aiogram.dispatcher import FSMContext

list_buttom = [
    ('Список user_group', 'UserGroup'),
    ('Список moder_group', 'ModerGroup'),
    ('Дать права группе', 'setModerGroup'),
    ('Снять права с группы', 'delModerGroup'),
    ('Настроить призовые места', 'setGrad'),
    ('Назад', 'StartPanel')
]


@dp.callback_query_handler(IsAdmin(), yes_no_callback.filter(answer='GroupPanel'), state='*')
async def group_panel(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer('Панель управление группами', reply_markup=inline_group_panel)


@dp.callback_query_handler(IsAdmin(), yes_no_callback.filter(answer='UserGroup'), state='*')
async def group_panel(call: types.CallbackQuery):
    await call.message.delete()
    result = get_list_user_group()
    if not result:
        await call.message.answer('Групп нет')
    else:
        new_string = ''
        for count_users, element in enumerate(result):
            new_string += f"{count_users + 1}.\nНазвание канала: {element[1]}\nid канала: {element[2]}\n"
        await call.message.answer(new_string)


@dp.callback_query_handler(IsAdmin(), yes_no_callback.filter(answer='ModerGroup'), state='*')
async def group_panel(call: types.CallbackQuery):
    await call.message.delete()
    result = get_list_user_group(moder=True)
    if not result:
        await call.message.answer('Групп нет')
    else:
        new_string = ''
        for count_users, element in enumerate(result):
            new_string += f"{count_users + 1}.\nНазвание канала: {element[1]}\nid канала: {element[2]}\n"
        await call.message.answer(new_string)


@dp.callback_query_handler(IsAdmin(), yes_no_callback.filter(answer='setModerGroup'), state='*')
async def group_panel(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer('Выберите группу кто будет следить', reply_markup=inline_list_user_group)
    await Admin_state.group.set()


@dp.callback_query_handler(IsAdmin(), state=Admin_state.group)
async def group_panel(call: types.CallbackQuery, state: FSMContext):
    await state.update_data(first=call.data.split(":")[1])
    await call.message.delete()
    await call.message.answer('Выберите группу за кем будут следить', reply_markup=inline_list_user_group)
    await Admin_state.group2.set()

@dp.callback_query_handler(IsAdmin(), state=Admin_state.group2)
async def group_panel(call: types.CallbackQuery, state: FSMContext):
    first = (await state.get_data()).get("first")
    lost = call.data.split(":")[1]
    set_moderator_chat(first, lost)
    await call.message.delete()
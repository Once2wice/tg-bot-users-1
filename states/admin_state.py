from aiogram.dispatcher.filters.state import StatesGroup, State


class Admin_state(StatesGroup):
    add_admin = State()
    del_admin = State()
    password = State()
    group = State()
    group2 = State()

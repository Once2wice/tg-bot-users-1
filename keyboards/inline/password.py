from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from keyboards.inline.filters_admin_comands import yes_no_callback

list_buttom = [
    ('Назад', 'AdminPanel')
]

res_list_buttom = []
for x, y in list_buttom:
    line = []
    buttom = InlineKeyboardButton(text=x, callback_data=yes_no_callback.new(answer=y))
    line.append(buttom)
    res_list_buttom.append(line)

inline_password = InlineKeyboardMarkup(row_width=1, inline_keyboard=res_list_buttom)



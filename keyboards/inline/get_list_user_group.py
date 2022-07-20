from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from keyboards.inline.filters_admin_comands import yes_no_callback
from SQL import get_list_user_group

list_buttom = get_list_user_group()
list_buttom = [(x[1], x[2]) for x in list_buttom]
list_buttom.append(('Отмена', 'StartPanel'))

res_list_buttom = []
for x, y in list_buttom:
    line = []
    buttom = InlineKeyboardButton(text=x, callback_data=yes_no_callback.new(answer=y))
    line.append(buttom)
    res_list_buttom.append(line)

inline_list_user_group = InlineKeyboardMarkup(row_width=1, inline_keyboard=res_list_buttom)

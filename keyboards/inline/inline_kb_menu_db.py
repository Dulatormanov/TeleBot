from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup
from  aiogram.utils.callback_data import CallbackData

products_cb = CallbackData('product', 'id', 'action')

def get_start_ikb() -> InlineKeyboardMarkup:
    ikb = InlineKeyboardMarkup(inline_keyboard==[
        [
            InlineKeyboardButton('Просмотр всех продуктов', callback_data=products_cb.new(action='get_all'))
        ],
        [
            InlineKeyboardButton('Добавить новый продукт', callback_data=products_cb.new(action='add'))
        ]
    ])
    return ikb
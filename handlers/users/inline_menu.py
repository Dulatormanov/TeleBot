from handlers.loader import dp
from aiogram import types
from aiogram.types import CallbackQuery
from keyboards.default import kb_test
from keyboards.inline.inline_kb_menu import ikb_menu
from keyboards.inline.inline_kb_menu2 import ikb_menu2
@dp.message_handler(text='Инлаин меню')
async def show_line_menu(message: types.Message):
    await message.answer('Инлаин кнопки ниже', reply_markup=ikb_menu)

@dp.callback_query_handler(text='Сообщение')
async def send_message(call: CallbackQuery):
    await call.message.answer('Кнопки заменены', reply_markup=kb_test)

@dp.callback_query_handler(text='alert')
async def send_message(call: CallbackQuery):
    await call.answer('Кнопки заменены', show_alert=True)

@dp.callback_query_handler(text='Кнопки2')
async def send_message(call: CallbackQuery):
    await call.message.edit_reply_markup(ikb_menu2)
 #  await call.message.answer('Инлаин Кнопки заменены', reply_markup=ikb_menu2)


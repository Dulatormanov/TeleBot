from aiogram import types
from handlers.loader import dp
@dp.message_handler(text='/start')
async def command_start(message: types.Message):
    await message.answer(f'Привет {message.from_user.full_name})! \n'
                         f'Твои айди: {message.from_user.id}')

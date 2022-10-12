from aiogram.dispatcher import FSMContext

from handlers.loader import dp
from aiogram.dispatcher.filters import Command
from aiogram import types
from states import register


@dp.message_handler(Command('register')) #/register
async def register_(message: types.Message):
    await message.answer('Привет ты начал регистрацию,\nВведи свое имя')
    await register.test1.set()

@dp.message_handler(state=register.test1)
async def state1(message: types.Message, state : FSMContext):
    answer = message.text

    await state.update_data(test1=answer)
    await message.answer('Сколько тебе лет?')
    await register.test2.set()


@dp.message_handler(state=register.test2)
async def state1(message: types.Message, state: FSMContext):
    answer = message.text

    await state.update_data(test2=answer)
    data = await state.get_data()
    # name = await state.get_data()
    # years = await state.get_data()
    name = data.get('test1')
    years = data.get('test2')


    await message.answer(f'Регистрация успещно заверщена\n'
                         f'Твое имя -  {name}\n'
                         f'Тебе - {years} лет')
    await state.finish()



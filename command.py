from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

import keyboard.creat_kb as kb
import text
from config import TOKEN_API
from db.db import search_id_user

bot = Bot(TOKEN_API)
dp = Dispatcher(bot, storage=MemoryStorage())


@dp.message_handler(commands=['start'])
async def command_start(message: types.Message):
    await message.answer(text=text.START, parse_mode='HTML')
    if search_id_user(message.from_user.id) == 0:
        await message.answer(text=text.START2, reply_markup=kb.start())
    else:
        await message.answer(text=text.START3, reply_markup=kb.profile())
    await message.delete()

#
# @dp.message_handler(commands=['help'])
# async def command_help(message: types.Message):
#     await message.answer(HELP, parse_mode='HTML')
#     await message.delete()

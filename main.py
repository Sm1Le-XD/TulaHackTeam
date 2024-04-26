from random import choice
from time import time
from aiogram import types, aiogram
from aiogram.types import ReplyKeyboardRemove
from aiogram import Bot, Dispatcher, types
import fms.login, fms.create, fms.question
import db.db
from config import TOKEN_API
import yagpt.gpt
from yagpt.gpt import epi
from command import dp
from db.db import db_start, db_deader

async def on_startup(_):
    print("HI, i work")

if __name__ == '__main__':
    print('hello world')
    db_deader()

    executor.start_polling(dp, on_startup=on_startup, skip_updates=True)

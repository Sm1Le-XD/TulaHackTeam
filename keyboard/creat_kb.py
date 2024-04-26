from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def start() -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup(resize_keyboard=True, row_width=2)
    button = InlineKeyboardButton("Авторизоваться", callback_data="start")
    keyboard.add(button)
    return keyboard

def ret_login_kb() -> InlineKeyboardMarkup:
    kb = InlineKeyboardMarkup(resize_keyboard=True, row_width=2)
    button = InlineKeyboardButton("Отмена", callback_data="ret_login")
    kb.add(button)
    return kb


def q_kb() -> InlineKeyboardMarkup:
    kb = InlineKeyboardMarkup(resize_keyboard=True, row_width=2)
    button = InlineKeyboardButton("Вопрос", callback_data="question")
    kb.add(button)
    return kb


def ret_prof_kb() -> InlineKeyboardMarkup:
    kb = InlineKeyboardMarkup(resize_keyboard=True, row_width=2)
    button = InlineKeyboardButton("Отмена", callback_data="ret_prof")
    kb.add(button)
    return kb


def question() -> InlineKeyboardMarkup:
    kb = InlineKeyboardMarkup(resize_keyboard=True, row_width=2)
    button1 = InlineKeyboardButton("Следующий вопрос", callback_data="next_q")
    button2 = InlineKeyboardButton("Предыдущий вопрос", callback_data="prev_q")
    kb.add(button2, button1)
    return kb


def question_2() -> InlineKeyboardMarkup:
    kb = InlineKeyboardMarkup(resize_keyboard=True, row_width=2)
    button1 = InlineKeyboardButton("Следующий вопрос", callback_data="next_q")
    button2 = InlineKeyboardButton("Предыдущий вопрос", callback_data="prev_q")
    button3 = InlineKeyboardButton("Закончить опрос", callback_data="finish_q")
    kb.add(button2, button1).add(button3)
    return kb

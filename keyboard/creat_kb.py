from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def start() -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup(resize_keyboard=True, row_width=2)
    button = InlineKeyboardButton("авторизоваться", callback_data="start")
    keyboard.add(button)
    return keyboard


def login_kb() -> InlineKeyboardMarkup:
    kb = InlineKeyboardMarkup(resize_keyboard=True, row_width=2)
    button = InlineKeyboardButton("email", callback_data="email")
    button1 = InlineKeyboardButton("phone", callback_data="phone")
    button2 = InlineKeyboardButton("password", callback_data="pass")
    kb.add(button).add(button1).add(button2)
    return kb


def ret_login_kb() -> InlineKeyboardMarkup:
    kb = InlineKeyboardMarkup(resize_keyboard=True, row_width=2)
    button = InlineKeyboardButton("cancel", callback_data="ret_login")
    kb.add(button)
    return kb


def q_kb() -> InlineKeyboardMarkup:
    kb = InlineKeyboardMarkup(resize_keyboard=True, row_width=2)
    button = InlineKeyboardButton("question", callback_data="question")
    kb.add(button)
    return kb


def epi_and_bio() -> InlineKeyboardMarkup:
    kb = InlineKeyboardMarkup(resize_keyboard=True, row_width=2)
    button = InlineKeyboardButton("epi", callback_data="epi")
    kb.add(button)
    button = InlineKeyboardButton("bio", callback_data="bio")
    kb.add(button)
    return kb


def epi() -> InlineKeyboardMarkup:
    kb = InlineKeyboardMarkup(resize_keyboard=True, row_width=2)
    button = InlineKeyboardButton("new epi", callback_data="epi")
    kb.add(button)
    button = InlineKeyboardButton("use tham", callback_data="epi_and_bio")
    kb.add(button)
    return kb


def bio() -> InlineKeyboardMarkup:
    kb = InlineKeyboardMarkup(resize_keyboard=True, row_width=2)
    button = InlineKeyboardButton("new bio", callback_data="bio")
    kb.add(button)
    button = InlineKeyboardButton("use tham", callback_data="epi_and_bio")
    kb.add(button)
    return kb


def ret_prof_kb() -> InlineKeyboardMarkup:
    kb = InlineKeyboardMarkup(resize_keyboard=True, row_width=2)
    button = InlineKeyboardButton("cancel", callback_data="ret_prof")
    kb.add(button)
    return kb


def profile() -> InlineKeyboardMarkup:
    kb = InlineKeyboardMarkup(resize_keyboard=True, row_width=2)
    button = InlineKeyboardButton("рандомная страничка", url="https://memorycode.ru/page/35984242")
    button1 = InlineKeyboardButton("Создать свою страничку", callback_data="profile")
    kb.add(button).add(button1)
    return kb


def creat_kb() -> InlineKeyboardMarkup:
    kb = InlineKeyboardMarkup(resize_keyboard=True, row_width=2)
    b1 = InlineKeyboardButton(text="имя", callback_data="name_cr")
    b2 = InlineKeyboardButton(text="фамилия", callback_data="surname_cr")
    b3 = InlineKeyboardButton(text="отчество", callback_data="fathname_cr")
    b4 = InlineKeyboardButton(text="дата рождения", callback_data="birth_cr")
    b5 = InlineKeyboardButton(text="дата смерти", callback_data="dead_cr")
    b6 = InlineKeyboardButton(text="фото", callback_data="photo_cr")
    button = InlineKeyboardButton("cancel", callback_data="ret_start")
    kb.add(b1).add(b2).add(b3).add(b4).add(b5).add(b6).add(button)
    return kb


def question() -> InlineKeyboardMarkup:
    kb = InlineKeyboardMarkup(resize_keyboard=True, row_width=2)
    button1 = InlineKeyboardButton("next", callback_data="next_q")
    button2 = InlineKeyboardButton("prev", callback_data="prev_q")
    kb.add(button2, button1)
    return kb


def question_2() -> InlineKeyboardMarkup:
    kb = InlineKeyboardMarkup(resize_keyboard=True, row_width=2)
    button1 = InlineKeyboardButton("next", callback_data="next_q")
    button2 = InlineKeyboardButton("prev", callback_data="prev_q")
    button3 = InlineKeyboardButton("finish", callback_data="finish_q")
    kb.add(button2, button1).add(button3)
    return kb

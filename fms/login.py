from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.types import InlineKeyboardButton

from command import dp
from db.db import add_user
from keyboard import creat_kb as kb

DATA = """
ВВЕДИТЕ Ваш email или телефон, а также пароль, по которым вы зарегестрированны на memmorycode
email        {}
Телефон      {}
Пароль       {}
"""
PAS = "********"


class LoginState(StatesGroup):
    phone = State()
    email = State()
    parow = State()
    wait = State()


async def update_keyboard(state: FSMContext):
    async with state.proxy() as data:
        p = data['phone']
        e = data['email']
        parow = data['parow']
        call = data['callback']
        if parow != "None" and (p != "None" or e != "None"):
            tt = kb.login_kb()
            tt.add(InlineKeyboardButton(text='все верно', callback_data="cr_pr_ok"))
            await call.message.edit_text(text="проверьте введенные данные и если все "
                                              "верно нажмите на соответсвующую кнопку \n\n" +
                                              DATA.format(e, p, PAS),
                                         reply_markup=tt)
        else:
            await call.message.edit_text(DATA.format(e, p, (PAS if parow != "None" else parow)),
                                         reply_markup=kb.login_kb())


@dp.callback_query_handler(text='start', state="*")
async def new_fr(call: types.CallbackQuery, state: FSMContext):
    await state.update_data(phone="None")
    await state.update_data(email="None")
    await state.update_data(parow="None")
    await state.update_data(callback=call)
    await update_keyboard(state)


@dp.callback_query_handler(text='email', state="*")
async def inl_new_fr_name(call: types.CallbackQuery, state: FSMContext):
    await call.message.edit_text("введите вашу почту", reply_markup=kb.ret_login_kb())
    await LoginState.email.set()


@dp.callback_query_handler(text='phone', state="*")
async def inl_new_fr_name(call: types.CallbackQuery, state: FSMContext):
    await call.message.edit_text("введите ваш телефон", reply_markup=kb.ret_login_kb())
    await LoginState.phone.set()


@dp.callback_query_handler(text='pass', state="*")
async def inl_new_fr_name(call: types.CallbackQuery, state: FSMContext):
    await call.message.edit_text("введите ваш пароль", reply_markup=kb.ret_login_kb())
    await LoginState.parow.set()


@dp.callback_query_handler(text='ret_login', state='*')
async def new_cancel(call: types.CallbackQuery, state: FSMContext):
    await update_keyboard(state)
    await LoginState.wait.set()


@dp.callback_query_handler(text='cr_pr_ok', state="*")
async def inl_new_fr_name(call: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        p = data['phone']
        e = data['email']
    await state.finish()
    add_user(call.message.chat.id, p, e)
    await call.message.edit_text("Данные сохранены\n\n", reply_markup=kb.profile())


@dp.message_handler(state=LoginState.phone)
async def price_state(message: types.Message, state: FSMContext):
    ph = message.text.lower()
    await state.update_data(phone=ph)
    await update_keyboard(state)
    await message.delete()
    await state.set_state(LoginState.wait.state)


@dp.message_handler(state=LoginState.email)
async def price_state(message: types.Message, state: FSMContext):
    em = message.text.lower()
    await state.update_data(email=em)
    await update_keyboard(state)
    await message.delete()
    await state.set_state(LoginState.wait.state)


@dp.message_handler(state=LoginState.parow)
async def price_state(message: types.Message, state: FSMContext):
    em = message.text.lower()
    await state.update_data(parow=em)
    await update_keyboard(state)
    await message.delete()
    await state.set_state(LoginState.wait.state)


@dp.message_handler(state=LoginState.wait)
async def wait_state(message: types.Message, state: FSMContext):
    await update_keyboard(state)

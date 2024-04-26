from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State

from command import dp
from keyboard import creat_kb as kb

# TODO скипать и возвращаться к вопросам

QQ = ["С кем он был близок", "Расскажите про его профессию", "где он учился",
      "что было важно для него", "чем он увлекался", "Место рождения почившего",
      "Образование", "Место работы", "Место смерти",
      "Характер", "Отношения с близкими", "Любимые хобби", "Яркое воспоминание"]

SIZE = len(QQ)


class QuestionState(StatesGroup):
    question = State()
    wait = State()


@dp.callback_query_handler(text='question', state="*")
async def new_fr(call: types.CallbackQuery, state: FSMContext):
    await state.update_data(num=0)
    await state.update_data(question=[i for i in range(SIZE)])
    await state.update_data(answer=[])
    await state.update_data(kb=kb.question())
    await state.update_data(callback=call)
    await call.message.edit_text(QQ[0], reply_markup=kb.question())
    await QuestionState.question.set()


@dp.callback_query_handler(text='next_q', state="*")
async def next_fr(call: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        num = data['num'] + 1
        qq = data['question']
        kb_ = data['kb']
        if num >= len(qq):
            num = 0
        q = QQ[qq[num]]
        a = data['answer']
    print(a)
    if len(qq) == SIZE - 5:
        kb_ = kb.question_2()
        await state.update_data(kb=kb_)

    await state.update_data(num=num)
    await call.message.edit_text(q, reply_markup=kb_)
    await QuestionState.question.set()


@dp.callback_query_handler(text='prev_q', state="*")
async def next_fr(call: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        num = data['num'] - 1
        qq = data['question']
        if num < 0:
            num = len(qq) - 1
        q = QQ[qq[num]]
        kb_ = data['kb']
    if len(qq) == SIZE - 5:
        kb_ = kb.question_2()
        await state.update_data(kb=kb_)
    await state.update_data(num=num)
    await call.message.edit_text(q, reply_markup=kb_)
    await QuestionState.question.set()


@dp.callback_query_handler(text='finish_q', state="*")
async def next_fr(call: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        aa = data['answer']
    state.finish()
    await call.message.edit_text("\n".join([" - ".join(i) for i in aa]), reply_markup=kb.epi_and_bio())

#
# @dp.callback_query_handler(text='email', state="*")
# async def inl_new_fr_name(call: types.CallbackQuery, state: FSMContext):
#     await call.message.edit_text("введите вашу почту", reply_markup=kb.ret_login_kb())
#     await QuestionState.email.set()
#
#
# @dp.callback_query_handler(text='phone', state="*")
# async def inl_new_fr_name(call: types.CallbackQuery, state: FSMContext):
#     await call.message.edit_text("введите ваш телефон", reply_markup=kb.ret_login_kb())
#     await QuestionState.phone.set()
#
#
# @dp.callback_query_handler(text='ret_login', state='*')
# async def new_cancel(call: types.CallbackQuery, state: FSMContext):
#     await update_keyboard(state)
#     await QuestionState.wait.set()
#
#
# @dp.callback_query_handler(text='cr_pr_ok', state="*")
# async def inl_new_fr_name(call: types.CallbackQuery, state: FSMContext):
#     async with state.proxy() as data:
#         p = data['phone']
#         e = data['email']
#     await state.finish()
#     add_user(call.message.chat.id, p, e)
#     await call.message.edit_text("Данные сохранены\n\n", reply_markup=kb.profile())
#
#
@dp.message_handler(state=QuestionState.question)
async def price_state(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        num = data['num']
        qq = data['question']
        q = QQ[qq[num]]
        a = data['answer']
        call = data['callback']
        kb_ = data['kb']
    if len(qq) == SIZE - 5:
        kb_ = kb.question_2()
        await state.update_data(kb=kb_)
    ph = message.text.lower()
    a.append([q, ph])
    qq = qq[:num]+qq[num+1:]
    if len(qq) >= num:
        await state.update_data(num=0)
    await state.update_data(answer=a)
    await state.update_data(question=qq)
    await message.delete()
    q = QQ[qq[num]]
    await call.message.edit_text(q, reply_markup=kb_)



#
# @dp.message_handler(state=QuestionState.email)
# async def price_state(message: types.Message, state: FSMContext):
#     em = message.text.lower()
#     await state.update_data(email=em)
#     await update_keyboard(state)
#     await message.delete()
#     await state.set_state(QuestionState.wait.state)
#
#
# @dp.message_handler(state=QuestionState.wait)
# async def wait_state(message: types.Message, state: FSMContext):
#     await update_keyboard(state)

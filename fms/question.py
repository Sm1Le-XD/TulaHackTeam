from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State

from command import dp
from keyboard import creat_kb as kb
from db import db

import yagpt.gpt

# TODO скипать и возвращаться к вопросам

QQ = ["С кем он был близок", "Расскажите про его профессию", "где он учился",
      "что было важно для него", "чем он увлекался", "Место рождения почившего",
      "Образование", "Место работы", "Место смерти",
      "Характер", "Отношения с близкими", "Любимые хобби", "Яркое воспоминание"]

SIZE = len(QQ)

#  ввод-вывод вопросов
class QuestionState(StatesGroup):
    question = State()
    epi = State()
    bio = State()
    epi_bio = State()
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
    await QuestionState.epi_bio.set()
    await epi_bio(state, call.from_user.id)

    await call.message.edit_text("\n".join([" - ".join(i) for i in aa]), reply_markup=kb.epi_and_bio())


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
    qq = qq[:num] + qq[num + 1:]
    if len(qq) >= num:
        await state.update_data(num=0)
    await state.update_data(answer=a)
    await state.update_data(question=qq)
    await message.delete()
    q = QQ[qq[num]]
    await call.message.edit_text(q, reply_markup=kb_)


#  работа с эпитафиями и био

async def epi_bio(state: FSMContext, id):
    await state.update_data(dead=db.search_id_dead(id))
    await state.update_data(epi="")
    await state.update_data(bio="")


@dp.callback_query_handler(text='epi_and_bio', state="*")
async def next_fr(call: types.CallbackQuery, state: FSMContext):

    async with state.proxy() as data:
        aa = data['answer']
    await QuestionState.epi_bio.set()

    await call.message.edit_text("\n".join([" - ".join(i) for i in aa]), reply_markup=kb.epi_and_bio())

@dp.callback_query_handler(text='epi', state="*")
async def next_fr(call: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        aa = data['answer']
    fio = db.ret_data_dead(db.search_id_dead(call.message.chat.id))[0]
    tt = "Обработка информации"
    await call.message.edit_text(tt, reply_markup=kb.epi())
    tt = yagpt.gpt.epi("\n".join([" - ".join(i) for i in aa]), fio[2] + " " + fio[3] + " " + fio[4])
    await call.message.edit_text(tt, reply_markup=kb.epi())
    await state.update_data(epi=tt)
    # await call.message.edit_text(q, reply_markup=kb_)
    await QuestionState.question.set()


@dp.callback_query_handler(text='bio', state="*")
async def next_fr(call: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        aa = data['answer']
    fio = db.ret_data_dead(db.search_id_dead(call.message.chat.id))[0]
    tt = "Обработка информации"
    await call.message.edit_text(tt, reply_markup=kb.bio())
    tt = yagpt.gpt.bio("\n".join([" - ".join(i) for i in aa]),  fio[2] + " " + fio[3] + " " + fio[4])
    await call.message.edit_text(tt, reply_markup=kb.bio())
    await state.update_data(bio=tt)
    # await call.message.edit_text(q, reply_markup=kb_)
    await QuestionState.question.set()


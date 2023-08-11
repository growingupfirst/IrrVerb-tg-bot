from aiogram.dispatcher.router import Router
from aiogram.filters.text import Text
from aiogram import types
import re, random, time
import os
from handlers.game import prepare_verbdict, get_random_line, check_answer
from aiogram.types import Message, ReplyKeyboardRemove, ReplyKeyboardMarkup
from keyboards.ready_kb import get_ready_keyboard, try_again_keyboard
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup


router = Router()

class Form(StatesGroup):
    a1_answer = State()
    a2_answer = State()
    a3_answer = State()
    a4_answer = State()
    a5_answer = State()
    
VerbDict = prepare_verbdict()
print(Form.a1_answer)
@router.message(Text(text='game', ignore_case=True))
async def game_start(message: types.Message, state: FSMContext):
        attempts = 5
        await state.set_data(data={'score':0, 'answer': None})
        await message.answer("Подгружаем игру...", reply_markup=types.ReplyKeyboardRemove())
        cd = await state.get_data()
        print(cd)
        time.sleep(3)
        await message.answer('You have {} attempts\n Press "Ready"'.format(attempts), reply_markup=get_ready_keyboard())



@router.message(Text(text='ready', ignore_case=True))
async def play_game(message: types.Message, state:FSMContext):
        current_state = await state.get_state()
        data = await state.get_data()
        current_score = data['score']
        # ПОСТАВИТЬ УСЛОВИЕ: если Форма а1 пуста, то установить state на а1, если не пуста, то на второй и тп. 
        # Если не пуста и пятая форма, то подсчитать результат.
        if current_state == None:
                random_line, _answer = get_random_line(VerbDict=VerbDict)
                await state.update_data(data={'answer':_answer})
                cd = await state.get_data()
                print(cd)
                await state.set_state(Form.a1_answer)
                await message.answer(f'Please write a nessessary verbs with dashes: {random_line}\n', reply_markup=ReplyKeyboardRemove())
        elif await state.get_state() == 'Form:a1_answer':
                random_line, _answer = get_random_line(VerbDict=VerbDict)
                await state.update_data(data={'answer':_answer})
                await state.set_state(Form.a2_answer)
                await message.answer(f'{random_line}\n')
        elif await state.get_state() == 'Form:a2_answer':
                random_line, _answer = get_random_line(VerbDict=VerbDict)
                await state.update_data(data={'answer':_answer})
                await state.set_state(Form.a3_answer)
                await message.answer(f'{random_line}\n')
        elif await state.get_state() == 'Form:a3_answer':
                random_line, _answer = get_random_line(VerbDict=VerbDict)
                await state.update_data(data={'answer':_answer})
                await state.set_state(Form.a4_answer)
                await message.answer(f'{random_line}\n')
        elif await state.get_state() == 'Form:a4_answer':
                random_line, _answer = get_random_line(VerbDict=VerbDict)
                await state.update_data(data={'answer':_answer})
                await state.set_state(Form.a5_answer)
                await message.answer(f'{random_line}\n')
        else:
                await message.answer(f'Your final score is {current_score}')
                time.sleep(3)
                if current_score == 5:
                        await message.answer('You are a brilliant student!', reply_markup=try_again_keyboard())
                elif current_score == 4:
                        await message.answer('You are a good student!', reply_markup=try_again_keyboard())
                else:
                        await message.answer('You are not a good student.',reply_markup=try_again_keyboard())
                        time.sleep(1)
                        await message.answer(':(')
                        time.sleep(1)
                        await message.answer('Try again one more time!', reply_markup=try_again_keyboard())
                        
@router.message(Text(contains='-'))
async def result(message: types.Message, state: FSMContext):
        data = await state.get_data()
        if check_answer(message.text, data['answer']):
                new_score = data['score'] + 1
                await state.update_data(score=new_score)
                await message.answer(f'Good Job! Your score is {new_score}')
                await play_game(message, state)
        else:
                correct_answer = data['answer']
                await message.answer(f'Wrong! The right answer is {correct_answer} \n')
                time.sleep(3)
                await play_game(message, state)

@router.message(Text(text='Try again'))
async def try_again(message: types.Message, state: FSMContext):
        await state.clear()
        await state.set_data(data={'score': 0, 'answer': None})
        cd = await state.get_data()
        print(cd)
        await play_game(message, state)
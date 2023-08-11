from aiogram.dispatcher.router import Router
from aiogram.filters.text import Text
from aiogram import types
import re, random, time
import os
from handlers.game import prepare_verbdict, get_random_line, check_answer
from aiogram.types import Message, ReplyKeyboardRemove, ReplyKeyboardMarkup
from keyboards.start_keyboard import get_start_keyboard
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

router = Router()

@router.message(Text(text="results", ignore_case=True))
async def check_results(message: Message):
    await message.answer(
        "Подгружаем таблицу...",
        reply_markup=ReplyKeyboardRemove()
    )
    await message.answer(
        "Таблицы пока нет.", reply_markup=get_start_keyboard()
    )  
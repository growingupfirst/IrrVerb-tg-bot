from aiogram.dispatcher.router import Router
from aiogram.filters.command import Command
from aiogram.filters.text import Text
from aiogram import types
from aiogram.types import Message, ReplyKeyboardRemove, ReplyKeyboardMarkup
from keyboards.start_keyboard import get_start_keyboard
from handlers import on_game

router = Router()

@router.message(Command(commands=['start']))
async def cmd_start(message: Message):
    await message.answer("Чего желаете?", reply_markup=get_start_keyboard())
    
@router.message(Text(text="results", ignore_case=True))
async def answer_no(message: Message):
    await message.answer(
        "Подгружаем таблицу...",
        reply_markup=ReplyKeyboardRemove()
    )  
    
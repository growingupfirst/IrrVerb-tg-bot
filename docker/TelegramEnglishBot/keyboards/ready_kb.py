from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, Message

def get_ready_keyboard():
    kb = [
        [KeyboardButton(text="Ready")]
    ]
    keyboard = ReplyKeyboardMarkup(keyboard=kb)
    return keyboard

def try_again_keyboard():
    kb = [
        [KeyboardButton(text="Try again")]
    ]
    keyboard = ReplyKeyboardMarkup(keyboard=kb)
    return keyboard
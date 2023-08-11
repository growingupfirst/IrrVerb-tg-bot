from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, Message

def get_start_keyboard():
    kb = [
        [KeyboardButton(text="Game")],
        [KeyboardButton(text="Results")]
    ]
    keyboard = ReplyKeyboardMarkup(keyboard=kb)
    return keyboard
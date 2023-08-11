from aiogram import BaseMiddleware
from aiogram.types import Message
from aiogram.types import TelegramObject
from typing import Callable, Dict, Any, Awaitable

class GameMiddleware(BaseMiddleware):
    async def __call__(self, handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]], event: TelegramObject,
     data: Dict[str, Any]) -> Any:
     if 'game' in self.message

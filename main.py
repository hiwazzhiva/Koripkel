import os
import random
import uuid
from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineQueryResultArticle, InputTextMessageContent
from aiogram.utils import executor

API_TOKEN = os.getenv("BOT_TOKEN")  # Railway environment variable

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

predictions = [
    "You will be dismissed",
    "It was a tough day, you deserve a coffee!",
    "Go chal you lazy bish",
    "A surprise awaits you (probation)",
    "It's never late to change your major...or uni",
    "Shower today. SHOWER TODAY!",
    "You are gay",
    "Food might be poisoned",
    "You may receive a love letter from someone",
    "I hope this email finds you depressed...",
    "50/50 chance of meeting Shigeo"
]

@dp.inline_handler()
async def send_prediction(inline_query: types.InlineQuery):
    result_t_

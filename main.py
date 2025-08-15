import os
import random
import uuid
from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineQueryResultArticle, InputTextMessageContent
from aiogram.utils import executor

API_TOKEN = os.getenv("BOT_TOKEN")  # Bot token will come from environment variables

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# You can change this list anytime
predictions = [
    "You will have a lucky day 🌟",
    "Be careful today 🐍",
    "Love is around the corner ❤️",
    "A surprise awaits you 🎁",
    "A new opportunity will open up soon 🚪",
    "Your patience will be rewarded ⏳"
]

@dp.inline_handler()
async def send_prediction(inline_query: types.InlineQuery):
    result_text = random.choice(predictions)
    input_content = InputTextMessageContent(result_text)
    item = InlineQueryResultArticle(
        id=str(uuid.uuid4()),
        title="Get your prediction ✨",
        input_message_content=input_content
    )
    await inline_query.answer([item], cache_time=1)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

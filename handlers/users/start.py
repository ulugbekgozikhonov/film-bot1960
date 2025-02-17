from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from data.config import ADMINS

from loader import dp

@dp.message_handler(CommandStart(),chat_id=ADMINS)
async def bot_start_for_admin(message: types.Message):
    await message.answer("Filmni yubor")


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Salom, {message.from_user.full_name}!")

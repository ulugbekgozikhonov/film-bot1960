from loader import dp
from aiogram import types
from data.config import ADMINS
from utils.db_api.models import Movies
from utils.db_api.database import LocalSession
import random

@dp.message_handler(content_types="video",chat_id=ADMINS)
async def download_video(message: types.Message):
    file_id = message.video.file_id
    caption = message.caption
    code = random.randint(999,10_000)
    movie = Movies(
        caption=caption,
        file_id=file_id,
        code=code
    )
    db = LocalSession()
    try:
        db.add(movie)
        db.commit()
        db.refresh(movie)
        await message.reply(f"Video yuklash tugadi.\nKod: {movie.code}")
    except Exception as e:
        await message.reply(f"Xatolik: {e}")
        db.rollback()
    finally:
        db.close()
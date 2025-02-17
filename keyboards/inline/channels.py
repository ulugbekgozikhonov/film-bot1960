from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton

channels_btn = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton("Channel 1", callback_data="channel1",url="https://t.me/+jPLs3p2fVywwMzJi"),
        ],
        [
            InlineKeyboardButton("Channel 2", callback_data="channel2",url="https://t.me/mendasturchiman")
        ],
        [
            InlineKeyboardButton("✅Tasdiqlash",callback_data="tasdiqlash")
        ],
    ]
)
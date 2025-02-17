from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton

async def channels(chat_urls):
    result = InlineKeyboardMarkup()
    for i,url in enumerate(chat_urls):
        result.row(InlineKeyboardButton(text=f"Channel {i+1}", url=url))
        
    result.row(InlineKeyboardButton(text="Confirm✅",callback_data="confirm"))
    return result
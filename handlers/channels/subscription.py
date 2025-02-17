from loader import dp
from aiogram import types
from utils.misc.subscription import check_user

@dp.callback_query_handler(text="confirm")
async def confirm_handler(call:types.CallbackQuery):
    chat_urls = await check_user(call.message.chat.id)
    if chat_urls:
        await call.answer("Kanallarga a'zo bo'ling",show_alert=True)
    else:
        await call.message.edit_reply_markup()
        await call.message.answer("Film kodini yuboring")
    await call.answer()
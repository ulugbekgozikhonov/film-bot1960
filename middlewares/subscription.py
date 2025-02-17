from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram.dispatcher.handler import CancelHandler
from aiogram import types
from utils.misc.subscription import check_user
from keyboards.inline.subscription import channels


class BigBrother(BaseMiddleware):
    
    async def on_pre_process_message(self, message: types.Message, data: dict):
        await self.check_subscription(message, message.from_user.id)

    async def on_pre_process_callback_query(self, call: types.CallbackQuery, data: dict):
        if call.data == "confirm":
            return
        await self.check_subscription(call.message, call.from_user.id)

    async def check_subscription(self, message: types.Message, user_id: int):
        if message.text in ["/start","/help"]:
            return
        chat_urls = await check_user(user_id)
        if not chat_urls:
            return
        await message.answer("Kanallarga a'zo bo'ling", reply_markup=await channels(chat_urls))
        raise CancelHandler()

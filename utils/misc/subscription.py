from data.config import CHANNEL_ID_AND_URLS
from loader import bot

async def check_user(user_id: int) -> list:
    chat_urls = []
    for ch_id,ch_url in CHANNEL_ID_AND_URLS.items():
        member = await bot.get_chat_member(ch_id, user_id)

        if member.status not in ["creator", "administrator", "member","owner"]:
            chat_urls.append(ch_url)
    return chat_urls
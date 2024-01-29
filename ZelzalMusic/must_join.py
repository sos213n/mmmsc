from functools import wraps
from config.config import MUST_JOIN
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors.exceptions.bad_request_400 import UserNotParticipant


def must_join_channel(func):
    @wraps(func)
    async def sz_message(_, message):
        try:
            await message._client.get_chat_member(MUST_JOIN, message.from_user.id)
            if MUST_JOIN.isalpha():          
                link = "https://t.me/" + MUST_JOIN
            else:
                chat_info = await message._client.get_chat(MUST_JOIN)
                link = chat_info.invite_link
        except UserNotParticipant:
            return await message.reply(
                    f"🗽يجب ان تشترك في قنـاة البــوت⬇️\n\n⚙¦ قنــاة ســورس️ الاغــانـي\n⩹━★⊷━𝑺𝑶𝑼𝑹𝑪𝑬 ⛧𝑪𝑹⛧━⊶★━⩺\n🤖قنـاة الـبـوت ⬅️ @{MUST_JOIN} »\n⩹━★⊷━𝑺𝑶𝑼𝑹𝑪𝑬 ⛧𝑪𝑹⛧━⊶★━⩺\n🖥¦حتي تتمكن من استخدامي\n◍ اشترك ثم اضغط « شغل والاغنيه » مره اخري√\n\n🌐¦ By [⌁ 𝔻𝔼𝕍 𝔼𝟛𝔻𝔸𝕄](https://t.me/SOURCE_CR )",
                    disable_web_page_preview=True,
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton("اضـغط هنا للأشتـراك بقـناة البـوت✅", url=f"https://t.me/{MUST_JOIN}"),
                            ],
                            [
                                InlineKeyboardButton("𝑺𝑶𝑼𝑹𝑪𝑬 ⛧𝑪𝑹⛧", url=f"https://t.me/SOURCE_CR "),
                            ] 
                         ] 
                      ) 
                   ) 
        return await func(_, message)    
    return sz_message

import wikipedia
from aiogram import types

from loader import dp

wikipedia.set_lang("uz")
# wiki bot
@dp.message_handler(state=None)
async def send_Wiki(message: types.Message):
    try:
        respond = wikipedia.summary(message.text)
        await message.answer(respond)
    except:
        await message.answer("Bu mavzuga oid maqola topilmadi")

from aiogram import Router, F
from aiogram.types import Message

router = Router()

@router.message()
async def echo_bot_process(message: Message):
    await message.answer(text=message.text)



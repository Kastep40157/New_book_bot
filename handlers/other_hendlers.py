import requests
from aiogram import Router
from aiogram.types import Message

router = Router()

@router.message()
async def echo_bot_process(message: Message):
    await message.answer(text=message.text)



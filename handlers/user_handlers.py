from aiogram import F, Router
from aiogram.types import Message
from aiogram.filters import CommandStart, Command
from lexicon.lexicon_ru import LEXICON
router = Router()


@router.message(CommandStart)
async def process_start_command(message: Message):
    await message.answer(LEXICON[message.text])



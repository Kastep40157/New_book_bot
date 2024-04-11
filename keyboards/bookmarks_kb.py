from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from lexicon.lexicon_ru import LEXICON
from services.file_handling import book


# Создаем функцию генерирующую клавиатуру для работы с закладками пользователя

def create_bookmarks_keyboard(*args: int) -> InlineKeyboardMarkup:
    # Сщоздаем объект клавиатуры
    kb_builder = InlineKeyboardBuilder()
    # Наполняем клавиатуру кнопка-закладкамив порядке возрастания
    for button in sorted(args):
        kb_builder.row(InlineKeyboardButton(
            text=f'{button}-{book[button][:100]}',
            callback_data=str(button)
            ))
        kb_builder.row(
            InlineKeyboardButton(
            text=LEXICON['edit_bookmarks_button'],
            callback_data='edit_bookmarks'
            ),
            InlineKeyboardButton(
                text='cancel',
                callback_data='cancel'
            ),
            width=2
        )
    return kb_builder.as_markup()


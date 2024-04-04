# данный модуль предназначен для преобразования текстовго файлай в удобочитаемый словарь где:
# ключ это страница
# значение - часть текста

import os
import sys

BOOK_PATH = '../books/book.txt'
BOOK_SIZE = 1050

book: dict[int, str] = {}


# Функция, возвращающая строку с текстом страницы и ее размер
def _get_part_text(text: str, start: int, size: int) -> tuple[str, int]:

    pass



def prepare_book (path: str) -> None:
   with open(file=BOOK_PATH, mode='r') as file:
       text = file.read()
       start, page_number = 0, 1
       while start< len(text):
           page_text, page_size = _get_part_text(text, start, BOOK_SIZE)
           start +=page_size
           book[page_number] = page_text.strip()
           page_number += 1





prepare_book(BOOK_PATH)
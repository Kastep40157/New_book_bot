# данный модуль предназначен для преобразования текстовго файлай в удобочитаемый словарь где:
# ключ это страница
# значение - часть текста

import os
import sys

BOOK_PATH = '../books/book.txt'
BOOK_SIZE = 1050

def prepare_book (path: str) -> None:
   with open(file=BOOK_PATH, mode='r') as file:
       text = file.read()
       print(text)

prepare_book(BOOK_PATH)
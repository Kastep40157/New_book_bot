# данный модуль предназначен для преобразования текстовго файлай в удобочитаемый словарь где:
# ключ это страница
# значение - часть текста

import os
import sys

BOOK_PATH = 'book/Bredberi_Marsianskie-hroniki.txt'
BOOK_SIZE = 1050

book: dict[int, str] = {}


# Функция, возвращающая строку с текстом страницы и ее размер
def _get_part_text(text: str, start: int, size: int) -> tuple[str, int]:
    end_point = ',.!:;?'
    last_size = size
    if len(text) <= size + start:
        last_size = len(text) - start
    else:
        for i in range(size + start - 1, start, -1):
            if text[i] in end_point and text[i + 1] not in end_point:
                break
            last_size -= 1
    return text[start: start + last_size], last_size


def prepare_book(path: str) -> None:
   with open(file=BOOK_PATH, mode='r') as file:
       text = file.read()
       start, page_number = 0, 1
       while start < len(text):
           page_text, page_size = _get_part_text(text, start, BOOK_SIZE)
           start += page_size
           book[page_number] = page_text.strip()
           page_number += 1


# Вызов функции prepare_book для подготовки книги из текстового файла
prepare_book(os.path.join(sys.path[0], os.path.normpath(BOOK_PATH)))

# Файл отвечает за начальную конфигурацию БОТа
from dataclasses import dataclass
from environs import Env

@dataclass
class Tg_Bot:
    token: str


@dataclass
class Config:
    tg_bot: Tg_Bot


def load_config(path: str| None =None)-> Config:
    # Создаем экземпляр класса
    env: Env = Env()
    # Добавляем в переменные окружения данные, прочитанные из .env
    env.read_env(path)
    return Config(tg_bot=Tg_Bot(token=env('BOT_TOKEN')))
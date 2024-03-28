# Файл отвечает за начальную конфигурацию БОТа
from dataclasses import dataclass
from environs import Env

@dataclass
class Tg_Bot:
    token: str
    #admins_ids: list[int]

@dataclass
class DatabaseConfig:
    db_name: str # Наименование базы данных
    db_host: str # URL-адрес базы данных
    db_user: str # Имя пользователя БД
    db_pass: str # Пароль к БД


@dataclass
class Config:
    tg_bot: Tg_Bot
    #db: DatabaseConfig



def load_config(path: str| None =None)-> Config:
    # Создаем экземпляр класса
    env: Env = Env()
    # Добавляем в переменные окружения данные, прочитанные из .env
    env.read_env(path)
    return Config(tg_bot=Tg_Bot(token=env('BOT_TOKEN')))
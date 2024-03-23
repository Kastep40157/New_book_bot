from dataclasses import dataclass
from environs import Env

@dataclass
class Tg_Bot:
    token: str
    admins_ids: list[int]

@dataclass
class DatabaseConfig:
    db_name: str # Наименование базы данных
    db_host: str # URL-адрес базы данных
    db_user: str # Имя пользователя БД
    db_pass: str # Пароль к БД


@dataclass
class Config:
    tg_bot: Tg_Bot
    db: DatabaseConfig

# Создаем экземпляр класса
env: Env = Env()
# Добавляем в переменные окружения данные, прочитанные из .env
env.read_env()

# создаем экземпляр класса Config и наполняем его данными из окружения
config = Config(
    tg_bot=Tg_Bot(
        token=env("BOT_TOKEN"),
        admins_ids=list(map(int, env.list('ADMINS_IDS')))
    ),
    db=DatabaseConfig(
        db_name=env('DATABASE'),
        db_host=env('DB_HOST'),
        db_user=env('DB_USER'),
        db_pass=env('DB_PASS')
    )
)
print("BOT_TOKEN", config.tg_bot.token)
print('ADMINS_IDS', config.tg_bot.admins_ids)
print('DATABASE', config.db.db_name)
print('DB_HOST', config.db.db_host)
print('DB_USER', config.db.db_user)
print('DB_PASS', config.db.db_pass)


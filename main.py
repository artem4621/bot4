import asyncio  # Работа с асинхронностью

from aiogram import Bot, Dispatcher
from aiogram.filters import Command, Text  # Фильтр для /start, /...
from aiogram.types import Message, ReplyKeyboardRemove  # Тип сообщения

from config import config  # Config
from keyboards.reply import cats_dogs_keyboard

API_TOKEN = config.token

bot = Bot(token=API_TOKEN)
dp = Dispatcher()  # Менеджер бота


# dp.message - обработка сообщений
# Command(commands=['start'] Фильтр для сообщений, берём только /start
@dp.message(Command(commands=['start']))  # Берём только сообщения, являющиеся командой /start
async def start_command(message: Message):  # message - сообщение, которое прошло через фильтр
    await message.answer("Привет!Кого ты больше любишь котов или собак?",  # Отвечаем на полученное сообщение
                reply_markup=cats_dogs_keyboard)
@dp.message(Text(text='Собак'))
async def handle_dogs_answer(message: Message):
    await message.answer('Мне тоже,но коты лучше')


@dp.message(Text(text='Котов'))
async def handle_cats_answer(message: Message):
    await message.answer('Мне они больше нравятся чем собаки')

@dp.message(Command(commands='help'))
async def handle_help(message:Message):
    await message.answer('чо та помогаю')
@dp.message(Command('delete_menu'))
async def handle_menu_delete(message: Message, bot: Bot):
    await bot.delete_my_commands()
    await message.answer('Вы удалили меню')


async def main():
    try:
        print('Bot Started')
        await bot.set_my_commands(main_menu_command)
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == '__main__':  # Если мы запускаем конкретно этот файл.
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        print('Bot stopped')
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

answer_dogs_button = KeyboardButton(text='Собак')
answer_cats_button = KeyboardButton(text='Котов')

cats_dogs_keyboard = ReplyKeyboardMarkup(keyboard=[
    [answer_dogs_button, answer_cats_button]
], resize_keyboard=True, one_time_keyboard=True)
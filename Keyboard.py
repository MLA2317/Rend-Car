from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import logging



menuStart = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Mashinalar rent")
        ],
        [
            KeyboardButton(text="Bog'lanish"),
            KeyboardButton(text="Bizning botlar")
        ]
    ],
    resize_keyboard=True
)


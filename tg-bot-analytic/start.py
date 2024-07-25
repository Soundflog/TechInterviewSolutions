from datetime import datetime

import gspread
import requests
from aiogram import Router, Bot
from aiogram.enums import ParseMode
from aiogram.filters import Command
from aiogram.types import Message, InlineKeyboardButton, CallbackQuery
from aiogram.utils.keyboard import InlineKeyboardBuilder
from google.oauth2.service_account import Credentials
from config import UNSPLASH_ACCESS_KEY, GOOGLE_SHEETS_JSON, SPREADSHEET_NAME


router = Router()

buttons = [
    "Кнопка 1 (карты)",
    "Кнопка 2 (оплата)",
    "Кнопка 3 (картинка)",
    "Кнопка 4 (гугл-таблица)"
]

def keyboard_buttons():
    keyboard_markup = InlineKeyboardBuilder()
    keyboard_markup.add(
        InlineKeyboardButton(
            text="Ленина 1 на Яндекс Картах",
            url="https://yandex.ru/maps/?text=Ленина 1",
            callback_data='maps'
        ),
        InlineKeyboardButton(
            text="Оплатить 2 рубля",
            url="https://payment.example.com/2rub",
            callback_data='pay'
        ),
        InlineKeyboardButton(
            text="Картинка",
            callback_data="send_image"
        ),
        InlineKeyboardButton(
            text="Получить значение А2",
            callback_data="get_value_A2"
        ))
    keyboard_markup.adjust(1)
    return keyboard_markup.as_markup()


@router.message(Command(commands=["start"]))
async def start(message: Message):
    # await callback_query.message.edit_reply_markup()
    # await bot.edit_message_reply_markup(chat_id=message.chat.id, message_id=message.message_id)
    # isAdmin = await IsAdminUser(user_id)
    await message.answer(
        text=f'Привет {message.from_user.first_name}, у вас имеется 4 кнопки\n'
             f'<b>Кнопка 1</b> -- ссылка на Яндекс карты\n'
             f'<b>Кнопка 2</b> -- ссылка на оплату 2 р.\n'
             f'<b>Кнопка 3</b> -- картинка “img1.jpg”\n'
             f'<b>Кнопка 4</b> -- получить значение А2 гугл таблички "гугл_табличка"\n',
        parse_mode=ParseMode.HTML,
        reply_markup=keyboard_buttons()
    )

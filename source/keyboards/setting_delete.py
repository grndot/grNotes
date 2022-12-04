from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from source.middlewares.i18n import get_text


def set_delete_kb() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup().add(
                InlineKeyboardButton(
                    text=get_text("Back"),
                    callback_data="settings"))

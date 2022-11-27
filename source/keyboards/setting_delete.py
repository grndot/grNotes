from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def set_delete_kb() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup().add(
                InlineKeyboardButton(
                    text="Back",
                    callback_data="settings"))

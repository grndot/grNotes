from aiogram.types import (
        InlineKeyboardButton,
        InlineKeyboardMarkup)

from source.middlewares.i18n import get_text


def settings_kb(locale: str|None = None) -> InlineKeyboardMarkup:

    back_button = InlineKeyboardButton(
            text=get_text(
                "Back",
                locale=locale),
            callback_data="main_menu")
    language_button = InlineKeyboardButton(
            text=get_text(
                "Languages",
                locale=locale),
            callback_data="language_settings")
    recovery_code_button = InlineKeyboardButton(
            text=get_text(
                "Recovery Code",
                locale=locale),
            callback_data="recovery_settings")
    delete_all_notes_button = InlineKeyboardButton(
            text=get_text(
                "Delete Account",
                locale=locale),
            callback_data="delete_account")
    keyboard = InlineKeyboardMarkup(row_width=2)
   
    keyboard.row(
            language_button,
            recovery_code_button)
    keyboard.row(delete_all_notes_button)
    keyboard.row(
            back_button)

    return keyboard



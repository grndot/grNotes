from aiogram.types import (
        InlineKeyboardButton,
        InlineKeyboardMarkup)


def settings_kb() -> InlineKeyboardMarkup:

    back_button = InlineKeyboardButton(
            text="Back",
            callback_data="main_menu")
    language_button = InlineKeyboardButton(
            text="Languages",
            callback_data="language_settings")
    recovery_code_button = InlineKeyboardButton(
            text="Recovery Code",
            callback_data="recovery_settings")
    delete_all_notes_button = InlineKeyboardButton(
            text="Delete Account",
            callback_data="delete_account")
    keyboard = InlineKeyboardMarkup(row_width=2)
   
    keyboard.row(
            language_button,
            recovery_code_button)
    keyboard.row(delete_all_notes_button)
    keyboard.row(
            back_button)

    return keyboard



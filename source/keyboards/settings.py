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
            text="Delete All",
            callback_data="delete_all_notes")
    keyboard = InlineKeyboardMarkup(row_width=3)
   
    keyboard.row(
            language_button,
            recovery_code_button,
            delete_all_notes_button)
    keyboard.insert(
            back_button)

    return keyboard



from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def menu_kb() -> InlineKeyboardMarkup:
    show_notes_button = InlineKeyboardButton(
            text="My notes",
            callback_data="notes")
    settings_button = InlineKeyboardButton(
            text="Settings",
            callback_data="settings")
    donate_button = InlineKeyboardButton(
            text="Donate",
            callback_data="donate")
    keyboard = InlineKeyboardMarkup(
            row_width=3,
            inline_keyboard=[
                [show_notes_button],
                [settings_button],
                [donate_button]])
    return keyboard

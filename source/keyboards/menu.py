from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def menu_kb() -> InlineKeyboardMarkup:
    create_note_button = InlineKeyboardButton(
            text="Create note",
            callback_data="create")
    show_notes_button = InlineKeyboardButton(
            text="Show notes",
            callback_data="show")
    settings_button = InlineKeyboardButton(
            text="Settings",
            callback_data="settings")
    donate_button = InlineKeyboardButton(
            text="Donate",
            callback_data="donate")
    keyboard = InlineKeyboardMarkup(
            row_width=4,
            inline_keyboard=[
                [create_note_button],
                [show_notes_button],
                [settings_button],
                [donate_button]])
    return keyboard

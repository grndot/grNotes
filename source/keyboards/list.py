from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def back_to_list_keyboard() -> InlineKeyboardMarkup:
    back_button = InlineKeyboardButton(
            text="Back",
            )
    keyboard = InlineKeyboardMarkup(
            inline_keyboard=[
                [back_button]
                ])


def list_of_notes_keyboard() -> InlineKeyboardMarkup:
    create_note_button = InlineKeyboardButton(
            text="Create new note",
            callback_data="create")
    keyboard = InlineKeyboardMarkup(
            row_width=11,
            inline_keyboard=[
                [create_note_button]
                ]
            )
    return keyboard


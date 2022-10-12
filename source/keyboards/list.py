from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def create_new_note_keyboard(
        title_is_64_symbols = False) -> InlineKeyboardMarkup:
    back_button = InlineKeyboardButton(
            text="Back to my notes",
            callback_data="notes"
            )
    checkbox_note_button = InlineKeyboardButton(
            text="Page with checkboxes",
            callback_data="checkbox")
    plug_button = InlineKeyboardButton(
            text="<--->")
    text_note_button = InlineKeyboardButton(
            text="Page with text",
            callback_data="text")
    
    keyboard = InlineKeyboardMarkup(
            row_width=4,
            inline_keyboard=[
                [back_button],
                [plug_button],
                [],
                []])
    if title_is_64_symbols:
        keyboard.inline_keyboard[2].insert(0, checkbox_note_button)
        keyboard.inline_keyboard[3].insert(0, text_note_button)
    return keyboard


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


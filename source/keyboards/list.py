from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def create_new_note_keyboard(
        is_title_64_symbols = False) -> InlineKeyboardMarkup:
    back_to_notes_button = InlineKeyboardButton(
            text="Back to my notes",
            callback_data="notes"
            )
    back_to_title_button = InlineKeyboardButton(
            text="Back to title",
            callback_data="")
    save_button = InlineKeyboardButton(
            text="Save note",
            callback_data="save")
    
    keyboard = InlineKeyboardMarkup(
            row_width=4,
            inline_keyboard=[
                [],
                [],
                []])
    if is_title_64_symbols:
        keyboard.inline_keyboard[0].insert(0, back_to_notes_button)
        keyboard.inline_keyboard[1].insert(0, back_to_title_button)
    else:
        keyboard.inline_keyboard[0].insert(0, back_to_notes_button)
        

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


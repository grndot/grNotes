from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def create_new_note_keyboard(is_title_correct=False): 
    return InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(
                        text="Save" if is_title_correct else 'Cancel',
                        callback_data="notes")
                    ]])


def notes_menu_keyboard() -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup()
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


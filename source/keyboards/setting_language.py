from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData

from source.keyboards.menu import pagination_cb
from source.middlewares.i18n import get_text


# Callbacks
choose_lang = CallbackData("lang", "db_id")


def language_kb(array: tuple, page: int = 1) -> InlineKeyboardMarkup:

    # Variables for keyboard page
    key = "languages" 
    max_items_per_page = 10
    first_lang_index = (page - 1) * max_items_per_page
    last_lang_index = page * max_items_per_page
    first_page = 1
    last_page = len(array) // max_items_per_page + 1 
    next_page = page + 1
    next_page_text = f'{next_page} →'
    previous_page = page - 1
    previous_page_text = f'← {previous_page}'
    sliced_array = array[first_lang_index:last_lang_index]

    # Buttons
    language_buttons = [
            InlineKeyboardButton(
                text=get_text(lang.HumanName),
                callback_data=choose_lang.new(
                    db_id=lang.ID)) for lang in sliced_array]

    next_page_button = InlineKeyboardButton(
            text=next_page_text,
            callback_data=pagination_cb.new(
                key=key,
                page=next_page))

    previous_page_button = InlineKeyboardButton(
            text=previous_page_text,
            callback_data=pagination_cb.new(
                key=key,
                page=previous_page))
    
    pages_buttons = []
    if previous_page >= first_page:
        pages_buttons.append(previous_page_button)
    if next_page <= last_page:
        pages_buttons.append(next_page_button)
    keyboard = InlineKeyboardMarkup(row_width=2)
    for button in language_buttons:
        keyboard.insert(button)
    if pages_buttons:
        keyboard.row(pages_buttons)

    return keyboard


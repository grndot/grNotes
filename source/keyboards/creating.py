from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from source.middlewares.i18n import get_text


def create_new_note_keyboard(is_title_correct=False): 
    return InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(
                        text=get_text("Save") if is_title_correct else get_text('Cancel'),
                        callback_data="main_menu")
                    ]])



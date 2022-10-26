from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def create_new_note_keyboard(is_title_correct=False): 
    return InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(
                        text="Save" if is_title_correct else 'Cancel',
                        callback_data="main_menu")
                    ]])



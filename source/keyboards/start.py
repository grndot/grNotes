from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from sqlalchemy.orm import reconstructor


def start_kb(
        is_back: bool = False,
        is_menu: bool = False) -> InlineKeyboardMarkup:
    
    start_button = InlineKeyboardButton(
                            text="Back",
                            callback_data="start"
                            )
    
    menu_button = InlineKeyboardButton(
                        text="Continue",
                        callback_data="menu"
                        )
    
    recovery_button = InlineKeyboardButton(
                        text="Recovery",
                        callback_data="recovery"
                        )

    if is_back:
        return InlineKeyboardMarkup().insert(start_button)
    elif is_menu:
        return InlineKeyboardMarkup().insert(menu_button)
    else:
        keyboard = InlineKeyboardMarkup()
        keyboard.insert(menu_button)
        keyboard.insert(recovery_button)
        return keyboard


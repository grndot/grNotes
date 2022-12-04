from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from source.middlewares.i18n import get_text


def start_kb(
        is_back: bool = False,
        is_menu: bool = False) -> InlineKeyboardMarkup:
    
    start_button = InlineKeyboardButton(
                            text=get_text("Back"),
                            callback_data="start"
                            )
    
    menu_button = InlineKeyboardButton(
                        text=get_text("Continue"),
                        callback_data="main_menu"
                        )
    
    recovery_button = InlineKeyboardButton(
                        text=get_text("Recovery"),
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


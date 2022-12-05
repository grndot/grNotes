from aiogram.types import (
        InlineKeyboardButton,
        InlineKeyboardMarkup)

from source.middlewares.i18n import get_text


def recovery_set_kb() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
            row_width=1,
            inline_keyboard=[
                    [InlineKeyboardButton(
                        text=get_text("Reset Recovery Key"),
                        callback_data="reset_recovery_code")],
                    [InlineKeyboardButton(
                        text=get_text("Back"),
                        callback_data="settings")]
                ])

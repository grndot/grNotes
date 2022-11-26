from aiogram.types import (
        InlineKeyboardButton,
        InlineKeyboardMarkup)


def recovery_set_kb() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
            row_width=1,
            inline_keyboard=[
                    [InlineKeyboardButton(
                        text="Reset Recovety Code",
                        callback_data="reset_recovery_code")],
                    [InlineKeyboardButton(
                        text="Back",
                        callback_data="settings")]
                ])

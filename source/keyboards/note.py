from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def note_kb() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
            row_width=2,
            inline_keyboard=[
                [
                    InlineKeyboardButton(
                        text="Edit",
                        callback_data="edit_note"),
                    InlineKeyboardButton(
                        text="Delete",
                        callback_data="del_note")
                    ],
                [
                    InlineKeyboardButton(
                        text="Back",
                        callback_data="main_menu"
                        )
                    ]
                ]
            )

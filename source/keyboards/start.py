from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def start_kb(is_back: bool = False) -> InlineKeyboardMarkup:
    if is_back:
        return InlineKeyboardMarkup(
                inline_keyboard=[
                    [
                        InlineKeyboardButton(
                            text="Back",
                            callback_data="start"
                            )]])
    else:
        return InlineKeyboardMarkup(
            row_width=2,
            inline_keyboard=[
                [
                    InlineKeyboardButton(
                        text="Telegram",
                        callback_data="menu"
                        )],
                [
                    InlineKeyboardButton(
                        text="RecoveryCode",
                        callback_data="recovery"
                        )]])

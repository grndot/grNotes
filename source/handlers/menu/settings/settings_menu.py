from aiogram import Dispatcher
from aiogram.types import CallbackQuery

from source.keyboards.settings import settings_kb


async def menu_settings(cb: CallbackQuery):
    await cb.answer()
    await cb.message.edit_text(
            text="Notes by grn.\n\n\nSettings.",
            reply_markup=settings_kb())


def reg_menu_settings(dp: Dispatcher):
    dp.register_callback_query_handler(
            menu_settings,
            text="settings")

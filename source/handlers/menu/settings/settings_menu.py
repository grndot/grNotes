from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery

from source.middlewares.i18n import get_text
from source.keyboards.settings import settings_kb


async def menu_settings(
        cb: CallbackQuery,
        state: FSMContext):
    await state.reset_state(with_data=True)
    await cb.answer()
    await cb.message.edit_text(
            text=get_text("Notes by grn.\n\n\nSettings."),
            reply_markup=settings_kb())


def reg_menu_settings(dp: Dispatcher):
    dp.register_callback_query_handler(
            menu_settings,
            state="*",
            text="settings")

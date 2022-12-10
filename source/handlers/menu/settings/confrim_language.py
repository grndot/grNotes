from aiogram import Dispatcher
from aiogram.types import CallbackQuery
from sqlalchemy.ext.asyncio import AsyncSession

from source.keyboards.settings import settings_kb
from source.keyboards.setting_language import choose_lang
from source.middlewares.i18n import get_text
from source.services.db.users import (
        getIDbyTelegramID, 
        updateUserLanguageIDByUserID
        )


async def menu_setting_after_updating_language(
        cb: CallbackQuery,
        callback_data: dict,
        session: AsyncSession):

    lang_id = callback_data.get("db_id")
    user_id = await getIDbyTelegramID(
            session=session,
            telegram_id=cb.from_user.id)
    
    await cb.answer()
    await updateUserLanguageIDByUserID(
            session=session,
            language_id=lang_id,
            user_id=user_id)
    await cb.message.edit_text(
            text=get_text("Notes by grn.\n\n\nSettings."),
            reply_markup=settings_kb())


def reg_menu_setting_after_updating_language(
        dp: Dispatcher):
    dp.register_callback_query_handler(
            menu_setting_after_updating_language,
            choose_lang.filter()
            )

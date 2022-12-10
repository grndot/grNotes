from aiogram import Dispatcher
from aiogram.types import CallbackQuery
from sqlalchemy.ext.asyncio import AsyncSession

from source.keyboards.setting_language import language_kb
from source.middlewares.i18n import get_text
from source.services.db.langugaes import getAllLanguageData


async def update_lang(
        cb: CallbackQuery,
        session: AsyncSession):
    
    await cb.answer()
    await cb.message.edit_text(
            text=get_text("Choose your language:"),
            reply_markup=language_kb(
                array=await getAllLanguageData(
                    session=session)))    


def reg_update_lang(
        dp: Dispatcher):
    
    dp.register_callback_query_handler(
            update_lang)

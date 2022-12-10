from aiogram import Dispatcher
from aiogram.types import CallbackQuery
from sqlalchemy.ext.asyncio import AsyncSession

from source.keyboards.menu import pagination_cb
from source.keyboards.setting_language import language_kb
from source.services.db.langugaes import getAllLanguageData


async def update_lang_with_chosen_page(
        cb: CallbackQuery,
        callback_data: dict,
        session: AsyncSession):
   
    array_of_languages = await getAllLanguageData(
                    session=session
                    )
    current_page = int(callback_data.get("page"))

    await cb.answer()
    await cb.message.edit_reply_markup(
            reply_markup=language_kb(
                array=array_of_languages,
                page=current_page
                )
            )    


def reg_update_lang_with_chosen_page(
        dp: Dispatcher):
    
    dp.register_callback_query_handler(
            update_lang_with_chosen_page,
            pagination_cb.filter(key="languages")
            )

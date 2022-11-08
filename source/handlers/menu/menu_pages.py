from aiogram import types, Dispatcher
from sqlalchemy.ext.asyncio import AsyncSession

from source.keyboards.menu import menu_kb, pagination_cb
from source.services.db.notes import getNotesTitleAndIDByOwnerID
from source.services.db.users import getIDbyTelegramID


async def main_menu_with_choosen_page(
        cb: types.CallbackQuery,
        callback_data: dict,
        session: AsyncSession):
    """
    "callback_data" is working because
    CallbackDataFilrer provide dictionary 
    {"callback_data": dict};
    "cb_data" won't be work
    """

    current_page = int(callback_data.get("page"))
    user_id = await getIDbyTelegramID(
            session=session,
            telegram_id=cb.from_user.id)
    array_of_notes = await getNotesTitleAndIDByOwnerID(
            session=session,
            owner_id=user_id)
    
    await cb.answer()
    await cb.message.edit_reply_markup(
            reply_markup=menu_kb(
                array=array_of_notes,
                page=current_page
                )
            ) 

def reg_main_menu_with_choosen_page(dp: Dispatcher):
    dp.register_callback_query_handler(
        main_menu_with_choosen_page,
        pagination_cb.filter(key="notes"),
        )

from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from sqlalchemy.ext.asyncio import AsyncSession

from source.keyboards.menu import menu_kb
from source.misc.content import main_menu_text
from source.services.db.notes import (
        getNotesTitleAndIDByOwnerID, 
        insertNewNote
        )
from source.services.db.users import (
        checkUserExists, 
        getIDbyTelegramID, 
        insertNewUser,
        )
from source.services.generators.key import generate_key
from source.states.createnote import CreatingNoteState


async def main_menu(
        cb: types.CallbackQuery,
        state: FSMContext,
        session: AsyncSession):
    await cb.answer()
    current_state = await state.get_state()
    if current_state == CreatingNoteState.Saving:
        state_data = await state.get_data()
        print(state_data.get("title"))
        await insertNewNote(
                session=session,
                owner_id=await getIDbyTelegramID(
                    session=session,
                    telegram_id=cb.from_user.id),
                title=state_data.get("title"),
                text="Change it!")
    if not await checkUserExists(
            session=session,
            telegram_id=cb.from_user.id):
        await insertNewUser(
                session=session,
                telegram_id=cb.from_user.id,
                language_id=1,
                recovery_key=generate_key(
                    cb.from_user.id)) 
        
    await cb.message.edit_text(
            text="\n".join(main_menu_text),
            reply_markup=menu_kb(await getNotesTitleAndIDByOwnerID(
                session=session,
                owner_id=await getIDbyTelegramID(
                    session=session,
                    telegram_id=cb.from_user.id)
                )))


def reg_main_menu(dp: Dispatcher):
    dp.register_callback_query_handler(
            main_menu,
            state="*",
            text="main_menu")

    dp.register_callback_query_handler(
            main_menu,
            state=CreatingNoteState.Saving,
            text="main_menu")

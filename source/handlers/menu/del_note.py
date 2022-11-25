from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from sqlalchemy.ext.asyncio import AsyncSession
from source.keyboards.note import note_kb

from source.services.db.notes import deleteNote
from source.states.note import NoteState


async def del_chosen_note(
        cb: types.CallbackQuery,
        state: FSMContext,
        session: AsyncSession):

    state_data = await state.get_data()
    note_id = state_data.get("NoteID")
    title = state_data.get("Title")
    await cb.answer()
    await deleteNote(
            session=session,
            note_id=int(note_id))
    await cb.message.edit_text(
            text=f"{title} has been deleted.",
            reply_markup=note_kb(del_status=True))


def reg_del_chosen_note(
        dp: Dispatcher):
    dp.register_callback_query_handler(
            del_chosen_note,
            text="del_note",
            state=NoteState.ID)


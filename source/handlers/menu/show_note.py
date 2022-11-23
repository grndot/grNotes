from aiogram import types, Dispatcher
from sqlalchemy.ext.asyncio import AsyncSession

from source.keyboards.menu import show_note
from source.keyboards.note import note_kb
from source.services.db.notes import getNoteTextByNoteID


async def show_chosen_note(
        cb: types.CallbackQuery,
        callback_data: dict,
        session: AsyncSession):

    note_id = callback_data.get("note_id")
    note_text = await getNoteTextByNoteID(
            session=session,
            note_id=int(note_id))
    await cb.answer()
    await cb.message.edit_text(
            text=f"<code>{note_text}</code>",
            reply_markup=note_kb())


def reg_show_note(dp: Dispatcher):
    dp.register_callback_query_handler(
            show_chosen_note,
            show_note.filter())


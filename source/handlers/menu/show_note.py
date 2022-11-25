from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from sqlalchemy.ext.asyncio import AsyncSession

from source.keyboards.menu import show_note
from source.keyboards.note import note_kb
from source.services.db.notes import getNoteTitleAndTextByNoteID
from source.states.note import NoteState


async def show_chosen_note(
        cb: types.CallbackQuery,
        callback_data: dict,
        session: AsyncSession,
        state: FSMContext):

    note_id = callback_data.get("note_id")
    note_data = await getNoteTitleAndTextByNoteID(
            session=session,
            note_id=int(note_id))
    title = note_data.title
    text = note_data.text
    await NoteState.ID.set()
    await state.set_data({
        "NoteID": note_id,
        "Title": title,
        "Text": text,
        "MessageID": cb.message.message_id})
    await cb.answer()
    await cb.message.edit_text(
            text=f"<b>{title}:</b>\n\n<code>{text}</code>",
            reply_markup=note_kb())


def reg_show_note(dp: Dispatcher):
    dp.register_callback_query_handler(
            show_chosen_note,
            show_note.filter(),
            state="*")


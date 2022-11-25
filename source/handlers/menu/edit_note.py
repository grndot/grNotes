from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext

from source.states.note import NoteState


async def edit_chosen_note(
        cb: types.CallbackQuery,
        state: FSMContext):
    
    state_data = await state.get_data()
    title = state_data.get("Title")
    text = state_data.get("Text")
    
    output = [
            f"<b>{title}</b>: (Edit-mode)",
            "(Type /cancel for canceling changes)",
            "",
            "",
            f"<code>{text}</code>"]

    await cb.answer()
    await cb.message.edit_text(
            text="\n".join(output))
    await NoteState.Edit.set()


def reg_edit_chosen_note(
        dp: Dispatcher):
    dp.register_callback_query_handler(
            edit_chosen_note,
            text="edit_note",
            state=NoteState.ID)

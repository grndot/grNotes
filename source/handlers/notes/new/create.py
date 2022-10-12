from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext

from source.keyboards.list import create_new_note_keyboard
from source.states.createnote import CreatingNoteState


async def create_note(
        cb: types.CallbackQuery,
        state: FSMContext):
    await cb.answer()
    await cb.message.edit_text(
            text="Create name of your note",
            reply_markup=create_new_note_keyboard())
    await CreatingNoteState.Title.set()
    await state.update_data(
            {"main_menu_message_id": cb.message.message_id})


def reg_create_note(dp: Dispatcher):
    dp.register_callback_query_handler(
            create_note,
            callback_data="create",
            state="*")

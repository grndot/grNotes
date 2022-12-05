from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext

from source.keyboards.creating import create_new_note_keyboard
from source.middlewares.i18n import get_text
from source.states.createnote import CreatingNoteState


async def create_note(
        cb: types.CallbackQuery,
        state: FSMContext):
    await cb.answer()
    await cb.message.edit_text(
            text=get_text("Create name of new note\n\n\n(Max. lenght is 64 symbols!)"),
            reply_markup=create_new_note_keyboard())
    await CreatingNoteState.Title.set()
    await state.update_data(
            {"main_menu_message_id": cb.message.message_id})


def reg_create_note(dp: Dispatcher):
    dp.register_callback_query_handler(
            create_note,
            text="create",
            state="*")

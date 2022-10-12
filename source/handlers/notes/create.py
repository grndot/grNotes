from aiogram import types, Dispatcher

from source.keyboards.list import back_to_list_keyboard
from source.states.createnote import CreatingNoteState


async def create_note(cb: types.CallbackQuery):
    await cb.answer()
    await cb.message.edit_text(
            text="Create name of your note",
            reply_markup=back_to_list_keyboard())
    await CreatingNoteState.Name.set()


def reg_create_note(dp: Dispatcher):
    dp.register_callback_query_handler(
            create_note,
            callback_data="create")

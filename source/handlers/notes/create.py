from aiogram import types, Dispatcher

from source.keyboards.list import list_of_notes_keyboard


async def create_note(cb: types.CallbackQuery):
    await cb.answer()
    await cb.message.edit_text(
            text="Create name of your note",
            reply_markup=list_of_notes_keyboard())


def reg_create_note(dp: Dispatcher):
    dp.register_callback_query_handler(
            create_note,
            callback_data="create")

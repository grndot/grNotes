from aiogram import types, Dispatcher

from source.keyboards.menu import show_note



async def show_note(
        cb: types.CallbackQuery,
        callback_data: dict,
        session: AsyncSession):

   current_note = callback_data.get("note_id")
   await cb.answer()
   await cb.message.edit_text(
           text="",
           reply_markup=[])

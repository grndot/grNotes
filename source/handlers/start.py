from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext

from source.keyboards.start import start_kb


async def start(
        instance: types.Message|types.CallbackQuery, 
        state: FSMContext):
    await state.reset_state(with_data=True)
    if isinstance(instance, types.Message):
        await instance.delete()
        await instance.answer(
                text="This is grnNotes!",
                reply_markup=start_kb())
    if isinstance(instance, types.CallbackQuery):
        await instance.message.edit_text(
                text="This is grnNotes!",
                reply_markup=start_kb())


def reg_start(dp: Dispatcher):
    dp.register_callback_query_handler(
            start,
            text="start",
            state="*")
    dp.register_message_handler(
            start,
            commands=["start"],
            state="*")

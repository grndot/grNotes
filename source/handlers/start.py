from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.utils.exceptions import MessageToEditNotFound

from source.keyboards.start import start_kb


async def start(
        instance: types.Message|types.CallbackQuery, 
        state: FSMContext):
    text = ["This is grnNotes!",
            "",
            "",
            "How do you want to login?"
            ]
    await state.reset_state(with_data=True)
    if isinstance(instance, types.Message):
        await instance.delete()
        try:
            await instance.edit_text(
                text="\n".join(text),
                reply_markup=start_kb())
        except MessageToEditNotFound:
            await instance.answer(
                text="\n".join(text),
                reply_markup=start_kb())
    if isinstance(instance, types.CallbackQuery):
        await instance.message.edit_text(
                text="\n".join(text),
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

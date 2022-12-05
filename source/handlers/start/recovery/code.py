from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext

from source.keyboards.start import start_kb
from source.middlewares.i18n import get_text
from source.states.coderecovery import CodeRecoveryState


async def get_recovery_code(
        cb: types.CallbackQuery,
        state: FSMContext):
    await cb.message.edit_text(
            text=get_text("Input your recovery code"),
            reply_markup=start_kb(is_back=True))
    await CodeRecoveryState.Input.set()
    await state.set_data({"message_id": cb.message.message_id})


def reg_get_recovery_code(dp: Dispatcher):
    dp.register_callback_query_handler(
            get_recovery_code,
            text="recovery",
            state="*")

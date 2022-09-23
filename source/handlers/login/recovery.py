from aiogram import types, Dispatcher

from source.keyboards.start import start_kb
from source.states.coderecovery import CodeRecoveryState


async def get_recovery_code(
        cb: types.CallbackQuery):
    await cb.message.edit_text(
            text="Input your recovery code",
            reply_markup=start_kb(is_back=True))
    await CodeRecoveryState.Input.set()


def reg_get_recovery_code(dp: Dispatcher):
    dp.register_callback_query_handler(
            get_recovery_code,
            text="recovery")

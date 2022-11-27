from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.types import Message
from sqlalchemy.ext.asyncio import AsyncSession
from source.keyboards.setting_delete import set_delete_kb
from source.services.db.users import (
        checkRecoveryKey,
        delUserByTelegramID)

from source.states.deleteall import DeleteState


async def check_delete_all(
        msg: Message,
        session: AsyncSession,
        state: FSMContext):
    await msg.delete()
    if await checkRecoveryKey(
                session=session,
                key=msg.text):
        data_from_state: dict[str,int]  = await state.get_data()
        message_id: int = data_from_state.get("MessageID")
        await delUserByTelegramID(
                    session=session,
                    telegram_id=msg.from_user.id)
        await msg.chat.delete_message(message_id=message_id)
    else:   
        text = msg.text.split("\n")
        text[-1] += '(Incorrect code, try again or press "Back")'
        await msg.edit_text(
                text="\n".join(text),
                reply_markup=set_delete_kb())

def reg_check_delete_all(
        dp: Dispatcher):
    dp.register_message_handler(
            check_delete_all,
            state=DeleteState.Check)

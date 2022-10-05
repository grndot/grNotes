from aiogram import Bot, types, Dispatcher
from aiogram.dispatcher import FSMContext
from sqlalchemy.ext.asyncio import AsyncSession
from source.config import load_config

from source.keyboards.start import start_kb
from source.services.db.users import (
    selectRecoveryCode)
from source.states.coderecovery import CodeRecoveryState


async def check_recovery_code(
        msg: types.Message,
        state: FSMContext,
        session: AsyncSession):
    
    token = load_config().tg_bot.token
    data = await state.get_data()
    await msg.delete()

    if await selectRecoveryCode(
            session, 
            msg.text):
        text = [
                "OK!",
                "",
                "",
                "Press button below."]
        await Bot(token=token).edit_message_text(
                chat_id=msg.chat.id,
                message_id=data.get("message_id"),
                text="\n".join(text),
                reply_markup=start_kb(is_menu=True))
        await state.reset_state(with_data=True)
      
    else:  
        text = [  
                "Your code isn't correct!",
                "",
                "",
                "Try again or get back!"
                ] 
        await Bot(token=token).edit_message_text(
                chat_id=msg.chat.id,
                message_id=data.get("message_id"),
                text="\n".join(text),
                reply_markup=start_kb(is_back=True))


def reg_check_recovery_code(dp: Dispatcher):
    dp.register_message_handler(
            check_recovery_code,
            state=CodeRecoveryState.Input)

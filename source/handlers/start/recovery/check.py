from aiogram import Bot, types, Dispatcher
from aiogram.dispatcher import FSMContext
from sqlalchemy.ext.asyncio import AsyncSession
from source.config import load_config

from source.keyboards.start import start_kb
from source.services.db.notes import updateOwnerID
from source.services.db.users import (
    checkRecoveryKey,
    getIDbyRecoveryKey,
    getIDbyTelegramID,
    updateUserRecoveryKey)
from source.services.generators.key import generate_key
from source.states.coderecovery import CodeRecoveryState


async def check_recovery_code(
        msg: types.Message,
        state: FSMContext,
        session: AsyncSession):

    data = await state.get_data()
    inline_keyboard = start_kb(is_menu=True)
    text = [
        "OK!",
        "",
        "",
        "Press button below."]
    token = load_config().tg_bot.token
    await msg.delete()

    if await checkRecoveryKey(
            session, 
            msg.text):
        new_id = await getIDbyTelegramID(
                    session=session,
                    telegram_id=msg.from_user.id)
        old_id = await getIDbyRecoveryKey(
                    session=session,
                    recovery_key=msg.text)
        if new_id != old_id:
            await updateOwnerID(
                    session=session,
                    old_id=old_id,
                    new_id=new_id)
            await updateUserRecoveryKey(
                    session=session,
                    recovery_key=msg.text,
                    new_recovery_key=generate_key(msg.from_user.id))
            text[2] = "Your key has been updated."
        else:
            text[2] = "Your key remains the same."
        await state.reset_state(with_data=True)
      
    else:  
        inline_keyboard = start_kb(is_back=True)
        text[0] = "Your code isn't correct!"
        text[-1] = "Try again or get back!"
    
    await Bot(token=token).edit_message_text(
        chat_id=msg.chat.id,
        message_id=data.get("message_id"),
        text="\n".join(text),
        reply_markup=inline_keyboard)


def reg_check_recovery_code(dp: Dispatcher):
    dp.register_message_handler(
            check_recovery_code,
            state=CodeRecoveryState.Input)

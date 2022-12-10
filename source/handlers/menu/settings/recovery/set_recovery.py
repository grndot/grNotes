from aiogram import Dispatcher
from aiogram.types import CallbackQuery
from sqlalchemy.ext.asyncio import AsyncSession

from source.keyboards.setting_recovery import recovery_set_kb
from source.middlewares.i18n import get_text
from source.services.db.users import (
        getRecoveryKeyByTelegramID, 
        updateUserRecoveryKey)
from source.services.generators.key import generate_key

async def set_recovery_code(
        cb: CallbackQuery,
        session: AsyncSession):
    
    recovery_key: str = await getRecoveryKeyByTelegramID(
            session=session,
            telegram_id=cb.from_user.id)

    await cb.answer()
    if cb.data == "reset_recovery_code":
        new_recovery_key: str = generate_key(telegram_id=cb.from_user.id)
        await updateUserRecoveryKey(
                    session=session,
                    recovery_key=recovery_key,
                    new_recovery_key=new_recovery_key)
        recovery_key = new_recovery_key

    text = [
            get_text('<b>Your recovery key:</b> <code>{rk}</code>').format(rk=recovery_key),
            '',
            '',
            '',
            get_text('The recovery key is needed to restore access to notes from another Telegram account of to delete an account.')]

    await cb.message.edit_text(
            text="\n".join(text),
            reply_markup=recovery_set_kb(),
            parse_mode="html")



def reg_set_recovery_code(dp: Dispatcher):
    dp.register_callback_query_handler(
            set_recovery_code,
            text="recovery_settings")
    dp.register_callback_query_handler(
            set_recovery_code,
            text="reset_recovery_code")


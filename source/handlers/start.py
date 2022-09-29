from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from sqlalchemy.ext.asyncio import AsyncSession

from source.keyboards.start import start_kb
from source.services.db.users import checkUserExists, insertNewUser
from source.services.generators.key import generate_key


async def start(
        instance: types.Message|types.CallbackQuery, 
        state: FSMContext,
        session: AsyncSession):
    
    text = "Notes by grn."
    
    await state.reset_state(with_data=True)
    
    if isinstance(instance, types.Message):
        await instance.delete()
        await instance.answer(
                text=text,
                reply_markup=start_kb())
    
    if isinstance(instance, types.CallbackQuery):
        if not checkUserExists(
                session=session,
                telegram_id=instance.from_user.id):
            await insertNewUser(
                    session=session,
                    telegram_id=instance.from_user.id,
                    language_id=1,
                    recovery_key=generate_key(
                        instance.from_user.id)) 
        await instance.answer()
        await instance.message.edit_text(
                text=text,
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

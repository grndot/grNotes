from aiogram import types, Dispatcher
from sqlalchemy.ext.asyncio import AsyncSession

from source.keyboards.menu import menu_kb
from source.services.db.users import checkUserExists, insertNewUser
from source.services.generators.key import generate_key


async def main_menu(
        cb: types.CallbackQuery,
        session: AsyncSession):
    text = [
            "Notes by grn.",
            "",
            "",
            "Just use it."
            ]
    if not await checkUserExists(
            session=session,
            telegram_id=cb.from_user.id):
        await insertNewUser(
                session=session,
                telegram_id=cb.from_user.id,
                language_id=1,
                recovery_key=generate_key(
                    cb.from_user.id)) 
    await cb.answer()
    await cb.message.edit_text(
            text="\n".join(text),
            reply_markup=menu_kb())


def reg_main_menu(dp: Dispatcher):
    dp.register_callback_query_handler(
            main_menu,
            text="main_menu")

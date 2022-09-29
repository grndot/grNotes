from aiogram import types, Dispatcher

from source.keyboards.menu import menu_kb


async def main_menu(cb: types.CallbackQuery):
    text = [
            "Notes by grn.",
            "",
            "",
            "Just use it."
            ]
    await cb.answer()
    await cb.message.edit_text(
            text="\n".join(text),
            reply_markup=menu_kb())


def reg_main_menu(dp: Dispatcher):
    dp.register_callback_query_handler(
            main_menu,
            text="menu")

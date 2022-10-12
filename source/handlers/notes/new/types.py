from aiogram import types, Bot, Dispatcher
from aiogram.dispatcher import FSMContext
from source.config import load_config
from source.keyboards.list import create_new_note_keyboard

from source.states.createnote import CreatingNoteState


async def choose_type_of_note(
        msg: types.Message,
        state: FSMContext):
    data = await state.get_data()
    title = msg.text
    token = load_config().tg_bot.token
    text = [
            # text[0] - for True
            [
                f"Choose type for {msg.text} note",
                "",
                "",
                ""],
            # text[1] - for False
            [
                "Your leght of title more than 64 symbols",
                "",
                "",
                "Try again or press \"Back\" button"
                ]]
    if len(title) <= 64:
        await Bot(token=token).edit_message_text(
                chat_id=msg.chat.id,
                message_id=data.get("main_menu_message_id"),
                text="\n".join(text[0]),
                reply_markup=create_new_note_keyboard(
                    title_is_64_symbols=True))
    else:
       pass 


def reg_choose_type_of_note(dp: Dispatcher):
    dp.register_message_handler(
            choose_type_of_note,
            state=CreatingNoteState.Title)

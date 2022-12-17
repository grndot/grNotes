from aiogram import types, Bot, Dispatcher
from aiogram.dispatcher import FSMContext

from source.config import load_config
from source.keyboards.creating import create_new_note_keyboard
from source.middlewares.i18n import get_text
from source.states.createnote import CreatingNoteState


async def check_title_of_note(
        msg: types.Message,
        state: FSMContext):
    
    data = await state.get_data()
    text = [
            # text[0] - for True
            [
                get_text('<code>{txt}</code> is a good title for note!'.format(txt=msg.text)),
                '',
                '',
                get_text("Press <b>Save</b> button to continue"),
                ],
            # text[1] - for False
            [
                get_text("Length of title cannot be more than 64 symbols!"),
                '',
                '',
                get_text('Try again...')
                ]]
    title = msg.text
    token = load_config().tg_bot.token
    await msg.delete()
    if len(title) <= 64:
        await Bot(token=token).edit_message_text(
                chat_id=msg.chat.id,
                message_id=data.get("main_menu_message_id"),
                text="\n".join(text[0]),
                reply_markup=create_new_note_keyboard(
                   is_title_correct=True),
                parse_mode="HTML")
        await CreatingNoteState.Saving.set()
        await state.set_data({"title": msg.text})
    else:
       await Bot(token=token).edit_message_text(
                chat_id=msg.chat.id,
                message_id=data.get("main_menu_message_id"),
                text="\n".join(text[1]),
                reply_markup=create_new_note_keyboard()) 


def reg_check_title_of_note(dp: Dispatcher):
    dp.register_message_handler(
            check_title_of_note,
            state=CreatingNoteState.Title)

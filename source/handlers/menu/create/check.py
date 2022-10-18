from aiogram import types, Bot, Dispatcher
from aiogram.dispatcher import FSMContext
from source.config import load_config
from source.keyboards.list import create_new_note_keyboard

from source.states.createnote import CreatingNoteState


async def choose_type_of_note(
        msg: types.Message,
        state: FSMContext):
    
    data = await state.get_data()
    text = [
            # text[0] - for True
            [
                f'<code>{msg.text}</code> is a good title for note!',
                '',
                '',
                'Press "Save" button to continue',
                ],
            # text[1] - for False
            [
                'Lenght of title cannot be more than 64 symobls!',
                '',
                '',
                'Try again...'
                ]]
    title = msg.text
    token = load_config().tg_bot.token
    
    if len(title) <= 64:
        await Bot(token=token).edit_message_text(
                chat_id=msg.chat.id,
                message_id=data.get("main_menu_message_id"),
                text="\n".join(text[0]),
                reply_markup=create_new_note_keyboard(
                   is_title_correct=True),
                parse_mode="HTML")
        await CreatingNoteState.Saving.set()
    
    else:
       await Bot(token=token).edit_message_text(
                chat_id=msg.chat.id,
                message_id=data.get("main_menu_message_id"),
                text="\n".join(text[1]),
                reply_markup=create_new_note_keyboard()) 


def reg_choose_type_of_note(dp: Dispatcher):
    dp.register_message_handler(
            choose_type_of_note,
            state=CreatingNoteState.Title)

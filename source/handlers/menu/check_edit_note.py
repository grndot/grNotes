from aiogram import Bot, types, Dispatcher
from aiogram.dispatcher import FSMContext
from sqlalchemy.ext.asyncio import AsyncSession
from source.config import load_config
from source.keyboards.note import note_kb
from source.services.db.notes import updateTextByNoteID

from source.states.note import NoteState


async def check_changes(
        msg: types.Message,
        session: AsyncSession,
        state: FSMContext):
    
    state_data = await state.get_data()
    title = state_data.get("Title")
    text = state_data.get("Text")
    message_id = state_data.get("MessageID")
    note_id = int(state_data.get("NoteID"))

    output_markup: types.InlineKeyboardMarkup
    output_text = [
            f'<b>{title}:</b>',
            '',
            f'<code>{text}</code>']

    if msg.text == "/cancel":
        await NoteState.ID.set() 
        output_markup = note_kb()
    else: 
        output_markup = note_kb(True)
        output_text[0] += ' (Saved)'
        output_text[-1] = msg.text
        await updateTextByNoteID(
                session=session,
                text=msg.text,
                note_id=note_id)
        await state.reset_state(with_data=True)

    await msg.delete()
    await Bot(
            token=load_config().tg_bot.token
            ).edit_message_text(
                chat_id=msg.chat.id,
                message_id=message_id,
                text='\n'.join(output_text),
                reply_markup=output_markup,
                parse_mode="html")


def reg_check_changes(
        dp: Dispatcher):
    dp.register_message_handler(
            check_changes,
            state=NoteState.Edit)


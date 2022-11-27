from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery
from source.keyboards.setting_delete import set_delete_kb

from source.states.deleteall import DeleteState


async def set_delete_all(
        cb: CallbackQuery,
        state: FSMContext):
    
    text = [
        '<b>Do you really want to delete grnNotes account?</b>',
        '<b>This acgtion cannot be changed!</b>',
        '',
        '',
        'Enter your recovery code for continue:']

    await cb.answer()
    await DeleteState.Check.set()
    await state.set_data({"MessageID":cb.message.message_id})
    await cb.message.edit_text(
            text='\n'.join(text),
            reply_markup=set_delete_kb())



def reg_set_delete_all(
        dp: Dispatcher):
    dp.register_callback_query_handler(
            set_delete_all,
            state="*",
            text="delete_account")


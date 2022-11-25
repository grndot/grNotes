from aiogram import types, Dispatcher

from source.states.note import NoteState


async def del_chosen_note(
        cb: types.CallbackQuery,
        ):
    pass


async def reg_del_chosen_note(
        dp: Dispatcher):
    dp.register_callback_query_handler(
            del_chosen_note,
            text="del_note",
            state=NoteState.ID)

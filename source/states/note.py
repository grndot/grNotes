from aiogram.dispatcher.filters.state import State, StatesGroup


class NoteState(StatesGroup):
    ID = State()

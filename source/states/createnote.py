from aiogram.dispatcher.filters.state import State, StatesGroup


class CreatingNoteState(StatesGroup):
    Name = State()
    Type = State()

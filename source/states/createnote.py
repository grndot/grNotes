from aiogram.dispatcher.filters.state import State, StatesGroup


class CreatingNoteState(StatesGroup):
    Title = State()
    Saving = State() 

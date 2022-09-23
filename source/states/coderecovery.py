from aiogram.dispatcher.filters.state import State, StatesGroup


class CodeRecoveryState(StatesGroup):
    Input = State()
    Verification = State()

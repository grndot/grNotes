from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def note_kb(del_status=False) -> InlineKeyboardMarkup:
    edit_note_button = InlineKeyboardButton(
                        text="Edit",
                        callback_data="edit_note")
    delete_note_button = InlineKeyboardButton(
                        text="Delete",
                        callback_data="del_note")
    main_menu_button = InlineKeyboardButton(
                        text="Ok" if del_status else "Back",
                        callback_data="main_menu")
    keyboard = InlineKeyboardMarkup(
            row_width=2
            )
    if del_status:
        keyboard.insert(main_menu_button)
    else:
        keyboard.row(
                edit_note_button,
                delete_note_button)
        keyboard.insert(main_menu_button)

    return keyboard

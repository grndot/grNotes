from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData


def menu_kb(array, page: int = 1) -> InlineKeyboardMarkup:
    
    # Callbacks
    pagination_cb = CallbackData("paginator", "key", "page")
    show_note = CallbackData("show_note", "note_id")
    
    # Varialbles for keyboard page
    key = "notes"
    max_items_per_page = 10
    first_note_index = (page - 1) * max_items_per_page
    last_note_index = page * max_items_per_page
    current_page_text = f'<{page}>'
    first_page = 1
    first_page_text = '|← 1'
    last_page = len(array) // max_items_per_page
    last_page_text = f'{last_page} →|'
    next_page = page + 1
    next_page_text = f'{next_page} →'
    previous_page = page - 1
    previous_page_text = f'← {previous_page}'
    sliced_array = array[first_note_index:last_note_index]
    
    # Buttons 
    create_note_button = InlineKeyboardButton(
            text="Create note",
            callback_data="create")
    current_page_button =InlineKeyboardButton(
                text=current_page_text,
                callback_data=pagination_cb.new(
                    key=key,
                    page="current_page")) 
    first_page_button = InlineKeyboardButton(
            text=first_page_text,
            callback_data=pagination_cb.new(
                key=key,
                page=first_page))
    last_page_button = InlineKeyboardButton(
            text=last_page_text,
            callback_data=pagination_cb.new(
                key=key,
                page=last_page))
    next_page_button = InlineKeyboardButton(
            text=next_page_text,
            callback_data=pagination_cb.new(
                key=key,
                page=next_page))

    plug_instead_of_note_button = InlineKeyboardButton(
            text="Here could be your notes. Create it below! ( •͡˘ _•͡˘)ノ",
            callback_data=pagination_cb.new(
                    key=key,
                    page="current_page"))
    settings_button = InlineKeyboardButton(
            text="Settings",
            callback_data="settings")
    stub_instead_of_button = InlineKeyboardButton(
            text=".",
            callback_data=pagination_cb.new(
                key=key,
                page="current_page"))
    previous_page_button = InlineKeyboardButton(
            text=previous_page_text,
            callback_data=pagination_cb.new(
                key=key,
                page=previous_page))

    # This is part of keyboard which contains buttons for notes
    notes_buttons = [
            InlineKeyboardButton(
                text=note[0],
                callback_data=show_note.new(
                    note_id=note.id)) for note in sliced_array]
    
    # This is part of keyboard which contain buttons for pages
    pages_buttons = []
    pages_buttons.append(first_page_button)
    
    if previous_page >= first_page:
        pages_buttons.append(previous_page_button)
    else:
        pages_buttons.append(stub_instead_of_button)
    
    pages_buttons.append(current_page_button)
    
    if next_page <= last_page:
        pages_buttons.append(next_page_button)
    else:
        pages_buttons.append(stub_instead_of_button)
    
    pages_buttons.append(last_page_button)

    # Keyboard for output    
    keyboard = InlineKeyboardMarkup(
            row_width=2)
    keyboard.row(create_note_button)
    if len(notes_buttons) != 0:
        for button in notes_buttons:
            keyboard.insert(button)
        keyboard.row(*pages_buttons)
    else:
        keyboard.row(plug_instead_of_note_button)
    keyboard.row(settings_button)

    return keyboard

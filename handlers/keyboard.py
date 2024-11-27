from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

give_memes_button = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="GIFF MEMES")]
], resize_keyboard=True)


def get_keyboard(last_request: str) -> ReplyKeyboardMarkup:
    if last_request == "GIFF MEMES":
        return give_memes_button
    return ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text="GIFF MEMES")],
        [KeyboardButton(text=last_request)]
    ], resize_keyboard=True)

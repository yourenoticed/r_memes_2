from aiogram import Router, F
from aiogram.types import Message, URLInputFile
from aiogram.filters import Command, CommandStart
from handlers.keyboard import give_memes_button, get_keyboard
from utils.service import Service
import handlers.texts.texts as texts


router = Router()


@router.message(CommandStart())
async def welcome_message(message: Message):
    await send_help(message)
    await message.answer(
        text="Sup! What memes do you want today? (give a subreddit name)", reply_markup=give_memes_button)


@router.message(F.text == "GIFF MEMES")
async def button_message(message: Message):
    meme = Service.get_totally_random_meme()
    await send_file(message, meme)


@router.message(F.text == "ДАЙТЕ МЕМЫ")
async def button_message(message: Message):
    meme = Service.get_random_russian_meme()
    await send_file(message, meme)


@router.message(Command("search"))
async def search(message: Message):
    msg = message.text.split()
    service = Service()
    search_result = service.get_search(msg[1])
    if search_result:
        names = "\n".join(search_result)
        await message.reply(names)
    else:
        await message.reply("Nothing was found")


@router.message(Command("best"))
async def send_best(message: Message):
    msg = message.text.split()
    service = Service(msg[1])
    if len(msg) > 2 and msg[2].isdigit():
        memes = service.get_best_memes(int(msg[2]))
    else:
        memes = service.get_best_memes()
    for meme in memes:
        await send_file(message, meme)


@router.message(Command("hot"))
async def send_hot(message: Message):
    msg = message.text.split()
    service = Service(msg[1])
    if len(msg) > 2 and msg[2].isdigit():
        memes = service.get_hot_memes(int(msg[2]))
    else:
        memes = service.get_hot_memes()
    for meme in memes:
        await send_file(message, meme)


@router.message(Command("new"))
async def send_new(message: Message):
    msg = message.text.split()
    service = Service(msg[1])
    if len(msg) > 2 and msg[2].isdigit():
        memes = service.get_new_memes(int(msg[2]))
    else:
        memes = service.get_new_memes()
    for meme in memes:
        await send_file(message, meme)


@router.message(Command("commands"))
async def send_commands(message: Message):
    await message.answer(texts.COMMANDS)


@router.message(Command("help"))
async def send_help(message: Message):
    await message.answer(texts.COMMANDS)


@router.message()
async def send_random(message: Message):
    msg = message.text.split()
    service = Service(msg[0])
    if len(msg) == 1:
        meme = service.get_random_meme()
        await send_file(message, meme)
    elif len(msg) == 2 and msg[1].isdigit():
        for _ in range(int(msg[1])):
            meme = service.get_random_meme()
            await send_file(message, meme)
    else:
        await message.reply("This is not how you use this bot :^)")


def is_image(url: str) -> bool:
    return "i.redd.it" in url


def is_video(url: str) -> bool:
    return "v.redd.it" in url


def is_animation(url: str) -> bool:
    file_format = url.split(".")[-1].lower()
    if file_format in ["gif"]:
        return True
    return False


async def send_file(message: Message, file_url: str):
    # await message.reply(file.url)
    if is_image(file_url):
        file = URLInputFile(file_url)
        await message.reply_photo(file, reply_markup=get_keyboard(message.text))
    elif is_video(file_url):
        file_url = file_url + "/DASH_480.mp4"
        await message.reply(file_url, reply_markup=get_keyboard(message.text))
    elif is_animation(file_url):
        await message.reply(file_url, reply_markup=get_keyboard(message.text))

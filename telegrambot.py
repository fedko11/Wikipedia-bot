import asyncio
import logging
import sys
from os import getenv

from aiogram import Bot, Dispatcher, html,F
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
from config import Token
import wikipedia



TOKEN = Bot(token=Token)


dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Salom, {html.bold(message.from_user.full_name)} siz qidiruvga lyuboy narsani yozing >>> Men sizga ma'lumot topib beraman!")

@dp.message(F.text.lower() == "salom")
async def Info(message:Message):
    text = message.text
    await message.reply(f"{html.bold(message.from_user.full_name)} >>> Xabar yozing men ma'lumot beraman!")

@dp.message(F.text)
async def wikipediaBot(message:Message):
    text = message.text
    wikipedia.set_lang('uz')
    izlash = wikipedia.summary(text)
    await message.reply(text=izlash)
    
        
    
@dp.message()
async def main() -> None:
    
    bot = Bot(token=Token, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
   
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
    
    
    
    
    
    
    
    



    
        
    






















    
    
    
    
    
    
    
    
    
    
    
    
    

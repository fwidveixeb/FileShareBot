import os
import requests
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

BOT_TOKEN = os.environ.get("BOT_TOKEN")
API_ID = int(os.environ.get("API_ID"))
API_HASH = os.environ.get("API_HASH")
BOT_USERNAME = os.environ.get("BOT_USERNAME")

Bot = Client(
    "File Store Bot",
    bot_token=BOT_TOKEN,
    api_id=API_ID,
    api_hash=API_HASH
)
@Bot.on_message(filters.command('start'))
async def start(bot, message):
    if len(message.command) == 1:
        await message.reply(
            text=f"Hello {message.from_user.mention}, I am a Powerful File Store Bot devoloped by @Hagadmansa.\n\nJust send me any photo, video, voice, audio, document, sticker, animation or videonote, i'll share you you it's permanent link.",
            reply_markup=InlineKeyboardMarkup(
        [[
            InlineKeyboardButton('Updates', url='https://t.me/hagadmansa'),
            InlineKeyboardButton('Support', url='https://t.me/hagadmansachat')
            ],[
            InlineKeyboardButton('Website', url='https://hagadmansa.com'),
            InlineKeyboardButton('Source', url='https://github.com/hagadmansa/FileStoreBot')
            ]])
        )
    elif len(message.command) == 2:
        try:
            teri = requests.get(f"https://open-apis-rest.up.railway.app/api/nekobinget?url=https://nekobin.com/{message.command[1]}").json()
            nani = teri['data']
            link = f"https://t.me/{BOT_USERNAME}?start={nani}"
            share = f"https://t.me/share/url?url={link}&text=Click%20on%20link%20to%20get%20the%20file%20now,%20Join%20@Hagadmansa"
            await message.reply_cached_media(
                file_id=nani,
                caption='Join @Hagadmansa',
                reply_markup=InlineKeyboardMarkup(
                [[
                  InlineKeyboardButton('Share now', url=share)
                ]])
            )
        except:
            await message.reply('The media you are trying to send is invalid.')
            
@Bot.on_message(filters.private)
async def hagadmansa(bot, message):
  if message.text:
      return 
  hagadmansa = await message.reply("`Processing...`")
  media = message.photo or message.video or message.voice or message.document or message.animation or message.audio or message.sticker or message.VideoNote
  mere = requests.get(f"https://open-apis-rest.up.railway.app/api/nekobin?text={media.file_id}").json()
  mosa = mere['data']['detail']['key']
  link = f"https://t.me/{BOT_USERNAME}?start={mosa}"
  share = f"https://t.me/share/url?url={link}&text=Click%20on%20link%20to%20get%20the%20file%20now,%20Join%20@Hagadmansa"
  await hagadmansa.edit(
    text=f"Here is your link: {link}",
    reply_markup=InlineKeyboardMarkup(
        [[
            InlineKeyboardButton('Share now', url=share)
        ]])
  )
    
Bot.run()

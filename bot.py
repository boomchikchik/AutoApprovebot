import os, random, traceback
import config
import asyncio

from pyrogram import filters, Client
from pyrogram.types import Message, ChatJoinRequest, InlineKeyboardButton, InlineKeyboardMarkup 
from pyrogram.errors import FloodWait, InputUserDeactivated, UserIsBlocked, PeerIdInvalid, ChatAdminRequired, UserNotParticipant
from pyrogram.enums import ChatMemberStatus
from database import add_user, add_group, all_users, all_groups, users, remove_user

app = Client("Auto Approve Bot", api_id=config.API_ID, api_hash=config.API_HASH, bot_token=config.BOT_TOKEN)
bot = Client("acceptor", api_id=config.API_ID, api_hash=config.API_HASH, session_string="BQDJqkIAIXQmiPFJu3UUSFWAXyjX30_P2YTj1YY_ryRQkgszOYbqig2nFveFdKtHzv6CDnmej9I6Rt7-VZrStQXqTY-Y1uusEkIowouxj6Nh307dDYDFtO75BRIkX-m-DLq8yhsqmZAXki6hmdAG2qshleFNtUdOGBBZusZV9V7c_sI4gqf_g28WRimKIfvP65Q48UuvPeu6_LCIozb12nwVu-U2kNMbJ8FcNveaPx513_0ldYlyeNzmAgN3ENuCia6-hSjhft4IfvZZun9KPqAV_PkM6YCPPprOKqZGyHW33FF1CH3RVf3CrX2pixVEgitvy3_K7vEKA6MjnynKcro8K6GHfwAAAAGX1VKSAA")

welcome=[
    "https://telegra.ph/file/51d04427815840250d03a.mp4",
    "https://telegra.ph/file/f41fddb95dceca7b09cbc.mp4",
    "https://telegra.ph/file/a66716c98fa50b2edd63d.mp4",
    "https://telegra.ph/file/17a8ab5b8eeb0b898d575.mp4",
]

#approve 
#@app.on_chat_join_request()
#async def approval(app: Client, m: ChatJoinRequest):
#    usr = m.from_user
#    cht = m.chat
#    try:
#        add_group(cht.id)
#        await app.approve_chat_join_request(cht.id, usr.id)
#        gif = random.choice(welcome)
#        await app.send_animation(chat_id=usr.id, animation=gif, caption=f"Hey There {usr.first_name}\nWelcome To {cht.title}\n\n{usr.first_name} Your Request To Join {cht.title} Has Been Accepted By {app.me.first_name}")
#        add_user(usr.id)
#    except (UserIsBlocked, PeerIdInvalid):
#        pass
#    except Exception as err:
#        print(str(err))   


#approve 
@app.on_chat_join_request()
async def approval(app: Client, m: ChatJoinRequest):
    usr = m.from_user
    cht = m.chat
    try:
        # Add a delay after each approval
        #await asyncio.sleep(5)  # Adjust the delay time as needed
        add_group(cht.id)
        await app.approve_chat_join_request(cht.id, usr.id)
        gif = random.choice(welcome)
        await app.send_animation(chat_id=usr.id, animation=gif, caption=f"Hey There {usr.first_name}\nWelcome To {cht.title}\n\n{usr.first_name} Your Request To Join {cht.title} Has Been Accepted By {app.me.first_name}")
        add_user(usr.id)
        
        # Add a delay after each approval
        await asyncio.sleep(10)  # Adjust the delay time as needed
        
    except (UserIsBlocked, PeerIdInvalid):
        pass
    except Exception as err:
        print(str(err))  
        


#pvtstart
@app.on_message(filters.command("start") & filters.private)
async def start(app: Client, msg: Message):
    if config.FSUB:
        try:
            await app.get_chat_member(chat_id=config.CHANNEL, user_id=msg.from_user.id)
            add_user(msg.from_user.id)
            await msg.reply_photo(photo="https://telegra.ph/file/f394c45e5f2f147a37090.jpg", caption=f"Hᴇʟʟᴏ {msg.from_user.mention}💞,\n\n☉︎ Tʜɪs ɪs {app.me.mention},\n\n➲ A ᴛᴇʟᴇɢʀᴀᴍ ʙᴏᴛ ᴍᴀᴅᴇ ғᴏʀ ᴀᴜᴛᴏ ᴀᴘᴘʀᴏᴠɪɴɢ ᴊᴏɪɴ ʀᴇǫᴜᴇsᴛ ɪɴ ɢʀᴏᴜᴘ/ᴄʜᴀɴɴᴇʟ.\n\n➲ Jᴜsᴛ ᴀᴅᴅ {app.me.mention} ɪɴ ɢʀᴏᴜᴘs/ᴄʜᴀɴɴᴇʟs ᴀɴᴅ ᴍᴀᴋᴇ ᴀᴅᴍɪɴ ᴡɪᴛʜ ɪɴᴠɪᴛᴇ ᴜsᴇʀs ᴠɪᴀ ʟɪɴᴋ ʀɪɢʜᴛs..",
                                 reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(f"ᴀᴅᴅ {app.me.first_name}", url=f"https://t.me/{app.me.username}?startgroup=true")], [InlineKeyboardButton("ᴄʜᴀɴɴᴇʟ", url=f"https://t.me/{config.CHANNEL}")]]))
        except UserNotParticipant:
            await msg.reply_text(text=f"To Use {app.me.mention}, You Must Subscribe To {(await app.get_chat(config.CHANNEL)).title}", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Join", url=f"https://t.me/{config.CHANNEL}")], [InlineKeyboardButton ("Joined ✅", url=f"https://t.me/{app.me.username}?start=start")]]))
        except ChatAdminRequired:
            await app.send_message(text=f"I'm not admin in fsub chat, Ending fsub...", chat_id=config.OWNER_ID)
    else:
        await msg.reply_photo(
            photo="https://telegra.ph/file/f394c45e5f2f147a37090.jpg",
            caption=f"Hᴇʟʟᴏ {msg.from_user.mention}💞,\n\n☉︎ Tʜɪs ɪs {app.me.mention},\n\n➲ A ᴛᴇʟᴇɢʀᴀᴍ ʙᴏᴛ ᴍᴀᴅᴇ ғᴏʀ ᴀᴜᴛᴏ ᴀᴘᴘʀᴏᴠɪɴɢ ᴊᴏɪɴ ʀᴇǫᴜᴇsᴛ ɪɴ ɢʀᴏᴜᴘ/ᴄʜᴀɴɴᴇʟ.\n\n➲ Jᴜsᴛ ᴀᴅᴅ {app.me.mention} ɪɴ ɢʀᴏᴜᴘs/ᴄʜᴀɴɴᴇʟs ᴀɴᴅ ᴍᴀᴋᴇ ᴀᴅᴍɪɴ ᴡɪᴛʜ ɪɴᴠɪᴛᴇ ᴜsᴇʀs ᴠɪᴀ ʟɪɴᴋ ʀɪɢʜᴛs.",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(f"ᴀᴅᴅ {app.me.first_name}", url=f"https://t.me/{app.me.username}?startgroup=true")
                    ],
                    [
                        InlineKeyboardButton("ᴄʜᴀɴɴᴇʟ", url=f"https://t.me/ZenBotX")
                    ],
                ]
            )
        )
        add_user(msg.from_user.id)
        

#Gcstart and id
@app.on_message(filters.command("start") & filters.group)
async def gc(app: Client, msg: Message):
    add_group(msg.chat.id)
    add_user(msg.from_user.id)
    await msg.reply_text(text=f"{msg.from_user.mention} Start Me In Private For More Info..", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Start Me In Private", url=f"https://t.me/{app.me.username}?start=start")]]))

#stats
@app.on_message(filters.command("stats") & filters.user(config.OWNER_ID))
async def dbtool(app: Client, m: Message):
    xx = all_users()
    x = all_groups()
    await m.reply_text(text=f"Stats for {app.me.mention}\n🙋‍♂️ Users : {xx}\n👥 Groups : {x}")

#Broadcast
@app.on_message(filters.command("fbroadcast") & filters.user(config.OWNER_ID))
async def fcast(_, m : Message):
    allusers = users
    lel = await m.reply_text("`⚡️ Processing...`")
    success = 0
    failed = 0
    deactivated = 0
    blocked = 0
    for usrs in allusers.find():
        try:
            userid = usrs["user_id"]
            #print(int(userid))
            if m.command[0] == "fbroadcast":
                await m.reply_to_message.forward(int(userid))
            success +=1
        except FloodWait as ex:
            await asyncio.sleep(ex.value)
            if m.command[0] == "fbroadcast":
                await m.reply_to_message.forward(int(userid))
        except InputUserDeactivated:
            deactivated +=1
            remove_user(userid)
        except UserIsBlocked:
            blocked +=1
        except Exception as e:
            print(e)
            failed +=1

    await lel.edit(f"✅Successful Broadcast to {success} users.\n❌ Failed to {failed} users.\n👾 Found {blocked} Blocked users \n👻 Found {deactivated} Deactivated users.")
    

@app.on_message(filters.command("massapprove") & filters.private)
async def approve_pending_requests(app: Client, m: Message):
    if len(m.command) < 2:
        return await m.reply_text("❌ Please provide a group/channel ID.\nExample: `/massapprove -100xxxxxxxxxx`", quote=True)

    chat_id = m.command[1]
    chat_id=int(chat_id)

    try:
        await bot.start()  # Start the user session
        chat = await bot.get_chat(chat_id)
        approved_count = 0

        async for req in bot.get_chat_join_requests(chat_id):
            try:
                try:  
                    await bot.approve_chat_join_request(chat_id, req.user.id)
                except Exception as e:
                    print(f"FAILED TO APPROVE USER \n ERROR: {e}")
                gif = random.choice(welcome)
                try:
                    await app.send_animation(
                        chat_id=req.user.id,
                        animation=gif,
                        caption=f"Hey {req.user.first_name},\nYour request to join **{chat.title}** has been approved!"
                    )
                except:
                    print("MEDIA NOT SENT")
                    
                
                approved_count += 1
                await asyncio.sleep(3)
                print(approved_count)
            except Exception as e:
                print(f"❌ Error approving user {req.user.id}: {e}")


        await m.reply_text(f"✅ Approved **{approved_count}** users in **{chat.title}**!")

    except Exception as e:
        print(f"❌ Error- 2: {e}")
        await m.reply_text("❌ Failed. Please make sure:\n- Chat ID is correct\n- You're the **channel owner**\n- User session is admin in the channel")

    finally:
        await bot.stop()



#run
print(f"Starting {app.name}")
try:
    app.run()
except:
    traceback.print_exc()

from main import cmd

welcome_image = 'https://i.imgur.com/2Co5ddF.jpeg'

def start(msg, bot, i):
    user_first_name = msg.from_user.first_name
    username = f"@{msg.from_user.username}" if msg.from_user.username else "N/A"
    user_id = msg.from_user.id
    user_language = msg.from_user.language_code if msg.from_user.language_code else "N/A"
    user_link = f"[{user_first_name}](tg://user?id={user_id})"

    welcome_message = f"""
☘️ Nᴀᴍᴇ : {user_first_name}

🔥 Uꜱᴇʀɴᴀᴍᴇ : {username}

🎁 Uꜱᴇʀ Iᴅ : {user_id}

🔠 **Uꜱᴇʀ Lᴀɴɢᴜᴀɢᴇ :** {user_language}

🔗 Uꜱᴇʀ Lɪɴᴋ : {user_link}

☄️ Pᴇʀᴍᴀɴᴇɴᴛ Lɪɴᴋ : [Click Here](tg://user?id={user_id})

ᴡᴇʟᴄᴏᴍᴇ to ɴᴀꜱʜʙᴏᴛ We're excited to have you here.  

Enjoy, mother fucker! 😎
"""
    bot.send_photo(msg.chat.id, welcome_image, caption=welcome_message, parse_mode='Markdown')

config = {
    "name": 'start',
    "credits": 'joshua Apostol',
    "usage": '/start',
    "description": 'Start the bot',
    "def": start
}

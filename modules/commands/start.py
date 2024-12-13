from main import cmd

welcome_image = 'https://i.imgur.com/2Co5ddF.jpeg'

def start(msg, bot, i):
    welcome_message = f"""
Welcome to NashBot

Hello, {msg.from_user.first_name}! We're excited to have you here.

How to use the bot:
- For help on other commands, type /help.

Enjoy mother fucker!
"""
    bot.send_photo(msg.chat.id, welcome_image, caption=welcome_message, parse_mode='Markdown')

config = {
    "name": 'start',
    "credits": 'joshua Apostol',
    "usage": '/start',
    "description": 'Start the bot',
    "def": start
}


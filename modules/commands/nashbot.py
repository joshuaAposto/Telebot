import requests

def nashbot(msg, bot, i):
    if not i.text or not i.text.strip():
        return bot.send_message(msg.chat.id, "Please provide a query.")
    
    query = i.text.strip()
    url = f'https://nash-api.onrender.com/api/nashbot?q={query}'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        result = data.get('response', 'No response found.')
        bot.send_message(msg.chat.id, f"{result}")
    else:
        bot.send_message(msg.chat.id, "❌ Error: Unable to fetch data from the API.")

config = {
    "name": 'nashbot',
    "credits": 'Joshua Apostol',
    "usage": '/nashbot <query>',
    "description": 'Chat with Nashbot AI',
    "def": nashbot
}

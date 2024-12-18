import requests

def ai(msg, bot, i):
    if not i.text or not i.text.strip():
        return bot.send_message(msg.chat.id, "Please provide a query.")

    query = i.text.strip()
    url = f'https://nash-api-vrx5.onrender.com/api/chatgpt?query={query}'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        if 'response' in data:
            result = data['response']
            bot.send_message(msg.chat.id, f"{result}")
        else:
            bot.send_message(msg.chat.id, "❌ Error: No response found")
    else:
        bot.send_message(msg.chat.id, "❌ Error: Unable to fetch")

config = {
    "name": 'ai',
    "credits": 'joshua Apostol',
    "usage": '/ai <query>',
    "description": 'Chat with ChatGpt',
    "def": ai
}
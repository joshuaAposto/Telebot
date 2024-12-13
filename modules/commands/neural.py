import requests

def neural(msg, bot, i):
    query = i.text.strip()
    if not query:
        return bot.send_message(msg.chat.id, "Please provide a query.")

    url = f'https://api.joshweb.click/ai/neural-chat-7b?q={query}&uid={msg.from_user.id}'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        if data.get('status'):
            result = data.get('result', 'No result found.')
            bot.send_message(msg.chat.id, f"{result}")
        else:
            bot.send_message(msg.chat.id, "❌ Error: No result found.")
    else:
        bot.send_message(msg.chat.id, "❌ Error: Unable to fetch data from the API.")

config = {
    "name": 'neural',
    "credits": 'joshua Apostol',
    "usage": '/neural_chat <query>',
    "description": 'Chat with Neural Chat-7B AI',
    "def": neural
}

import requests

def gemma(msg, bot, i):
    query = i.text.strip()
    if not query:
        return bot.send_message(msg.chat.id, "Please provide a query.")

    url = f'https://api.joshweb.click/api/gemma-7b?q={query}'
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
    "name": 'gemma',
    "credits": 'joshua Apostol',
    "usage": '/gemma <query>',
    "description": 'Interact With Gemma-7B',
    "def": gemma
}

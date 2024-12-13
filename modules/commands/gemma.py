import requests

def gemma(msg, bot, i):
    if not i.text or not i.text.strip():
        return bot.send_message(msg.chat.id, "Please provide a query.")

    query = i.text.strip()
    url = f'https://api.joshweb.click/api/gemma-7b?q={query}'
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            if data.get('status'):
                result = data.get('result', 'No result found.')
                bot.send_message(msg.chat.id, result)
            else:
                bot.send_message(msg.chat.id, "❌ Error: No result found.")
        else:
            bot.send_message(msg.chat.id, "❌ Error: Unable to fetch data from the API.")
    except requests.RequestException as e:
        bot.send_message(msg.chat.id, f"❌ Error: {str(e)}")

config = {
    "name": 'gemma',
    "credits": 'joshua Apostol',
    "usage": '/gemma <query>',
    "description": 'Interact With Gemma-7B',
    "def": gemma
}

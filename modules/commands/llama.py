import requests

def llama(msg, bot, i):
    if not i.text or not i.text.strip():
        return bot.send_message(msg.chat.id, "Please provide a query.")
    
    query = i.text.strip()
    url = f'https://api.joshweb.click/api/llama-3-70b?q={query}'
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
    "name": 'llama',
    "credits": 'joshua Apostol',
    "usage": '/llama <query>',
    "description": 'caht with Llama Ai',
    "def": llama
}

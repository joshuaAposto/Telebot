import requests

def gpt4(msg, bot, i):
    if not i.text or not i.text.strip():
        return bot.send_message(msg.chat.id, "Please provide a query.")
    
    query = i.text.strip()
    url = f'https://nash-api.onrender.com/api/gpt4?query={query}'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        result = data.get('response', 'No response found.')
        bot.send_message(msg.chat.id, f"{result}")
    else:
        bot.send_message(msg.chat.id, "❌ Error: Unable to fetch data from the API.")

config = {
    "name": 'gpt4',
    "credits": 'Joshua Apostol',
    "usage": '/gpt4 <query>',
    "description": 'Chat with GPT-4 AI',
    "def": gpt4
}

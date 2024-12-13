import requests

def gemini(msg, bot, i):
    if not i.text or not i.text.strip():
        return bot.send_message(msg.chat.id, "Please provide a prompt.")
    
    prompt = i.text.strip()
    url = f'https://api.joshweb.click/gemini?prompt={prompt}'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        gemini_response = data.get('gemini', 'No response found.')
        bot.send_message(msg.chat.id, f"{gemini_response}")
    else:
        bot.send_message(msg.chat.id, "❌ Error: Unable to fetch data from the API.")

config = {
    "name": 'gemini',
    "credits": 'joshua Apostol',
    "usage": '/gemini <prompt>',
    "description": ' chat with Gemini',
    "def": gemini
}

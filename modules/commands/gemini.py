import requests

def gemini(msg, bot, i):
    if not i.text or not i.text.strip():
        return bot.send_message(msg.chat.id, "Please provide a prompt.")

    prompt = i.text.strip()
    url = f'https://api.joshweb.click/gemini?prompt={prompt}'
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            gemini_response = data.get('gemini', 'No response found.')
            bot.send_message(msg.chat.id, gemini_response)
        else:
            bot.send_message(msg.chat.id, "❌ Error: Unable to fetch data from the API.")
    except requests.RequestException as e:
        bot.send_message(msg.chat.id, f"❌ Error: {str(e)}")

config = {
    "name": 'gemini',
    "credits": 'joshua Apostol',
    "usage": '/gemini <prompt>',
    "description": 'Chat with Gemini',
    "def": gemini
}

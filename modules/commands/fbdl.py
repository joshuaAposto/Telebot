import requests

def fbdl(msg, bot, i):
    if not i.text or not i.text.strip():
        return bot.send_message(msg.chat.id, "Please provide a Facebook URL.")

    url = i.text.strip()
    api_url = f'https://api.joshweb.click/facebook?url={url}'
    try:
        response = requests.get(api_url)
        if response.status_code == 200:
            data = response.json()
            video_url = data.get('result', None)
            if video_url:
                bot.send_video(msg.chat.id, video_url)
            else:
                bot.send_message(msg.chat.id, "❌ Error: Unable to find the video URL.")
        else:
            bot.send_message(msg.chat.id, "❌ Error: Unable to fetch data from the API.")
    except requests.RequestException as e:
        bot.send_message(msg.chat.id, f"❌ Error: {str(e)}")

config = {
    "name": 'fbdl',
    "credits": 'joshua Apostol',
    "usage": '/fbdl <Facebook URL>',
    "description": 'Download and send Facebook videos',
    "def": fbdl
}

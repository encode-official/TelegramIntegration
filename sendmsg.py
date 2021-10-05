import requests

def telegram_bot_sendtext(bot_message):
    bot_token = 'TelegramAPI_key'
    bot_chatID = 'BOT_id'
    img = "https://helperbyte.com/img/logo.png"
    text = "hellloooo"
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID +'&parse_mode=markdown'+'&text='+text
    response = requests.get(send_text)

    return response.json()

print(telegram_bot_sendtext("Hellllllllllllloooo"))

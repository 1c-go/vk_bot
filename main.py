import random
import time

import vk_api


token = "8c979da69ee52c11cb5376e51bd3c79ae2bc3110055afc396650571563c5852ac0fdbaa7a4b4c834b5353"

print("start")
vk = vk_api.VkApi(token=token)
vk._auth_token()


while True:
    try:
        messages = vk.method("messages.getConversations", {"offset": 0, "count": 1, "filter": "unanswered"})
        if messages["count"] == 1:
            message = messages["items"][0]["last_message"]
            id = message["from_id"]
            body = message["text"].lower()

            if body == "привет" or body == "хай" or body == "Здорова" or body == "hi" or body == "hello" :
                response = "Привет! Я чат бот Банка России! Хочешь узнать, как получить стикеры?"
            elif body == "да" or body == "ага" or body == "yes":
                response = "Чтобы получить стикеры, скачай приложение \"Сообщество Банка Россия\" и пройди любой опрос! <ссылка на маркет и апстор>."
            elif body == "нет" or body == "неа" or body == "no" or body == "не" :
                response = "Очень жаль... Но если ты передумаешь, то всегда можешь написать \"Да\" "
            elif body == "код":
                response = "Получай стикеры"
            else:
                response = "Не понял"

            vk.method("messages.send", {"peer_id": id, "message": response, "random_id": random.randint(1, 2147483647)})
    except Exception as E:
        time.sleep(1)

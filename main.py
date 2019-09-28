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
            id = messages["items"][0]["last_message"]["from_id"]
            body = messages["items"][0]["last_message"]["text"].lower()
            if body == "привет":
                response = "Привет! Я чат бот Банка Росси! Хочешь узнать как получить стикеры? Да или Нет"
            elif body == "да":
                response = "Чтобы получить стикеры скачай и пройди опрос в новоп приложении от сбербанка! Типа ссылка И введи код"
            elif body == "код":
                response = "Получай стикеры"
            else:
                response = "ЧАВООО???"
            vk.method("messages.send", {"peer_id": id, "message": response, "random_id": random.randint(1, 2147483647)})
    except Exception as E:
        time.sleep(1)

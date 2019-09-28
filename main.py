import vk_api
import random
import time


token = "8c979da69ee52c11cb5376e51bd3c79ae2bc3110055afc396650571563c5852ac0fdbaa7a4b4c834b5353"

print("start")
vk = vk_api.VkApi(token=token)

vk._auth_token()


while True:
    try:
        messages = vk.method("messages.getConversations", {"offset": 0, "count": 20, "filter": "unanswered"})
        if messages["count"] >= 1:
            id = messages["items"][0]["last_message"]["from_id"]
            body = messages["items"][0]["last_message"]["text"]
            if body.lower() == "привет":
                vk.method("messages.send", {"peer_id": id, "message": "Привет! Я чат бот Банка Росси! Хочешь узнать как получить стикеры? Да или Нет", "random_id": random.randint(1, 2147483647)})
            elif body.lower() == "да":
                vk.method("messages.send", {"peer_id": id, "message": "Чтобы получить стикеры скачай и пройди опрос в новоп приложении от сбербанка! Типа ссылка И введи код", "random_id": random.randint(1, 2147483647)})
            elif body.lower() == "код":
                vk.method("messages.send", {"peer_id": id, "message": "Получай стикеры", "random_id": random.randint(1, 2147483647)})
            else:
                vk.method("messages.send", {"peer_id": id, "message": "ЧАВООО???", "random_id": random.randint(1, 2147483647)})
    except Exception as E:
        time.sleep(1)



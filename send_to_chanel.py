import time
import telebot
import requests
import list_events

TOKEN = "2018062713:AAHwD5-D5fHqhROVJdSh7k5QaoYpyGbnPgo"
URL = "https://api.telegram.org/bot"
tb = telebot.TeleBot(TOKEN)

def send_telegram(text: str):
    token = TOKEN
    url = URL
    channel_id = "-1001597684081"
    url += token
    method = url + "/sendMessage"

    r = requests.post(method, data={
        "chat_id": channel_id,
        "text": text
    })
    print(r.json())
    if r.status_code != 200:
        print(r.json())
        raise Exception("post_text error")
    return r.json().get('message_id')


def get_history():
        token = TOKEN
        url = URL
        channel_id = "@calendarnik"
        url += token
        method = url + "/getHistory"

        r = requests.post(method, data={
            "chat_id": channel_id,
            "text": text
        })
        print(r.json())
        if r.status_code != 200:
            print(r.json())
            raise Exception("post_text error")
        return r.json()


def get_updates():
    result = requests.get(f'{URL}{TOKEN}/getUpdates').json()
    return result['result']


def deleted(message_id):
    token = TOKEN
    url = URL
    channel_id = "@calendarnik"
    url += token
    method = url + "/deleteMessage"

    r = requests.post(method, data={
        "chat_id": channel_id,
        "message_id": message_id
    })
    return r


if __name__ == '__main__':
    for i in range(90, 150):
       deleted(message_id=i)
    text = list_events.main()
    send_telegram('\n'.join([i for i in text[1:]]))

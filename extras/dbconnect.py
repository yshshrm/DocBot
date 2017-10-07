import json 
import requests
import time
# import urllib
import datetime

now = datetime.datetime.now()
print now.hour

from dbhelper2 import DBHelper

db = DBHelper()

TOKEN = "451932661:AAEjBUpVHcpE549UL1sumLaET0d_B6kHzyY"
URL = "https://api.telegram.org/bot{}/".format(TOKEN)

def get_url(url):
    response = requests.get(url)
    content = response.content.decode("utf8")
    return content

def get_json_from_url(url):
    content = get_url(url)
    js = json.loads(content)
    return js

# def get_updates():
#     url = URL + "getUpdates"
#     js = get_json_from_url(url)
#     return js
# def get_updates(offset=None):
#     url = URL + "getUpdates"
#     if offset:
#         url += "?offset={}".format(offset)
#     js = get_json_from_url(url)
#     return js
def get_updates(offset=None):
    url = URL + "getUpdates?timeout=100"
    if offset:
        url += "&offset={}".format(offset)
    js = get_json_from_url(url)
    return js

def get_last_update_id(updates):
    update_ids = []
    for update in updates["result"]:
        update_ids.append(int(update["update_id"]))
    return max(update_ids)

def handle_updates(updates):
    for update in updates["result"]:
        text = update["message"]["text"]
        chat = update["message"]["chat"]["id"]
        items = db.get_items(chat)  ##
        if text == "/start":
            send_message("Welcome to DocBot")
        else:
            db.add_item(text, chat)  
            items = db.get_items(chat)  ##
            message = "\n".join(items)
            send_message(message, chat)

def get_last_chat_id_and_text(updates):
    num_updates = len(updates["result"])
    last_update = num_updates - 1
    text = updates["result"][last_update]["message"]["text"]
    chat_id = updates["result"][last_update]["message"]["chat"]["id"]
    return (text, chat_id)

def send_message(text, chat_id):
    url = URL + "sendMessage?text={}&chat_id={}".format(text, chat_id)
    get_url(url)
# def send_message(text, chat_id):
#     text = urllib.parse.quote_plus(text)
#     url = URL + "sendMessage?text={}&chat_id={}".format(text, chat_id)
#     get_url(url)

# text, chat = get_last_chat_id_and_text(get_updates())
# send_message(text, chat)

def main():
    db.setup()
    last_update_id = None
    while True:
        
        print("getting updates")
        updates = get_updates(last_update_id)
        if len(updates["result"]) > 0:
            last_update_id = get_last_update_id(updates) + 1
            handle_updates(updates)
        # if(datetime.datetime.now.year == )
        time.sleep(0.5)

if __name__ == '__main__':
    main()

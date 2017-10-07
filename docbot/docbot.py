import json 
import requests
import time
# import urllib
import datetime

now = datetime.datetime.now()

from docbotdb import DBHelper
db = DBHelper()

TOKEN = "451932661:AAEjBUpVHcpE549UL1sumLaET0d_B6kHzyY"
CHAT_ID = "368443214"
URL = "https://api.telegram.org/bot{}/".format(TOKEN)

def get_url(url):
    response = requests.get(url)
    content = response.content.decode("utf8")
    return content


####################################


def get_json_from_url(url):
    content = get_url(url)
    js = json.loads(content)
    return js

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

###############################

def send_message(medicine, disease, remarks, chat_id):
    text ="You need to take " +  medicine + " for " + disease + ". Other remarks: " + remarks
    url = URL + "sendMessage?text={}&chat_id={}".format(text, chat_id)
    get_url(url)

db.setup()
# db.add_item("hey", "hey", "hey", "hey")

def main():
    while True:
        items = db.auto_message(now.hour, now.minute)
        items = db.get_all()
        print("getting updates")
        for item in items:
            send_message(item[0], item[1], item[2], item[3])
        # send_message("paracetamol", "fever", "sirf aadhi peeli goli khaana", CHAT_ID)

        # testcase = db.get_all()
        # for test in testcase:
        #     send_message(test[0], test[1], test[2], CHAT_ID)
        time.sleep(60)

if __name__ == '__main__':
    main()


############################
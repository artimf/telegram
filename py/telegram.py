from builtins import len

import requests
import config

url = config.url

print (config.url)

def get_updates_json(request):
    response = requests.get(request + 'getUpdates')
    return response.json()


def last_update(data):
    results = data['result']
    total_updates = len(results) - 1
    return results[total_updates]


def get_chat_id(update):
    chat_id = update['message']['chat']['id']
    return chat_id

def send_mess(chat, text):
    params = {'chat_id': chat, 'text': text}
    response = requests.post(url + 'sendMessage', data=params)
    return response

def get_chat_id(update):
    chat_id = update['message']['chat']['id']
    return chat_id

def send_mess(chat, text):
    params = {'chat_id': chat, 'text': text}
    response = requests.post(url + 'sendMessage', data=params)
    return response

x=get_updates_json(url)
print("Length x=" + str(len(x['result'])))
#print(x)
#print(x['result'][0]['message']['text'])


for i in range(0, len(x['result'])):
    print (print(x['result'][i]['message']['chat']['username']+": " + x['result'][i]['message']['text']))
    print ("----")


print(last_update(get_updates_json(url)))
chat_id = get_chat_id(last_update(get_updates_json(url)))

#send_mess(chat_id, 'Your message goes here')
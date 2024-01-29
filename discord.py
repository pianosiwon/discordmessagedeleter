import requests
import json

token = 'ODA5ODk3NTMxODk0NzkyMjYy.GyWHcq.AyaeD-CCS_3Kiui0Lyg6In8uiVtF_FvgEbSjUw'
my_id = "809897531894792262"


user_id = '1018173925609447488'

 
def sendMessage(channel_id, message):
    url = 'https://discord.com/api/v8/channels/%s/messages'%channel_id
    data = {"content": message}
    header = {"authorization": token}
 
    r = requests.post(url, data=data, headers=header)
    print(r.status_code)

def getMessageID(channel_id,cnt):
    url = "https://discord.com/api/v9/channels/%s/messages?limit=%d"%(channel_id,cnt)
    header = {"authorization": token}

    r = requests.get(url, headers=header)
    return r.text

 
def getChennelID(user_id):
    data = {"recipient_id": user_id}
    headers = {"authorization": token}
 
    r = requests.post(f'https://discord.com/api/v9/users/@me/channels', json=data, headers=headers)
    print(r.status_code)
 
    channel_id = r.json()['id']
 
    return channel_id

def deleteMessage(channel_id,message_id):
    url = "https://discord.com/api/v9/channels/%s/messages/%s"%(channel_id,message_id)
    headers = {"authorization": token}
    r = requests.delete(url,headers=headers)
    print(r.status_code)


channel_id = getChennelID(user_id)


while 1:
    flag = 0
    message = getMessageID(channel_id,50)
    json_data = json.loads(message)

    for i in json_data:
        if (i['author']['id'] == my_id):
            flag = 1
            print(i['id'])
            deleteMessage(channel_id,i['id'])
    
    if (flag == 0):
        break

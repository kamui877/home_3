import requests
import time


def stack_quest():
    fromdate = int(time.time()) - 172800
    todate = int(time.time())
    link = "https://api.stackexchange.com/2.3/questions"
    params = {'fromdate': fromdate, 'todate': todate, 'tagged': 'python',
              'sort': 'creation', 'order': 'desc', 'site': 'stackoverflow'}
    resp = requests.get(link, params=params)
    for val in resp.json()['items']:
        print(val["link"])


stack_quest()

import requests


def best_int(heroes_list):
    ints = {}
    for hero in heroes_list:
        resp = requests.get(f'https://superheroapi.com/api/2619421814940190/search/{hero}')
        ints[resp.json()["results"][0]["name"]] = (int(resp.json()['results'][0]['powerstats']['intelligence']))
    print(f'{sorted(ints.items(), reverse=True)[0][0]} - {sorted(ints.items(), reverse=True)[0][1]} int')


heroes = ['Hulk', 'Thanos', 'Captain America']
best_int(heroes)
import requests
import vk
from config import token
from random import choice
from voice import say, recognize

session = vk.Session(access_token=token)
vk_api = vk.API(session)

while True:
    themes = ['петрович', 'вовочка', 'мужик', 'петька', 'a']
    records = vk_api.wall.search(domain='baneks', query=choice(themes), owners_only=1, v=5.68, count=100)
    for i in range(10):
        try:
            random_record = choice(records['items'])
            say(random_record['text'])
        except:
            pass
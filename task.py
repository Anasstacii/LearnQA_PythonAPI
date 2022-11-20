import requests
import json
import time

create_task = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job")
obj = json.loads(create_task.text)
token = {"token":obj['token']}
seconds = obj['seconds']

before = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params=token)
print(before.text)

time.sleep(seconds)
after = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params=token)
print(after.text)
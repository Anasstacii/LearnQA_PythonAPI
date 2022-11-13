import requests

response = requests.get("https://playground.learnqa.ru/api/long_redirect",allow_redirects=True)
first = response.history[0]
second = response.history[1]
third = response

print(first.url,'\n',second.url,'\n',third.url)

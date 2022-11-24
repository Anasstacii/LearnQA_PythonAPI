import requests

class Test:
    def testCookieMethod(self):
        url = "https://playground.learnqa.ru/api/homework_cookie"
        response = requests.get(url)
        print(dict(response.cookies))
        cookie_value = response.cookies.get('HomeWork')

        assert 'HomeWork' in response.cookies,"There is no HomeWork in the response"
        assert cookie_value == "hw_value", "HomeWork != 'hw_value' in the response"
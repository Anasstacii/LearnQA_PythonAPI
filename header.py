import requests

class Test:
    def HeadersMethod(self):
        url="https://playground.learnqa.ru/api/homework_header"
        response = requests.get(url)
        print(response.headers)
        header_value = response.headers.get('x-secret-homework-header')

        assert 'x-secret-homework-header' in response.headers, "There is no 'x-secret-homework-header' in the response"
        assert header_value == 'Some secret value', "x-secret-homework-header != 'Some secret value' in the response"
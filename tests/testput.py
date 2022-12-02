from lib.base_case import BaseCase
from lib.assertions import Assertions
import requests
import allure

@allure.title("User edit cases")
class TestUserEdit(BaseCase):
    def test_edit_created_user(self):
        register_data = self.prepare_registration_data()
        response = requests.post("https://playground.learnqa.ru/api/user/", data=register_data)

        Assertions.assert_code_status(response, 200)
        Assertions.assert_json_has_key(response, "id")

        email = register_data['email']
        first_name = register_data['firstName']
        password = register_data['password']
        user_id = self.get_json_value(response, "id")

        login_data = {
            'email': email,
            'password': password
        }

        response2 = requests.post("https://playground.learnqa.ru/api/user/login", data=login_data)

        auth_sid = self.get_cookie(response2, "auth_sid")
        token = self.get_header(response2, "x-csrf-token")

        new_name = 'Changed name'
        response3 = requests.put(
            f"https://playground.learnqa.ru/api/user/{user_id}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid},
            data={"firstName": new_name})

        Assertions.assert_code_status(response3, 200)

        response4 = requests.get(
            f"https://playground.learnqa.ru/api/user/{user_id}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid}
        )

        Assertions.assert_json_value_name(
            response4,
            "firstName",
            new_name,
            "Wrong name of the user after edit"
        )

        new_username = 'Incorrect name' # изменить неавторизованными
        response5 = requests.put(
            f"https://playground.learnqa.ru/api/user/{user_id}",
            data={"username": new_username})

        Assertions.assert_code_status(response5, 400)
        assert response5.content.decode("utf-8") == f"Auth token not supplied", f"Unexpected response content {response.content}"

        response6 = requests.get(
            f"https://playground.learnqa.ru/api/user/{user_id}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid}
        )

        Assertions.assert_json_value_name(
            response6,
            "username",
            "learnqa",
            "Wrong name of the user after edit"
        )

        # - изменить авторизованными другим пользователем
        response7 = requests.put(
            "https://playground.learnqa.ru/api/user/2",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid},
            data={"username": new_username})

        response8 = requests.get(
            "https://playground.learnqa.ru/api/user/2",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid}
        )

        Assertions.assert_json_value_name(
            response8,
            "username",
            "Vitaliy",
            "Wrong name of the user after edit"
        )

        # изменить email пользователя, будучи авторизованными тем же пользователем, на новый email без символа @
        new_email = 'learnqaexample.ru'
        response9 = requests.put(
            f"https://playground.learnqa.ru/api/user/{user_id}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid},
            data={"email": new_email})

        Assertions.assert_code_status(response9, 400)
        assert response9.content.decode("utf-8") == "Invalid email format", f"Unexpected response content {response.content}"

        response10 = requests.get(
            f"https://playground.learnqa.ru/api/user/{user_id}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid}
        )

        Assertions.assert_json_value_name(
            response10,
            "email",
            email,
            "Wrong name of the user after edit"
        )

        # изменить firstName пользователя, будучи авторизованными тем же пользователем, на очень короткое значение в один символ
        short_name = 'C'
        response11 = requests.put(
            f"https://playground.learnqa.ru/api/user/{user_id}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid},
            data={"firstName": short_name})

        Assertions.assert_code_status(response11, 400)
        Assertions.assert_json_value_name(
            response11,
            "error",
            "Too short value for field firstName",
            "Wrong name of the user after edit"
        )

        response12 = requests.get(
            f"https://playground.learnqa.ru/api/user/{user_id}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid}
        )

        Assertions.assert_code_status(response12, 200)
        Assertions.assert_json_value_name(
            response12,
            "firstName",
            "Changed name",
            "Wrong name of the user after edit"
        )
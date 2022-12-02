import pytest
from lib.assertions import Assertions
import requests
from lib.base_case import BaseCase

@allure.epic("Registrations cases")
class TestUserRegister(BaseCase):
    data = [
        ("email"),
        ("password"),
        ("username"),
        ("firstName"),
        ("lastName")
    ]

    def test_create_user_with_incorrect_email(self): # без символа @
        email = 'learnqaexample.ru'
        data = self.prepare_registration_data(email)
        response = requests.post("https://playground.learnqa.ru/api/user/", data=data)

        Assertions.assert_code_status(response, 400)
        assert response.content.decode(
            "utf-8") == "Invalid email format", f"Unexpected response content {response.content}"


    @pytest.mark.parametrize('condition', data) #без указания одного из полей
    def test_user_without_filed(self, condition):
        if condition == "email":
            data = self.prepare_registration_data().copy()
            data.pop(condition)
            response = requests.post("https://playground.learnqa.ru/api/user/", data=data)

            Assertions.assert_code_status(response, 400)
            assert response.content.decode("utf-8") == f"The following required params are missed: {condition}", f"Unexpected response content {response.content}"

        if condition == "password":
            data = self.prepare_registration_data().copy()
            data.pop(condition)
            response = requests.post("https://playground.learnqa.ru/api/user/", data=data)

            Assertions.assert_code_status(response, 400)
            assert response.content.decode("utf-8") == f"The following required params are missed: {condition}", f"Unexpected response content {response.content}"

        if condition == "username":
            data = self.prepare_registration_data().copy()
            data.pop(condition)
            response = requests.post("https://playground.learnqa.ru/api/user/", data=data)

            Assertions.assert_code_status(response, 400)
            assert response.content.decode("utf-8") == f"The following required params are missed: {condition}", f"Unexpected response content {response.content}"

        if condition == "firstName":
            data = self.prepare_registration_data().copy()
            data.pop(condition)
            response = requests.post("https://playground.learnqa.ru/api/user/", data=data)

            Assertions.assert_code_status(response, 400)
            assert response.content.decode("utf-8") == f"The following required params are missed: {condition}", f"Unexpected response content {response.content}"

        if condition == "lastName":
            data = self.prepare_registration_data().copy()
            data.pop(condition)
            response = requests.post("https://playground.learnqa.ru/api/user/", data=data)

            Assertions.assert_code_status(response, 400)
            assert response.content.decode("utf-8") == f"The following required params are missed: {condition}", f"Unexpected response content {response.content}"


    def test_user_short_name(self): # имя с одним символом
        data = self.prepare_registration_data().copy()
        short_value = 'a'
        data.update({'firstName': short_value})
        response = requests.post("https://playground.learnqa.ru/api/user/", data=data)
        Assertions.assert_code_status(response, 400)
        assert response.content.decode("utf-8") == f"The value of 'firstName' field is too short", f"Unexpected response content {response.content}"


    def test_user_with_long_name(self): #имя длиннее 250 символов
        data = self.prepare_registration_data().copy()
        long_value = self.generate_random_string(251)
        print(long_value)
        data.update({'firstName': long_value})
        response = requests.post("https://playground.learnqa.ru/api/user/", data=data)
        Assertions.assert_code_status(response, 400)
        print(response.content)
        assert response.content.decode("utf-8") == f"The value of 'firstName' field is too long", f"Unexpected response content {response.content}"

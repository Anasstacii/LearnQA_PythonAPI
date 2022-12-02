from lib.base_case import BaseCase
from lib.assertions import Assertions
from lib.My_requests import My_requests
import allure

class TestUserDelete(BaseCase):
    @allure.description("Delete user")
    def test_delete_user_id2(self):

        data = {
            'email': 'vinkotov@example.com',
            'password': '1234'
        }
        response1 = My_requests.post("/user/login", data=data)
        auth_sid = self.get_cookie(response1, "auth_sid")
        token = self.get_header(response1, "x-csrf-token")
        user_id_from_auth_method = self.get_json_value(response1, "user_id")


        response2 = My_requests.delete(f"/user/{user_id_from_auth_method}",
                                   headers={"x-csrf-token": token},
                                   cookies={"auth_sid": auth_sid}
                                   )
        Assertions.assert_code_status(response2, 400)
        assert response2.content.decode("utf-8") == "Please, do not delete test users with ID 1, 2, 3, 4 or 5.", f"User ID in not equal {user_id_from_auth_method}"

        response3 = My_requests.get(f"/user/{user_id_from_auth_method}",
                                   headers={"x-csrf-token": token},
                                   cookies={"auth_sid": auth_sid}
                                   )
        Assertions.assert_json_value_name(
            response3,
            "email",
            "vinkotov@example.com",
            "User with same ID deleted"
        )

    @allure.description("Create, Auth, Delete")
    def test_del_new_user(self):
        register_data = self.prepare_registration_data()
        response4 = My_requests.post("/user/", data=register_data)
        Assertions.assert_code_status(response4, 200)
        Assertions.assert_json_has_key(response4, "id")
        email = register_data['email']
        password = register_data['password']
        user_id = self.get_json_value(response4, "id")

        login_data = {
            'email': email,
            'password': password
        }
        response5 = My_requests.post("/user/login", data=login_data)
        auth_sid = self.get_cookie(response5, "auth_sid")
        token = self.get_header(response5, "x-csrf-token")

        response6 = My_requests.delete(
            f"/user/{user_id}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid}
        )
        Assertions.assert_code_status(response6, 200)

        response7 = My_requests.get(f"/user/{user_id}",
                                   headers={"x-csrf-token": token},
                                   cookies={"auth_sid": auth_sid}
                                   )
        Assertions.assert_code_status(response7, 404)
        assert response7.content.decode("utf-8") == "User not found", f"User ID in not equal {user_id}"

    @allure.description("Delete by another user")
    def test_del_another_user(self):
        register_data = self.prepare_registration_data()
        response8 = My_requests.post("/user/", data=register_data)
        Assertions.assert_code_status(response8, 200)
        Assertions.assert_json_has_key(response8, "id")
        email = register_data['email']
        password = register_data['password']

        login_data = {
            'email': email,
            'password': password
        }
        response9 = My_requests.post("/user/login", data=login_data)
        auth_sid = self.get_cookie(response9, "auth_sid")
        token = self.get_header(response9, "x-csrf-token")

        register_data = self.prepare_registration_data()
        response10 = My_requests.post("/user/", data=register_data)
        Assertions.assert_code_status(response10, 200)
        Assertions.assert_json_has_key(response10, "id")
        another_user_id = self.get_json_value(response10, "id")

        response11 = My_requests.delete(
            f"/user/{another_user_id}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid}
        )
        Assertions.assert_code_status(response11, 200)

        response12 = My_requests.get(f"/user/{another_user_id}",
                                   headers={"x-csrf-token": token},
                                   cookies={"auth_sid": auth_sid}
                                   )
        Assertions.assert_code_status(response12, 200)
        assert "username" in response12.json(), f"User ID in not equal {another_user_id}"
import pytest
import requests
from lib.basecase import BaseCase
from lib.assertions import Assertions


class TestUserAuth(BaseCase):
    url_auth = "https://playground.learnqa.ru//api/user/auth"

    exclude_params = [
        ("no_cookie"),
        ("no_token")
    ]

    def setup(self):
        data = {
            'email': 'vinkotov@example.com',
            'password': '1234'
        }

        response = requests.post("https://playground.learnqa.ru//api/user/login", data=data)
        self.auth_sid = self.get_cookie(response, "auth_sid")
        self.token = self.get_header(response, "x-csrf-token")
        self.user_id_from_auth_method = self.get_json_value(response, "user_id")

    def test_auth_user(self):
        response = requests.get(
            url=TestUserAuth.url_auth,
            headers={"x-csrf-token": self.token},
            cookies={"auth_sid": self.auth_sid}
        )

        Assertions.assert_json_value_by_name(
            response,
            "user_id",
            self.user_id_from_auth_method,
            "User id from auth method is not equal to user id from check method"
        )

    @pytest.mark.parametrize('condition', exclude_params)
    def test_negative_auth_check(self, condition):
        if condition == "n0_cookie":
            response = requests.get(
                TestUserAuth.url_auth,
                headers={"x-csrf-token": self.token}
            )
        else:
            response = requests.get(
                TestUserAuth.url_auth,
                cookies={"auth_sid": self.auth_sid}
            )

        Assertions.assert_json_value_by_name(
            response,
            "user_id",
            0,
            f"User is authorized with condition {condition}"
        )
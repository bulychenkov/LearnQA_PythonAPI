import requests


class TestCookie:
    def test_cookie(self):
        response = requests.get("https://playground.learnqa.ru/api/homework_cookie")
        print(response.cookies)

        assert "HomeWork" in response.cookies, "There is no 'HomeWork' cookie!"
        assert response.cookies.get("HomeWork") == "hw_value", "Unexpected 'HomeWork' cookie value!"

import requests


class TestCookie:
    def test_cookie(self):
        response = requests.get("https://playground.learnqa.ru/api/homework_header")
        print(response.headers)

        assert "x-secret-homework-header" in response.headers, "There is no 'x-secret-homework-header' header!"
        assert response.headers.get("x-secret-homework-header") == "Some secret value", "Unexpected 'x-secret-homework-header' header value!"
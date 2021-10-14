import requests


response = requests.get('https://playground.learnqa.ru/api/long_redirect')
num = len(response.history)
print(f'Number of redirects is {num}')
print(f'Final URL is {response.url}')
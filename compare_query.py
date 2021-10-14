import requests

url = 'https://playground.learnqa.ru/ajax/api/compare_query_type'

response = requests.get(url)
print(response.status_code)
print(response.text)

response = requests.head(url)
print(response.status_code)
print(response.text)

response = requests.get(url, params={'method': 'GET'})
print(response.status_code)
print(response.text)

methods = ['GET', 'POST', 'PUT', 'DELETE']
for method in methods:
    for method_value in methods:
        if method == 'GET':
            response = requests.request(method, url, params={'method': method_value})
        else:
            response = requests.request(method, url, data={'method': method_value})
        print(f'Method is {method}, method param is {method_value}, server response is {response.text}')
import requests
import time

url = 'https://playground.learnqa.ru/ajax/api/longtime_job'
response = requests.get(url)

t = time.time()
time_to_complete = response.json()['seconds']
token = response.json()['token']

if time.time() - t < time_to_complete:
    response = requests.get(url, params={'token': token})
    if 'status' in response.json():
        if response.json()['status'] == 'Job is NOT ready':
            print('Get expected status: Job is NOT ready')
        else:
            print(f'Warning! Unexpected status: {response.json()["status"]}')
    else:
        print('No status field in the server response!')

time.sleep(time_to_complete)

response = requests.get(url, params={'token': token})
if 'status' in response.json():
    if response.json()['status'] == 'Job is ready':
        print('Get expected status: Job is ready')
    else:
        print(f'Warning! Unexpected status: {response.json()["status"]}')
else:
    print('No status field in the server response!')

if 'result' in response.json():
    print('Result received')
else:
    print('Warning! Result has not been received!')

a = 1
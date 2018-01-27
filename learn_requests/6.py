import requests
import json


root_url = "https://api.github.com"

def build_url(endpoint):
    return '/'.join([root_url,endpoint])

def bt_print(json_str):
    return json.dumps(json.loads(json_str),indent=4)

def request_method():
    response = requests.get(build_url('user/emails'),auth=("xxxxxx",'xxxxxx'),timeout=10)
    res = response.text
    print(response.status_code)
    print(response.request.headers)
    print(response.url)
    print(bt_print(res))


if __name__ == '__main__':
    try:
        request_method()
    except Exception as e:
        print(e)

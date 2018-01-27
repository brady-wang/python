import requests
import json


root_url = "https://api.github.com"

def build_url(endpoint):
    return '/'.join([root_url,endpoint])

def bt_print(json_str):
    return json.dumps(json.loads(json_str),indent=4)

def request_method():
    response = requests.patch(build_url('user'),auth=("xxxxxx",'xxxxxx'),json={'name':'aaaaa'})
    res = response.text
    print(response.request.headers)
    print(response.url)
    print(bt_print(res))


if __name__ == '__main__':
    try:
        request_method()
    except Exception as e:
        print(e)

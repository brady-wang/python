import requests
import json


root_url = "https://api.github.com"

def build_url(endpoint):
    return '/'.join([root_url,endpoint])

def bt_print(json_str):
    return json.dumps(json.loads(json_str),indent=4)

def request_method():
    response = requests.get(build_url('user/emails'),auth=("xxxxxx",'xxxxxx'))
    res = response.text
    print(bt_print(res))
if __name__ == '__main__':
    try:
        request_method()
    except Exception as e:
        print(e)

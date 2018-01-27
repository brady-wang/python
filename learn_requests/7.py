import requests
import json


root_url = "https://api.github.com"

def build_url(endpoint):
    return '/'.join([root_url,endpoint])

def bt_print(json_str):
    return json.dumps(json.loads(json_str),indent=4)

def request_method():
 from requests import  Request,Session
 s = Session()
 headers = {"User-Agent":'fake'}
 req = Request('GET',build_url('user/emails'),auth=('xxxxxx','xxxxxx'),headers=headers)
 prepared = req.prepare();
 print(prepared.body)
 print(prepared.headers)

 resp = s.send(prepared,timeout=10)
 print(resp.status_code)
 print(resp.headers)
 print(resp.text)


if __name__ == '__main__':
    try:
        request_method()
    except Exception as e:
        print(e)

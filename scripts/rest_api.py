import json
import requests

ENDPOINT = "http://127.0.0.1:8000/api/status/"

def do(method='get', data={} ,is_json=True): # no need of parameter 'pk'
    headers = {}
    if is_json:
        headers['content-type'] = 'application/json'
        data = json.dumps(data)
    # r = requests.request(method , ENDPOINT + "?pk=" + str(pk) , data=data)

    r = requests.request(method , ENDPOINT, data=data , headers=headers)
    print(r.text)
    print(r.status_code)
    return r

# do(data={'pk':15}) # no method arg is passed so calling 'get'

do(method='delete', data={'pk':10})

# do(method='put' , data={'pk':10 , 'user':1 , 'content':'updated 10'})

# do(method='post' , data={'user':1 , 'content':'created 13'})

import requests

def handler(event, context):
    r = requests.get('https://www.fernandomc.com')
    print(r.text[0:500])
    if r.status_code == 200:
        return 'Success!'
    else:
        return 'FAILURE!'
    
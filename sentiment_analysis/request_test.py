import requests
import json

url = "https://api.miro.com/v2/boards/o9J_lhriW6c%3D/widgets?limit=10"

headers = {
    "Accept": "application/json",
    "Authorization": "Bearer RQ2tztQ-8Yy6zWgp5Vvsa4gM1es"
}

response = requests.request("GET", url, headers=headers)
print(json.loads(response.text)['data'][0]['data']['content'])


import requests

url = "https://api.miro.com/v2/boards/o9J_lhrBIPg%3D/embeds"

payload = {
    "data": {"url": "https://junction-332712.appspot.com/"},
    "geometry": {
        "x": "0",
        "y": "0"
    }
}
headers = {
    "Accept": "application/json",
    "Content-Type": "application/json",
    "Authorization": "Bearer WHH9f392jOb2MmfVYK4CA0-3P9k"
}

response = requests.request("POST", url, json=payload, headers=headers)

print(response.text)

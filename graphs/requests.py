import requests

url = "https://api.miro.com/v2/boards/o9J_lhrBIPg%3D/embeds"

payload = {
    "data": {"url": "http://127.0.0.1:8000/"},
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

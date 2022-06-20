import requests
from env.config import GRAPH_ENDPOINT, HEADERS

GRAPH_CONFIG = {
    "id": "graph1",
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "shibafu"
}

res = requests.post(url=GRAPH_ENDPOINT, json=GRAPH_CONFIG, headers=HEADERS)

print(res.text)
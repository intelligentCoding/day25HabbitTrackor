from datetime import datetime
import requests
import os
from dotenv import load_dotenv

load_dotenv('.env')
pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": os.getenv("token"),
    "username": os.getenv("user_name"),
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{os.getenv('user_name')}/graphs"

graph_config = {
    "id": "graph1",
    "name": "My walking graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": os.getenv("token")
}

# To create the graph
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)


# get today's date
today = datetime.now()

pixel_creation_endpoint = f"{pixela_endpoint}/{os.getenv('user_name')}/graphs/graph1"
pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "6"
}

response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
print(response.text)
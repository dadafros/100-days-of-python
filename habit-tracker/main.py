import requests
from datetime import datetime

USERNAME = "dadafros"
TOKEN = "dsnklfqpmpcpwoqjwbokhosbxoj"
GRAPH_ID = "graph1"

# Create a user
# params = {
#     "token": TOKEN,
#     "username": USERNAME,
#     "agreeTermsOfService": "yes",
#     "notMinor": "yes",
# }
# response = requests.post("https://pixe.la/v1/users", json=params)
# print(response.text)

# Create a graph
# graph = {
#     "id": GRAPH_ID,
#     "name": "PM out",
#     "unit": "days",
#     "type": "int",
#     "color": "shibafu",
#     "timezone": "America/Sao_Paulo",
# }
# response = requests.post(f"https://pixe.la/v1/users/{USERNAME}/graphs", headers={"X-USER-TOKEN": TOKEN}, json=graph)
# print(response.text)

# Post a pixel to the graph
pixel = {
    "date": datetime.now().strftime("%Y%m%d"),
    "quantity": "1",
}
response = requests.post(f"https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPH_ID}",
                         headers={"X-USER-TOKEN": TOKEN}, json=pixel)
print(response.text)

# Update a pixel to the graph
# pixel = {
#     "quantity": "1",
# }
# response = requests.put(f"https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPH_ID}/{datetime.now().strftime('%Y%m%d')}",
#                         headers={"X-USER-TOKEN": TOKEN}, json=pixel)
# print(response.text)

# Delete a pixel to the graph
# response = requests.delete(f"https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPH_ID}/{datetime.now().strftime('%Y%m%d')}",
#                            headers={"X-USER-TOKEN": TOKEN})
# print(response.text)



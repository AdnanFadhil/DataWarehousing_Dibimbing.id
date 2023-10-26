import requests

url= "https://api.openaq.org/v2/locations?limit=100&page=1&offset=0&sort=desc&radius=1000&country=ID&location=Jakarta%20Central&order_by=lastUpdated&dump_raw=false"

headers={"accept":"application/json"}

response = requests.get(url, headers=headers)

print(response)

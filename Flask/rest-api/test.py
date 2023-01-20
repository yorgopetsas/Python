import requests 
# I got an error when I tried to run so I had to "pip3 install requests"

# Set the base URL
BASE = "http://127.0.0.1:5000/"

# Send get request to the helloworld endpoint
response = requests.get(BASE + "helloworld/tim/19")

print(response.json())
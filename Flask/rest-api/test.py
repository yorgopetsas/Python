import requests 
# I got an error when I tried to run so I had to "pip3 install requests"

# Set the base URL
BASE = "http://127.0.0.1:5000/"

# Load those in to the DB part 1
# data = [
# 		{"likes": 10, "name" : "Tim", "views" : 100000}, 
# 		{"likes": 20, "name" : "Jim", "views" : 200000}, 
# 		{"likes": 30, "name" : "Bim", "views" : 300000}]

# Load those in to the DB part 2
# for i in range(len(data)):
# 	response = requests.put(BASE + "video/" + str(i), data[i])
# 	print(response.json())

# input()
# reposnse = requests.delete(BASE + 'video/0')
# print(response)

#input()

response = requests.patch(BASE + "video/2", {"likes" : 101})
print(response.json())

# Send get request to the helloworld endpoint
# We are passing arguments data  
# response2 = requests.put(BASE + "video/2", {"likes": 10, "name" : "Jim", "views" : 100000})


import requests 

# Set the base URL
BASE = "http://127.0.0.1:5000/"

# FILL DB / CREATE ITEM
# We use this snippet in order to upload this data into the DB part 1
# data = [
# 		{"likes": 10, "name" : "Tim", "views" : 100000}, 
# 		{"likes": 20, "name" : "Jim", "views" : 200000}, 
# 		{"likes": 30, "name" : "Bim", "views" : 300000}]
#
# for i in range(len(data)):
# 	response = requests.put(BASE + "video/" + str(i), data[i])
# 	print(response.json())
# FILL DB END

# DELETE ITEM
# resposnse = requests.delete(BASE + 'video/0')
# print(response)

# UPDATE ITEM. In this case we only update one argument: "likes".
response = requests.patch(BASE + "video/2", {"likes" : 101})
print(response.json())

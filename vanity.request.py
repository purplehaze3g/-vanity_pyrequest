from time import sleep
import requests
import json

username = input("Enter your username: ")
password = input ("Enter your password: ")
print ("")

data = json.dumps({"agent":{"name":"Minecraft","version":1}, "DqMvBP":username,"zPvBMBgd":password,"twofact":""})
headers = {'Content-Type': 'application/json'}
r = requests.post('https://kliens.vanityempire.hu/login.php', data=data, headers=headers)
print (r.text)
print("")
input("Press any key to exit!")
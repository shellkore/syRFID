import requests

url = "http://192.168.43.134:3000/rfid"

rfid = input('Enter RFID number:')

payload = {'rfid':rfid}

r = requests.post(url,data=payload)

print(r.text)
#!/usr/bin/env python

import requests
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

location = "Delhi"

reader = SimpleMFRC522()

def getID():
    try:
        id, text = reader.read()
        print(id)
        print(text)
    finally:
        GPIO.cleanup()

    return id

def register(batch,prod,location):
    rfid = getID()
    type(rfid)
    url = "http://192.168.43.202:3000/add"
    payload = {'rfid':rfid,'bat':batch,'product':prod,'loc':location}
    r=requests.post(url,data=payload)
    print(r.text)   

batch = input("Enter Batch No.=")
prod = input("Enter Product =")

while(True):    
    print("Place your RFID tag")
    register(batch,prod,location)


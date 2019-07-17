#!/usr/bin/env python

import requests
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
from flask import Flask, render_template, request

reader = SimpleMFRC522()

app = Flask(__name__)

location = ''

def getID():
    id, text = reader.read()
    print(id)
    print(text)
    GPIO.cleanup()

    return id

def registerProd(batch,prod,location):
    rfid = getID()
    url = "http://192.168.43.134:3000/add"
    payload = {'rfid':rfid,'bat':batch,'product':prod,'loc':location}
    r=requests.post(url,data=payload)
    print(r.text)   

def traceRFID(rfid,location,level):
    url = "http://192.168.43.134:3000/updatepath"
    payload = {'rfid':rfid,'level':level,'loc':location}
    r=requests.post(url,data=payload)
    return(r.text)

def getLevel(loc):
    if(loc == 'state1'):
        return (int(1))
    elif (loc == 'div1' or loc == 'div2' or loc == 'div3'):
        return (int(2))
    elif(loc == 'dist1' or loc == 'dist2' or loc == 'dist3' or loc == 'dist4'):
        return (int(3))
    elif(loc == 'fps1' or loc == 'fps2' or loc == 'fps3' or loc == 'fps4'):
        return (int(4))

@app.route('/register',methods = ['POST', 'GET'])
def register():
    if request.method == 'GET':
        return render_template("getData.html")
        
    if request.method == 'POST':
        result = request.form
        batch = request.form['batch']
        prod = request.form['product']
        registerProd(batch,prod,location)
        return render_template("register.html",result = result)

@app.route('/trace',methods = ['POST', 'GET'])
def trace():
    if request.method == 'GET':
        rfid = getID()
        loc = location
        level = getLevel(loc)
        #level = int(1)
        print(type(level))
        response = traceRFID(rfid,loc,level)
        print(response)
        return render_template('trace.html')

@app.route('/location',methods =['POST', 'GET'])
def location():
    global location
    if request.method =='GET':
        return render_template('getlocation.html')
    if request.method =='POST':
                loc = request.form['loc']
                location=loc
                print(location)
                return render_template('printLocation.html')           
 

if __name__ == '__main__':
   app.run(debug = True)


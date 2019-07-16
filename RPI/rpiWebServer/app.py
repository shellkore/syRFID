#!/usr/bin/env python


#import RPi.GPIO as GPIO
#from mfrc522 import SimpleMFRC522
from flask import Flask, render_template, request

app = Flask(__name__)


#reader = SimpleMFRC522()

'''
try:
        id, text = reader.read()
        print(id)
        print(text)
finally:
        GPIO.cleanup()
'''
	
@app.route("/getData",methods = ['POST','GET'])
def getData():
   return render_template('getData.html')

@app.route('/register',methods = ['POST', 'GET'])
def register():
   if request.method == 'POST':
      result = request.form
      return render_template("register.html",result = result)

if __name__ == '__main__':
   app.run(debug = True)

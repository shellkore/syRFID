from flask import Flask, render_template
from graph import *
import datetime
import os
 
#Initialize on GCP
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

credential_path = "./Angular-learn-5035d419fd60.json"
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credential_path

# Use the application default credentials
cred = credentials.ApplicationDefault()
firebase_admin.initialize_app(cred, {
  'projectId': "angular-learn-8c93c",
})


db = firestore.client()

app = Flask(__name__)

countPerHour=[0]*24

#function to read data from firestore

def readDataFromFirestore():
    users_ref = db.collection(u'bigData')
    docs = users_ref.stream()

    return (docs)

def getCountPerHour():

    docs = readDataFromFirestore()

    timeList=[]
    date_time_obj_list=[]

    #initializing count of rider per hour to zero
    for i in range(24):
        countPerHour[i]=0

    for doc in docs:
        timeList.append((doc.get(u'time')))

    for timeStrObject in timeList:
        date_time_obj_list.append(datetime.datetime.strptime(timeStrObject, '%H:%M:%S'))

    for ti in date_time_obj_list:
        countPerHour[ti.hour]+=1

    return countPerHour


@app.route('/')
def graphs():

    graph1_url = build_bar_from_list(getCountPerHour(),24)
    graph2_url = build_bar_from_dict(getPlaceFromFreq())
    graph3_url = build_pie_from_list(getCountPerHour())


    return render_template('graphs.html',
    graph1=graph1_url,
    graph2=graph2_url,
    graph3=graph3_url,
    )
 
if __name__ == '__main__':
    app.debug = True
    app.run()
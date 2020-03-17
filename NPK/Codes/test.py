import pickle
import pandas as pd
import numpy as np

import firebase_admin
from firebase_admin import credentials, firestore
from firebase_admin import db
import json

cred =credentials.Certificate('./ServiceAccountKey.json')
firebase_admin.initialize_app(cred, {'databaseURL' : 'https://liquid-sylph-234009.firebaseio.com/'})

ref = db.reference('SoilData/sensorData')
strg = ref.get().__str__().replace("\'", "\"")
print(strg)
key = strg[strg.index('-'):strg.index(':')-1]

y = json.loads(strg)

nmodelfile = r'/Users/nayanalakshitha/Desktop/NPK/nModel.sav'
pmodelfile = r'/Users/nayanalakshitha/Desktop/NPK/pModel.sav'
kmodelfile = r'/Users/nayanalakshitha/Desktop/NPK/kModel.sav'
datafile=r'/Users/nayanalakshitha/Desktop/NPK/TestFormat/dataset2.xlsx'
savedfile=r'/Users/nayanalakshitha/Desktop/NPK/prediction.txt'

names=['pH ','humidity %','ec ','temperature']
nmodel = pickle.load(open(nmodelfile , 'rb'))
pmodel = pickle.load(open(pmodelfile , 'rb'))
kmodel = pickle.load(open(kmodelfile , 'rb'))

pH=y[key]['Ph']
humidity=y[key]['Moisture']
ec= y[key]['EC']
temperature=y[key]['Temperature']
print(y[key])
def PreProcessData(getData):
    
    sum=0
    for i in range(len(getData)):
        sum=sum+getData[i]
    tList=(pH/sum,humidity/sum,ec/sum,temperature/sum)
    return tList

getData=[pH,humidity,ec,temperature]
tList=PreProcessData(getData)

testdata=pd.DataFrame(tList)
tList=np.array(tList)
tList=tList.reshape(1,-1)
n=nmodel.predict(tList)
print("n : ",n)
p=pmodel.predict(tList)
print("p : ",p)
k=kmodel.predict(tList)
print("k : ",k)

f= open(savedfile,"w+")
f.write(str([n[0],p[0],k[0]]))
f.close() 
print("text file Done")

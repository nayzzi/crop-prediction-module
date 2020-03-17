import firebase_admin
from firebase_admin import credentials, firestore
from firebase_admin import db
import json

cred =credentials.Certificate('./ServiceAccountKey.json')
firebase_admin.initialize_app(cred, {'databaseURL' : 'https://liquid-sylph-234009.firebaseio.com/'})

ref = db.reference('SoilData/sensorData')
strg = ref.get().__str__().replace("\'", "\"")

key = strg[strg.index('-'):strg.index(':')-1]

y = json.loads(strg)

print(y[key]['EC'])


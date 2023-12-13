import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Use the application default credentials.
cred = credentials.Certificate('glassboilerplate-firebase-adminsdk-ayxb7-905abea505.json')
firebase_admin.initialize_app(cred)

db = firestore.client()

#Hola
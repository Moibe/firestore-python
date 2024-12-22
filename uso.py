import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Use the application default credentials.
cred = credentials.Certificate('config.json')
firebase_admin.initialize_app(cred)

db = firestore.client()

print(db)

quote = "Tan lejos del cielo y tan cerca de Estados Unidos."
author = "Anónimo"

doc_ref = db.collection('sampleData').document('inspiration')

print(doc_ref)
doc_ref.set({
    # 'quote': quote,
    'author': author,
})

print(quote+" and "+author+" successfully written to database")

try: 
    doc = doc_ref.get()
    print("Document data:", doc.to_dict())

except Exception as e:
    print("Documento no encontrado:", e)
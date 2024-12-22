import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Use the application default credentials.
cred = credentials.Certificate('config.json')
firebase_admin.initialize_app(cred)

db = firestore.client()


##Vamos

#Primero debemos definir la referencia al documentos, o sea a la hoja de usuario.
doc_ref = db.collection('usuarios').document('ella')
documento = doc_ref.get()


diccionario = documento.to_dict()


print("Documento:")
print(diccionario.get('password'))
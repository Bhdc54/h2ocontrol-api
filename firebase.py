import firebase_admin
from firebase_admin import credentials, firestore

# Substitua pelo caminho correto do seu JSON
cred = credentials.Certificate("C:\Users\hbrun\OneDrive\Documentos\h2ocontrol\api\sistemademonitoramento-32fb9-firebase-adminsdk-fbsvc-07985cba11.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

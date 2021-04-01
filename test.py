import firebase_admin
from firebase_admin import credentials,firestore
cred=credentials.Certificate('serviceAccountkey.json')
app=firebase_admin.initialize_app(cred)
print(app.name)


dp=firestore.client()
dp.collection("name").document("username").set({"name":"anubhav"})
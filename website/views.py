from django.http import HttpResponse
from django.shortcuts import render
# import firebase_admin
# from  pyrebase import pyrebase
# from firebase_admin import credentials
# firebaseConfig = {
#   "apiKey": "AIzaSyC7fz_pXat1z2hEvzVvEk3waoQnMjmyook",
#   "authDomain": "startup-carvaan-4c5db.firebaseapp.com",
#   "projectId": "startup-carvaan-4c5db",
#   "databaseURL": "https://startupcarvaan.firebaseio.com",
#   "storageBucket": "startup-carvaan-4c5db.appspot.com",
#   "messagingSenderId": "581476801467",
#   "appId": "1:581476801467:web:038c2a553a3b660312829e",
#   "measurementId": "G-P8WXN23XPF"
# }
# cred=credentials.Certificate('serviceAccountkey.json')
# firebase_admin.initialize_app(cred)
# pyrebase_app=pyrebase.initialize_app(firebaseConfig)
# auth=pyrebase_app.auth()
# auth.sign_in_with_email_and_password("test@gmail.com","testuser")
# print(auth.current_user['email'])
def home(request):
    return render(request,'home.html',{})

def login(request):
    return render(request,'login.html',{})

def join(request):
    return render(request,'join.html',{})

def achievements(request):
    return render(request,'index.html',{})


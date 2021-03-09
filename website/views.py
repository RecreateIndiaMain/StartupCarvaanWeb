from django.http import HttpResponse
from django.shortcuts import render
import firebase_admin
from pyrebase import pyrebase
from firebase_admin import credentials,auth
cred=credentials.Certificate('serviceAccountKey.json')
app=firebase_admin.initialize_app(cred)
print(type(auth))
def home(request):
    return render(request,'index.html',{})

def login(request):
    return render(request,'login.html',{})


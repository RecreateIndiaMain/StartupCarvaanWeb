from django.shortcuts import render
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from django.http import HttpResponse


# Create your views here.
def home(request):
    return render(request,'general.html',{})
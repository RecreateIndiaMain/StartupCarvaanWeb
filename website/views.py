from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib import messages
import firebase_admin
from django.utils.datastructures import MultiValueDictKeyError
from  pyrebase import pyrebase
from firebase_admin import credentials,firestore
firebaseConfig = {
   "apiKey": "AIzaSyC7fz_pXat1z2hEvzVvEk3waoQnMjmyook",
   "authDomain": "startup-carvaan-4c5db.firebaseapp.com",
   "projectId": "startup-carvaan-4c5db",
   "databaseURL": "https://startupcarvaan.firebaseio.com",
   "storageBucket": "startup-carvaan-4c5db.appspot.com",
   "messagingSenderId": "581476801467",
   "appId": "1:581476801467:web:038c2a553a3b660312829e",
   "measurementId": "G-P8WXN23XPF"
}
cred=credentials.Certificate('serviceAccountkey.json')
firebase_admin.initialize_app(cred)
pyrebase_app=pyrebase.initialize_app(firebaseConfig)
auth=pyrebase_app.auth()
db=firestore.client()
storage=pyrebase_app.storage()
# auth.sign_in_with_email_and_password("test@gmail.com","testuser")
# print(auth.current_user['email'])
def home(request):
    return render(request,'home.html',{})

def startuplogin(request):
    if request.method == 'POST':
        email=request.POST.get('startupemail')
        password=request.POST.get('startuppwd')
        try:
            user=auth.sign_in_with_email_and_password(email, password)
            if email=='yashagrawal0601@gmail.com' :
                return redirect('/table')
            return redirect('/dashboard')
        except:
            return render(request,'login.html',{})                
    return render(request,'login.html',{})

def userlogin(request):
    if request.method == 'POST':
        email=request.POST.get('useremail')
        password=request.POST.get('userpwd')
        try:
            user=auth.sign_in_with_email_and_password(email, password)
            return redirect('/')
        except:
            return render(request,'login.html',{})                
    return render(request,'login.html',{})    

def join(request):
    if request.method == 'POST' and request.FILES['blueone']:
        teamName=request.POST.get('teamname')
        email=request.POST.get('email')
        number=request.POST.get('phone')
        student=request.POST.get('student')
        professional=request.POST.get('professional')
        myfile = request.FILES['blueone']
        storage.child('startupFiles').put(myfile)
        filename = myfile.name
        db.collection('registration').document().set({
            'teamName':teamName,
            'email':email,
            'number':number,
            'student':student,
            'professional':professional,
            'filename':filename
        })
        return redirect('/userlogin')
    return render(request, 'join.html',{})

def startups(request):
    return render(request,'startups.html',{})

def users(request):
    return render(request,'users.html',{})

def delete(request,id):
    id=id.replace('>','')
    id=id.replace('<','')
    print(id)
    return HttpResponse(str(id))
def table(request):
    return render(request,'table.html',{})
    
def dashboard(request):
    return render(request,'dashboard.html',{})

def blog(request):
    return render(request, 'blog.html', {})



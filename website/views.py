import json
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib import messages
import uuid
from datetime import datetime
import firebase_admin
from django.utils.datastructures import MultiValueDictKeyError
from google.oauth2 import service_account
from pyasn1.type.univ import Null
from  pyrebase import pyrebase
from django.core.files.storage import FileSystemStorage 
from firebase_admin import credentials,firestore
import requests
from requests.models import REDIRECT_STATI
from requests.sessions import HTTPAdapter
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
serviceAccountKey= {
  "type": "service_account",
  "project_id": "startup-carvaan-4c5db",
  "private_key_id": "63ffa70265193e4209188101388c644167a6f918",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQDIb0Mv8Cc9QZ0q\nKjXWqXOtAdMHwvEzFAQ7n8anLUlMcZOln5xZ9RS9REgSKt5wmAfdCSIFO2cVp8uB\nbOxtCHBxYqptTT1zT4qthEJ/nCqs5I2oKKrSnj4ZRRtnTSzmldkHpmyjF+Za89G4\n+RNCTmvupBRxe1kGlHNN7BGhsSYbubK0BBd1nwox1DDnL846OgRYw6uYHiyVfDvy\nHsckaCYOdgtwiMqmlmPWzExKJQX2B6A3bhVHyrLKl/wjtbhWtA2JVyT99p15fyQ+\n4q0zJj78QKp/L3T2ahSM5tLwNPROO+Ea7d3YO0ti6Q9v5uCpV65Z1xeeT0w3rzVO\nOq4CpEdvAgMBAAECggEAVhhs3M+km0xu7Si6fZ3GIX+SHVhgcRddBhuIolDyllKH\nIHKiH4YFxZLp/lvJtsWnQwvkQCkXC5dK9CpMmD0yx5GhMVgnWDvHjucsBVKYhjGa\no6vsTJJKjGJB9iqRae7eDcowChJ/EXyADpt26Vl0RUrXuTNJt2jW6pbHsBO/EdL8\nQ1ckPtSGTLe1g3Js1y+j1miTNSR+yVA3uZWxMUJt05TPRbWGa6acQMW6W/Dl5TOj\nkdLhMULW09Lj8pnIwOX2UESrWbfoA9arKcCqSwxSnziirGMsomgQapfzKlRQtxQL\nR/9uufCveQNBsQpmgyYTFAepntLE5Tz/w86/TeGfsQKBgQD0fkOsSMgcWYKExngD\nuuIMva7pUisgcZmg3XNpGt+nPXkXx0jrtLBcFXeyiWFUlBnMANbJkVyONbT4jKeU\ns/tUzvTxR0/pzKRwluT8uMkvn016HfAdEdqon6+mgGhHbnMGWut3QdM4xFSlaKgN\no0PYmE0M68JDq3y90wGvJCH8eQKBgQDR3ipY4O+CLAlf20cypwZQScmoE5curiNv\nbFImYi7iVseU3x+Djz+h7aK+GEpBbXt+lzxpebOSyJQeP6gxvjb6a3C6caUc5Jou\nX5i/YqZ8idpWJ8ahv1w08tK1EZn1a8k7sJIYOQS1vz9H0uHju7GepYOyjkf+5id0\nPuYRbIcZJwKBgQDSGruPD1CgRC+MaH30PqJJbqwkJ4+WJultu0CVnxl5v7MTQxeg\nLrurtmsRi0uQAmGU1Ve/CmLudqrZOQ4+FNk0DVGjErRS56CcfJ+1qhqCCTTsb1PL\nt28fn3Kz8/8o+3pviKx25KNeUiGnr6NTbO098cutAeEEhBcDjZQR7UwjiQKBgErv\nwj00LDFV2g8RNC4A978packLHbt8UIjTq82q10TYabFdrloCh10hhi/Mao9MMYF1\nLQwYeada2ZCneD4yxlzKilj4hVV4xxjx54/HAN2NN5n13/YXZyw83EHtRAUe9J7M\noI3npifjXwwdX606cuTMAud56Hk64zGd1/a2wtKXAoGBALGNmDDyqS9ugwMQG4D/\nFWih9o0GCTz7iH6Dq2V9TY2+iAqHCUYRko22AZPgkoPdEtwas/MrJ9qNpoGlFepe\noWiJLBp5z5it+Q/Kkbvazde7Wz0zN5q9UMryzU9F3zJOfnLa/QqbpHPmfEW9Quqn\n5UF7AJPSYQyXoOmLvtYjqeXW\n-----END PRIVATE KEY-----\n",
  "client_email": "firebase-adminsdk-auypg@startup-carvaan-4c5db.iam.gserviceaccount.com",
  "client_id": "107813312352877718493",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-auypg%40startup-carvaan-4c5db.iam.gserviceaccount.com"
}
cred=credentials.Certificate(serviceAccountKey)
firebase_admin.initialize_app(cred)
pyrebase_app=pyrebase.initialize_app(firebaseConfig)
auth=pyrebase_app.auth()
db=firestore.client()
storage=pyrebase_app.storage()


def competition(request):
    if request.method == 'POST':
        startupname=request.POST.get('startup-name')
        email=request.POST.get('email')
        videourl=request.POST.get('video')
        description=request.POST.get('desc')
        number=request.POST.get('number')
        db.collection('competition').document(email).set({
            'startupname':startupname,
            'email':email,
            'videourl':videourl,
            'description':description,
            'number':number,
            'status':'Pending'
        })
        return redirect('/')
    docs=db.collection('competition').document('isopened').get()
    doc = docs.to_dict()['yes']
    if(doc):
        return render(request, 'competition.html',{})
    return render(request,'home.html',{})     

def home(request):
    return render(request,'home.html',{})

def startuplogin(request):
    if request.method == 'POST':
        email=request.POST.get('startupemail')
        password=request.POST.get('startuppwd')
        try:
            user=auth.sign_in_with_email_and_password(email, password)
            return redirect('/dashboard')
        except:
            return render(request,'login.html',{})                
    return render(request,'login.html',{})
  

def join(request):
    if request.method == 'POST' and request.FILES['blueone']:
        teamName=request.POST.get('teamname')
        email=request.POST.get('email')
        number=request.POST.get('phone')
        teamsize=request.POST.get('teamsize')
        student=True
        professional=True
        if request.POST.get('student')==None:
            student=False
        if request.POST.get('professional')==None:
            professional=False
        myfile = request.FILES['blueone']
        folder = uuid.uuid4().hex
        folder = folder[:20]
        storage.child('startupFiles').child(folder).put(myfile)
        filename = myfile.name
        db.collection('newstartups').document(folder).set({
            'teamName':teamName,
            'email':email,
            'number':number,
            'student':student,
            'teamsize':teamsize,
            'professional':professional,
            'filename':"/startupfiles/"+folder,
            'status':'Pending'
        })
        return redirect('/startuplogin')
    return render(request, 'join.html',{})

def startups(request):
    return render(request,'startups.html',{})

def users(request):
    return render(request,'users.html',{})

def table(request):
    if auth.current_user:
        if auth.current_user['email'] in ['yashagrawal0601@gmail.com', "login@gmail.com"]:
            docs = db.collection(u'allshares').document(u'shareid').collection(u'sharedetails').stream()
            return render(request,'table.html',{'docs':docs})
    return redirect("/startuplogin")   


# yashagrawal0601@gmail.com

def dashboard(request):
    if auth.current_user:
        if request.method == 'GET':
            val = False
            if auth.current_user['email'] in ['yashagrawal0601@gmail.com', "login@gmail.com"]:
                val = True
            localId = auth.current_user['localId']
            docs = db.collection('allshares').document(localId).collection("sharedetails").document("sharedetails").get()
            return render(request,"dashboard.html",{'docs':docs, 'val':val})     
    return redirect("/startuplogin")  

def startabout(request):
    docs = db.collection(u'allshares').stream()
    return render(request, 'startabout.html', {'docs':docs})

def addblog(request):
    if auth.current_user:
        if request.method == 'POST':
            localId=auth.current_user['localId']
            title=request.POST.get('title')
            videourl=request.POST.get('video')
            description=request.POST.get('description')
            types = "video"
            if videourl==None:
                types = "image"
            filename = None    
            if request.FILES['image']:
                myfile = request.FILES['image']
                folder = uuid.uuid4().hex
                folder = folder[:20]
                storage.child('blogs').child(folder).put(myfile)
                filename = myfile.name    
            db.collection('allshares').document(localId).collection('blogs').document(uuid.uuid4().hex).set({
               'title':title,
               'url':videourl,
               'likes':{},
               'comments':{},
               'description':description,
               'type':types,
               'date':datetime.now(tz=None),
               'filename':filename 
           })
        return render(request,'addblog.html',{})    
    return redirect("/startuplogin")


def help(request):
    if auth.current_user:
       if request.method=='GET':
           return render(request,'help.html',{})
       if request.method == 'POST':
           Ask_for_Assistance=True
           Ask_for_Intern=True
           Ask_for_Freelancing=True
           if request.POST.get('assistance')==None:
               Ask_for_Assistance=False
           if request.POST.get('intern')==None:
               Ask_for_Intern=False
           if request.POST.get('freelancing')==None:
               Ask_for_Freelancing=False
           Add_Comment=request.POST.get('comment')
           author = auth.current_user['email']
           db.collection('help').document().set({
               'Ask_for_Assistance':Ask_for_Assistance,
               'Ask_for_Intern':Ask_for_Intern,
               'Ask_for_Freelancing':Ask_for_Freelancing,
               'Add_Comment':Add_Comment,
               'date':datetime.now(tz=None),
               'status':"Pending",
               'author':author 
           })
           return render(request,'help.html',{})
    return redirect("/startuplogin")       

def userprofile(request):
    return render(request, "userprofile.html", {})

def helpdash(request):
    if auth.current_user:
        if auth.current_user['email'] in ['yashagrawal0601@gmail.com', "login@gmail.com"]:
            hlp = db.collection(u'help').stream()
            return render(request,"help-dash.html",{'hlp':hlp})
        else:
            return render(request,"login.html")
    return redirect("/startuplogin")     

def joindash(request):
    if auth.current_user:
        if auth.current_user['email'] in ['yashagrawal0601@gmail.com', 'login@gmail.com']:
            docs=db.collection('newstartups').stream()
            return render(request,"joindash.html",{'docs':docs})
    return redirect("/startuplogin")   

def compdash(request):
    if auth.current_user:
        if auth.current_user['email'] in ['yashagrawal0601@gmail.com', 'login@gmail.com']:
            docs=db.collection('competition').stream()
            return render(request,"compdash.html",{'docs':docs})
    return redirect("/startuplogin")    
         

def registerUser(request):
    if request.method == 'POST' and request.FILES['logoFile']:
        username=request.POST.get('email')
        password=request.POST.get('password')
        auth.create_user_with_email_and_password(username, password)
        auth.sign_in_with_email_and_password(username, password)
        localId=auth.current_user['localId']
        myfile = request.FILES['logoFile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        storage.child("shareFiles").child(localId).child(filename).put(myfile)
        if auth.current_user:
            name=request.POST.get('companyName')
            special=request.POST.get('description')
            growth=request.POST.get('growth')
            introVideoUrl=request.POST.get('introVideoUrl')
            invest=request.POST.get('peopleInvested')
            tag=request.POST.get('tag')
            buyingPrice=request.POST.get('buyingPrice')
            occupied=request.POST.get('occupied')
            sellingPrice=request.POST.get('sellingPrice')
            totalshares=request.POST.get('totalShares')
            db.collection('allshares').document(localId).set({
                'advice':"advice",
                'name':name,
                'nextslot':datetime.now(tz=None),
                'graph':[],
                'description':special,
                'growth':int(growth),
                'introvideourl':introVideoUrl,
                'logourl':"/shareFiles/"+auth.current_user['localId']+"/"+filename,
                'users':invest,
                'type':"beginner",
                'tags':[tag for tag in tag.split(' ')],
            })
            db.collection('allshares').document(localId).collection("sharedetails").document("sharedetails").set({
                'availableforbuying':int(totalshares),
                'availableforselling':0,
                'buyingprice':int(buyingPrice),
                'sellingprice':int(sellingPrice),
                'buyingtips':"positive",
                "sellingtips":"negative",
                'price':{},
                'totalinvested':0,
                "totalsharesatusers":0,
                "totalsharesonmarket":0,
            })
            return HttpResponse("successfully registered")
        else :
            return render(request,'login.html')
    return render(request,'registerstartup.html',{})

def blog(request):
    if auth.current_user:
        docs = db.collection(u'allshares').document(u'shareid').collection(u'blogs').stream()  
        return render(request,'blog.html',{'docs': docs})    
    return redirect("/startuplogin")    

def forgot(request):
    if request.method == 'POST' :
        email=request.POST.get('reset')
        auth.send_password_reset_email(email)
        return redirect("/startuplogin")
    return render(request,'forgot-pass.html')   
    
def delete_help(request,id):
    if auth.current_user:
        if auth.current_user['email'] in ['yashagrawal0601@gmail.com', "login@gmail.com"]:
            id = id
            print(id)
            doc=db.collection("help").document(id).delete()
            return redirect("/help-dash")
    return redirect('/startuplogin') 

def delete_join(request,id):
    if auth.current_user:
        if auth.current_user['email'] in ['yashagrawal0601@gmail.com', "login@gmail.com"]:
            id = id
            print(id)
            doc=db.collection("newstartups").document(id).delete()
            return redirect("/join-dash")
    return redirect('/startuplogin')        

def delete_comp(request,id):
    if auth.current_user:
        if auth.current_user['email'] in ['yashagrawal0601@gmail.com', "login@gmail.com"]:
            id = id
            print(id)
            #doc=db.collection("competition").document(id).delete()
            return redirect("/comp-dash")
    return redirect('/startuplogin')        

def accept_help(request,id):
    if auth.current_user:
        if auth.current_user['email'] in ['yashagrawal0601@gmail.com', "login@gmail.com"]:
            id = id
            print(id)
            db.collection("help").document(id).update({
                'status': 'Accepted'
            })
            return redirect("/help-dash")
    return redirect('/startuplogin')    

def accept_join(request,id):
    if auth.current_user:
        if auth.current_user['email'] in ['yashagrawal0601@gmail.com', "login@gmail.com"]:
            id = id
            print(id)
            db.collection("newstartups").document(id).update({
                'status': 'Accepted'
            })
            return redirect("/join-dash")
    return redirect('/startuplogin')    

def accept_comp(request,id):
    if auth.current_user:
        if auth.current_user['email'] in ['yashagrawal0601@gmail.com', "login@gmail.com"]:
            id = id
            print(id)
            db.collection("competition").document(id).update({
                'status': 'Accepted'
            })
            return redirect("/comp-dash")
    return redirect('/startuplogin')    

def logout(request):
    if auth.current_user:
         auth.current_user = None
         return redirect("/startuplogin") 
























def checkPayment(request):
    payments=db.collection("test").stream()
    for payment in payments:
        dict_payment=payment.to_dict()
        # print(dict_payment)
        response=requests.get("http://127.0.0.1:8000/payment/")
        link=response.text
        db.collection("test").document("test").update({
            "link":link
        })
    return HttpResponse(link)
def payment(request):
    response=requests.post('https://api.instamojo.com/oauth2/token/', data={
        'grant_type': 'client_credentials',
        'client_id': 'WUUP4tPdNShfzLsVrMbeMKHk56KB7ovA7mvrCpz6',
        'client_secret': 'iPLQoTVa4XbLyIwQLRha2HJiYp1blY9t23vybxCWcruwiUgH78Soyy3CFJABJKLajAgDZEeES4SUDAfzzMHHSmdMQzHo08SfxcLIlrrMkgc6pBZI8y9XOEnVP3Gf9UnO'
    })
    headers = { 
    "Authorization": "Bearer "+response.json()['access_token']
    }
    payload = {
    'purpose': 'FIFA 16',
    'amount': '11',
    'buyer_name': 'John Doe',
    'email': 'foo@example.com',
    'phone': '8171365728',
    'redirect_url': 'https://startup-carvaan.herokuapp.com/successful',
    'send_email': 'True',
    'send_sms': 'True',
    'webhook': 'https://startup-carvaan.herokuapp.com/successful',
    'allow_repeated_payments': 'False',
    }
    response = requests.post(
    "https://api.instamojo.com/v2/payment_requests/",
        data=payload, 
        headers=headers
    )
    id=response.json()['id']
    url=response.json()['longurl']
    return HttpResponse(url)

    

def status(request,id):
    headers = { "X-Api-Key": "4775c2f06f3d85a5b9cbeb9cfd2eeb69", "X-Auth-Token": "c8e0383df746f9d6f1c87fa1c1cab81e"}
    response = requests.get("https://www.instamojo.com/api/1.1/payment-requests/5c2b04e0ecb24b669734a90e7b332afa/",headers=headers)
    print (response.text)
    return 

def successful(request):
    return HttpResponse("successful")
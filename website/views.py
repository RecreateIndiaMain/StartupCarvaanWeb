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
        db.collection('competition').document().set({
            'startupname':startupname,
            'email':email,
            'videourl':videourl,
            'description':description
        })
        return redirect('/startuplogin')
    docs=db.collection('competition').document('isopened').get()
    doc = docs.to_dict()['yes']
    if(doc):
        return render(request, 'competition.html',{})
    return render(request,'login.html',{})    

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
            'professional':professional,
            'filename':"/startupfiles/"+folder,
            'status':False
        })
        return redirect('/startuplogin')
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
    if auth.current_user:
        val = False
        if(auth.current_user['email'] == 'yashagrawal0601@gmail.com'):
            val = True
        return render(request,'dashboard.html',{'val':val})
    return render(request,"login.html",{})    

def startabout(request):
    return render(request, 'startabout.html', {})

def addblog(request):
    if request.method == 'POST':
        print("entered in the first if")
        if  auth.current_user is not Null:
            print("entered in the nested if")
            localId=auth.current_user['localId']
            title=request.POST.get('title')
            blogurl=request.POST.get('blogurl')
            description=request.POST.get('description')
            db.collection('allshares').document(localId).collection('blogs').document(uuid.uuid4().hex).set({
               'title':title,
               'url':blogurl,
               'likes':{},
               'comments':{},
               'description':description,
               'type':"image",
               'date':datetime.now(tz=None)
           })
        return render(request,'addblog.html',{})    
    else:
        return render(request, 'addblog.html', {})


def help(request):
    if request.method is not "POST":
        return render(request,'help.html',{})
    if auth.current_user:
       if request.method=='GET':
           return render(request,'help.html',{})
       if request.method == 'POST':
           Ask_for_Assistance=True
           Ask_for_Mentor=True
           Increase_My_Share_Price=True
           if request.POST.get('assistance')==None:
               needAsistance=False
           if request.POST.get('mentorship')==None:
               needFreelancer=False
           if request.POST.get('share_price')==None:
               needIntern=False
           Add_Comment=request.POST.get('comment')
           db.collection('help').document().set({
               'Ask_for_Assistance':Ask_for_Assistance,
               'Ask_for_Mentor':Ask_for_Mentor,
               'Increase_My_Share_Price':Increase_My_Share_Price,
               'Add_Comment':Add_Comment
           })
           return render(request,'help.html',{})
def userprofile(request):
    return render(request, "userprofile.html", {})

def addBlogPage(request):
    return render(request, 'addblog.html', {})

def helpdash(request):
    return render(request, 'help-dash.html', {})

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
<<<<<<< HEAD
        #for document in docs:
        #    likes=document.to_dict()['likes']
        #    document.to_dict()['likes']=len(likes)       
=======
        for doc in docs:
            likes= doc.to_dict()['likes']
            print(len(likes))
>>>>>>> db505029f6d40d97c583f188896a23da2f1814d1
        return render(request,'blog.html',{'docs': docs})    
    return redirect("/startuplogin")    
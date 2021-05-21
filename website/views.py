from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib import messages
import uuid
import firebase_admin
from django.utils.datastructures import MultiValueDictKeyError
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
            if  email=='yashagrawal0601@gmail.com':
                print(auth.user)
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
            'filename':filename,
            'status':False
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
    print(auth.current_user)
    return render(request,'dashboard.html',{})

def blog(request):
    return render(request, 'blog.html', {})

def startabout(request):
    return render(request, 'startabout.html', {})

def addblog(request):
   if request.method == 'POST':
       if auth.current_user:
           localId=auth.current_user['localId']
           title=request.POST.get('title')
           blogurl=request.POST.get('blogurl')
           description=request.Post.get('description')
           needAsistance=True
           needFreelancer=True
           needIntern=True
           if request.POST.get('assistance')==None:
               needAsistance=False
           if request.POST.get('freelancing')==None:
               needFreelancer=False
           if request.POST.get('intern')==None:
               needIntern=False
           db.collection('allshares').document(localId).collection('blogs').document().set({
               'title':title,
               'url':videourl,
               'needAsistance':needAsistance,
               'needFreelancer':needFreelancer,
               'needIntern':needIntern,
               'description':description
           })


def help(request):
    return render(request,'help.html',{})
#    if auth.current_user:
#        if request.method=='GET':
#            return render(request,'help.html',{})
#        if request.method == 'POST':
#            Ask_for_Assistance=True
#            Ask_for_Mentor=True
#            Increase_My_Share_Price=True
#            if request.POST.get('assistance')==None:
#                needAsistance=False
#            if request.POST.get('mentorship')==None:
#                needFreelancer=False
#            if request.POST.get('share_price')==None:
#                needIntern=False
#            Add_Comment=request.POST.get('comment')
#            db.collection('help').document().set({
#                'Ask_for_Assistance':Ask_for_Assistance,
#                'Ask_for_Mentor':Ask_for_Mentor,
#                'Increase_My_Share_Price':Increase_My_Share_Price,
#                'Add_Comment':Add_Comment
#            })
#            return render(request,'help.html',{})
#    return redirect('/login/')
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
                'nextslot':" ",
                'graph':[],
                'description':special,
                'growth':int(growth),
                'introvideourl':introVideoUrl,
                'logourl':"shareFiles/"+auth.current_user['localId']+"/"+filename,
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
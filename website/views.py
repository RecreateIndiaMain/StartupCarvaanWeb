# import json
# from django import http
# from django.shortcuts import HttpResponse,render,redirect
# from django.contrib import messages
# import uuid
# from datetime import datetime
# import firebase_admin
# from django.utils.datastructures import MultiValueDictKeyError
# from google.oauth2 import service_account
# from pyasn1.type.univ import Null
# from  pyrebase import pyrebase
# from django.core.files.storage import FileSystemStorage 
# from firebase_admin import credentials,firestore
# import requests
# from requests.models import REDIRECT_STATI
# from requests.sessions import HTTPAdapter
# firebaseConfig = {
#     "apiKey": "AIzaSyBSWuQjmVQ1TJSKbYr8_A_Hw8zEp4Bhtb8",
#     "authDomain": "startup-carvaan-bbfe2.firebaseapp.com",
#     "projectId": "startup-carvaan-bbfe2",
#     "storageBucket": "startup-carvaan-bbfe2.appspot.com",
#     "messagingSenderId": "132130200533",
#     "appId": "1:132130200533:web:adc4fb4fac949601947b5c",
#     "measurementId": "G-RV429MN3PM",
#     "databaseURL": "https://startupcarvaan.firebaseio.com",
# }
# serviceAccountKey= {
#   "type": "service_account",
#   "project_id": "startup-carvaan-bbfe2",
#   "private_key_id": "a68d81a4bdbfb1b06f7e247e080328c68df63a51",
#   "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQCyCtVOgG/tqr5G\nPB7HhG+sdOZbgMbEiD2CTSZnruFbB1cUSu2uw7ydOlZaHbJKGuQv9nKu7I6Zawbq\napVq/BZNicnibN+4c/K1XviRcpajwomz9cwzWWh1d91KOKw6G9su1yBMfaP7h9Q5\n9AlMEFNZUw+DWALoWE/2Pe4+8Y9orwKO/FJkFTtK3OY7g7cjV9BXfJT5J2LyyDkd\ntIAOCErMukUpB6LQBlSlHcwq9DYVrSf6BXLTR+/d+Td9CxlC5zRi/5ZN7o5X+CXn\nD2QtYK6qgLesQ8T2UOrCplo6wgsc1BK1r2NnyrrwUBd1uVTijvD8l2kxVSdHQZVH\nOPvLt2XlAgMBAAECggEAP8gtvl+4uVXvsE2dYTCKqSd/1sv9aS69ik6FMaOuy+OH\nSJfHKlKo4VKi2MnGs1GK6bvKPew08bUr1xKz0I3al5CDKICEbRnsmxkYx1JbsPLi\nTfwCWWrwRxTXy90dpfuQu+kJgx2Hf3abit9n7T3z/g4Jgq4m7IGms7pf/WCgVYmz\ndgrws35tPLYUd+nOM0SVb6AgfKLdpExRBvAwF91o0Ou7AP0c+q3CVZ7kG5pOrC/L\nhORlmjKcxTBMwww7ZBXEo3GXIiJO2nbb+Yuf21HYHQCLgFvM8JMYCVIFGCDqRCM4\nYyrEc5RVZqxO+XGX1PPX+SL0tbjQ2RnNLajwlw9eiQKBgQDkyf5vBCIROqXbAPQz\nlB3LQWPa0MQAnRdG+74//MpN2nPX17QsHsJErcbpnPPX/qtMQXHrCeKAFxRdvlWM\n94jBU8Odsq2L6WahuJvLwdTRkmhoM5tS9mUcTARAKgRvlYcdHolqT4zNLoLAdfya\nFFFl8QnQOyKQ8VAeTUqOZwHDDwKBgQDHN70+AK6HFRXnudlPS/EFoRTdsid5uL3z\nVxgKdqzJCmNumLOBP+bS2Jlbj1lW+aYpCx6BUz1z4QICB+KCt6cxHyxUKHFYpqOX\nD/2ZyJ/pO1Q15ySlxFed6kG6suyOGvc/4oZYXlhOKF3c7CXUI+Hw4Exk8W1Jh7OB\nlKfEjv63ywKBgHwYH9xhVoUX1XwbYVlUnnBvsFSwZY+bpVOIGmIkoCpoMetCAWTo\n7iBITZrK2ewvIwSCfuKoguVNH2vVYBvM661I3NJ9Zup7l4JiWobDRMbDbcQPMdFm\n+eLGTIvs/mjzpsyhkpFKQqnL73mqxW9hU+FCQzthx9bsPLOi4qyorGj7AoGAdBeQ\nSUR+cCuic0JDV8lqcBxZm4PJK060Ks0zLk3QDOvn27hSytwhN/ePDuMvbdbXtI1N\nPpHyesfBsstDfWdmn+KJo5VZ0A5zwIFKCMb4ISM4xJypJ4yOfnDX0uOXpIwkT29D\nWNXJ4en2INrghIpQjV04R47FYBcbTUUCqzGlUBcCgYBVxCHu1MSIEKri5VH3CB7w\ne5sGPH55C9+GNSb2OXclgyA42Y2wxr0VPIqbUNAPdewItpfS4pofC4aEGyGNcW2N\n8Zk4MBqad9iKYj0WRqXs6YRd1OJf8mjnr0bVaQSUONMU+ZNGV6w+vulAO8L8chZG\nF992JSmUzJdZskXcA+aSTg==\n-----END PRIVATE KEY-----\n",
#   "client_email": "firebase-adminsdk-3t3qn@startup-carvaan-bbfe2.iam.gserviceaccount.com",
#   "client_id": "106154750526902436541",
#   "auth_uri": "https://accounts.google.com/o/oauth2/auth",
#   "token_uri": "https://oauth2.googleapis.com/token",
#   "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
#   "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-3t3qn%40startup-carvaan-bbfe2.iam.gserviceaccount.com"
# }


# cred=credentials.Certificate(serviceAccountKey)
# firebase_admin.initialize_app(cred)
# pyrebase_app=pyrebase.initialize_app(firebaseConfig)
# auth=pyrebase_app.auth()
# db=firestore.client()
# storage=pyrebase_app.storage()



# def competition(request):
#     if request.method == 'POST':
#         startupname=request.POST.get('startup-name')
#         email=request.POST.get('email')
#         videourl=request.POST.get('video')
#         description=request.POST.get('desc')
#         number=request.POST.get('number')
#         db.collection('competition').document(email).set({
#             'startupname':startupname,
#             'email':email,
#             'videourl':videourl,
#             'description':description,
#             'number':number,
#             'status':'Pending'
#         })
#         return redirect('/')
#     docs=db.collection('competition').document('isopened').get()
#     doc = docs.to_dict()['yes']
#     if(doc):
#         return render(request, 'competition.html',{})
#     return render(request,'home.html',{})     

# def home(request):
#     return render(request,'home.html',{})

# def startuplogin(request):
#     if request.method == 'POST':
#         email=request.POST.get('startupemail')
#         password=request.POST.get('startuppwd')
#         try:
#             user=auth.sign_in_with_email_and_password(email, password)
#             return redirect('/dashboard')
#         except:
#             return render(request,'login.html',{})                
#     return render(request,'login.html',{})
  

# def join(request):
#     if request.method == 'POST' and request.FILES['blueone']:
#         teamName=request.POST.get('teamname')
#         email=request.POST.get('email')
#         number=request.POST.get('phone')
#         teamsize=request.POST.get('teamsize')
#         student=True
#         professional=True
#         if request.POST.get('student')==None:
#             student=False
#         if request.POST.get('professional')==None:
#             professional=False
#         myfile = request.FILES['blueone']
#         folder = uuid.uuid4().hex
#         folder = folder[:20]
#         storage.child('startupFiles').child(folder).put(myfile)
#         filename = myfile.name
#         db.collection('newstartups').document(folder).set({
#             'teamName':teamName,
#             'email':email,
#             'number':number,
#             'student':student,
#             'teamsize':teamsize,
#             'professional':professional,
#             'filename':"/startupfiles/"+folder,
#             'status':'Pending'
#         })
#         return redirect('/startuplogin')
#     return render(request, 'join.html',{})

# def startups(request):
#     return render(request,'startups.html',{})

# def users(request):
#     return render(request,'users.html',{})

# def table(request):
#     if auth.current_user:
#         if auth.current_user['email'] in ['yashagrawal0601@gmail.com', "login@gmail.com"]:
#             docs = db.collection(u'allshares').document(u'shareid').collection(u'sharedetails').stream()
#             return render(request,'table.html',{'docs':docs})
#     return redirect("/startuplogin")   


# # yashagrawal0601@gmail.com

# def dashboard(request):
#     if auth.current_user:
#         if request.method == 'GET':
#             val = False
#             if auth.current_user['email'] in ['yashagrawal0601@gmail.com', "login@gmail.com"]:
#                 val = True
#             localId = auth.current_user['localId']
#             docs = db.collection('allshares').document(localId).collection("sharedetails").document("sharedetails").get()
#             return render(request,"dashboard.html",{'docs':docs, 'val':val})     
#     return redirect("/startuplogin")  

# def startabout(request):
#     docs = db.collection(u'allshares').stream()
#     return render(request, 'startabout.html', {'docs':docs})

# def addblog(request):
#     if auth.current_user:
#         if request.method == 'POST':
#             localId=auth.current_user['localId']
#             title=request.POST.get('title')
#             videourl=request.POST.get('video')
#             description=request.POST.get('description')
#             types = "video"
#             if videourl==None:
#                 types = "image"
#             filename = None    
#             if request.FILES['image']:
#                 myfile = request.FILES['image']
#                 folder = uuid.uuid4().hex
#                 folder = folder[:20]
#                 storage.child('blogs').child(folder).put(myfile)
#                 filename = myfile.name    
#             db.collection('allshares').document(localId).collection('blogs').document(uuid.uuid4().hex).set({
#                'title':title,
#                'url':videourl,
#                'likes':{},
#                'comments':{},
#                'description':description,
#                'type':types,
#                'date':datetime.now(tz=None),
#                'filename':filename 
#            })
#         return render(request,'addblog.html',{})    
#     return redirect("/startuplogin")


# def help(request):
#     if auth.current_user:
#        if request.method=='GET':
#            return render(request,'help.html',{})
#        if request.method == 'POST':
#            Ask_for_Assistance=True
#            Ask_for_Intern=True
#            Ask_for_Freelancing=True
#            if request.POST.get('assistance')==None:
#                Ask_for_Assistance=False
#            if request.POST.get('intern')==None:
#                Ask_for_Intern=False
#            if request.POST.get('freelancing')==None:
#                Ask_for_Freelancing=False
#            Add_Comment=request.POST.get('comment')
#            author = auth.current_user['email']
#            db.collection('help').document().set({
#                'Ask_for_Assistance':Ask_for_Assistance,
#                'Ask_for_Intern':Ask_for_Intern,
#                'Ask_for_Freelancing':Ask_for_Freelancing,
#                'Add_Comment':Add_Comment,
#                'date':datetime.now(tz=None),
#                'status':"Pending",
#                'author':author 
#            })
#            return render(request,'help.html',{})
#     return redirect("/startuplogin")       

# def userprofile(request):
#     return render(request, "userprofile.html", {})

# def helpdash(request):
#     if auth.current_user:
#         if auth.current_user['email'] in ['yashagrawal0601@gmail.com', "login@gmail.com"]:
#             hlp = db.collection(u'help').stream()
#             return render(request,"help-dash.html",{'hlp':hlp})
#         else:
#             return render(request,"login.html")
#     return redirect("/startuplogin")     

# def joindash(request):
#     if auth.current_user:
#         if auth.current_user['email'] in ['yashagrawal0601@gmail.com', 'login@gmail.com']:
#             docs=db.collection('newstartups').stream()
#             return render(request,"joindash.html",{'docs':docs})
#     return redirect("/startuplogin")   

# def compdash(request):
#     if auth.current_user:
#         if auth.current_user['email'] in ['yashagrawal0601@gmail.com', 'login@gmail.com']:
#             docs=db.collection('competition').stream()
#             return render(request,"compdash.html",{'docs':docs})
#     return redirect("/startuplogin")    
         

# def registerUser(request):
#     if request.method == 'POST' and request.FILES['logoFile']:
#         username=request.POST.get('email')
#         password=request.POST.get('password')
#         auth.create_user_with_email_and_password(username, password)
#         auth.sign_in_with_email_and_password(username, password)
#         localId=auth.current_user['localId']
#         myfile = request.FILES['logoFile']
#         fs = FileSystemStorage()
#         filename = fs.save(myfile.name, myfile)
#         storage.child("shareFiles").child(localId).child(filename).put(myfile)
#         if auth.current_user:
#             name=request.POST.get('companyName')
#             special=request.POST.get('description')
#             growth=request.POST.get('growth')
#             introVideoUrl=request.POST.get('introVideoUrl')
#             invest=request.POST.get('peopleInvested')
#             tag=request.POST.get('tag')
#             buyingPrice=request.POST.get('buyingPrice')
#             occupied=request.POST.get('occupied')
#             sellingPrice=request.POST.get('sellingPrice')
#             totalshares=request.POST.get('totalShares')
#             db.collection('allshares').document(localId).set({
#                 'advice':"advice",
#                 'name':name,
#                 'nextslot':datetime.now(tz=None),
#                 'graph':[],
#                 'description':special,
#                 'growth':int(growth),
#                 'introvideourl':introVideoUrl,
#                 'logourl':"/shareFiles/"+auth.current_user['localId']+"/"+filename,
#                 'users':invest,
#                 'type':"beginner",
#                 'tags':[tag for tag in tag.split(' ')],
#             })
#             db.collection('allshares').document(localId).collection("sharedetails").document("sharedetails").set({
#                 'availableforbuying':int(totalshares),
#                 'availableforselling':0,
#                 'buyingprice':int(buyingPrice),
#                 'sellingprice':int(sellingPrice),
#                 'buyingtips':"positive",
#                 "sellingtips":"negative",
#                 'price':{},
#                 'totalinvested':0,
#                 "totalsharesatusers":0,
#                 "totalsharesonmarket":0,
#             })
#             return HttpResponse("successfully registered")
#         else :
#             return render(request,'login.html')
#     return render(request,'registerstartup.html',{})

# def blog(request):
#     if auth.current_user:
#         docs = db.collection(u'allshares').document(u'shareid').collection(u'blogs').stream()  
#         return render(request,'blog.html',{'docs': docs})    
#     return redirect("/startuplogin")    

# def forgot(request):
#     if request.method == 'POST' :
#         email=request.POST.get('reset')
#         auth.send_password_reset_email(email)
#         return redirect("/startuplogin")
#     return render(request,'forgot-pass.html')   
    
# def delete_help(request,id):
#     if auth.current_user:
#         if auth.current_user['email'] in ['yashagrawal0601@gmail.com', "login@gmail.com"]:
#             id = id
#             print(id)
#             doc=db.collection("help").document(id).delete()
#             return redirect("/help-dash")
#     return redirect('/startuplogin') 

# def delete_join(request,id):
#     if auth.current_user:
#         if auth.current_user['email'] in ['yashagrawal0601@gmail.com', "login@gmail.com"]:
#             id = id
#             print(id)
#             doc=db.collection("newstartups").document(id).delete()
#             return redirect("/join-dash")
#     return redirect('/startuplogin')        

# def delete_comp(request,id):
#     if auth.current_user:
#         if auth.current_user['email'] in ['yashagrawal0601@gmail.com', "login@gmail.com"]:
#             id = id
#             print(id)
#             #doc=db.collection("competition").document(id).delete()
#             return redirect("/comp-dash")
#     return redirect('/startuplogin')        

# def accept_help(request,id):
#     if auth.current_user:
#         if auth.current_user['email'] in ['yashagrawal0601@gmail.com', "login@gmail.com"]:
#             id = id
#             print(id)
#             db.collection("help").document(id).update({
#                 'status': 'Accepted'
#             })
#             return redirect("/help-dash")
#     return redirect('/startuplogin')    

# def accept_join(request,id):
#     if auth.current_user:
#         if auth.current_user['email'] in ['yashagrawal0601@gmail.com', "login@gmail.com"]:
#             id = id
#             print(id)
#             db.collection("newstartups").document(id).update({
#                 'status': 'Accepted'
#             })
#             return redirect("/join-dash")
#     return redirect('/startuplogin')    

# def accept_comp(request,id):
#     if auth.current_user:
#         if auth.current_user['email'] in ['yashagrawal0601@gmail.com', "login@gmail.com"]:
#             id = id
#             print(id)
#             db.collection("competition").document(id).update({
#                 'status': 'Accepted'
#             })
#             return redirect("/comp-dash")
#     return redirect('/startuplogin')    


# def logout(request):
#     if auth.current_user:
#          auth.current_user = None
#          return redirect("/startuplogin") 


# def payments(request,id):
#     response= render(request,'payments.html',{})
#     response.set_cookie('userid',id,max_age=100)
#     return response


# def payment_status(request):
#     # id=request.COOKIES['userid']
#     data=db.collection('users').document("ByT93rO6JbXqTXNDXZLZXW3dlBv2").get()
#     db.collection('users').document("ByT93rO6JbXqTXNDXZLZXW3dlBv2").update({
#         'addedrci' : data.to_dict()["addedrci"]+10
#     })
#     return HttpResponse("hello user your payment is completed")

# #buy-sell section
# def buySell(request):
#     return render(request,'buy-sell.html',{})

# # def setting_cookie(request):
# #     response = HttpResponse("")
# #     response.set_cookie('userid', 'hahahahaha',5)
# #     return response

# # def getting_cookie(request):
# #     first_test  = request.COOKIES['userid'] 
# #     return first_test





















# # def checkPayment(request):
# #     payments=db.collection("test").stream()
# #     for payment in payments:
# #         dict_payment=payment.to_dict()
# #         # print(dict_payment)
# #         response=requests.get("http://127.0.0.1:8000/payment/")
# #         link=response.text
# #         db.collection("test").document("test").update({
# #             "link":link
# #         })
# #     return HttpResponse(link)
# # def payment(request):

# #     response1=requests.post('https://api.instamojo.com/oauth2/token/', data={
# #         'grant_type': 'client_credentials',
# #         'client_id': 'WUUP4tPdNShfzLsVrMbeMKHk56KB7ovA7mvrCpz6',
# #         'client_secret': 'iPLQoTVa4XbLyIwQLRha2HJiYp1blY9t23vybxCWcruwiUgH78Soyy3CFJABJKLajAgDZEeES4SUDAfzzMHHSmdMQzHo08SfxcLIlrrMkgc6pBZI8y9XOEnVP3Gf9UnO'
# #     })
# #     headers = { 
# #     "Authorization": "Bearer "+response1.json()['access_token']
# #     }
# #     payload = {
# #     'purpose': 'FIFA 16',
# #     'amount': '11',
# #     'buyer_name': 'John Doe',
# #     'email': 'foo@example.com',
# #     'phone': '8171365728',
# #     'redirect_url': 'https://api.instamojo.com/integrations/android/redirect/',
# #     'send_email': 'True',
# #     'send_sms': 'True',
# #     'webhook': 'https://api.instamojo.com/integrations/android/redirect/',
# #     'allow_repeated_payments': 'False',
# #     }
# #     response = requests.post(
# #         "https://api.instamojo.com/v2/payment_requests/", 
# #         data=payload, 
# #         headers=headers
# #     ) 
# #     print(response.text)

# #     headers = { 
# #     "Authorization": "Bearer "+response1.json()['access_token']
# #     }
# #     payload = {
# #     'id': response.json()['id'],
# #     }
# #     response2 = requests.post(
# #     "https://api.instamojo.com/v2/gateway/orders/payment-request/", 
# #     data=payload, 
# #     headers=headers
# #     )
# #     return HttpResponse(response2.json()['order_id'])
    

# # def status(request,id):
# #     headers = { "X-Api-Key": "4775c2f06f3d85a5b9cbeb9cfd2eeb69", "X-Auth-Token": "c8e0383df746f9d6f1c87fa1c1cab81e"}
# #     response = requests.get("https://www.instamojo.com/api/1.1/payment-requests/5c2b04e0ecb24b669734a90e7b332afa/",headers=headers)
# #     print (response.text)
# #     return 

# # def successful(request):
# #     status=request.POST.get('payment_status')
# #     if status == "Failed":
# #         return HttpResponse("payment failed")
# #     else:
# #         return HttpResponse("payment completed")



from django.http.response import HttpResponse
from rssi.models import Rssi

def bla(request):
    ma={}
    for key,value in request.POST.items():
        object=Rssi(value=1.001)
        object.save()
    return HttpResponse(ma)


def showRssi(request):
    obj=Rssi.objects.all()
    return HttpResponse(obj) 
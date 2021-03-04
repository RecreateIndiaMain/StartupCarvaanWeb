from django.http import HttpResponse

def home(request):
    return HttpResponse("CLEVER i AM ")
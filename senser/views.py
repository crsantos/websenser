from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello!")

def sense(request,lol):
        return HttpResponse("Sensed "+lol)
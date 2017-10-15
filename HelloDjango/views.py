from django.http import HttpResponse


def index(request):
    return HttpResponse("this is main page.")

def second(request):
    return HttpResponse("this is second page.")
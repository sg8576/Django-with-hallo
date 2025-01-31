from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "hello/index.html")
def Shobhit(request):
    return HttpResponse("Hello, Shobhit")
def harry(request):
    return HttpResponse("Hello, Harry")
def mike(request):
    return HttpResponse("Hello, Mike")
def greet(request, name):
    return render(request, "hello/greet.html", { "name":name.capitalize()})
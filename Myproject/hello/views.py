from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse("Hello World!")
def Shobhit(request):
    return HttpResponse("Hello, Shobhit")
def harry(request):
    return HttpResponse("Hello, Harry")
def mike(request):
    return HttpResponse("Hello, Mike")
from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("My home page")
    
def about(request):
    return HttpResponse("My About page")
    
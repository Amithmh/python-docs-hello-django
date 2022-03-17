from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    return HttpResponse("Hello, ITC team How are you ")

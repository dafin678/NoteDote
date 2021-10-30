from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    tes = '<h1>This page is under maintenance</h1>'
    return HttpResponse(tes)
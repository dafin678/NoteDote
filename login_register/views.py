from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.views import LoginView 

# Create your views here.
def index(request):
    tes = '<h1>This page is under maintenance</h1>'
    return HttpResponse(tes)

class AdminLogin(LoginView):
    template_name = 'login_form.html'
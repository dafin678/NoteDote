from django.shortcuts import render
from django.http import HttpResponse
# from django.contrib.auth.views import LoginView 

# Create your views here.
def login(request):
    return render(request, 'login_form.html')
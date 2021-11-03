from django.shortcuts import render
from django.http import HttpResponse
# from django.contrib.auth.views import LoginView 

# Create your views here.
def index(request):
    return render(request, 'login_form.html')

# class AdminLogin(LoginView):
#     template_name = 'login_form.html'
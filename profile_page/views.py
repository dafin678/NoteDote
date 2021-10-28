from django.shortcuts import render
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# @login_required(login_url='/admin/login/')
def index(request):
    profile = Profile.objects.filter(user=User.objects.get (username=request.user))
    response = {'profiles': profile}
    return render(request, 'profile_index.html', response)


from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import ProfileEditForm
# @login_required(login_url='/admin/login/')
def index(request):
    profile = Profile.objects.filter(user=User.objects.get (username=request.user))
    response = {'profiles': profile}
    return render(request, 'profile_index.html', response)

def edit(request):
    if request.method == 'POST':
        form = ProfileEditForm(request.POST, request.FILES, instance=request.user.profile) 
        if form.is_valid():
            
            form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('/profile')

    else:
        form = ProfileEditForm(instance=request.user.profile)

    context = {
        'form': form
    }

    return render(request, 'profile_edit.html', context)
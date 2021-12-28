from django.http.response import JsonResponse
from django.shortcuts import render, redirect
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import ProfileEditForm
from django.views.decorators.csrf import csrf_exempt

@login_required(login_url='/admin/login/')
def index(request):
    profile = Profile.objects.filter(user=User.objects.get (username=request.user))
    response = {'profiles': profile}
    return render(request, 'profile_index.html', response)

@login_required(login_url='/admin/login/')
def edit(request):
    if request.method == 'POST':
        form = ProfileEditForm(request.POST, instance=request.user.profile) 
        if form.is_valid():
            
            form.save()
            return redirect('/profile')

    else:
        form = ProfileEditForm(instance=request.user.profile)

    context = {
        'form': form
    }

    return render(request, 'profile_edit.html', context)

@csrf_exempt
def get_profile(request):
    if request.method == 'GET':
        profile = Profile.objects.filter(user=User.objects.get (username=request.user))
        name = profile.values('name')[0]['name']
        about = profile.values('about')[0]['about']
        image_name = profile.values('image_name')[0]['image_name']
        data = {
            "name": name,
            "about": about,
            "imageUrl" : "http://notedote.herokuapp.com/static/img/" + image_name
        }
        return JsonResponse(data)

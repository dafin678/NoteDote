from django.shortcuts import render
from django.http import HttpResponse
from .models import Weekly_schedule
# from django.contrib.auth.decorators import login_required

# Create your views here.
# @login_required(login_url='/admin/login')
def index(request):
    # profile = UserProfile.objects.create(user=request.user)
    # schedules = Weekly_schedule.objects.filter(user=request.user).order_by('start_time')
    schedules = Weekly_schedule.objects.order_by('start_time')
    response = {'schedules': schedules}
    return render(request, 'schedule.html', response)



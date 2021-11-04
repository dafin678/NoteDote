from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Weekly_schedule
from .forms import ScheduleForm
# from django.contrib.auth.decorators import login_required

# Create your views here.
# @login_required(login_url='/admin/login')
def index(request):
    # profile = UserProfile.objects.create(user=request.user)
    schedules = Weekly_schedule.objects.filter(user=request.user).order_by('start_time')
    # schedules = Weekly_schedule.objects.order_by('start_time')
    response = {'schedules': schedules}
    return render(request, 'schedule.html', response)

def add_schedule(request):
    form = ScheduleForm(request.POST or None)

    if (form.is_valid and request.method == 'POST'):
        form.save()
        return HttpResponseRedirect('/weekly_schedule')

    response = {'form':form}
    return render(request, 'schedule_form.html', response)

from django.http.response import JsonResponse
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Weekly_schedule
from .forms import ScheduleForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView
from django.core import serializers
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
class list_schedule(LoginRequiredMixin, ListView):
    # @login_required(login_url='/admin/login')
    model = Weekly_schedule
    template_name = 'schedule.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        for i in range(1,8):
            context['day' + str(i)] = Weekly_schedule.objects.filter(user=self.request.user).filter(day=i).order_by('start_time')
        return context

# @login_required(login_url='/admin/login/')
def add_schedule(request):
    form = ScheduleForm(request.POST or None)

    if (form.is_valid and request.method == 'POST'):
        fs = form.save(commit=False)
        fs.user= request.user
        fs.save()
        return redirect('/weekly_schedule')

    response = {'form':form}
    return render(request, 'schedule_form.html', response)

@csrf_exempt
def get_all_schedule(request):
    # list_schedule = Weekly_schedule.objects.all().filter(user=User.objects.get(username=request.user)).order_by('start_time')
    list_schedule = Weekly_schedule.objects.all().order_by('start_time')
    data = serializers.serialize('json',list_schedule)
    return HttpResponse(data, content_type="application/json")

@csrf_exempt
def get_monday_schedule(request):
    list_schedule = Weekly_schedule.objects.all().filter(day=1).order_by('start_time')
    data = serializers.serialize('json',list_schedule)
    return HttpResponse(data, content_type="application/json")

@csrf_exempt
def get_tuesday_schedule(request):
    list_schedule = Weekly_schedule.objects.all().filter(day=2).order_by('start_time')
    data = serializers.serialize('json',list_schedule)
    return HttpResponse(data, content_type="application/json")

@csrf_exempt
def get_wednesday_schedule(request):
    list_schedule = Weekly_schedule.objects.all().filter(day=3).order_by('start_time')
    data = serializers.serialize('json',list_schedule)
    return HttpResponse(data, content_type="application/json")

@csrf_exempt
def get_thursday_schedule(request):
    list_schedule = Weekly_schedule.objects.all().filter(day=4).order_by('start_time')
    data = serializers.serialize('json',list_schedule)
    return HttpResponse(data, content_type="application/json")

@csrf_exempt
def get_friday_schedule(request):
    list_schedule = Weekly_schedule.objects.all().filter(day=5).order_by('start_time')
    data = serializers.serialize('json',list_schedule)
    return HttpResponse(data, content_type="application/json")

@csrf_exempt
def get_saturday_schedule(request):
    list_schedule = Weekly_schedule.objects.all().filter(day=6).order_by('start_time')
    data = serializers.serialize('json',list_schedule)
    return HttpResponse(data, content_type="application/json")

@csrf_exempt
def get_sunday_schedule(request):
    list_schedule = Weekly_schedule.objects.all().filter(day=7).order_by('start_time')
    data = serializers.serialize('json',list_schedule)
    return HttpResponse(data, content_type="application/json")


# def delete_schedule(request, id):
#     schedule = Weekly_schedule.get(pk=id)
#     schedule.delete()
#     return redirect('/weekly_schedule')
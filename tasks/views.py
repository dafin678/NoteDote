from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, JsonResponse
from django.views import View
from tasks.forms import TaskForm
from tasks.models import Task
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core import serializers
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

# from django.shortcuts import render, redirect
# from django.template import loader

@method_decorator(csrf_exempt, name='dispatch')
class TaskView(LoginRequiredMixin, View):
    login_url = '/admin/login/'
    form_class = TaskForm
    def post(self, request, *args, **kwargs):
        if request.is_ajax():
            form = self.form_class(request.POST)
            if form.is_valid():
                fs= form.save(commit=False)
                fs.user= request.user
                fs.save()
                return JsonResponse({"message": "success"})
            return JsonResponse({"message": "Validation failed"})
        return JsonResponse({"message": "Wrong request"})

    def get(self,request, *args, **kwargs):
        return render(request, "form.html", {})

class ViewTaskView(LoginRequiredMixin,View):
    login_url = '/admin/login/'
    def get(self,request, *args, **kwargs):
        tasks = Task.objects.filter(user=User.objects.get(username=request.user))
        return render(request, "view.html", {"tasks":tasks.order_by("task_date", "end_time")})

@method_decorator(csrf_exempt, name='dispatch')
class TaskDeleteView(LoginRequiredMixin,View):
    login_url = '/admin/login/'
    def get(self,request, pk, *args, **kwargs):
        if request.is_ajax():
            task = Task.objects.get(pk=pk)
            task.delete()
            return JsonResponse({"message":"success"})
        return JsonResponse({"message": "Wrong request"})

def get_all_tasks(request):
    all_tasks = Task.objects.all()
    data = serializers.serialize('json', all_tasks)
    return HttpResponse(data, content_type="application/json")

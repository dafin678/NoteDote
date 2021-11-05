from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views import View
from tasks.forms import TaskForm
from tasks.models import Task
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, user_passes_test
# from django.shortcuts import render, redirect
# from django.template import loader

class TaskView(View):
    form_class = TaskForm
    @login_required(login_url='admin')
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

class ViewTaskView(View):
    def get(self,request, *args, **kwargs):
        tasks = Task.objects.filter(user=User.objects.get(username=request.user))
        return render(request, "view.html", {"tasks":tasks.order_by("end_time", "task_date")})

class TaskDeleteView(View):
    @login_required(login_url='admin')
    def get(self,request, pk, *args, **kwargs):
        if request.is_ajax():
            task = Task.objects.get(pk=pk)
            task.delete()
            return JsonResponse({"message":"success"})
        return JsonResponse({"message": "Wrong request"})

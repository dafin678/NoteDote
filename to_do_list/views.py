from django.shortcuts import render
from .models import to_do_list
from .forms import ToDoForm
from rest_framework.response import Response
# from .serializers import TaskSerializer
from django.http.response import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

# @login_required(login_url='/admin/login/')
def index(request):
    to_do = to_do_list.objects.all()
    response = {'to_do': to_do.order_by("due_date")}
    return render(request, 'index.html', response)

def add_task(request):
    form = ToDoForm(request.POST or None)
    if (form.is_valid and request.method == "POST"):
        form.save()
        return HttpResponseRedirect('/to-do-list')
    else:
        response = {'form': form}
        return render(request, 'todo_form.html', response)

# def taskUpdate(request, pk):
# 	task = to_do_list.objects.get(id=pk)
# 	serializer = TaskSerializer(instance=task, data=request.data)

# 	if serializer.is_valid():
# 		serializer.save()

	return Response(serializer.data)

def taskDelete(request, pk):
	task = to_do_list.objects.get(id=pk)
	task.delete()

	return Response('Item succsesfully delete!')

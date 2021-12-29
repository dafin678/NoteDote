from django.urls import path
from .views import TaskView, ViewTaskView, TaskDeleteView
from .views import get_all_tasks

app_name = "tasks"

urlpatterns = [
    path('', ViewTaskView.as_view(), name="view"),
    path('add-task', TaskView.as_view(), name="task"), 
    path('add-task/<int:pk>', TaskDeleteView.as_view(), name="delete"),
    path('get_all_tasks', get_all_tasks, name='get-all-tasks'),
]
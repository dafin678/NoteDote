from django.urls import path
from .views import add_task, index

# app_name = 'main'

urlpatterns = [
    path('', index, name='index'),
    path('add-task', add_task),
]

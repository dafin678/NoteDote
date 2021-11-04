from django.urls import path
from .views import index, add_schedule

urlpatterns = [
    path('', index, name='index'),
    path('add-schedule/', add_schedule, name='add_schedule'),
]
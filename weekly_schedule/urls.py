from django.urls import path
from .views import  list_schedule, add_schedule

app_name = 'weekly_schedule'

urlpatterns = [
    path('', list_schedule.as_view(), name='list_schedule'),
    path('add-schedule/', add_schedule, name='add_schedule'),
    # path('delete_schedule/<int:id', delete_schedule, name="delete_schedule"),
]
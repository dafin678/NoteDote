from os import name
from django.urls import path
from .views import  list_schedule, add_schedule, get_all_schedule, get_monday_schedule, get_tuesday_schedule, get_wednesday_schedule, get_thursday_schedule, get_friday_schedule, get_saturday_schedule, get_sunday_schedule, post_data

app_name = 'weekly_schedule'

urlpatterns = [
    path('', list_schedule.as_view(), name='list_schedule'),
    path('add-schedule/', add_schedule, name='add_schedule'),
    path('get_all_schedule/', get_all_schedule, name='get_all_schedule'),
    path('get-monday-schedule/', get_monday_schedule, name='get_monday_schedule'),
    path('get-tuesday-schedule/', get_tuesday_schedule, name='get_tuesday_schedule'),
    path('get-wednesday-schedule/', get_wednesday_schedule, name='get_wednesday_schedule'),
    path('get-thursday-schedule/', get_thursday_schedule, name='get_thursday_schedule'),
    path('get-friday-schedule/', get_friday_schedule, name='get_friday_schedule'),
    path('get-saturday-schedule/', get_saturday_schedule, name='get_saturday_schedule'),
    path('get-sunday-schedule/', get_sunday_schedule, name='get_sunday_schedule'),
    path('post-data/', post_data, name='post_data'),

    # path('delete_schedule/<int:id', delete_schedule, name="delete_schedule"),
]
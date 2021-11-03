from typing import ValuesView
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('add/',views.add, name='add'),
    path('update/<event_id>', views.update , name='update'),
    path('delete/<event_id>', views.delete , name='delete'),
    path('detail/<event_id>', views.detail , name= 'detail'),
]
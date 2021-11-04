from django.urls import path

from . import views

app_name = 'main'

urlpatterns = [
    path('', views.Add_Motivasi, name='motivasi'),
    path('view_motivasi/', views.view_motivasi, name='view_motivasi'),
    path('json/', views.json, name='json'),
    path('delete_motivasi/<mot_id>/', views.delete_motivasi, name='delete-motivasi'),
]

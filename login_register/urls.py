from django.urls import path
from.views import index
# from.views import AdminLogin

urlpatterns = [
    path('login/', index, name='index'),
    
]
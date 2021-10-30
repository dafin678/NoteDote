from django.urls import path
from.views import index
from.views import AdminLogin

urlpatterns = [
    path('', index, name='index'),
    path('login/', AdminLogin.as_view(), name="login")
]
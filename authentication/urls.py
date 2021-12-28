from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import login


urlpatterns = [
    path('login', login, name='auth-login'),
]


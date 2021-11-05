from django.urls import path
from.views import login
from.views import signup

urlpatterns = [
    path('login/', login, name='login'),
    path('signup/', signup, name='signup')
]
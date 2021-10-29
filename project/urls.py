"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path, re_path
import to_do_list.urls as to_do_list
from to_do_list.views import index as index_to_do_list
<<<<<<< HEAD
<<<<<<< HEAD
# import weekly_schedule.urls as weekly_schedule
=======
=======
import profile_page.urls as profile
>>>>>>> e48d9b79ce2a013cdec4e8bac144e2e88cf4146e
import weekly_schedule.urls as weekly_schedule
>>>>>>> 286fb67b0c5938aaa5d167981a7095f51e32f329

urlpatterns = [
    path('admin/', admin.site.urls),
    path('to-do-list/', include(to_do_list)),
<<<<<<< HEAD
<<<<<<< HEAD
    # path('weekly_schedule/', include(weekly_schedule)),
=======
=======
    path('profile/', include(profile)),
>>>>>>> e48d9b79ce2a013cdec4e8bac144e2e88cf4146e
    path('weekly_schedule/', include(weekly_schedule)),
>>>>>>> 286fb67b0c5938aaa5d167981a7095f51e32f329
    re_path(r'^$', index_to_do_list, name='index')
]
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
from tasks.views import ViewTaskView as index_to_do_list
import tasks.urls as tasks
import profile_page.urls as profile
import weekly_schedule.urls as weekly_schedule
import personal_journal.urls as personal_journal
import notes.urls as notes
import login_register.urls as login_register

urlpatterns = [
    path('admin/', admin.site.urls),
    path('notes/', include(notes)),
    path("tasks/",include(tasks)),
    path('profile/', include(profile)),
    path('weekly_schedule/', include(weekly_schedule)),
    path('login/', include(login_register)),
    path('personal_journal/', include(personal_journal)),
    re_path(r'^$', index_to_do_list.as_view(), name='index')
]

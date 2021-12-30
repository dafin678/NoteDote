from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import index, edit, get_profile, submit_profile


urlpatterns = [
    path('', index, name='index'),
    path('edit', edit, name='edit'),
    path('get-profile', get_profile, name='get-profile'),
    path('submit-profile', submit_profile, name ='submit-profile'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


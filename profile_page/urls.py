from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import index, edit


urlpatterns = [
    path('', index, name='index'),
    path('edit', edit, name='edit'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


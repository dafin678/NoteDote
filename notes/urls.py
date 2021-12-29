from django.urls import path
from .views import add_note, index

urlpatterns = [
    path('', index, name='index'),
    path('add-note', add_note, name='add-note')
]

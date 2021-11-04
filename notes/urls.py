from django.urls import path
from .views import add_note, note_list

urlpatterns = [
    path('', note_list, name='note-list'),
    path('add-note', add_note, name='add-note')
]

from django.urls import path
from .views import add_note, note_list

urlpatterns = [
    path('add-note', add_note, name='add-note'),
    path('note-list', note_list, name='note-list')
]

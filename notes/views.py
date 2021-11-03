from django.http.response import HttpResponseRedirect
from .models import notes
from django.shortcuts import render

from notes.forms import notesForm

def add_note(request):
    context = {}
    form = notesForm(request.POST or None, request.FILES or None)

    if (form.is_valid() and request.method == 'POST'):
        form.save()
        return HttpResponseRedirect('/notes')
    
    context['form'] = form
    return render(request, "notes_form.html", context)

def note_list(request):
    note = notes.objects.all()
    response = {'notes': note}
    return render(request, "notes_list.html", response)
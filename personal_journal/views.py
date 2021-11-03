from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render, get_object_or_404
from .models import Entry
from .forms import EntryForm


def back(request):
    return redirect('home')

def index(request):
    entries = Entry.objects.all

    context = {'entries' : entries}

    return render(request,'personal.html', context)

def update(request,event_id):
    entries = Entry.objects.get(pk=event_id)
    form = EntryForm(request.POST or None, instance=entries)
    if form.is_valid():
        form.save()
        return redirect('home')
    
    context = {'entries' : entries,'form': form}
    return render(request,'update.html',context)

def delete(request,event_id):
    entries = Entry.objects.get(pk=event_id)
    entries.delete()
    return redirect('home')

def detail(request,event_id):
    entries = get_object_or_404(Entry, pk=event_id)
    context = {'entries' : entries}
    return render(request,'detail.html',context)


def add(request):
    if request.method == 'POST':
        form = EntryForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = EntryForm()

    context = {'form': form}
    return render(request,'add.html', context)
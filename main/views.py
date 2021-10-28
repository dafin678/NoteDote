from django.shortcuts import get_object_or_404, redirect, render
from .models import Motivasi
from .forms import MotivasiForm
from django.core import serializers
from django.http.response  import HttpResponse
from django.contrib import messages

def home(request):
    return render(request, 'main/home.html')

def json(request):
    data = serializers.serialize('json', Motivasi.objects.all())
    return HttpResponse(data, content_type="application/json")


def Add_Motivasi(request):
    form = MotivasiForm(request.POST or None, request.FILES or None)
    response = {'form': form}
    # check if form data is valid
    if form.is_valid():
        # save the form data to model
        form.save()
    return render(request, 'main/motivasi/motivasi.html',response)

def view_motivasi(request):
    motivasi =  Motivasi.objects.all()
    response = {'motivasi': motivasi}
    return render(request, 'main/motivasi/view_motivasi.html', response)


def delete_motivasi(request,mot_id):
    motivasi = get_object_or_404(Motivasi,pk=mot_id)
    motivasi.delete()
    return redirect('main:view_motivasi')
   
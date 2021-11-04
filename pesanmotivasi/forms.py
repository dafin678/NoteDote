from django.forms import widgets
from .models import Motivasi
from django import forms



class MotivasiForm(forms.ModelForm):
    class Meta:
        model = Motivasi
        fields = ('to','pesan')

        widgets = {
            'to' : forms.TextInput(attrs={'class':'form-control'}),
            'pesan' : forms.Textarea(attrs={'class':'form-control'})
        }


from django import forms
from django.db.models import fields
from .models import notes

class notesForm(forms.ModelForm):
    class Meta:
        model = notes
        fields = "__all__"
        error_messages = {
            'required' : 'Please write your note'
        }
        input_attrs = {
			'type' : 'text',
		}

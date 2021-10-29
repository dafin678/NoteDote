from django import forms
from django.db.models import fields
from .models import to_do_list


class ToDoForm(forms.ModelForm):
	class Meta:
		model = to_do_list
		fields = "__all__"
		error_messages = {
			'required' : 'Please Fill All Required Informations'
		}
		input_attrs = {
			'type' : 'text',
		}
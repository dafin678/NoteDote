from django import forms
from django.db.models import fields
from .models import Task


class TaskForm(forms.ModelForm):
	class Meta:
		model = Task
		fields = ['name', 'description', 'task_date', 'end_time']
		error_messages = {
			'required' : 'Please Fill All Required Informations'
		}
		input_attrs = {
			'type' : 'text',
		}
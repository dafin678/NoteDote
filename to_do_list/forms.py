from django import forms
from django.db.models import fields
from .models import to_do_list

# class DateInput(forms.DateInput):
#     input_type = "date"
#     def __init__(self, **kwargs):
#         kwargs["format"] = "%Y-%m-%d"
#         # kwargs["format"] = "%d-%m-%Y"
#         super().__init__(**kwargs)



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
		# widgets = {
        #     'my_date':DateInput(format=["%Y-%m-%d"],),
        #     # 'my_date': XYZ_DateInput(format=["%d-%m-%Y"], ),
		# }
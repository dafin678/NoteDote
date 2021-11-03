from django.forms import ModelForm
from .models import Weekly_schedule
from django.forms.widgets import TimeInput

class ScheduleForm(ModelForm):
    class Meta:
        model = Weekly_schedule
        fields = '__all__'

        widgets = {
            'start_time': TimeInput(attrs={'type':'time'}),
            'due_time': TimeInput(attrs={'type':'time'}),
        }
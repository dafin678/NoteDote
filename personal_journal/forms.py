from django.db.models import fields
from django.forms import ModelForm
from .models import Entry


class EntryForm(ModelForm):
    class Meta:
        model = Entry
        fields = ('text','title')
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['text'].widget.attrs.update({'class' :'textarea', 'placeholder' : 'What\'s on your mind ?'})
        self.fields['title'].widget.attrs.update({'class' :'input', 'placeholder' : 'What\'s your title ?'})
        
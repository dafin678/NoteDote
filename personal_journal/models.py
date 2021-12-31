from django.db import models
from ckeditor.fields import RichTextField


class Entry(models.Model):
    title = models.CharField(max_length=1000)
    text = RichTextField(blank=True,null=True)


    def __str__(self):
        return 'Entry #{}'.format(self.id)
        # return title
    
    class Meta:
        verbose_name_plural = 'entries'

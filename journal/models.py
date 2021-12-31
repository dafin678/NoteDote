from django.db import models


class Journal(models.Model):
    title = models.CharField(max_length=1000)
    text = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    



    def __str__(self):
        return 'Journal {}'.format(self.id)

    class Meta:
        ordering = ['-updated'] 

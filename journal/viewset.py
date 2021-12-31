from rest_framework import viewsets
from . import models
from . import serializers


class JournalViewset(viewsets.ModelViewSet):
    queryset = models.Journal.objects.all()
    serializer_class = serializers.JournalSerializer



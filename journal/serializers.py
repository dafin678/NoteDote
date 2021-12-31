from django.db import models
from rest_framework.serializers import ModelSerializer
from journal.models import Journal

class JournalSerializer(ModelSerializer):
    class Meta:
        model = Journal
        fields = '__all__'
    
from django.conf import settings
from django.db import models
from django.urls import reverse

class Task(models.Model):
    name = models.CharField(max_length=40)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('task_detail', args=[str(self.id)])

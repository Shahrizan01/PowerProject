from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length=100)
    numroom = models.IntegerField(default=1)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

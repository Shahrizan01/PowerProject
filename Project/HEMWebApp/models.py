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


class Room(models.Model):
    name = models.CharField(max_length=100)
    desc = models.CharField(max_length=300)
    app = models.CharField(max_length=50, default='Living Room')
    length = models.FloatField()
    width = models.FloatField()
    height = models.FloatField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(default=timezone.now)
    color = models.CharField(max_length=7, default='#4154f1')
    occupants = models.IntegerField(default=1)
    window_num = models.IntegerField(default=1)
    window_orientation = models.CharField(max_length=11, default='')
    window_size = models.FloatField(default=0)
    illumination_req = models.IntegerField(default=200)
    lamp_specs = models.CharField(max_length=50, default='')
    aircond_type = models.CharField(max_length=50, default='')

    def __str__(self):
        return self.name

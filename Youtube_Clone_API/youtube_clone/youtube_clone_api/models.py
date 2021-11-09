from django.db import models

# Create your models here.
class Video(models.Model):
    title: models.CharField(max_length=100)
    description: models.CharField(max_length=100)
    artist: models.CharField(max_length= 100)
    release_date: models.DateTimeField()

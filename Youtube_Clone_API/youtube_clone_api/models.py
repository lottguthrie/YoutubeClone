from django.db import models
from django.db.models.fields.related import ForeignKey
from django.template.defaultfilters import slugify
from django.shortcuts import render, get_object_or_404


# Create your models here.
class Video(models.Model):
    title: models.CharField(max_length=100)
    description: models.CharField(max_length=100)
    artist: models.CharField(max_length= 100)
    release_date: models.DateTimeField()
    video_id: models.IntegerField(default=0)
    likes= models.IntegerField(default=0)
    dislikes= models.IntegerField(default=0)
     
    
    def save(self, *args, **kwargs):
        self.url= slugify(self.title)
        super(Video, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

class Comment(models.Model):
    comment: models.TextField(max_length=500)
    video_id = models.ForeignKey('youtube_clone_api.Video', blank=True, null=True, on_delete=models.CASCADE)
    likes= models.IntegerField(default=0)
    dislikes= models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        self.url= slugify(self.comment)
        super(Comment, self).save(*args, **kwargs)

    def __str__(self):
        return self.comment
    
class Reply(models.Model):
    reply: models.TextField(max_length=500)
    comment_id = models.ForeignKey('youtube_clone_api.Comment', blank=True, null=True, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        self.url= slugify(self.reply)
        super(Reply, self).save(*args, **kwargs)

    def __str__(self):
        return self.reply

class LikeButton(models.Model):
    video = models.ForeignKey('youtube_clone_api.Video', blank=True, null=True, on_delete=models.CASCADE)
    comment = models.ForeignKey('youtube_clone_api.Comment', blank=True, null=True, on_delete=models.CASCADE)
    value= models.IntegerField()
    

    
    def __str__(self):
        return str(self.video) +':' + str(self.comment) +':' + str(self.value)

    class Meta:
        unique_together = ("video", "comment", "value")
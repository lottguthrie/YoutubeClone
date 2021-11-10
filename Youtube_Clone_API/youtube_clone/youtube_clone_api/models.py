from django.db import models
from django.template.defaultfilters import slugify
from django.shortcuts import render, get_object_or_404


# Create your models here.
class Video(models.Model):
    title: models.CharField(max_length=100)
    description: models.CharField(max_length=100)
    artist: models.CharField(max_length= 100)
    release_date: models.DateTimeField()
    likes= models.IntegerField(default=0)
    dislikes= models.IntegerField(default=0)
    
    def save(self, *args, **kwargs):
        self.url= slugify(self.title)
        super(Video, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

class Comment(models.Model):
    comment: models.TextField(max_length=500)
    video_id: models.ForeignKey(Video)
    likes= models.IntegerField(default=0)
    dislikes= models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        self.url= slugify(self.comment)
        super(Comment, self).save(*args, **kwargs)

    def __str__(self):
        return self.comment
    
class Reply(models.Model):
    reply: models.TextField(max_length=500)
    comment_id: models.ForeignKey(Video)

    def save(self, *args, **kwargs):
        self.url= slugify(self.reply)
        super(Reply, self).save(*args, **kwargs)

    def __str__(self):
        return self.reply

class LikeButton(models.Model):
    video= models.ForeignKey(Video)
    comment= models.ForeignKey(Comment)
    value= models.IntegerField()
    

    
    def __str__(self):
        return str(self.video) +':' + str(self.comment) +':' + str(self.value)

    class Meta:
       


        
        


from django.db import models

class Comment(models.Model):
    comment: models.TextField(max_length=500)
    video_id = models.CharField(max_length=50)
    likes= models.IntegerField(default=0)
    dislikes= models.IntegerField(default=0)

    def __str__(self):
        return self.comment
    
class Reply(models.Model):
    reply: models.TextField(max_length=500)
    comment = models.ForeignKey(Comment, blank=True, null=True, on_delete=models.CASCADE)

#     def save(self, *args, **kwargs):
#         self.url= slugify(self.reply)
#         super(Reply, self).save(*args, **kwargs)

#     def __str__(self):
#         return self.reply

# class LikeButton(models.Model):
#     video = models.ForeignKey('youtube_clone_api.Video', blank=True, null=True, on_delete=models.CASCADE)
#     comment = models.ForeignKey('youtube_clone_api.Comment', blank=True, null=True, on_delete=models.CASCADE)
#     value= models.IntegerField()
    

    
#     def __str__(self):
#         return str(self.video) +':' + str(self.comment) +':' + str(self.value)

#     class Meta:
#         unique_together = ("video", "comment", "value")
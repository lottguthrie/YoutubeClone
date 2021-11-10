from rest_framework import serializers
from .models import Comment, Reply

# class VideoSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Video
#         fields = ['id', 'title', 'comments', 'artist', 'release_date']

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['comment', 'video_id', 'likes', 'dislikes']

class ReplySerializer(serializers.ModelSerializer):
    class Meta:
        model = Reply
        fields = ['reply', 'comment']

# class LikeButtonSerializer(serializers.ModelSerializer):
#     class Meta:
#         unique_together = ("video", "comment", "value")


        


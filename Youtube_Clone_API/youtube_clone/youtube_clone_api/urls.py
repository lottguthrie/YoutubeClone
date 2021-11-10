from django.urls import path
from . import views

urlpatterns = [
    path('video/', views.VideoList.as_view()),
    path('video_detail/<int:pk>/', views.VideoDetail.as_view()),
    path('comment/', views.CommentList.as_view()),
    path('comment_detail/<int:fk>/', views.CommentDetail.as_view()),
    path('reply/', views.ReplyList.as_view()),
    path('reply_detail/<int:fk>/', views.ReplyDetail.as_view()),
]
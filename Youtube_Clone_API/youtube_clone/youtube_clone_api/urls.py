from django.urls import path
from . import views

urlpatterns = [
    path('youtube_clone_api', views.VideoList.as_view()),
    path('youtube_clone_api/<int:pk>/', views.VideoDetail.as_view()),
    path('youtube_clone_api', views.CommentList.as_view()),
    path('youtube_clone_api/<int:pk>/', views.CommentDetail.as_view()),
    path('youtube_clone_api', views.ReplyList.as_view()),
    path('youtube_clone_api/<int:sk>/', views.ReplyDetail.as_view()),
    path('youtube_clone_api', views.VideoList.as_view()),
    path('youtube_clone_api/<int:pk>/', views.VideoDetail.as_view()),
]
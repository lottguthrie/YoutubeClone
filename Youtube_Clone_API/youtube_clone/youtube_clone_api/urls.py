from django.urls import path
from . import views

urlpatterns = [
    path('youtube_clone_api', views.VideoList.as_view()),
    
]
from django.shortcuts import render
from .serilaizers import VideoSerializer
from rest_frameswork.views import APIView
from rest_framework.response import Response
from rest.framework import status
from .models import Video

# Create your views here.
class VideoList(APIView):
    def get(self,request):
        video = Video.objects.all()
        serializer = VideoSerializer(video, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = VideoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

from .serilaizers import VideoSerializer, CommentSerializer, ReplySerializer, LikeButtonSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import LikeButton, Video
from .models import Comment
from .models import Reply
from django.http.response import Http404
from django.shortcuts import render, get_object_or_404

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

class VideoDetail(APIView):

    def get_object(self, pk):
        try:
            return Video.objects.get(pk=pk)
        except Video.DoesNotExist:
            raise Http404

    
    def get(self, request, pk):
        Video = self.get_object(pk)
        serializer = VideoSerializer(video)
        return Response(serializer.data)

class CommentList(APIView):
    def get(self,request):
        comment = Comment.objects.all()
        serializer = CommentSerializer(comment, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CommentDetail(APIView):

    def get_object(self, pk):
        try:
            return Comment.objects.get(pk=pk)
        except Comment.DoesNotExist:
            raise Http404

    
    def get(self, request, pk):
        Comment = self.get_object(pk)
        serializer = CommentSerializer(comment)
        return Response(serializer.data)

        #update
    def put(self, request, pk):
        comment = self.get_object(pk)
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    #delete
    def delete(self, request, pk):
        comment = self.get_object(pk)
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ReplyList(APIView):
    def get(self,request):
        reply = Reply.objects.all()
        serializer = ReplySerializer(reply, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ReplySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ReplyDetail(APIView):

    def get_object(self, pk):
        try:
            return Reply.objects.get(pk=pk)
        except Reply.DoesNotExist:
            raise Http404

    
    def get(self, request, pk):
        Reply = self.get_object(pk)
        serializer = ReplySerializer(reply)
        return Response(serializer.data)

        #update
    def put(self, request, pk):
        reply = self.get_object(pk)
        serializer = ReplySerializer(reply, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    #delete
    def delete(self, request, pk):
        reply = self.get_object(pk)
        reply.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)





def createcomment(request):
        if request.method == 'POST':
            if request.POST.get('title') and request.POST.get('comments'):
                comment=Comment()
                comment.title= request.POST.get('title')
                comment.comment= request.POST.get('comment')
                comment.save()
                

                return render(request, 'comment/create.html')  

        

        else:
                return render(request,'comment/create.html')


def home(request):
        allcomments= Comment.objects.all()

        context={'allcomments': allcomments }

        return render(request, 'comment/home.html', context)


def detail_comment_view(request, id=None):
        eachcomment= get_object_or_404(Comment, id=id)

        

        context={'eachcomment': eachcomment}

        return render (request, 'comment/detail.html', context)



def commentlikebutton(request, commentid, videolikebutton):
        
        if request.method == "POST":
                eachcomment= get_object_or_404(Comment, id=commentid)

                obj=''

                valueobj=''

                try:
                        obj= LikeButton.objects.get(user= request.video, post= eachcomment)

                        valueobj= obj.value 


                        valueobj= int(valueobj)

                        userpreference= int(videolikebutton)
                
                        if valueobj != videolikebutton:
                                obj.delete()


                                upref= LikeButton()
                                upref.video= request.video

                                upref.comment= eachcomment

                                upref.value= videolikebutton


                                if videolikebutton == 1 and valueobj != 1:
                                        eachcomment.likes += 1
                                        eachcomment.dislikes -=1
                                elif videolikebutton == 2 and valueobj != 2:
                                        eachcomment.dislikes += 1
                                        eachcomment.likes -= 1
                                

                                upref.save()

                                eachcomment.save()
                        
                        
                                context= {'eachcomment': eachcomment,
                                  'commentid': commentid}

                                return render (request, 'comment/detail.html', context)

                        elif valueobj == videolikebutton:
                                obj.delete()
                        
                                if videolikebutton == 1:
                                        eachcomment.likes -= 1
                                elif userpreference == 2:
                                        eachcomment.dislikes -= 1

                                eachcomment.save()

                                context= {'eachcomment': eachcomment,
                                  'commentid': commentid}

                                return render (request, 'comment/detail.html', context)
                                
                        
        
                
                except LikeButton.DoesNotExist:
                        upref= LikeButton()

                        upref.video= request.video

                        upref.comment= eachcomment

                        upref.value= videolikebutton

                        videolikebutton= int(videolikebutton)

                        if videolikebutton == 1:
                                eachcomment.likes += 1
                        elif videolikebutton == 2:
                                eachcomment.dislikes +=1

                        upref.save()

                        eachcomment.save()                            


                        context= {'eachcomment': eachcomment,
                          'commentid': commentid}

                        return render (request, 'comment/detail.html', context)


        else:
                eachcomment= get_object_or_404(Comment, id=commentid)
                context= {'eachcomment': eachcomment,
                          'commentid': commentid}

                return render (request, 'comment/detail.html', context)


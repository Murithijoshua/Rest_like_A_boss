from django.shortcuts import render
from rest_framework import generics, permissions, mixins,status
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from . models import Post, Vote
from .serializers import PostSerializer, VoteSerializer


class PostList(generics.ListCreateAPIView):
    """
    sorts out GET,POST,PUT 
    
    """
    # getting all the data as python objects
    queryset = Post.objects.all()
    # serializing the Data
    serializer_class = PostSerializer
    # authentication_classes where if autheticated you can send post request else readonly
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    # saving data on post
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class VoteCreate(generics.CreateAPIView, mixins.DestroyModelMixin):
    serializer_class = VoteSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    # geting the users,post 
    def get_queryset(self):
        user = self.request.user
        post = Post.objects.get(pk=self.kwargs['pk'])
        return Vote.objects.filter(voter=user, post=post)
    # performing vote create to (pk) vote
    def perform_create(self, serializer):
        if self.get_queryset().exists():
            raise ValidationError("You have already voted for this post")
        serializer.save(voter=self.request.user, post=Post.objects.get(pk=self.kwargs['pk']))
    
    
    def delete(self,request,*args,**kwargs):
        if self.get_queryset().exists():
            self.get_queryset().delete()
            return Response(status = status.HTTP_204_NO_CONTENT) 
        else:
            raise ValidationError("You didnt voted for this Silly!!") 
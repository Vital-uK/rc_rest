from django.shortcuts import render
from rest_framework import generics
from . import serializers
from django.contrib.auth.models import User
from .models import post, comment
# Create your views here.

class user_list(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.user_serializer

class user_detail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.user_serializer

class post_list(generics.ListCreateAPIView):
    queryset = post.objects.all()
    serializer_class = serializers.post_serializer
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class post_detail(generics.RetrieveDestroyAPIView):
    queryset = post.objects.all()
    serializer_class = serializers.post_serializer

class comment_list(generics.ListCreateAPIView):
    queryset = post.objects.all()
    serializer_class = serializers.post_serializer
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class comment_detail(generics.RetrieveDestroyAPIView):
    queryset = post.objects.all()
    serializer_class = serializers.post_serializer


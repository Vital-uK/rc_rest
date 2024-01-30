from django.shortcuts import render
from rest_framework import generics, permissions
from . import serializers
from django.contrib.auth.models import User
from .models import post, comment
from .permissions import is_author_or_readonly
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
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class post_detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = post.objects.all()
    serializer_class = serializers.post_serializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, is_author_or_readonly]

class comment_list(generics.ListCreateAPIView):
    queryset = comment.objects.all()
    serializer_class = serializers.comment_serializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class comment_detail(generics.RetrieveDestroyAPIView):
    queryset = comment.objects.all()
    serializer_class = serializers.comment_serializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, is_author_or_readonly]

# TODO: endpoint for jwt registration

# TODO: login for jwt
from django.shortcuts import render
from rest_framework import generics
from . import serializers
from django.contrib.auth.models import User
# Create your views here.

class user_list(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.user_serializer

class user_detail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.user_serializer
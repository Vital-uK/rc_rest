from rest_framework import serializers
from django.contrib.auth.models import User
from .models import post, comment


class user_serializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']

class post_serializer(serializers.ModelSerializer):
    class Meta:
        model = post
        fields = '__all__'

class comment_serializer(serializers.ModelSerializer):
    class Meta:
        model = comment
        fields = '__all__'

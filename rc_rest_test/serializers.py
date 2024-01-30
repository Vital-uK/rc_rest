from rest_framework import serializers
from django.contrib.auth.models import User
from .models import post, comment

class user_serializer(serializers.ModelSerializer):
    posts = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    comments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = User
        fields = ['id', 'username', 'posts', 'comments']

# post serializer
class post_serializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    comments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = post
        fields = '__all__'

# comment serializer
class comment_serializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    class Meta:
        model = comment
        fields = '__all__'

# TODO: registration seria;izer for jwt auth

# TODO: login serializer for jwt

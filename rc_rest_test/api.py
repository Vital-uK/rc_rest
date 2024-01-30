from .models import post
from rest_framework import viewsets, permissions
from .serializers import post_serializer

# first realization

#class post_viewset(viewsets.ModelViewSet):
#    queryset = post.objects.all()
#    permissions_classes = permissions.AllowAny
#    serializer_class = post_serializer

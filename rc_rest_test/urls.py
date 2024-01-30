#from rest_framework import routers
#from .api import post_viewset

# TODO: urlpatterns post/comment/user with id

#router = routers.DefaultRouter()
#router.register('api/rc_rest_test', post_viewset, 'rc_rest_test')

#urlpatterns = router.urls

from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('users/', views.user_list.as_view()),
    path('users/<int:pk>/', views.user_detail.as_view()),
    path('posts/', views.post_list.as_view()),
    path('posts/<int:pk>/', views.post_detail.as_view()),
    path('comments/', views.comment_list.as_view()),
    path('comments/<int:pk>/', views.comment_detail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
from rest_framework import routers
from .api import post_viewset

# TODO: urlpatterns post/comment/user with id

router = routers.DefaultRouter()
router.register('api/rc_rest_test', post_viewset, 'rc_rest_test')

urlpatterns = router.urls

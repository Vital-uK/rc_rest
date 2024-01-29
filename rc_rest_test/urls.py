from rest_framework import routers
from .api import post_viewset


router = routers.DefaultRouter()
router.register('api/rc_rest_test', post_viewset, 'rc_rest_test')

urlpatterns = router.urls
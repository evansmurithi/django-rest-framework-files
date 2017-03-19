from __future__ import unicode_literals

from rest_framework import routers

from .views import ABCViewSet

router = routers.SimpleRouter()
router.register(r'abc', ABCViewSet)

urlpatterns = router.urls

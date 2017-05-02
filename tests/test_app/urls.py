from __future__ import unicode_literals

from rest_framework_files import routers

from .views import ABCViewSet, DEFViewSet

router = routers.ImportExportRouter()
router.register(r'abc', ABCViewSet)
router.register(r'def', DEFViewSet)

urlpatterns = router.urls

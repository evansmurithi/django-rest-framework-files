from __future__ import unicode_literals

from django.conf.urls import url
from rest_framework_files import routers

from .views import ABCViewSet, DEFViewSet, GHIImportExportView

router = routers.ImportExportRouter()
router.register(r'abc', ABCViewSet)
router.register(r'def', DEFViewSet)

urlpatterns = router.urls

urlpatterns += (
    url(r'^ghi/$', GHIImportExportView.as_view(), name='ghi'),
)

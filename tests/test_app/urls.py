from __future__ import unicode_literals

from django.conf.urls import url

from rest_framework_files import routers

from . import views

router = routers.ImportExportRouter()
router.register(r'abc', views.ABCViewSet)
router.register(r'def', views.DEFViewSet)

urlpatterns = router.urls

urlpatterns += (
    url(
        r'^abc_import/$', views.ABCImportView.as_view(),
        name='abc_import'
    ),
    url(
        r'^abc_export/$', views.ABCExportView.as_view(),
        name='abc_export'
    ),
    url(
        r'^abc_import_export/$', views.ABCImportExportView.as_view(),
        name='abc_import_export'
    ),
)

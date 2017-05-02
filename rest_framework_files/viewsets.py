from __future__ import unicode_literals

from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet

from . import mixins


class ReadOnlyImportExportModelViewSet(mixins.ExportMixin,
                                       ReadOnlyModelViewSet):
    pass


class ImportExportModelViewSet(mixins.ImportMixin,
                               mixins.ExportMixin,
                               ModelViewSet):
    pass

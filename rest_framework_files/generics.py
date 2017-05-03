"""
Generic views that provide commonly needed behaviour.
"""
from __future__ import unicode_literals

from rest_framework.generics import GenericAPIView

from . import mixins


class ImportCreateAPIView(mixins.ImportMixin, GenericAPIView):
    """
    Concrete view for uploading a file.
    """

    def post(self, request, *args, **kwargs):
        return self.upload(request, *args, **kwargs)


class ExportListAPIView(mixins.ExportMixin, GenericAPIView):
    """
    Concrete view for downloading a file.
    """

    def get(self, request, *args, **kwargs):
        return self.download(request, *args, **kwargs)


class ExportListImportCreateAPIView(mixins.ExportMixin,
                                    mixins.ImportMixin,
                                    GenericAPIView):
    """
    Concrete view for downloading and uploading a file.
    """

    def get(self, request, *args, **kwargs):
        return self.download(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.upload(request, *args, **kwargs)

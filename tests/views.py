from __future__ import unicode_literals

from rest_framework.renderers import JSONRenderer
from rest_framework.viewsets import ModelViewSet
from rest_framework_csv.renderers import CSVRenderer
from rest_framework_xml.renderers import XMLRenderer
from rest_framework_yaml.renderers import YAMLRenderer

from rest_framework_files.downloader import DownloadListMixin

from .models import ABC
from .serializers import ABCSerializer


class ABCViewSet(DownloadListMixin, ModelViewSet):

    queryset = ABC.objects.all()
    serializer_class = ABCSerializer
    renderer_classes = (
        JSONRenderer, XMLRenderer, CSVRenderer, YAMLRenderer,
    )

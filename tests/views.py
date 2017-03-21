from __future__ import unicode_literals

from rest_framework.renderers import JSONRenderer
from rest_framework.viewsets import ModelViewSet
from rest_framework_csv.renderers import CSVRenderer
from rest_framework_xml.renderers import XMLRenderer
from rest_framework_yaml.renderers import YAMLRenderer

from rest_framework_files.downloader import DownloadFileMixin

from .models import ABC
from .serializers import ABCSerializer


class ABCViewSet(DownloadFileMixin, ModelViewSet):

    queryset = ABC.objects.all()
    serializer_class = ABCSerializer
    renderer_classes = (
        JSONRenderer, XMLRenderer, CSVRenderer, YAMLRenderer,
    )


class DEFViewSet(DownloadFileMixin, ModelViewSet):

    queryset = ABC.objects.all()
    serializer_class = ABCSerializer
    renderer_classes = (
        JSONRenderer, XMLRenderer, CSVRenderer, YAMLRenderer,
    )
    filename = "My file"

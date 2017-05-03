from __future__ import unicode_literals

from rest_framework.parsers import JSONParser, MultiPartParser
from rest_framework.renderers import JSONRenderer
from rest_framework_csv.parsers import CSVParser
from rest_framework_csv.renderers import CSVRenderer
from rest_framework_xml.parsers import XMLParser
from rest_framework_xml.renderers import XMLRenderer
from rest_framework_yaml.parsers import YAMLParser
from rest_framework_yaml.renderers import YAMLRenderer

from rest_framework_files.generics import ExportListImportCreateAPIView
from rest_framework_files.viewsets import ImportExportModelViewSet

from .models import ABC
from .serializers import ABCSerializer


class ABCViewSet(ImportExportModelViewSet):
    """
    Test use of model viewset.
    """

    queryset = ABC.objects.all()
    serializer_class = ABCSerializer
    parser_classes = (MultiPartParser, )
    renderer_classes = (
        JSONRenderer, XMLRenderer, CSVRenderer, YAMLRenderer,
    )
    file_content_parser_classes = (
        JSONParser, XMLParser, YAMLParser, CSVParser,
    )


class DEFViewSet(ImportExportModelViewSet):
    """
    Test use of ``filename`` attribute during download.
    """

    queryset = ABC.objects.all()
    serializer_class = ABCSerializer
    renderer_classes = (
        JSONRenderer, XMLRenderer, CSVRenderer, YAMLRenderer,
    )
    filename = "My file"


class GHIImportExportView(ExportListImportCreateAPIView):
    """
    Test use of generic views.
    """

    queryset = ABC.objects.all()
    serializer_class = ABCSerializer
    parser_classes = (MultiPartParser, )
    renderer_classes = (
        JSONRenderer, XMLRenderer, CSVRenderer, YAMLRenderer,
    )
    file_content_parser_classes = (
        JSONParser, XMLParser, YAMLParser, CSVParser,
    )
    filename = "GHI"

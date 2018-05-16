from __future__ import unicode_literals

import six
from django.utils.datastructures import MultiValueDictKeyError
from rest_framework.exceptions import ParseError, ValidationError
from rest_framework.mixins import CreateModelMixin
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED


class ImportMixin(CreateModelMixin):
    """
    Upload a file and parse its content.
    """

    def upload(self, request, *args, **kwargs):
        try:
            uploaded_file = request.data['file']
        except MultiValueDictKeyError:
            raise MultiValueDictKeyError("Upload a file with the key 'file'")

        content = b''
        for chunk in uploaded_file.chunks():
            content += chunk

        # try parsers defined in the `file_content_parser_classes`
        for parser_cls in self.file_content_parser_classes:
            try:
                data = parser_cls().parse(six.BytesIO(content))
                break
            except (ParseError, ValidationError):
                # try all parsers provided
                continue
        else:
            raise ParseError(
                'Could not parse content of the file to any of the parsers '
                'provided.'
            )

        # create model instances from contents of the file
        serializer = self.get_serializer(data=data, many=True)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            data=serializer.data, status=HTTP_201_CREATED, headers=headers
        )


class ExportMixin(object):
    """
    Download a rendered serialized response.
    """

    def download(self, request, *args, **kwargs):
        qs = self.filter_queryset(self.get_queryset())
        queryset = self.paginate_queryset(qs) or qs
        serializer = self.get_serializer(queryset, many=True)

        filename = getattr(self, 'filename', self.get_view_name())
        extension = self.get_content_negotiator().select_renderer(
            request, self.renderer_classes
        )[0].format

        return Response(
            data=serializer.data, status=HTTP_200_OK,
            headers={
                'content-disposition': (
                    'attachment; filename="{}.{}"'.format(filename, extension)
                )
            }
        )

"""
Upload a file and parse the content using its media type.
"""
from __future__ import unicode_literals

import six

from rest_framework.decorators import list_route
from rest_framework.exceptions import ParseError, ValidationError
from rest_framework.response import Response
from rest_framework.settings import api_settings
from rest_framework.status import HTTP_201_CREATED


class UploadFileMixin(object):
    """
    Upload a file and parse its content.
    """

    @list_route(methods=['post', ])
    def upload(self, request, *args, **kwargs):
        uploaded_file = request.data['file']
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
                'Could not parse content of file to any of the parsers '
                'specified.'
            )

        # create model instances from contents of the file
        serializer = self.get_serializer(data=data, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        headers = self.get_success_headers(serializer.data)
        return Response(
            data=serializer.data, status=HTTP_201_CREATED, headers=headers
        )

    def get_success_headers(self, data):
        try:
            return {'Location': data[api_settings.URL_FIELD_NAME]}
        except (TypeError, KeyError):
            return {}

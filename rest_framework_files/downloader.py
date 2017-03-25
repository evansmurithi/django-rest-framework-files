"""
Download a serialized response into a file format used to render the response.
"""
from __future__ import unicode_literals

from rest_framework.decorators import list_route
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK


class DownloadFileMixin(object):
    """
    Download a rendered serialized response.
    """

    @list_route(methods=['get', ])
    def download(self, request, *args, **kwargs):
        qs = self.filter_queryset(self.get_queryset())
        queryset = self.paginate_queryset(qs) or qs
        serializer = self.get_serializer(queryset, many=True)

        filename = "{}".format(
            getattr(self, 'filename', self.get_view_name())
        )
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

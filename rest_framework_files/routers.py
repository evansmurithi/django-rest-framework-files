from __future__ import unicode_literals

import copy

from rest_framework.routers import DefaultRouter, SimpleRouter


class ImportExportRouter(DefaultRouter):
    """
    Map http methods to actions defined on the import-export mixins.
    """

    routes = copy.deepcopy(SimpleRouter.routes)
    routes[0].mapping.update({
        'get': 'download',
        'post': 'upload',
    })

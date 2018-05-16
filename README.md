# REST framework files

[![build-status-image]][travis]
[![coverage-status-image]][codecov]

**File download and upload support for Django REST framework.**

---

# Overview

REST framework files allows you to download a file in the format used to render the response and
also allows creation of model instances by uploading a file containing the model fields.

# Requirements

* Python (2.7, 3.5, 3.6)
* Django REST framework (3.4, 3.5, 3.6, 3.7, 3.8)

# Installation

Install using `pip`:

    pip install djangorestframework-files

# Example

*models.py*
```python
from django.db import models

class ABC(models.Model):
    name = models.CharField(max_length=255)
```

*serializers.py*
```python
from rest_framework import serializers

from .models import ABC

class ABCSerializer(serializers.ModelSerializer):
    class Meta:
        model = ABC
        fields = '__all__'
```

*views.py*
```python
from rest_framework.parsers import JSONParser, MultiPartParser
from rest_framework_files.viewsets import ImportExportModelViewSet

from .models import ABC
from .serializers import ABCSerializer

class ABCViewSet(ImportExportModelViewSet):
    queryset = ABC.objects.all()
    serializer_class = ABCSerializer
    # if filename is not provided, the view name will be used as the filename
    filename = 'ABC'
    # renderer classes used to render your content. will determine the file type of the download
    renderer_classes = (JSONParser, )
    parser_classes = (MultiPartParser, )
    # parser classes used to parse the content of the uploaded file
    file_content_parser_classes = (JSONParser, )
```

Some third party packages that offer media type support:

* [Parsers][parsers]
* [Renderers][renderers]

*urls.py*
```python
from rest_framework import routers

from .views import ABCViewSet

router = routers.ImportExportRouter()
router.register(r'abc', ABCViewSet)

urlpatterns = router.urls
```

## Downloading

To download a `json` file you can go to the url `/abc/?format=json`. The `format` query parameter
specifies the media type you want your response represented in. To download an `xml` file, your
url would be `/abc/?format=xml`. For this to work, make sure you have the respective `renderers`
to render your response.

## Uploading

To create model instances from a file, upload a file to the url `/abc/`. Make sure the content
of the file can be parsed by the parsers specified in the `file_content_parser_classes` or else
it will return a `HTTP_415_UNSUPPORTED_MEDIA_TYPE` error.

For sample file examples you can upload, check the [assets folder][assets]

For more examples on how to use the viewsets or generic views, check the [test application][test-app]

[build-status-image]: https://travis-ci.org/evansmurithi/django-rest-framework-files.svg?branch=master
[travis]: https://travis-ci.org/evansmurithi/django-rest-framework-files
[coverage-status-image]: https://codecov.io/gh/evansmurithi/django-rest-framework-files/branch/master/graph/badge.svg
[codecov]: https://codecov.io/gh/evansmurithi/django-rest-framework-files

[parsers]: http://www.django-rest-framework.org/api-guide/parsers/#third-party-packages
[renderers]: http://www.django-rest-framework.org/api-guide/renderers/#third-party-packages
[assets]: https://github.com/evansmurithi/django-rest-framework-files/tree/master/tests/assets
[test-app]: https://github.com/evansmurithi/django-rest-framework-files/tree/master/tests/test_app

from __future__ import unicode_literals

import os

from django.conf import settings
from rest_framework.test import APITestCase

from tests.test_app.models import ABC


class TestImportGenericViews(APITestCase):

    assets_dir = os.path.join(settings.BASE_DIR, 'assets/')

    def upload_file(self, filename, url='/abc/'):
        with open(self.assets_dir + filename, 'rb') as f:
            response = self.client.post(url, {'file': f})

        return response

    def test_upload_using_import_generic_view(self):
        """
        Upload a file and create model instances using generic view.
        """
        response = self.upload_file('abc.csv', '/abc_import/')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(ABC.objects.count(), 3)
        self.assertTrue(ABC.objects.filter(name='giraffe').exists())

    def test_upload_using_import_export_generic_view(self):
        """
        Upload a file and create model instances using generic view.
        """
        response = self.upload_file('abc.xml', '/abc_import_export/')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(ABC.objects.count(), 2)
        self.assertTrue(ABC.objects.filter(name='cheetah').exists())

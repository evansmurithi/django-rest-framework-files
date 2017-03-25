from __future__ import unicode_literals

import os

from django.conf import settings
from rest_framework.test import APITestCase

from tests.test_app.models import ABC


class TestUploadFileMixin(APITestCase):

    assets_dir = os.path.join(settings.BASE_DIR, 'assets/')

    def upload_file(self, filename):
        with open(self.assets_dir + filename, 'rb') as f:
            response = self.client.post('/abc/upload/', {'file': f})

        return response

    def test_upload_json_file(self):
        """
        Should create model instances from the json file uploaded.
        """
        response = self.upload_file('abc.json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(ABC.objects.count(), 2)
        self.assertTrue(ABC.objects.filter(name='lion').exists())

    def test_upload_xml_file(self):
        """
        Should create model instances from the xml file uploaded.
        """
        response = self.upload_file('abc.xml')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(ABC.objects.count(), 2)
        self.assertTrue(ABC.objects.filter(name='gazelle').exists())

    def test_upload_csv_file(self):
        """
        Should create model instances from the csv file uploaded.
        """
        response = self.upload_file('abc.csv')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(ABC.objects.count(), 3)
        self.assertTrue(ABC.objects.filter(name='leopard').exists())

    def test_upload_yaml_file(self):
        """
        Should create model instances from the yaml file uploaded.
        """
        response = self.upload_file('abc.yaml')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(ABC.objects.count(), 4)
        self.assertTrue(ABC.objects.filter(name='hyena').exists())

    def test_upload_unsupported_file_type(self):
        """
        Should give an error when uploading an unsupported file type.
        """
        response = self.upload_file('abc.xlsx')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(
            response.data['detail'],
            (
                'Could not parse content of file to any of the '
                'parsers specified.'
            )
        )
        self.assertEqual(ABC.objects.count(), 0)

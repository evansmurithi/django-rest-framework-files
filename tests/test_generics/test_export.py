from __future__ import unicode_literals

from rest_framework.test import APITestCase

from tests.test_app.models import ABC


class TestExportGenericViews(APITestCase):

    def setUp(self):
        """
        Create records in ABC model.
        """
        names = ['me', 'you', 'him', 'her']
        for name in names:
            ABC.objects.create(name=name)

    def test_download_using_export_generic_view(self):
        """
        Download a file using generic view.
        """
        response = self.client.get('/abc_export/?format=json')
        content = (
            b'[{"id":1,"name":"me"},{"id":2,"name":"you"},'
            b'{"id":3,"name":"him"},{"id":4,"name":"her"}]'
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, content)
        self.assertEqual(
            response._headers.get('content-type'),
            ('Content-Type', 'application/json')
        )
        self.assertEqual(
            response._headers.get('content-disposition'),
            ('content-disposition', 'attachment; filename="ABC.json"')
        )

    def test_download_using_import_export_generic_view(self):
        """
        Download a file using generic view.
        """
        response = self.client.get('/abc_import_export/?format=yaml')
        content = (
            b'- id: 1\n  name: me\n- id: 2\n  name: you\n'
            b'- id: 3\n  name: him\n- id: 4\n  name: her\n'
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, content)
        self.assertEqual(
            response._headers.get('content-type'),
            ('Content-Type', 'application/yaml; charset=utf-8')
        )
        self.assertEqual(
            response._headers.get('content-disposition'),
            ('content-disposition', 'attachment; filename="ABC.yaml"')
        )

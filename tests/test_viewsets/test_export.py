from __future__ import unicode_literals

from rest_framework.test import APITestCase

from tests.test_app.models import ABC


class TestExportViewsets(APITestCase):

    def setUp(self):
        """
        Create records in ABC model.
        """
        names = ['me', 'you', 'him', 'her']
        for name in names:
            ABC.objects.create(name=name)

    def test_download_file_name(self):
        """
        Filename in viewset is the name of the file to be downloaded.
        """
        response = self.client.get('/def/?format=json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response._headers.get('content-disposition'),
            ('content-disposition', 'attachment; filename="My file.json"')
        )

    def test_download_json(self):
        """
        Response rendered in json, should output a json file when requested.
        """
        response = self.client.get('/abc/?format=json')
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
            ('content-disposition', 'attachment; filename="Abc List.json"')
        )

    def test_download_xml(self):
        """
        Response rendered in xml, should output a xml file when requested.
        """
        response = self.client.get('/abc/?format=xml')
        content = (
            b'<?xml version="1.0" encoding="utf-8"?>\n'
            b'<root><list-item><id>1</id><name>me</name></list-item>'
            b'<list-item><id>2</id><name>you</name></list-item>'
            b'<list-item><id>3</id><name>him</name></list-item>'
            b'<list-item><id>4</id><name>her</name></list-item></root>'
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, content)
        self.assertEqual(
            response._headers.get('content-type'),
            ('Content-Type', 'application/xml; charset=utf-8')
        )
        self.assertEqual(
            response._headers.get('content-disposition'),
            ('content-disposition', 'attachment; filename="Abc List.xml"')
        )

    def test_download_csv(self):
        """
        Response rendered in csv, should output a csv file when requested.
        """
        response = self.client.get('/abc/?format=csv')
        content = b'id,name\r\n1,me\r\n2,you\r\n3,him\r\n4,her\r\n'
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, content)
        self.assertEqual(
            response._headers.get('content-type'),
            ('Content-Type', 'text/csv; charset=utf-8')
        )
        self.assertEqual(
            response._headers.get('content-disposition'),
            ('content-disposition', 'attachment; filename="Abc List.csv"')
        )

    def test_download_yaml(self):
        """
        Response rendered in yaml, should output a yaml file when requested.
        """
        response = self.client.get('/abc/?format=yaml')
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
            ('content-disposition', 'attachment; filename="Abc List.yaml"')
        )

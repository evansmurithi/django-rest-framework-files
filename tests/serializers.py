from __future__ import unicode_literals

from rest_framework import serializers

from .models import ABC


class ABCSerializer(serializers.ModelSerializer):

    class Meta(object):
        model = ABC
        fields = '__all__'

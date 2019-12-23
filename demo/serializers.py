from django.contrib.auth.models import Permission
from rest_framework import serializers
from rest_framework_utils.serializers import ModelSerializer

class PermissionSerializer(ModelSerializer):
    class Meta:
        model = Permission
        fields = '__all__'
        data = {'6': 7}

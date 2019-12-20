# from rest_framework_utils.filter import FilterSet
from django.contrib.auth.models import Permission
from django_filters import FilterSet


class PermissionFilterSet(FilterSet):
    class Meta:
        model = Permission
        fields = '__all__'
        # fields = {
        #     'codename': ['icontains']
        # }
        # lookup_expr = ['icontains']

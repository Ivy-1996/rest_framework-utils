from rest_framework.viewsets import ModelViewSet

# from rest_framework_utils.mixin import FilterMixIn
from .serializers import Permission, PermissionSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from . import filters


class PermissionViewSet(ModelViewSet):
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer
    # filter_backends = [DjangoFilterBackend, SearchFilter]
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['codename']
    search_fields = ['codename']

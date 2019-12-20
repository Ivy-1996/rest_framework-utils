from rest_framework.routers import DefaultRouter
from . import views
from rest_framework_utils.views import EXCEPTION_HANDLE
route = DefaultRouter()

route.register('permission', views.PermissionViewSet)
urlpatterns = route.urls

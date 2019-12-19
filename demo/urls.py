from rest_framework.routers import DefaultRouter
from . import views

route = DefaultRouter()

route.register('permission', views.PermissionViewSet)
urlpatterns = route.urls

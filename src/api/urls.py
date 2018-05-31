from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

application_name = 'omnicrm'

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'session', views.SessionViewSet)
router.register('task', views.TaskViewSet)
router.register(r'log', views.LogViewSet)
# The API URLs are now determined automatically by the router.
urlpatterns = router.urls
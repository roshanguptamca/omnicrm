from django.urls import path
from . import views

application_name = 'omnicrm'

urlpatterns = [
    path('session', views.SessionView.as_view(), name='session'),
]
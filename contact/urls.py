from django.urls import path

from . import views

urlpatterns = [
    path('mesasge/new', views.send_message,name='new_message' )
]

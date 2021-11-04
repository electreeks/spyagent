"""
Electreeks® SpyAgent
An App based on a Django framework

© Electreeks® - Hans Umlauft
"""

from django.urls import path

from . import views

app_name= "electreeksspy"

urlpatterns = [
    path('', views.index, name="index"),
    path('<int:stream_id>/recognition/', views.recognition, name='recognition'),
    path('<int:stream_id>/fullscreen/', views.fullscreen, name='fullscreen'),
    path('<int:stream_id>/delete/', views.delete, name='delete'),
    path('create/', views.create, name='create'),
]

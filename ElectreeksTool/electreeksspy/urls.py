"""
Electreeks® SpyAgent
An App based on a Django framework

© Electreeks® - Hans Umlauft
"""

from django.urls import path

from . import views

app_name= "electreeksspy"

urlpatterns = [
    path('', views.index, name="index")
]

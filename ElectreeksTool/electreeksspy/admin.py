"""
Electreeks® SpyAgent
An App based on a Django framework

© Electreeks® - Hans Umlauft
"""

from django.contrib import admin

from .models import *

admin.site.register(Stream)

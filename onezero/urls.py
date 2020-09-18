"""onezero URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from . import settings

from .views import maintenance

urlpatterns = [
    path('', include('browse.urls')),
    path('letter/', include('letter.urls')),
    path('anniversary/', include('anniversary.urls')),
    # path('blog/', include('blog.urls')),
    path('blog/', maintenance),
    path('', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('maintenance/', maintenance, name="maintenance"),
]

handler404 = 'onezero.views.error_404'
handler500 = 'onezero.views.error_500'

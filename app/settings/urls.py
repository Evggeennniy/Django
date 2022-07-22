"""settings URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
# Default import
from django.contrib import admin
from django.urls import path
# Main views import
from trainingapps.views import index
# Table ContactUs generation fake data's
from trainingapps.views import gen_fake_info
# Table Rate get currency value
from trainingapps.views import get_currency_info
# General functions
from trainingapps.views import dbshow

urlpatterns = [
    path('', index),

    # ContactUs model
    path('geninfo/emaildata/', gen_fake_info),

    # Rate model
    path('getinfo/currencydata/', get_currency_info),

    # General function database
    path('data/', dbshow),

    # Other
    path('admin/', admin.site.urls),
]

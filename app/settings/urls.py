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
# Main
from trainingapps.views import index
# Functions
from trainingapps.views import gen_fake_info, get_currency_info, gen_source_info
# Table's
from trainingapps.views import show_ratelist, show_contactuslist, show_sourcelist
# Forms
from trainingapps.views import create_source, update_source, detail_source, delete_source


urlpatterns = [
    # Main page
    path('', index),

    # ContactUs page's
    path('geninfo/emaildata/', gen_fake_info),
    path('data/contactus', show_contactuslist),

    # Rate page's
    path('getinfo/currencydata/', get_currency_info),
    path('data/rate', show_ratelist),

    # Source page's
    path('geninfo/source', gen_source_info),
    path('data/source', show_sourcelist),
    path('data/source/create', create_source),
    path('data/source/update/<int:idin>', update_source),
    path('data/source/detail/<int:idin>', detail_source),
    path('data/source/delete/<int:idin>', delete_source),

    # Other
    path('admin/', admin.site.urls),
]

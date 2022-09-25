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
from django.urls import path
from trainingapps import views


urlpatterns = [
    # Rate
    path('rate', views.RateListView.as_view(), name='rate_list'),
    path('rate/create', views.RateCreateView.as_view(), name='rate_create'),
    path('rate/update/<int:pk>', views.RateUpdateView.as_view(), name='rate_update'),
    path('rate/detail/<int:pk>', views.RateDetailsView.as_view(), name='rate_detail'),
    path('rate/delete/<int:pk>', views.RateDeleteView.as_view(), name='rate_delete'),


    # ContactUs
    path('contactus', views.ContactUsListView.as_view(), name='contactus_list'),
    path('contactus/create', views.ContactUsCreateView.as_view(), name='contactus_create'),
    path('contactus/update/<int:pk>', views.ContactUsUpdateView.as_view(), name='contactus_update'),
    path('contactus/detail/<int:pk>', views.ContactUsDetailsView.as_view(), name='contactus_detail'),
    path('contactus/delete/<int:pk>', views.ContactUsDeleteView.as_view(), name='contactus_delete'),

    # Source
    path('source', views.SourceListView.as_view(), name='source_list'),
    path('source/create', views.SourceCreateView.as_view(), name='source_create'),
    path('source/update/<int:pk>', views.SourceUpdateView.as_view(), name='source_update'),
    path('source/detail/<int:pk>', views.SourceDetailsView.as_view(), name='source_detail'),
    path('source/delete/<int:pk>', views.SourceDeleteView.as_view(), name='source_delete'),

    # ResponseLog
    path('responselog/table', views.ResponseLogListView.as_view(), name='response_list'),
]

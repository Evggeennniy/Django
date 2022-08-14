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
from django.urls import path
# ListView
from trainingapps.views import ContactUsListView, RateListView, SourceListView
# EditView
from trainingapps.views import RateCreateView, RateUpdateView, RateDeleteView, RateDetailsView
from trainingapps.views import SourceCreateView, SourceUpdateView, SourceDeleteView, SourceDetailsView
from trainingapps.views import ContactUsCreateView, ContactUsUpdateView, ContactUsDeleteView, ContactUsDetailsView
from trainingapps.views import ResponseLogListView


urlpatterns = [
    # Rate
    path('rate', RateListView.as_view(), name='rate_list'),
    path('rate/create', RateCreateView.as_view(), name='rate_create'),
    path('rate/update/<int:pk>', RateUpdateView.as_view(), name='rate_update'),
    path('rate/detail/<int:pk>', RateDetailsView.as_view(), name='rate_detail'),
    path('rate/delete/<int:pk>', RateDeleteView.as_view(), name='rate_delete'),

    # ContactUs
    path('contactus', ContactUsListView.as_view(), name='contactus_list'),
    path('contactus/create', ContactUsCreateView.as_view(), name='contactus_create'),
    path('contactus/update/<int:pk>', ContactUsUpdateView.as_view(), name='contactus_update'),
    path('contactus/detail/<int:pk>', ContactUsDetailsView.as_view(), name='contactus_detail'),
    path('contactus/delete/<int:pk>', ContactUsDeleteView.as_view(), name='contactus_delete'),

    # Source
    path('source', SourceListView.as_view(), name='source_list'),
    path('source/create', SourceCreateView.as_view(), name='source_create'),
    path('source/update/<int:pk>', SourceUpdateView.as_view(), name='source_update'),
    path('source/detail/<int:pk>', SourceDetailsView.as_view(), name='source_detail'),
    path('source/delete/<int:pk>', SourceDeleteView.as_view(), name='source_delete'),

    # ResponseLog
    path('responselog/table', ResponseLogListView.as_view(), name='response_list'),

]

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
from django.urls import include, path
# ListView
from trainingapps.views import ContactUsListView, RateListView, SourceListView
# EditView
from trainingapps.views import SourceCreateView, SourceUpdateView, SourceDeleteView, SourceDetailsView
# Forms


urlpatterns = [
    # ContactUs page's
    path('contactus', ContactUsListView.as_view(), name='contactus_list'),

    # Rate page's
    path('rate', RateListView.as_view(), name='rate_list'),

    # Source page's
    path('source', SourceListView.as_view(), name='source_list'),
    path('source/create', SourceCreateView.as_view(), name='source_create'),
    path('source/update/<int:pk>', SourceUpdateView.as_view(), name='source_update'),
    path('source/detail/<int:pk>', SourceDetailsView.as_view(), name='source_detail'),
    path('source/delete/<int:pk>', SourceDeleteView.as_view(), name='source_delete'),
]

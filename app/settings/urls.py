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
from django.contrib import admin
from django.urls import include, path
from trainingapps.views import IndexView, UserUpdateView
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView

urlpatterns = [
    path('auth/', include('django.contrib.auth.urls')),
    # ^ Django auth

    path('', IndexView.as_view(), name='main'),
    # ^ Main page

    path('data/', include('trainingapps.urls'), name='main'),
    # ^ Include app urls

    path('admin/', admin.site.urls),
    path('__debug__/', include('debug_toolbar.urls')),
    # ^ User's

    path('user/profile/', UserUpdateView.as_view(), name='user_profile'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/4321432143/',
        auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('password-change/', PasswordChangeView.as_view(), name='password_change'),
    path('password-change/done/', PasswordChangeDoneView.as_view(), name='password_change_done'),
    # ^ Password
]

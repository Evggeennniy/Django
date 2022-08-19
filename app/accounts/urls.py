from django.urls import path
from accounts import views
from accounts.views import UserUpdateView

urlpatterns = [
    path('signup/', views.SingUpView.as_view(), name='signup'),
    path('activate/<uuid:username>', views.UserActivateView.as_view(), name='user_activate'),

    path('user/profile/', UserUpdateView.as_view(), name='user_profile'),
    # ^ Password
]

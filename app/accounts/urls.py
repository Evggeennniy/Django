from django.urls import path
from accounts import views
from accounts.views import UserUpdateView, AccountPreviouslyConfirmView, AccountConfirmView


urlpatterns = [
    path('signup/', views.SingUpView.as_view(), name='signup'),
    path('activate/<uuid:username>', views.UserActivateView.as_view(), name='user_activate'),

    path('activate/confirmed', AccountConfirmView.as_view(), name='activate_account'),
    path('activate/previouslyconfirmed', AccountPreviouslyConfirmView.as_view(), name='account_is_activated'),

    path('user/profile/', UserUpdateView.as_view(), name='user_profile'),
    # ^ Password
]

# from django.urls import path
from api import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('rates', views.RateViewSet, basename='rate')
router.register('source', views.SourceViewSet, basename='source')
router.register('contactus', views.ContactUsViewSet, basename='contactus')
# ^  In order to execute the commands shown below, the router is registered only once.
# !! You cannot add generic Views in routers !!

urlpatterns = [
    # path('rates/', views.RatesView.as_view(), name='rates'),
    # path('rates/<int:pk>', views.RateDetailsView.as_view(), name='rates'),
]

urlpatterns += router.urls

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from perm.ath import views

router = DefaultRouter('studentapi', views.StudentModelViewSet, basename='student')

urlpatterns = [
    path('',include(router.urls)),
     path('auth/', include('rest_framework.urls', namespace='rest_framework'))
]
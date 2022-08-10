from django.urls import path, include
from rest_framework.routers import DefaultRouter
from lists import views


router = DefaultRouter()
router.register('', views.ListViewSet)

urlpatterns = [
    path('', include(router.urls))
]

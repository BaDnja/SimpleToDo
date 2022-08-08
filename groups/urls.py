from django.urls import path, include
from rest_framework.routers import DefaultRouter
from groups import views


router = DefaultRouter()
router.register('', views.GroupViewSet)

urlpatterns = [
    path('', include(router.urls))
]

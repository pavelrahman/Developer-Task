from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('cars', views.CarViewSet)
router.register('showrooms', views.ShowroomViewSet)
router.register('models', views.ManufactorModelViewSet)
router.register('manufacturer', views.ManufactureViewSet)

urlpatterns = [
    path('', include(router.urls))
]
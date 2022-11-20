
from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('leadboard', views.LeadboardView)
router.register('players', views.PlayerView)


urlpatterns = [
    path('', include(router.urls))
]

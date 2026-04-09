from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CharacterViewSet, DemonViewSet

router = DefaultRouter()
router.register(r'characters', CharacterViewSet, basename='character')
router.register(r'demons', DemonViewSet, basename='demon')

urlpatterns = [
    path('', include(router.urls)),
]
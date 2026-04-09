from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from .views import CharacterViewSet, DemonViewSet

router =  DefaultRouter()
router.register(r'api/characters', CharacterViewSet)
router.register(r'api/demons', DemonViewSet)

urlpatterns = [
    path('', views.index, name='index'),
    path('characters/', views.characters, name='characters'),
    path('demons/', views.demons, name='demons'),
    path('hashira/', views.hashira, name='hashira'),
    path('characters/<int:character_id>/', views.character_detail, name='character_detail'),
]
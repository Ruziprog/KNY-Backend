from django.db import OperationalError
from django.shortcuts import render
from main.models import Character, Demon
from rest_framework import viewsets
from .serializers import CharacterSerializer, DemonSerializer
from django.shortcuts import get_object_or_404
# get_object_or_404 - это функция, которая пытается получить объект из базы данных по заданным параметрам. 
# Если объект не найден, она возвращает ошибку 404 (страница не найдена). Это удобный способ обработки случаев, когда пользователь запрашивает несуществующий ресурс.

def index(request):
    return render(request, 'main/index.html')

def characters(request):
    """Страница с персонажами"""
    try:
        characters = Character.objects.all()
        return render(request, 'main/characters.html', {'characters': characters})
    except OperationalError as e:
        error_message = f"Ошибка доступа к базе данных: {str(e)}"
        return render(request, 'main/characters.html', {'error_message': error_message})
    except Exception as e:
        error_message = f"Произошла ошибка: {str(e)}"
        return render(request, 'main/characters.html', {'error_message': error_message})

def hashira(request):
    """Страница со столпами"""
    try:
        hashira = Character.objects.filter(is_hashira=True)
        return render(request, 'main/hashira.html', {'hashira': hashira})
    except OperationalError as e:
        error_message = f"Ошибка доступа к базе данных: {str(e)}"
        return render(request, 'main/hashira.html', {'error_message': error_message})
    except Exception as e:
        error_message = f"Произошла ошибка: {str(e)}"
        return render(request, 'main/hashira.html', {'error_message': error_message})

def demons(request):
    """Страница с демонами"""
    try:
        demons = Demon.objects.all()
        return render(request, 'main/demons.html', {'demons': demons})
    except OperationalError as e:
        error_message = f"Ошибка доступа к базе данных: {str(e)}"
        return render(request, 'main/demons.html', {'error_message': error_message})
    except Exception as e:
        error_message = f"Произошла ошибка: {str(e)}"
        return render(request, 'main/demons.html', {'error_message': error_message})
    
class CharacterViewSet(viewsets.ModelViewSet):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer

class DemonViewSet(viewsets.ModelViewSet):
    queryset = Demon.objects.all()
    serializer_class = DemonSerializer

def character_detail(request, character_id):
    """Страница с деталями персонажа"""
    try:
        character = get_object_or_404(Character, id=character_id)
        return render(request, 'main/character_detail.html', {'character': character})
    except OperationalError as e:
        error_message = f"Ошибка доступа к базе данных: {str(e)}"
        return render(request, 'main/character_detail.html', {'error_message': error_message})
    except Exception as e:
        error_message = f"Произошла ошибка: {str(e)}"
        return render(request, 'main/character_detail.html', {'error_message': error_message})
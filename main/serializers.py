from rest_framework import serializers
from .models import Character, Demon

class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = '__all__'

class DemonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Demon
        fields = '__all__'
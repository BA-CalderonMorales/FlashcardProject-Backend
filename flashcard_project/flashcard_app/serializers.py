from rest_framework import serializers
from .models import FlashcardCollection, Card


class FlashcardCollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = FlashcardCollection
        fields = '__all__'


class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = '__all__'

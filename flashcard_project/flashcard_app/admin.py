from django.contrib import admin
from .models import FlashcardCollection, Card

# Register your models here.
admin.site.register(FlashcardCollection)
admin.site.register(Card)

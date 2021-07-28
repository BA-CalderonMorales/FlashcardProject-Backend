from django.db import models


# Create your models here.
class FlashcardCollection(models.Model):
    name = models.CharField(max_length=140)
    like = models.IntegerField(default=0)
    dislike = models.IntegerField(default=0)


class Card(models.Model):
    front_content = models.CharField(max_length=70)  # word, question, topic
    back_content = models.CharField(max_length=140)  # definition, answer, description
    deck = models.ForeignKey('flashcard_app.FlashcardCollection', on_delete=models.CASCADE, null=True)

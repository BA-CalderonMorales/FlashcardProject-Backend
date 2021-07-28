from django.urls import path
from . import views

urlpatterns = [
    path('all_decks', views.FlashcardDeckList.as_view()),
    path('all_decks/<int:pk>', views.FlashcardDeckDetail.as_view()),
    path('all_decks/like/<int:pk>', views.Like.as_view()),
    path('all_decks/dislike/<int:pk>', views.Dislike.as_view()),
    path('all_cards', views.CardList.as_view()),
    path('all_cards/<int:pk>', views.CardDetail.as_view())
]
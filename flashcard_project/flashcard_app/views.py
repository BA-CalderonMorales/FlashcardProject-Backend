from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import FlashcardCollection, Card
from .serializers import FlashcardCollectionSerializer, CardSerializer


# Create your views here.
class FlashcardDeckList(APIView):
    """
    This FlashcardCollectionList class is used to allow a front-end users to easily identify and manipulate a list
    of flashcard decks in the 'most up-to-date' MySQL database.
    """

    def get(self, request):
        """
        Get all the decks in the current Flashcard Collection within MySQL.
        :param request: Comes from the client.
        :return: The list of collection of flashcard decks.
        """
        collection = FlashcardCollection.objects.all()
        # Converts all objects into JSON
        serializer = FlashcardCollectionSerializer(collection, many=True)
        return Response(serializer.data)

    def post(self, request):
        """
        Creates a new deck object with input taken in from the client.
        :param request: Comes from client.
        :return: Returns whether the post was successful or not.
        """
        serializer = FlashcardCollectionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FlashcardDeckDetail(APIView):
    """
    This FlashcardDeckDetail class is used to allow a front-end users to easily identify and manipulate specific
     decks  in a list of decks  contained in my current MySQL database.
    """

    def get_Deck(self, pk):
        """
        Allows you to search for a deck contained in the current MySQL database containing all the deck objects.
        :param pk: Given by the client.
        :return: The specific details of a deck in a deck object.
        """
        try:
            return FlashcardCollection.objects.get(pk=pk)
        except FlashcardCollection.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        deck = self.get_Deck(pk)
        serializer = FlashcardCollectionSerializer(deck)
        return Response(serializer.data)

    def put(self, request, pk):
        """
        Allows you to update a specific object inside of the current list of deck objects thats contained in the
        MySQL database.
        :param request:Taken in from the client.
        :param pk: The specific deck that the client wants to manipulate. (It's location.)
        :return: The updated deck object.
        """
        deck = self.get_Deck(pk)
        serializer = FlashcardCollectionSerializer(deck, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        """
        Deletes the deck that is searched by the client wanting to delete it.
        :param request: Taken in from the client.
        :param pk: The specific deck that the client wants to manipulate (It's location)
        :return: A response to the client stating that there is no content.
        """
        deck = self.get_Deck(pk)
        deck.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class Like(APIView):
    """
    Allows user clients the ability to add likes to a deck of cards.
    """

    def get_Deck(self, pk):
        """
        Allows you to search for a deck contained in the current MySQL database containing all the deck objects.
        :param pk: Given by the client.
        :return: The specific details of a deck in a deck object.
        """
        try:
            return FlashcardCollection.objects.get(pk=pk)
        except FlashcardCollection.DoesNotExist:
            raise Http404

    def patch(self, request, pk):
        """
        Can be used to isolate any specific attribute inside of comment. In this case, it's being
        used to isolate the number of likes inside of the current comment model being viewed.
        :param request: Taken in from the client.
        :param pk: The specific comment that the client wants to manipulate. (It's location.)
        :return: The updated comment object.
        """
        deck = self.get_Deck(pk)
        deck.like += 1
        serializer = FlashcardCollectionSerializer(deck, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Dislike(APIView):
    """
    Allows user clients the ability to add dislike to a deck of cards.
    """

    def get_Deck(self, pk):
        """
        Allows you to search for a deck contained in the current MySQL database containing all the deck objects.
        :param pk: Given by the client.
        :return: The specific details of a deck in a deck object.
        """
        try:
            return FlashcardCollection.objects.get(pk=pk)
        except FlashcardCollection.DoesNotExist:
            raise Http404

    def patch(self, request, pk):
        """
        Can be used to isolate any specific attribute inside of comment. In this case, it's being
        used to isolate the number of likes inside of the current comment model being viewed.
        :param request: Taken in from the client.
        :param pk: The specific comment that the client wants to manipulate. (It's location.)
        :return: The updated comment object.
        """
        deck = self.get_Deck(pk)
        deck.dislike += 1
        serializer = FlashcardCollectionSerializer(deck, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CardList(APIView):
    """
    This CardList class is used to allow a front-end users to easily identify and manipulate a list
    of cards attached to a Flashcard collection in the database (via foreign key).
    """

    def get(self, pk):
        """
        Get all the information contained in the card collection, such as the front-content, back-content, and
        the foreign key ('deck' See models.py).
        :param request: Comes from the client.
        :return: The information retained within every card in the collection of cards in MySQL.
        """
        contents = Card.objects.all()
        # Converts all objects into JSON
        serializer = CardSerializer(contents, many=True)
        return Response(serializer.data)

    def post(self, request):
        """
        Creates a new card object with input taken in from the client.
        :param request: Comes from client.
        :return: Returns whether the post was successful or not.
        """
        serializer = CardSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CardDetail(APIView):
    """
        This CardDetail class is used to allow a front-end users to easily identify and manipulate specific
         card in a list of cards contained in my current MySQL database.
        """

    def get_Card(self, pk):
        """
        Allows you to search for a card contained in the current MySQL database containing all the card objects.
        :param pk: Given by the client.
        :return: The specific details of a card in a card object.
        """
        try:
            return Card.objects.get(pk=pk)
        except Card.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        a_card = self.get_Card(pk)
        serializer = CardSerializer(a_card)
        return Response(serializer.data)

    def put(self, request, pk):
        """
        Allows you to update a specific object inside of the current list of card objects that's contained in the
        MySQL database.
        :param request: Taken in from the client.
        :param pk: The specific card id that the client wants to manipulate. (It's location.)
        :return: The updated card object.
        """
        a_card = self.get_Card(pk)
        serializer = CardSerializer(a_card, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        """
        Deletes the card that is searched by the client wanting to delete it.
        :param request: Taken in from the client.
        :param pk: The specific card that the client wants to manipulate (It's location)
        :return: A response to the client stating that there is no content.
        """
        a_card = self.get_Card(pk)
        a_card.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

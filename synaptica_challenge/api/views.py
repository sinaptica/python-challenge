from synaptica_challenge.api.models import Item
from synaptica_challenge.api.serializers import ItemSerializer
from rest_framework import generics


class ItemList(generics.ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class ItemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

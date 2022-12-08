import datetime

from django.utils import timezone
from rest_framework.filters import SearchFilter
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from apps.main.models import PaymentCard
from apps.main.serializers import (
    CardListSerializer, CardDetailSerializer, UpdateCardSerializer
)


class CardListAPIView(ListAPIView):
    """Endpoint for card list"""

    queryset = PaymentCard.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = CardListSerializer
    filter_backends = (SearchFilter,)
    search_fields = (
        'series__title', 'number', 'start_date', 'end_date', 'status'
    )


class CardDetailAPIView(RetrieveUpdateDestroyAPIView):
    """Endpoint for card detail card and update card and delete card"""

    permission_classes = (AllowAny,)
    queryset = PaymentCard.objects.all()
    serializer_class = UpdateCardSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = CardDetailSerializer(instance)
        return Response(serializer.data)

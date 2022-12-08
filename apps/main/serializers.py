from rest_framework import serializers

from apps.main.models import PaymentCard, SeresCard, HistoryTransactions


class SeriesCardSerializer(serializers.ModelSerializer):
    """Serializer for series card list"""

    class Meta:
        model = SeresCard
        fields = ('id', 'title')


class CardListSerializer(serializers.ModelSerializer):
    """Serializer for card list"""

    series = SeriesCardSerializer(read_only=True)
    status = serializers.CharField(source='get_status_display')

    class Meta:
        model = PaymentCard
        fields = ('series', 'id', 'number', 'start_date', 'end_date', 'status')


class HistoryTransactionsSerializer(serializers.ModelSerializer):
    """Serializer for history transaction card"""

    type = serializers.CharField(source='get_type_display')

    class Meta:
        model = HistoryTransactions
        fields = ('datetime', 'type', 'sum')


class CardDetailSerializer(serializers.ModelSerializer):
    """Serializer for detail and delete card"""

    series = SeriesCardSerializer(read_only=True)
    status = serializers.CharField(source='get_status_display')
    history_transactions = HistoryTransactionsSerializer(many=True)

    class Meta:
        model = PaymentCard
        fields = (
            'series', 'id', 'number', 'start_date', 'end_date', 'sum', 'status',
            'history_transactions'
        )


class UpdateCardSerializer(serializers.ModelSerializer):
    """Serializer for update status card"""

    status = serializers.ChoiceField(
        choices=[("active", "Активирована"), ("not_active", "Не активирована")]
    )

    class Meta:
        model = PaymentCard
        fields = ('status',)

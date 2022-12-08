from django.db import models
from django.utils import timezone

from core.utils import number_card_regex


class SeresCard(models.Model):
    """Model for series card"""

    title = models.CharField(
        verbose_name='Серия карты', max_length=255, unique=True
    )

    class Meta:
        verbose_name = 'Серия карты'
        verbose_name_plural = 'Серии Карт'

    def __str__(self):
        return self.title


class PaymentCard(models.Model):
    """Model for online payment card"""

    STATUS_CHOICES = (
        ("active", "Активирована"),
        ("not_active", "Не активирована"),
        ("overdue", "Просрочена")
    )

    series = models.ForeignKey(
        to=SeresCard, verbose_name='Серия карты', max_length=255,
        on_delete=models.PROTECT, related_name='cards'
    )
    number = models.CharField(
        verbose_name='Номер карты', max_length=255, unique=True,
        validators=[number_card_regex]
    )
    start_date = models.DateTimeField(
        verbose_name='Дата создания', default=timezone.now
    )
    end_date = models.DateTimeField(
        verbose_name='Дата окончания', blank=True, null=True
    )
    use_date = models.DateTimeField(
        verbose_name='Дата использования', blank=True, null=True
    )
    sum = models.DecimalField(
        verbose_name='Сумма', default=0, decimal_places=2, max_digits=10
    )
    status = models.CharField(
        verbose_name='Статус', choices=STATUS_CHOICES, max_length=255,
        default='not_active'
    )

    class Meta:
        verbose_name = 'Платежная карта'
        verbose_name_plural = 'Платежные карты'

    def __str__(self):
        return f"{str(self.series)}: {self.number}"


class HistoryTransactions(models.Model):
    """Model for history online payment card"""

    TYPE_CHOICES = (
        ("received_account", "Поступило на счет"),
        ("debited_account", "Списано со счета"),
    )

    datetime = models.DateTimeField(
        verbose_name='Дата транзакции', blank=True, null=True
    )
    type = models.CharField(
        verbose_name='Тип транзакции', max_length=255, choices=TYPE_CHOICES
    )
    sum = models.DecimalField(
        verbose_name='Сумма', default=0, decimal_places=2, max_digits=10
    )
    payment_card = models.ForeignKey(
        to=PaymentCard, verbose_name='Платежная карта', max_length=255,
        on_delete=models.CASCADE, related_name='history_transactions'
    )

    class Meta:
        verbose_name = 'История транзакции'
        verbose_name_plural = 'История транзакций'

    def __str__(self):
        return self.payment_card.number

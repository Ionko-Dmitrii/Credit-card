from django.contrib import admin

from apps.main.models import SeresCard, PaymentCard, HistoryTransactions


@admin.register(SeresCard)
class SeresCardAdmin(admin.ModelAdmin):
    pass


@admin.register(PaymentCard)
class PaymentCardAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'status')


@admin.register(HistoryTransactions)
class HistoryTransactionsAdmin(admin.ModelAdmin):
    pass

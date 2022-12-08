from django.utils import timezone

from apps.main.models import PaymentCard


def deactivate_card_job():
    total_time = timezone.now()
    cards = PaymentCard.objects.filter(end_date__lte=total_time)
    update_cards = []
    if cards:
        for card in cards:
            if card.status != 'not_active':
                card.status = 'not_active'
                update_cards.append(card)
        if len(update_cards) > 0:
            PaymentCard.objects.bulk_update(update_cards, ['status'])
            print(f'[{total_time}]: {str(update_cards)}')

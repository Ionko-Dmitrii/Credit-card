import datetime
import random

from django.core.management import BaseCommand
from django.utils import timezone

from apps.main.models import PaymentCard, SeresCard


class Command(BaseCommand):
    help = u'Генератор платежных карт'

    def add_arguments(self, parser):
        parser.add_argument(
            '-s', '--series', type=str, required=True,
            help='Серия карты например: (MasterCard)'
        )
        parser.add_argument(
            '-c', '--count', type=int, required=True,
            help='Количество создаваемых карт'
        )

    def handle(self, *args, **kwargs):
        series = kwargs['series']
        count = kwargs['count']
        now_date = timezone.now()
        end_date = now_date + datetime.timedelta(days=548)
        series_obj, created = SeresCard.objects.get_or_create(title=series)
        new_card_list = []
        for i in range(count):
            number = "-".join(
                (''.join(random.sample("1234567890", 4)) for i in range(4))
            )
            card_obj = PaymentCard(
                series=series_obj,
                number=number,
                start_date=now_date,
                end_date=end_date,
            )
            new_card_list.append(card_obj)

        PaymentCard.objects.bulk_create(new_card_list)
        self.stdout.write(self.style.SUCCESS('Платежные карты добавлены!'))

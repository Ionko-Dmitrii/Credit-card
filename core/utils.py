from django.core.validators import RegexValidator

number_card_regex = RegexValidator(
    regex=r'^([0-9]{4}[-]){3}[0-9]{4}$',
    message="Формат номера карты: 1234-1234-1234-1234"
)

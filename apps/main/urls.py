from django.urls import path

from apps.main.views import CardListAPIView, CardDetailAPIView

urlpatterns = [
    path('card-list/', CardListAPIView.as_view(), name='card_list'),
    path('card/<int:pk>/', CardDetailAPIView.as_view(), name='card_detail'),
]

from django.urls import path
from .views import *


urlpatterns = [
    path('order/', OrderListCreateView.as_view(), name='order-list'),
    path('order/<int:pk>/', OrderRetrieveUpdateDestroyView.as_view(), name='order-detail')
]

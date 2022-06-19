from django.urls import path
from .views import *


urlpatterns = [
    path('orders/', OderListView.as_view(), name='orders-list'),
    path('orders/', OrderCreateView.as_view(), name='orders-create'),
    path('orders/<int:pk>/', OrderRetrieveDestroyView.as_view(), name='order-get'),
    path('orders/<int:pk>/', OrderUpdateDeleteView.as_view(), name='order-update')
]

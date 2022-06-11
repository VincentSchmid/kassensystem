from django.urls import path
from .views import *


urlpatterns = [
    path('', ListCreateMenuItemView.as_view(), name='menuitem-list'),
    path('/<int:pk>/', RetrieveUpdateDestroyMenuItemView.as_view(), name='menuitem-detail'),
]

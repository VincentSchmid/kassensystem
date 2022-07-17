from django.contrib import admin
from .models import Order, OrderItem, Table, Payment, PaymentMethod


admin.site.register(OrderItem)
admin.site.register(Order)
admin.site.register(Table)
admin.site.register(Payment)
admin.site.register(PaymentMethod)

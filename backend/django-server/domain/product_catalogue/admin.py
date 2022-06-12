from django.contrib import admin
from .models import MenuItem, Category, SalesTax


admin.site.register(SalesTax)
admin.site.register(Category)
admin.site.register(MenuItem)

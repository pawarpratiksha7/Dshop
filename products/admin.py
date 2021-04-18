from django.contrib import admin
from products.models import Product


# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ['type','flavor','price','stock','image']
admin.site.register(Product,ProductAdmin)


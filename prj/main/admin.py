from django.contrib import admin
from .models import Product, Category, User, Cart, Order, Recension

class ProductAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "price", "availability", "manufacturer", "category", "description", "picture"]

class CategoryAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "list_of_products"]

class UserAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "e_mail", "order_history", "advertisements"]

class CartAdmin(admin.ModelAdmin):
    list_display = ["id", "products_in", "total_price", "payment_method"]

class OrderAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "list_of_products", "price", "order_status"]

class RecensionAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "product_name"]

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Cart, CartAdmin )
admin.site.register(Order, OrderAdmin)
admin.site.register(Recension, RecensionAdmin)
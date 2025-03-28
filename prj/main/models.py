from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=512)
    price = models.IntegerField(blank=True, null=True)
    availability = models.CharField(max_length=128)
    manufacturer = models.CharField(max_length=512)
    category = models.ForeignKey("Category", on_delete=models.SET_NULL, null=True)
    description = models.TextField(blank=True, default="")
    picture = models.ImageField(blank=True)

    def __str__(self):
        return f"Movie <{self.id}> {self.name}"

class Category(models.Model):
    name = models.CharField(max_length=512)
    list_of_products = models.TextField(blank=True, default="")

    def __str__(self):
        return f"Movie <{self.id}> {self.name}"

class User(models.Model):
    name = models.CharField(max_length=512)
    e_mail = models.EmailField(blank=True)
    #password = models.
    order_history = models.TextField(blank=True, default="")
    advertisements = models.TextField(blank=True, default="")

    def __str__(self):
        return f"Movie <{self.id}> {self.name}"

class Cart(models.Model):
    products_in = models.TextField(blank=True, default="")
    total_price = models.IntegerField(blank=True, null=True)
    payment_method = models.CharField(max_length=128)

    def __str__(self):
        return f"Movie <{self.id}> {self.products_in}"

class Order(models.Model):
    user = models.ForeignKey("User", on_delete=models.SET_NULL, null=True)
    list_of_products = models.TextField(blank=True, default="")
    price = models.IntegerField(blank=True, null=True)
    order_status = models.CharField(max_length=128)

    def __str__(self):
        return f"Movie <{self.id}> {self.user}"

class Recension(models.Model):
    user = models.ForeignKey("User", on_delete=models.SET_NULL, null=True)
    product_name = models.CharField(max_length=512)

    def __str__(self):
        return f"Movie <{self.id}> {self.user}"
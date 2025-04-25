from django.shortcuts import render
from main.models import Product

# change to components theme
def get_homepage(request):
    context = {

        "svatek": "Libor",
        # SELECT * from Products;
        "movies": Product.objects.all()
    }
 
    return render(request, "main/homepage.html", context)
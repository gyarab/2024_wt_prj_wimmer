from django.shortcuts import render
from main.models import Product

# change to components theme
def get_homepage(request):
    context = {

        "svatek": "Libor",
        # SELECT * from Products ORDER BY "title" LIMIT 10;
        "movies": Product.objects.all().order_by("title")[:10]
    }

    products = Product.objects.all().order_by("title")

    #check if search parameter is in the request
    if request.GET.get("search"):
        print("SEARCH", request.GET.get("search"))
        products = products.filter(title__icontains=request.GET.get("search"))
 
    return render(request, "main/homepage.html", context)
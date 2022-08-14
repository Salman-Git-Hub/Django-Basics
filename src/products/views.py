from django.shortcuts import render
from .models import Product
# Create your views here.


def dynamic_lookup_view(request, id):
    obj = Product.objects.get(id=id)
    ctx = {
        "object": obj
    }
    return render(request, "products/product_detail.html", ctx)

from django.shortcuts import render
from .models import Product


# Create your views here.
def product_detail_view(request):
    obj = Product.objects.get(id=1)
    # ctx = {
    #     "title": obj.title,
    #     "price": obj.price,
    #     "description": obj.description
    # }
    ctx = {
        "object": obj
    }
    return render(request, 'products/product_detail.html', ctx)

from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
# Create your views here.


def dynamic_lookup_view(request, id):
    # obj = Product.objects.get(id=id)
    obj = get_object_or_404(Product, id=id)
    # try:
    #     obj = Product.objects.get(id=id)
    # except Product.DoesNotExist:
    #     raise Http404

    ctx = {
        "object": obj
    }
    return render(request, "products/product_detail.html", ctx)


def product_delete_view(request, id):
    obj = get_object_or_404(Product, id=id)
    if request.method == 'POST':
        obj.delete()
        return redirect("../../")
    ctx = {
        "object": obj
    }
    return render(request, "products/product_delete.html", ctx)


def product_list_view(request):
    query_set = Product.objects.all()
    ctx = {
        "object_list": query_set
    }
    return render(request, "products/product_list.html", ctx)

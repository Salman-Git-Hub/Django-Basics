from django.shortcuts import render
from .models import Product
from .forms import ProductForm,RawProductForm


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


# def product_create_view(request):
#     form = ProductForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         form = ProductForm()
#
#     ctx = {
#         "form": form
#     }
#     return render(request, 'products/product_create.html', ctx)

# def product_create_view(request):
#     # print(request.GET)
#     # print(request.POST)
#     if request.method == 'POST':
#         new_title = request.POST.get("title")
#         new_description = request.POST.get("description")
#         new_price = request.POST.get("price")
#         Product.objects.create(title=new_title, description=new_description, price=new_price)
#     ctx = {}
#     return render(request, 'products/product_create.html', ctx)


def product_create_view(request):
    form = RawProductForm()
    if request.method == 'POST':
        form = RawProductForm(request.POST)
        if form.is_valid():
            # print(form.cleaned_data)
            Product.objects.create(**form.cleaned_data)
        else:
            print(form.errors)
    ctx = {
        "form": form
    }
    return render(request, 'products/product_create.html', ctx)


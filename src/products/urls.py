from django.urls import path
from .views import (
    product_detail_view,
    product_create_view,
    product_delete_view,
    product_list_view
)

app_name = 'products'  # namespace
urlpatterns = [
    path("<int:id>/", product_detail_view, name='product-detail'),
    path("create/", product_create_view, name='product-create'),
    path("<int:id>/delete/", product_delete_view, name='product-delete'),
    path("", product_list_view, name='product-list'),
]

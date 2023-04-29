from django.urls import path

from products.views import get_products_list, get_category_list, get_product, get_category

urlpatterns = [
    path("products/", get_products_list, name="products_list"),
    path('categoryies/', get_category_list, name="category_list"),
    path('product/<int:pk>', get_product, name="product"),
    path('category/<int:pk>', get_category, name="category")
]

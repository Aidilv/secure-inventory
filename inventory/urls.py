from django.urls import path
from .views import *

urlpatterns = [
    path('register/', register),
    path('products/', product_list),
    path('products/add/', add_product),
    path('products/edit/<int:product_id>/', edit_product),
    path('products/delete/<int:product_id>/', delete_product),
    path('profile/', profile),
    path('audit/', audit_log),
]

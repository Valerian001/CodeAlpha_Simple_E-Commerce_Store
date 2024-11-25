from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('cart/', views.cart, name='cart'),
    path('api/products/', views.ProductListAPI.as_view(), name='product-list-api'),
    path('api/products/<int:pk>/', views.ProductDetailAPI.as_view(), name='product-detail-api'),
]
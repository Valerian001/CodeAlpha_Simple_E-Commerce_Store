from django.shortcuts import render
from .models import Product, Category
from django.db.models import Q

from rest_framework import generics
from .serializers import ProductSerializer

# Create your views here.

def product_list(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    search_query = request.GET.get('search', '')
    category_filter = request.GET.get('category', '')

    if search_query:
        products = products.filter(
            Q(name__icontains=search_query) | Q(description__icontains=search_query)
        )

    if category_filter:
        products = products.filter(category__name=category_filter)

    context = {
        'products': products,
        'categories': categories,
        'search_query': search_query,
        'category_filter': category_filter,
    }
    return render(request, 'products/product_list.html', context)


def cart(request):
    return render(request, 'products/cart.html')


class ProductListAPI(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetailAPI(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
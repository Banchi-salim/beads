from django.shortcuts import render, get_object_or_404
from .models import Product, Category


def home(request):
    """Homepage view with featured products"""
    featured_products = Product.objects.filter(available=True)[:6]
    return render(request, 'products/home.html', {
        'featured_products': featured_products
    })


def product_list(request, category_slug=None):
    """Product listing page with optional category filter"""
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    return render(request, 'products/product_list.html', {
        'category': category,
        'categories': categories,
        'products': products
    })

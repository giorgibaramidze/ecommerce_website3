from django.shortcuts import render
from .models import Product
from category.models import Category
from category.admin import SubCategoryInline
from .filters import productFilter

def product_detail(request, category_slug, sub_category_slug, product_slug):
    product = Product.objects.get(category__category__slug=category_slug, category__slug=sub_category_slug, slug=product_slug)
    context = {
        'product': product
    }
    return render(request, 'product_detail.html', context)

def product_by_category(request, category_slug):
    products = productFilter(request.GET, queryset=Product.objects.filter(category__category__slug=category_slug))
    context = {
        "products": products
    }
    print(products)
    return render(request, 'product_by_category.html', context)



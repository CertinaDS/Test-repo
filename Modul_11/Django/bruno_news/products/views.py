from django.shortcuts import render

from .models import Category, Product


def product_list(request):
    categories = Category.objects.all()
    products = Product.objects.all()

    context = {
        'categories': categories,
        'products': products,
    }

    return render(request, 'product_list.html', context)

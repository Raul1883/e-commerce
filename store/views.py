from django.shortcuts import render, get_object_or_404

import store.models


def main_page(request):
    items = store.models.Product.objects.all()
    return render(request, "main_page.html", {"items": items})


def product_page(request, slug):
    product = get_object_or_404(store.models.Product, slug=slug)
    return render(request, 'product.html', {'product': product})

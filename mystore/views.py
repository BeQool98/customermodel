from django.shortcuts import render
from .models import StoreProduct

# Create your views here.
def landing_page(request):
    context = {}
    return render(request, 'mystore/landing_page.html', context)

def store(request):
    products = StoreProduct.objects.all()
    context = {'products':products}
    return render(request, 'mystore/store.html', context)

def cart(request):
    context = {}
    return render(request, 'mystore/cart.html', context)

def checkout(request):
    context = {}
    return render(request, 'mystore/checkout.html', context)
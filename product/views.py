from django.shortcuts import render
from .models import Product
# from .forms import ProductForm

def list_products(request):
    products = Product.objects.all()
    return render(request, 'products.html', {'products': products})

def create_product(request):
    form = ProductForm(request.Post or None)

    if form.is_vaild():
        form.save()
        return redirect('list_products')

    return render(request, 'products-form.html', {'form': form})

def update_product(request, id):
    product = Product.objects.get(id=id)
    form = ProductForm(request.Post or None, instance=product)

    if form.is_vaild():
        form.save()
        return redirect('list_products')
    return render(request, 'products-form.html', {'form': form})

def delete_product(request, id):
    product = Product.objects.get(id=id)

    return render(request, 'products.html', {'products': products})

# Create your views here.

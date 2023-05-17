from django.shortcuts import render,redirect
from .models import Product,Cart
# Create your views here.

def index(request):
    
    product_list = Product.objects.all()
    cart_list = Cart.objects.all()
    return render(request,'main/index.html',context={
        'product_list':product_list,
        'cart_list':cart_list
    })


def cart(request):
    summ = 0
    if request.method == 'POST':
        prod_id = request.POST.get('id')
        my_prod = Product.objects.get(id=prod_id)
        Cart.objects.create(cart_item=my_prod)
        return redirect('index')
    cart_list = Cart.objects.all()
    cart_sum = Cart.objects.all()
    for i in cart_sum:
        summ += i.cart_item.price
    
    return render(request,'main/cart.html',context={
        'cart_list':cart_list,
        'summ':summ
    })


def delete_item(request):
    if request.method == 'POST':
        prod_id = request.POST.get('id')
        Cart.objects.filter(id=prod_id).delete()
        return redirect('cart')

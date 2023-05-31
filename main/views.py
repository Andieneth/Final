from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from main.models import Cart
from mangashop.models import ArticlesShop
from django.shortcuts import redirect


def index(request):
    data = {
        'title': 'Приветствую тебя на сайте MangaLib!'
    }
    return render(request, 'main/manga.html',data)

def Shop(request):
    return render(request, 'main/shop.html')

def Account(request):
    if request.user.is_authenticated:
        cart = Cart.objects.get_or_create(user=request.user)[0]
        products = cart.products.all()
        context = {'products': products}
        return render(request, 'main/account.html', context)
    else:
        return render(request, 'main/account.html')

@login_required
def add_to_cart(request, ArticlesShop_id):
    product = ArticlesShop.objects.get(id=ArticlesShop_id)
    cart = Cart.objects.get_or_create(user=request.user)[0]
    cart.products.add(product)
    response = redirect('/account')
    return response

@login_required
def remove_from_cart(request, ArticlesShop_id):
    product = ArticlesShop.objects.get(id=ArticlesShop_id)
    cart = Cart.objects.get(user=request.user)
    cart.products.remove(product)
    response = redirect('/account')
    return response


@login_required
def buy_order(request):
    cart = Cart.objects.get(user=request.user)
    products = cart.products.all()
    for product in products:
        product.order_count += 1
        product.save()
    cart.products.clear()
    cart.save()
    response = redirect('/account')
    return response
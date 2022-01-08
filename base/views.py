from django.shortcuts import render, redirect
from .models import Meal, Cart, Order
from .forms import CartForm, OrderForm


def cartForm(request, pk):
    cart = CartForm()
    meal = Meal.objects.get(id=pk)
    context = {'meal': meal, 'form': cart}

    if request.method == "POST":
        cart = CartForm(request.POST)
        print(request.POST)
        if cart.is_valid():
            cart.save()
            return redirect('home')

    return render(request, 'base/cartform.html', context)


def home(request):
    meals = Meal.objects.all()
    context = {'meals': meals}
    return render(request, 'base/home.html', context)


def cart(request):
    cart = Cart.objects.all()
    if request.method == "POST":
        meals = {}
        it = 0
        post = request.POST
        names_list = post['names_arr'].split(',')
        amounts_list = post['amounts_arr'].split(',')

        for i in range(1, len(names_list)*2, 2):
            meals.update({i: names_list[it], i+1: int(amounts_list[it])})
            it += 1

        orderForm = OrderForm({'csrfmiddlewaretoken': post['csrfmiddlewaretoken'], 'meals': meals, 'costs': float(post['costs_sum']), 'is_done': False})
        if orderForm.is_valid():
            orderForm.save()
            cart.delete()
            return redirect('home')
    context = {'cart': cart}
    return render(request, 'base/cart.html', context)


def deleteCart(request, pk):
    element = Cart.objects.get(id=pk)
    context = {'element': element}
    if request.method == "POST":
        element.delete()
        return redirect('cart')

    return render(request, 'base/delete.html', context)


def deleteAllCart(request):
    cart = Cart.objects.all()
    if request.method == "POST":
        cart.delete()
        return redirect('cart')
    return render(request, 'base/delete_all.html')


def orderInfo(request):
    order = Order.objects.all()
    context = {'order': order}
    return render(request, 'base/orderinfo.html', context)

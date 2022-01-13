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

        for i in range(1, len(names_list) * 2, 2):
            meals.update({i: names_list[it], i + 1: int(amounts_list[it])})
            it += 1

        orderForm = OrderForm(
            {"csrfmiddlewaretoken": post["csrfmiddlewaretoken"], "meals": meals, "costs": float(post["costs_sum"]),
             "is_done": False, "is_received": False})
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


def panel(request):
    list_of_meals = Order.objects.values_list('meals')
    list_of_order_id = Order.objects.values_list('id')
    list_of_bools = Order.objects.values_list('is_done', 'is_received')
    list_of_all = []
    list_of_id = []

    if request.method == "POST":
        data = request.POST
        data_id = data['id']
        row = Order.objects.get(id=data_id)

        if data['data'] == 'done':
            row.is_done = True
            row.save()
        elif data['data'] == 'received':
            row.is_received = True
            row.save()

    for el in list_of_order_id:
        list_of_id.append(el)

    for el in list_of_meals:
        meal = el[0]
        temp = []
        for i in range(1, len(meal) + 1):
            temp.append(meal[str(i)])
        list_of_all.append(temp)

    zipped = zip(list_of_id, list_of_all, list_of_bools)
    context = {'order': zipped}

    return render(request, 'base/panel.html', context)

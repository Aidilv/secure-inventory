from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.paginator import Paginator
from .models import Product, AuditLog

def is_admin(user):
    return user.is_staff


def register(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
        elif len(password) < 6:
            messages.error(request, "Password must be at least 6 characters")
        else:
            user = User.objects.create_user(username=username, password=password)
            messages.success(request, "Account created successfully")
            login(request, user)
            return redirect('/products/')

    return render(request, 'inventory/register.html')


@login_required
def product_list(request):
    search = request.GET.get('search', '')
    products = Product.objects.filter(name__icontains=search)

    paginator = Paginator(products, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'inventory/product_list.html', {
        'page_obj': page_obj,
        'search': search
    })


@login_required
@user_passes_test(is_admin)
def add_product(request):
    if request.method == "POST":
        name = request.POST['name']
        quantity = int(request.POST['quantity'])
        price = float(request.POST['price'])

        if quantity < 0 or price <= 0:
            messages.error(request, "Invalid quantity or price")
        else:
            Product.objects.create(name=name, quantity=quantity, price=price)
            AuditLog.objects.create(
                user=request.user,
                action="Added product",
                product_name=name
            )
            messages.success(request, "Product added successfully")
            return redirect('/products/')

    return render(request, 'inventory/product_form.html', {'action': 'Add'})


@login_required
@user_passes_test(is_admin)
def edit_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if request.method == "POST":
        product.name = request.POST['name']
        product.quantity = int(request.POST['quantity'])
        product.price = float(request.POST['price'])
        product.save()

        AuditLog.objects.create(
            user=request.user,
            action="Edited product",
            product_name=product.name
        )
        messages.success(request, "Product updated successfully")
        return redirect('/products/')

    return render(request, 'inventory/product_form.html', {
        'action': 'Edit',
        'product': product
    })


@login_required
@user_passes_test(is_admin)
def delete_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    AuditLog.objects.create(
        user=request.user,
        action="Deleted product",
        product_name=product.name
    )
    product.delete()
    messages.success(request, "Product deleted")
    return redirect('/products/')


@login_required
def profile(request):
    return render(request, 'inventory/profile.html')


@login_required
@user_passes_test(is_admin)
def audit_log(request):
    logs = AuditLog.objects.all().order_by('-timestamp')
    return render(request, 'inventory/audit_log.html', {'logs': logs})

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Product, AuditLog

def is_admin(user):
    return user.is_staff


@login_required
def product_list(request):
    products = Product.objects.all()
    return render(request, 'inventory/product_list.html', {'products': products})


@login_required
@user_passes_test(is_admin)
def add_product(request):
    if request.method == "POST":
        Product.objects.create(
            name=request.POST['name'],
            quantity=request.POST['quantity'],
            price=request.POST['price']
        )
        AuditLog.objects.create(user=request.user, action="Added product")
        return redirect('/products/')
    return render(request, 'inventory/product_form.html', {'action': 'Add'})


@login_required
@user_passes_test(is_admin)
def edit_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == "POST":
        product.name = request.POST['name']
        product.quantity = request.POST['quantity']
        product.price = request.POST['price']
        product.save()
        AuditLog.objects.create(user=request.user, action="Edited product")
        return redirect('/products/')
    return render(request, 'inventory/product_form.html', {
        'action': 'Edit',
        'product': product
    })


@login_required
@user_passes_test(is_admin)
def delete_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    product.delete()
    AuditLog.objects.create(user=request.user, action="Deleted product")
    return redirect('/products/')


@login_required
def profile(request):
    return render(request, 'inventory/profile.html')


@login_required
@user_passes_test(is_admin)
def audit_log(request):
    logs = AuditLog.objects.all().order_by('-timestamp')
    return render(request, 'inventory/audit_log.html', {'logs': logs})

from django.contrib import admin
from .models import Product, AuditLog

admin.site.register(Product)
admin.site.register(AuditLog)

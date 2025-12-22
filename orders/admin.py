from django.contrib import admin
from .models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']
    extra = 0


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'email', 'total_amount', 'paid', 'status', 'created_at']
    list_filter = ['paid', 'status', 'created_at']
    inlines = [OrderItemInline]
    search_fields = ['id', 'user__username', 'email', 'paystack_reference']

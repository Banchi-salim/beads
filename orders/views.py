from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from cart.cart import Cart
from .models import Order, OrderItem
import json
import requests


@login_required
def create_order(request):
    """Display checkout page"""
    cart = Cart(request)
    if len(cart) == 0:
        return redirect('cart:cart_detail')

    # You should set your Paystack public key in settings.py
    # For now, we'll use a placeholder
    paystack_public_key = getattr(settings, 'PAYSTACK_PUBLIC_KEY', 'pk_test_xxxxx')

    return render(request, 'orders/create_order.html', {
        'cart': cart,
        'paystack_public_key': paystack_public_key
    })


@login_required
@csrf_exempt
def verify_payment(request):
    """Verify Paystack payment and create order"""
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            reference = data.get('reference')

            # Verify payment with Paystack
            paystack_secret_key = getattr(settings, 'PAYSTACK_SECRET_KEY', 'sk_test_xxxxx')
            headers = {
                'Authorization': f'Bearer {paystack_secret_key}'
            }
            response = requests.get(
                f'https://api.paystack.co/transaction/verify/{reference}',
                headers=headers
            )

            if response.status_code == 200:
                result = response.json()
                if result['data']['status'] == 'success':
                    # Create order
                    cart = Cart(request)
                    order = Order.objects.create(
                        user=request.user,
                        first_name=data.get('first_name'),
                        last_name=data.get('last_name'),
                        email=data.get('email'),
                        phone=data.get('phone'),
                        address=data.get('address'),
                        city=data.get('city'),
                        state=data.get('state'),
                        postal_code=data.get('postal_code', ''),
                        paid=True,
                        paystack_reference=reference,
                        total_amount=cart.get_total_price()
                    )

                    # Create order items
                    for item in cart:
                        OrderItem.objects.create(
                            order=order,
                            product=item['product'],
                            price=item['price'],
                            quantity=item['quantity']
                        )

                    # Clear the cart
                    cart.clear()

                    return JsonResponse({
                        'success': True,
                        'redirect_url': f'/orders/success/{order.id}/'
                    })

            return JsonResponse({'success': False, 'error': 'Payment verification failed'})

        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})

    return JsonResponse({'success': False, 'error': 'Invalid request'})


def order_success(request, order_id):
    """Order success page"""
    order = get_object_or_404(Order, id=order_id, user=request.user)
    return render(request, 'orders/order_success.html', {'order': order})

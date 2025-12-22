from .cart import Cart


def cart(request):
    """
    Make the cart available to all templates.
    """
    return {'cart': Cart(request)}

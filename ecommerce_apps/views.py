from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProductSerializer
from .models import Product


@api_view()
def product_list(request):
    queryset = Product.objects.select_related('collection').all()
    serializer = ProductSerializer(queryset, many=True, context={'request': request})
    return Response(serializer.data)


@api_view()
def product_detail(request, id):
    product = get_object_or_404(Product, pk=id)
    serializer = ProductSerializer(product)
    return Response(serializer.data)


@api_view()
def collection_detail(request, pk):
    return Response(pk)

#
# def index(request):
#     products = Product.objects.all()
#
#     response = requests.get('https://picsum.photos/picsum/300/300')
#     images = response.json()
#     # images = HttpResponse('image')
#     return render(request, 'ecommerce_app/index.html', {'products': products, 'images': images})
#
#
# def product_list(request):
#     products = Product.objects.all()
#     """
#     Displays a list of all products.
#     """
#     return render(request, 'ecommerce_app/product_list.html', {'products': products})
#
#
# def product_detail(request, pk):
#     """
#     Displays the details of a specific product.
#     """
#     product = Product.objects.get(pk=pk)
#     return render(request, 'ecommerce_app/product_detail.html', {'product': product})
#
#
# def category_detail(request):
#     """
#     Displays the details of a category.
#     """
#     categories = Collection.objects.all()
#     # categories = get_object_or_404(Collection)
#     return render(request, 'ecommerce_app/category_detail.html', {'categories': categories})
#
#
# def add_to_cart(request, pk):
#     """
#     Adds a product to the cart.
#     """
#     product = Product.objects.get(pk=pk)
#     # add product to the cart
#     return redirect('cart')
#
#
# def cart(request, product, quantity):
#     """
#     Displays the contents of the cart.
#     """
#     cart_items = CartItem()
#     cart_items.add_item(product, quantity)
#     cart_items.remove_item(product)
#     cart_items.clear()
#     total_price = cart_items.total_price()
#     return render(request, 'cart.html', {'cart_items': cart_items, 'total_price': total_price})
#
#
# def checkout(request, quantity, product):
#     """
#     Processes the order and displays the confirmation page.
#     """
#     cart_items = CartItem()
#     cart_items.add_item(product, quantity)
#     cart_items.remove_item(product)
#     cart_items.clear()
#     total_price = cart
#
#     if request.method == 'POST':
#         form = CheckoutForm(request.POST)
#         if form.is_valid():
#             # create an Order and Customer objects
#             customer, _ = Customer.objects.get_or_create(
#                 name=form.cleaned_data['name'],
#                 email=form.cleaned_data['email'],
#                 phone=form.cleaned_data['phone'],
#                 shipping_addresses=form.cleaned_data['shipping_addresses'],
#             )
#             order = Order.objects.create(
#                 customer=customer,
#                 total_price=form.cleaned_data['total_price'],
#             )
#             order.items.set(form.cleaned_data['items'])
#             # clear the cart
#             cart_items.clear()
#             return render(request, 'confirmation.html', {'order': order})
#     else:
#         form = CheckoutForm()
#     return render(request, 'checkout.html', {'form': form})

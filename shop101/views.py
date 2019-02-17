from django.shortcuts import render , HttpResponse

from shop101.models import Product,Cart

# Create your views here.
def test(request):
    return HttpResponse( 'hello world')

def products_list(request):
    products = Product.objects.all()
    print(products)
    return render(request,'products_list.html', context = {'product_list':products})

def show_product(request,id):
    p_id = id
    product = Product.objects.get(id=p_id)
    return render(request, 'show_product.html',context={'product':product})



def cart(request):
    if request.method == 'POST':
        p_id = request.POST.get('product_id')
        u_id = request.user.id
        cart_item = Cart()
        cart_item.user_id = u_id
        cart_item.product_id = p_id
        cart_item.save()

        return redirect('/cart')
    else:
        cart_list = Cart.objects.all()
        print(len(cart_list))
        return render(request, 'cart.html', context={'cart_list': cart_list})

def delete_cart_item(request):
    if request.method == 'POST':
        c_id = request.POST.get('cart_id')
        cart_item = Cart.objects.get(id=c_id)
        cart_item.delete()
        return redirect('/cart')
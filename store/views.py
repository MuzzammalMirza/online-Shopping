from django.shortcuts import render,HttpResponseRedirect,redirect,HttpResponse
from .models import Cetagory,Product,contact_us,Order,Brand
from .forms import SignupForm,loginForm
from django.contrib import messages
from django.contrib.auth import authenticate ,login,logout
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm
from django.contrib.auth.decorators import login_required
from cart.cart import Cart
from django.contrib.auth.models import User
# Create your views here.

def base(request):
    return render(request,'base.html')


def index(request):
    cetagory = Cetagory.objects.all()
    brand =Brand.objects.all()
    brandID = request.GET.get('brand')
    cetagoryID = request.GET.get('cetagory')
    if cetagoryID:
        product=Product.objects.filter(sub_cetagory=cetagoryID).order_by('-id')
    elif brandID:
        product = Product.objects.filter(Brand=brandID).order_by('-id')
    else:
        product =Product.objects.all()
    return render(request,'index.html',{'pro':cetagory,'duct':product,'brand':brand,'product':product})

def Signup(request):
        if request.method == 'POST':
            fm = SignupForm(request.POST)
            if fm.is_valid():
                fm.save()
                messages.success(request,'Your account has been created')
        else:
            fm = SignupForm()
        return render(request, 'Registerform.html', {'form': fm})

def Login(request):
    if request.method =="POST":
        fm =loginForm(request=request , data= request.POST)
        if fm.is_valid():
            messages.success(request,'You have been login..')
            uname = fm.cleaned_data['username']
            upas = fm.cleaned_data['password']
            user = authenticate(username=uname , password=upas)
            if user is not None:
               login(request,user)
               return HttpResponseRedirect('/')
    else:
        fm = loginForm
    return render(request,'login.html',{'form':fm})

def  Logout(request):
    logout(request)
    return HttpResponseRedirect('/')

def change_pass(request):
    if request.method =='POST':
        fm=PasswordChangeForm(user=request.user,data=request.POST)
        if fm.is_valid():
            fm.save()
            return HttpResponseRedirect('/login/')
    else:
        fm=PasswordChangeForm(user=request.user)
    return render(request,'changepass.html',{'form':fm})

@login_required(login_url="/login/")
def cart_add(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("index")


@login_required(login_url="/login/")
def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    return redirect("cart_detail")


@login_required(login_url="/login/")
def item_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")


@login_required(login_url="/login/")
def item_decrement(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("cart_detail")


@login_required(login_url="/login/")
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart_detail")


@login_required(login_url="/login/")
def cart_detail(request):
    return render(request, 'cart_detail.html')

def contact(request):
    if request.method =='POST':
        user=contact_us(name=request.POST.get('name'),
                        email=request.POST.get('email'),
                        subject=request.POST.get('subject'),
                        message=request.POST.get('message'))
        user.save()
    return render(request,'Contact.html')

def Checkout(request):
    if request.method =='POST':
        # phone = request.POST.get('phone')
        address=request.POST.get('address')
        phone = request.POST.get("phone")
        pincode = request.POST.get('pincode')
        cart = request.session.get('cart')
        uid = request.session.get('_auth_user_id')
        user = User.objects.get(pk = uid)
        # print(phone,pincode,message,cart,user)

        for i in cart:
            a = int(cart[i]['price'])
            b = cart[i]['quantity']
            total = a + b
            order = Order(
                user = user,
                product = cart[i]['name'],
                price = cart[i]['price'],
                quantity = cart[i]['quantity'],
                image = cart[i]['image'],
                address = address,
                phone = phone,
                pincode = pincode,
                total = total
            )
            order.save()
        request.session['cart']={}
        return redirect('index')



    return HttpResponse('This is Checkout page ')


def order(request):
    uid = request.session.get('_auth_user_id')
    user = User.objects.get(pk=uid)
    Order = order.objects.filter(user = user )
    print(user,Order)
    return render(request,'order.html',{'order':Order})

def product(request):
    cetagory = Cetagory.objects.all()
    brand = Brand.objects.all()
    brandID = request.GET.get('brand')
    cetagoryID = request.GET.get('cetagory')
    if cetagoryID:
        product = Product.objects.filter(sub_cetagory=cetagoryID).order_by('-id')
    elif brandID:
        product = Product.objects.filter(Brand=brandID).order_by('-id')
    else:
        product = Product.objects.all()

    return render(request,'product.html',{'pro':cetagory,'brand':brand,'duct':product})

def order_detail(reqeust,id):
    product=Product.objects.filter(id=id).first()
    return render(reqeust,'product_detail.html',{'product':product})
def search(request):
    query = request.GET.get('query','')

    product = Product.objects.filter(name__icontains=query)
    return render(request,'search.html',{'product':product})
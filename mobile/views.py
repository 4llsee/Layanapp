from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse,JsonResponse
from django.template import loader
from .models import Category,Products,Cart
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate,login
from django.contrib.auth.forms import UserCreationForm
from decimal import Decimal
from mobile.models import Cart , PaymentCard, Order, OrderItem
from django.db import transaction
from django.contrib import messages
from django.db.models import Q



def Welcome(request):
    return HttpResponse('أهلا بكم في دروس جانقو')

def auth_login(request):
    if request.method == "POST":
        username=request.POST.get("username")
        password=request.POST.get("password")

        user=authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
        return redirect("checkout")
    
    return render(request,"auth/auth_login.html")


@csrf_exempt


def auth_register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('auth_login')
    else:
            form = UserCreationForm()
    return render(request, 'auth/auth_register.html',{'form': form})





def Landpage(request):
    category=Category.objects.all()
    context={
        'data':category
    }
    return render(request,'landpage.html',context)

def Aboutus(request):
    template=loader.get_template('aboutus.html')
    return HttpResponse(template.render())

def blog(request):
    template=loader.get_template('blog.html')
    return HttpResponse(template.render())

def Getdata(request):
    data = {
        'name': 'أحمد',
        'age': 25, 
        'skills': ['python', 'Django', 'HTML']
        }
    return JsonResponse(data)

def datasend(request,name):
    return HttpResponse(name)

def Add(request,d1,d2):
    return HttpResponse(d1+d2)


def example(request, p1, p2, p12):
    return HttpResponse(p1 + " " + p2 + " " + p12)

def lastInvoice(request):
    template=loader.get_template('last.html')
    return HttpResponse(template.render())


def runindex(request):
    template=loader.get_template('index.html')
    return HttpResponse(template.render())

@login_required(login_url='auth_login')
def Checkout(request):
    cart=Cart.objects.select_related("product") .all()
    
    context={
        'cart':cart
    }
    return render(request,'checkout.html',context)

def GetphoneMenu(request):
    id=request.GET.get("id")
    Product=Products.objects.filter(category_id=id)
    context={
        "product":Product
    }
    

    return render(request,"phonemenu.html",context)

def Details(request):
    id=request.GET.get("id")
    Product=Products.objects.filter(id=id)
    context={
        "product":Product
    }
    return render(request, "details.html", context)


def invoice(request):
    if request.method=="POST":
        phone_id=request.POST.get("phone_id")
        full_name=request.POST.get("full_name")
        phone=request.POST.get("phone")
        Email=request.POST.get("Email")


        phone=[
        {
        "id":"0001",
        "name":"iphone 15",
        "brand":"Apple",
        "price":5400,
        "storage":"255GB",
        "color":"Gold",
        "image":"images/iphone15.jpg"
    },
    {
        "id":"0002",
        "name":"iphone 16",
        "brand":"Apple",
        "price":6200,
        "storage":"255GB",
        "color":"Blue",
        "image":"images/iphone16.jpg"
    },
    {
        "id":"0003",
        "name":"Galaxy s24 Ultra ",
        "brand":"Samsung",
        "price":3700,
        "storage":"255GB",
        "color":"Black",
        "image":"images/galaxy_s24.jpg"


    },

    {
        "id":"0004",
        "name":" pixel 8 pro",
        "brand":"Google",
        "price":6000,
        "storage":"255GB",
        "color":"gray",
        "image":"images/pixel8.jpg"
    },
    {
        "id":"0005",
        "name":" camera",
        "brand":"canon",
        "price":2800,
        "storage":"255GB",
        "color":"Black",
        "image":"images/Canon.jpg"
    },
    {
        "id":"0006",
        "name":" smart Pincel",
        "brand":"Apple",
        "price":400,
        "storage":"255GB",
        "color":"White",
        "image":"images/pincel.jpg"
    }
    
 ]
        phones=[p for p in phone if str(p["id"])== str(phone_id)]

        return render(request,"invoice.html",{
        "full_name":full_name,
        "phone":phone,
        "Email":Email,
        "product":phones
    })




def add_to_cart(request):
    product_id = request.GET.get("id")


    cart_item, created = Cart.objects.get_or_create(
        product_id=product_id,
        defaults={"quntity":1}
    )

    if not created:
        cart_item.quntity += 1
        cart_item.save()


    Product=Products.objects.filter(id=product_id)
    context={
        "product":Product
    }
    return render(request, "details.html", context)

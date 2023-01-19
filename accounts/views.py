from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import OrderForm, CreateUserForm, CustomerForm
from .filters import OrderFilter
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from .decorators import unauthenticated_user, allowed_users, admin_only
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json

# Create your views here.

def landing_page(request):
    context = {}
    return render(request, 'accounts/landing_page.html', context)

@unauthenticated_user
def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form  = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for' + username)
            return redirect('login')
            
    context = {'form':form}
    return render (request, 'accounts/register.html', context)

@unauthenticated_user
def loginPage(request):   
    if request.user.is_authenticated:
        return redirect('home')
    else: 
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            
            user = authenticate(request, username = username, password = password)
            
            if user is not None:
                login(request, user) #we used the view method as loginPage to avoid conflict with this django login method
                return redirect('home')
            else:
                messages.info(request, 'username or password isnt correct')
            
        context = {}
        return render (request, 'accounts/login.html', context)

@login_required(login_url = 'login')
@admin_only
def home(request):
    
    STATUS = ''
    
    orders = Order.objects.all().order_by('date_created').reverse() 
    #orders = orders.reverse()     
    #items = orders.orderitem_set.all()
    customers = Customer.objects.all()
    total_customers = customers.count()
    total_orders = orders.count()
    delivered  = orders.filter(status ='Delivered').count()
    pending = orders.filter(status ='Pending').count(   )
    context = {'orders':orders, 'total_customers': total_customers, 'customers':customers,
               'total_orders': total_orders, 'delivered':delivered, 
               'pending':pending, 'products': products}
    return render(request, "accounts/dashboard.html", context)

@login_required(login_url = 'login')
@allowed_users(allowed_roles = ['customer'])
def userPage(request):
    orders = request.user.customer.order_set.all()
    print ("ORDERS: ", orders)
    
    total_orders = orders.count()
    delivered = orders.filter(status = 'Delivered').count()
    pending = orders.filter(status = 'Pending').count()
    
    context = {'orders': orders,
               'total_orders': total_orders, 'delivered':delivered, 
               'pending':pending, }
    return render (request, 'accounts/user.html', context)

@login_required(login_url = 'login')
@allowed_users(allowed_roles = ['customer'])
def accountSettings(request):
    customer = request.user.customer
    form  = CustomerForm(instance = customer)
    
    if request.method == 'POST':
        form =  CustomerForm(request.POST, request.FILES, instance = customer)
        if form.is_valid():
            form.save()
        
    context = {'form':form}
    return render(request, 'accounts/account_settings.html', context)

@login_required(login_url = 'login')
@allowed_users(allowed_roles = ['admin'])
def products(request):
    products = Product.objects.all()
    return render(request, "accounts/products.html", {'products':products})

@login_required(login_url = 'login')
@allowed_users(allowed_roles = ['admin'])
def customer(request, pk_test):
    customer = Customer.objects.get(id = pk_test)
    orders = customer.order_set.all()
    orders_item = None

    order_count = orders.count()
    items = ''   
    
    myFilter = OrderFilter(request.GET, queryset = orders)
    orders = myFilter.qs
 
    context = {'customer': customer, 'orders': orders, 
               'order_count':order_count, 'myFilter': myFilter, 
               "items":items}
    return render(request, "accounts/customer.html", context)

def customerView(request, pk):
    print(request.user.id)
    orders = Order.objects.get(id = pk)
    items = orders.orderitem_set.all()
    
    contex = {'items': items}
    return render(request, 'accounts/customer_view.html', contex)

def logoutUser(request):
    logout(request)
    return redirect('login')
    
@login_required(login_url = 'login')
@allowed_users(allowed_roles = ['admin'])
def createOrder(request):
    form  = OrderForm()
    if request.method == 'POST':
        #print("Printing POST:", request.POST)
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
        
    context = {'form':form}
    return render(request, 'accounts/order_form.html', context)




@login_required(login_url = 'login')
@allowed_users(allowed_roles = ['admin'])
def updateOrder(request, pk):
    order = Order.objects.get(id = pk)
    form  = OrderForm(instance  = order)
    
    if request.method == 'POST':
        form  = OrderForm(request.POST, instance = order) #we have to the instace so we can save the new data
        if form.is_valid():
            form.save()
            return redirect("/")
    context = {'form':form}
    return render(request, 'accounts\order_form.html', context)

@login_required(login_url = 'login')
@allowed_users(allowed_roles = ['admin'])
def deleteOrder(request, pk):
    order = Order.objects.get(id = pk)   
    
    if request.method == 'POST':
        order.delete()
        return redirect('/')
    context = {'item':order}
    return render (request, 'accounts\delete.html', context)

@csrf_exempt
def orderProcessing(request):
    data = json.loads(request.body) 
    print(data)
    
    user  = request.user
    
    if user.is_authenticated:
        customer= Customer.objects.get(
            id = request.user.customer.id
             )
        customer.save()
        
        #items = order.orderitem_set_all()
        
        if request.user.is_authenticated:
            order = Order(customer = customer, status = 'Pending', complete = False)
            order.save();
            
            
            for i in data:
                products = StoreProduct.objects.get(id = data[i]['productId'])
                print(products)
                order_item = OrderItem(order = order, 
                                       products =products, 
                                       price = data[i]['price'], 
                                       quantity = data[i]['quantity'])
                order.complete = True
                order_item.save();
                order.save();
                print('it is done')
            return redirect("user-page")
                
    return JsonResponse('Item was addded', safe = False)
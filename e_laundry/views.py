from django.shortcuts import render, redirect
from django.http import HttpResponse,HttpResponseRedirect
from .models import Holder 
from django.contrib import messages
from .models import demo
from .models import item
from .models import orders
from django.contrib.auth import authenticate
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import login as auth_login


# Create your views here.

def index(request):
    login = demo.objects.all()
    return render(request, 'Login.html', {'Login' : login})
# above function is for demonstration

def register(request):
    if request.method == 'POST':
        email = request.POST['email']
        username = request.POST['name']
        phone = request.POST['phone']
        password = request.POST['password']
        re_password = request.POST['re_password']
        role = request.POST["role"]

        if password == re_password:
            if Holder.objects.filter(email=email).exists():
                messages.info(request, 'Email Already Exists')
                return redirect('register')
            elif Holder.objects.filter(username=username).exists():
                messages.info(request, 'Username Already Exists')
                return redirect('register')
            else:
                user = Holder.objects.create_user(username=username, email=email, password=password ,role=role ,phone=phone)
                user.save() 
                
                return redirect('login')
        else:
            messages.info(request, 'Password Not Matched')
            return redirect('register')
    else:
        return render(request, 'Registration.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(username=username, password=password)
        
        if user is not None :
            if user.role == 0:
                auth_login(request ,user)
                return redirect('home')
            elif user.role == 1:
                auth_login(request ,user)
                return redirect('seller_home')
            elif user.role == 2:
                auth_login(request ,user)
                return redirect('admin_home')
                
        else:
            messages.info(request,'Credential Invalid')
            return redirect('login')
    else:
        return render(request, 'Login.html')
    
def logout(request):
    auth_logout(request)
    return redirect('login')    

def home(request):
    if request.user.is_anonymous:
        return redirect('login')
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")

def service(request):
    return render(request, "services.html")

def order(request):
    return render(request, "order.html")

def admin_home(request):
    if request.user.is_anonymous:
        return redirect('login')
    return render(request, "admin_index.html")

def bill(request):
    return render(request, "bill.html")

def seller_home(request):
    if request.user.is_anonymous:
        return redirect('login')
    return render(request, "seller_index.html")

def items(request):
    if request.method == 'POST':
        item_name = request.POST['Item_name']
        item_price = request.POST['Item_price']
        
        additem = item(item_name = item_name , item_price = item_price)
        additem.save()
        
        return redirect('admin_home')
        
    else:
        return render(request, "Add_Item.html")
        
def get_order(request):
    if request.method == 'POST':
        num1 = int(request.POST['number1'])
        num2 = int(request.POST['number2'])
        num3 = int(request.POST['number3'])
        ph_num = request.user.phone
        username = request.user.username
        
        name_1 = item.objects.all()[0].item_name
        name_2 = item.objects.all()[1].item_name
        name_3 = item.objects.all()[2].item_name
        
        price_1 = int(item.objects.all()[0].item_price)
        price_2 = int(item.objects.all()[1].item_price)
        price_3 = int(item.objects.all()[2].item_price)
        
        in_price1 = num1*price_1
        in_price2 = num2*price_2
        in_price3 = num3*price_3
        
        total_quantity = num1+num2+num3
        total_price = in_price1+in_price2+in_price3
        
        if(total_quantity == 0):
            messages.info(request,'Select product for order place')
            return redirect('order')
        else:
            take_item = orders(username = username,  ph_num = ph_num , total_quantity =total_quantity , total_price = total_price)
            take_item.save()
    
            context = {'num1': num1 , 'num2' : num2 , 'num3' : num3,
                   'name_1' : name_1 , 'name_2' : name_2 , 'name_3' : name_3,
                   'in_price1' : in_price1 , 'in_price2' : in_price2 , 'in_price3' : in_price3,
                   'total_quantity' : total_quantity , 'total_price' : total_price} 
        
            return render(request, 'bill.html' , context)
    else:
        return render(request, "order.html")
            
def cus_order(request):
    order = orders.objects.all()
    return render(request, 'order_list.html', {'orders' : order})
    
def delete(request , id):
    order_data = orders.objects.get(id = id)
    order_data.delete()
    return redirect('order')
    
def order_compleate(request):
    user = request.user.username
    user_orders = orders.objects.all().filter(username = user)
    if len(user_orders) > 0: 
        return render(request, 'order_deliver.html', {'user_orders' : user_orders})
    else:
        messages.info(request,'No orders placed , please place order for view order detail')
        return render(request, 'order_deliver.html')   
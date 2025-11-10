from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import auth
from .models import Customuser



# Create your views here.

def ind(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def product(request):
    return render(request,'product.html')

def blog(request):
    return render(request,'blog.html')

def contact(request):
    return render(request,'contact.html')

def register(request):
    if request.method=='POST':
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        adress = request.POST.get('adress')
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        username = request.POST.get('username')
        if Customuser.objects.filter(username=username).exists():
            a="user already registerd"
            return render(request,'registration.html',{'a':a})
        data=Customuser.objects.create_user(first_name=firstname,last_name=lastname,email=email,phone=phone,adress=adress,users="farmer",password=password,username=username)
        data.save()
        return redirect('login')
    else:
        return render(request,'registration.html')
    
def register_user(request):
    if request.method=='POST':
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        adress = request.POST.get('adress')
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        username = request.POST.get('username')
        if Customuser.objects.filter(username=username).exists():
            a="user already registerd"
            return render(request,'registration.html',{'a':a})
        data=Customuser.objects.create_user(first_name=firstname,last_name=lastname,email=email,phone=phone,adress=adress,users="user",password=password,username=username)
        data.save()
        return redirect('login')
    else:
        return render(request,'register_user.html')
    
def Login(request):
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print("aaaa")
        user=authenticate(request,username=username,password=password)
        print(user)
        if user is not None and user.is_superuser==False:

            if user.users == "farmer":
                login(request,user)
                return redirect('farmer_home')
            if user.users == "user":
                login(request,user)
                return redirect('user')
            
        else:
            return render(request,'login1.html')
    else:
        return render(request,'login1.html')

def user(request):
    return render(request,'userhome.html')

def farmer_home(request):
    return render(request,'farmer_home.html')



# def profile(request):
#     a=User.objects.get(id=request.user.id)
#     return render(request,'profile.html',{'a':a})
def profile(request):
    return render(request, 'profile.html', {'a': request.user})


def Logout(request):
    auth.logout(request)
    return redirect('index')

def farmer_home(request):
    return render(request,'farmer_home.html')

def addproduct(request):
    return render(request,'Addproduct.html')

def farmer_products(request):
    return render(request,'farmer_products.html')

def farmer_orders(request):
    return render(request,'farmer_orders.html')

def farmer_profile(request):
    return render(request,'farmer_profile.html')

def farmer_wallet(request):
    return render(request,'farmer_wallet.html')
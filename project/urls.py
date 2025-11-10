"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.ind,name='index'),
    path('about',views.about,name='about'),
    path('product',views.product,name='product'),
    path('blog',views.blog,name='blog'),
    path('contact',views.contact,name='contact'),
    path('login',views.Login,name='login'),
    path('regist',views.register,name='regist'),
    path('register_user',views.register_user,name='register_user'),
    path('user',views.user,name='user'),
    path('farmer_home',views.farmer_home,name='farmer_home'),
    path('profile/',views.profile,name='profile'),
    path('logout',views.Logout,name='logout'),
    path('farmer_home',views.farmer_home,name='farmer_home'),
    path('addproduct',views.addproduct,name='addproduct'),
    path('farmer_products',views.farmer_products,name='farmer_products'),
    path('farmer_orders',views.farmer_orders,name='farmer_orders'),
    path('farmer_profile',views.farmer_profile,name='farmer_profile'),
    path('farmer_wallet',views.farmer_wallet,name='farmer_wallet'),
]

if settings.DEBUG:
  urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
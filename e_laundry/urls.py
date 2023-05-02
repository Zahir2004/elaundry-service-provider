from django.urls import path
from . import views 
urlpatterns = [
    path('', views.index, name='index'), 
#    for demonstation
    path('register', views.register, name='register'), 
    path('login', views.login, name='login'),
    path('logout', views.logout , name='logout'),
    path('home', views.home, name='home'),
    path('about', views.about, name='about'),
    path('service', views.service, name='service'),
    path('order', views.order, name='order'),
    path('items', views.items, name='items'),
    path('admin_home', views.admin_home, name='admin_home'),
    path('get_order', views.get_order, name='get_order'),
    path('bill' , views.bill, name='bill'),
    path('cus_order' , views.cus_order , name='cus_order'),
    path('seller_home' , views.seller_home , name='seller_home'),
    path('order_compleate' , views.order_compleate , name="order_compleate"),
    path('delete/<int:id>' , views.delete , name="delete"),
    # path('your_order' , views.your_order , name="your_order"),
]
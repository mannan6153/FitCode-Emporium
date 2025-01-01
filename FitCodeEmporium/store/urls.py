from django.urls import path
from . import views

urlpatterns = [
    path('', views.landingpage, name='home'),
    path('shop/', views.shop, name='shop'),
    path('blog/', views.blog, name='blog'),
    path('blogpage/', views.blogpage, name='blogpage'),
    path('contactus/', views.contactus, name='contactus'),  
    path('login/', views.login, name='login'),
    path('join/', views.register, name='join_us'),
    path('cart/', views.cart, name='cart'),
    path('profile/', views.profile, name='profile'),
    path('feedback/', views.feedback, name='feedback'),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('register/', views.register, name='register'),
]

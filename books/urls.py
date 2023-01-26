from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('login/', views.loginpage, name="login"),
    path('register/', views.register, name="register"),
    path('product/', views.product, name="product"),
    path('customer/', views.customer, name="customer"),
    path('form/', views.createstudent, name="form"),
    path('update/', views.update, name="update"),
    path('logout/', views.logoutpage, name="logout"),
    path('user/', views.Userpage, name="user"),



]

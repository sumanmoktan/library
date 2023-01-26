from django.shortcuts import render, redirect
from .models import *
from .forms import StudentForm, CreateUserForm
from django.contrib.auth.forms import UserCreationForm

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# Create your views here.
def loginpage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'username or password incorrect')
        context = {}
        return render(request, 'books/login.html', context)


def logoutpage(request):
    logout(request)
    return redirect('login')


def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        forms = CreateUserForm()
        if request.method == 'POST':
            forms = CreateUserForm(request.POST)
            if forms.is_valid():
                forms.save()
                user = forms.cleaned_data.get('username')
                messages.success(request, 'Account was created for' + user)
                return redirect("login")

        context = {'forms': forms}
        return render(request, 'books/register.html', context)


@login_required(login_url='login')
def home(request):
    products = Student.objects.all()
    return render(request, 'books/Dashboard.html', {'products': products})


def product(request):
    products = Student.objects.all()
    context = {'products': products}
    return render(request, 'books/product.html', context)


def customer(request):
    return render(request, 'books/customer.html')


def createstudent(request):
    forms = StudentForm()
    if request.method == 'POST':
        forms = StudentForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect("product")

    context = {'forms': forms}
    return render(request, 'books/student_form.html', context)


def update(request, pk):
    forms = StudentForm()
    # std = Student.objects.get(id=pk)
    context = {'forms': forms}
    return render(request, 'books/student_form.html', context)


def Userpage(request):
    context = {}
    return render(request, 'books/user.html', context)

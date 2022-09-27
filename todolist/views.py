from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from todolist.models import Task
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
@login_required(login_url='/todolist/login/')
def show_todolist(request):
    data_todolist = Task.objects.filter(user=request.user)
    context = {
    'list_todolist' : data_todolist,
    'username' :  request.user.username,
    'last_login': request.COOKIES['last_login'],
    }
    return render(request, "todolist.html", context)

# REGISTER
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)

# LOGIN
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)                                                    # Melakukan login terlebih dahulu
            response = HttpResponseRedirect(reverse("todolist:show_todolist"))      # Membuat response
            response.set_cookie('last_login', str(datetime.datetime.now()))         # Membuat cookie last_login dan menambahkannya ke dalam response
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

# LOGOUT
def logout_user(request):
    logout(request)
    return redirect('todolist:login')


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
    response = HttpResponseRedirect(reverse('todolist:login'))
    response.delete_cookie('last_login')
    return redirect('todolist:login')

# CREATE TASK
def create_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        date = datetime.datetime.now()
        user = request.user
        is_finished = False
        Task.objects.create(title=title, description=description, date=date, user=user, is_finished=is_finished)
        response = HttpResponseRedirect(reverse("todolist:show_todolist")) 
        return response

    return render(request, "create.html")

# DELETE
def delete(request, pk):
    Task.objects.filter(id=pk).delete()
    return redirect('todolist:show_todolist')

# OPTIONS
def options(request, pk):
    data = Task.objects.get(id=pk)
    data.is_finished = not(data.is_finished)
    data.save()
    return redirect('todolist:show_todolist')


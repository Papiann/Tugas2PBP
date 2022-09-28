from django.urls import path
from todolist.views import show_todolist, register, login_user, logout_user, create_task, delete, options

app_name = 'todolist'

urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('create/', create_task, name='create'),
    path('delete/<int:pk>', delete, name='delete'),
    path('options/<int:pk>', options, name='options'),
]
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from .models import Post, Wanted
from . forms import UserCreateForm, PostForm, WantedForm, LoginForm


# Create your views here.
class Create_account(CreateView):
    def post(self, request, *args, **kwargs):
        form = UserCreateForm(data=request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/')
        return render(request, 'signup.html', {'form': form,})
    def get(self, request, *args, **kwargs):
        form = UserCreateForm(request.POST)
        return render(request, 'signup.html', {'form':form,})
create_account = Create_account.as_view()

class Account_Login(LoginView):
    def post(self, request, *args, **kwargs):
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            user = User.objects.get(username=username)
            login(request, user)
            return redirect(to='/top')
        return render(request, 'signin.html', {'form': form,})
    def get(self, request, *arg, **kwargs):
        form = LoginForm(request.POST)
        return render(request, 'signin.html', {'form': form,})
account_login = Account_Login.as_view()

def index(request):
    params ={
        'title':'Welcome to Close Cloth!!'
    }
    return render(request, 'clothes/index.html', params)

def top(request):
    data = Post.objects.order_by('buying_date').first()
    params = {
        'title': 'all cloth',
        'data': data,
    }
    return render(request, 'clothes/index/top.html')

def detail(request):
    data = Post.objects.all()
    params = {
        'title': 'cloth detail',
        'data': data,
    }
    return render(request, 'clothes/index/detail.html')

def post(request):
    params = {
        'title': 'Post new cloth',
        'form': PostForm(), 
    }
    if request.method == 'POST':
        name = request.POST['cloth_name']
        info = request.POST['cloth_info']
        brand_name = request.POST['brand_name']
        season = request.POST['season']
        cloth_size = request.POST['cloth_size']
        material = request.POST['material']
        price = request.POST['price']
        buying_place = request.POST['buying_place']
        buying_date = request.POST['buying_date']
        post_images = request.POST['post_images']
        post = Post(cloth_name=name, cloth_info=info, brand_name=brand_name, season=season, cloth_size=cloth_size,\
            material=material, price=price, buying_place=buying_place, post_images=post_images)
        post.save()
        return redirect(to='/top')
    return render(request, 'clothes/index/top.html', params)

def edit(request, num):
    obj = Post.objects.get(id=num)
    if request.method == 'POST':
        post = PostForm(request.POST, instance=obj)
        post.save()
        return redirect(to='/top')
    params = {
        'title': 'Edit',
        'id': num,
        'form': PostForm(instance=obj),
    }
    return render(request, 'clothes/index/top/edit.html', params)

def delete(request, num):
    post = Post.objects.get(id=num)
    if request.method == 'POST':
        post.delete()
        return redirect(to='/top')
    params = {
        'title': 'Delete',
        'id': num,
        'obj': post,
    }
    return render(request, 'clothes/index/top/delete.html', params)




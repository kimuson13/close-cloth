from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView, LogoutView
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from .models import Post, Wanted
from . forms import UserCreateForm, PostForm, WantedForm, LoginForm, FindForm


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
            return redirect('/clothes')
        return render(request, 'clothes/signup.html', {'form': form,})
    def get(self, request, *args, **kwargs):
        form = UserCreateForm(request.POST)
        return render(request, 'clothes/signup.html', {'form':form,})

class Account_Login(LoginView):
    def post(self, request, *args, **kwargs):
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            user = User.objects.get(username=username)
            login(request, user)
            return redirect(to='/clothes/top')
        return render(request, 'clothes/signin.html', {'form': form,})
    def get(self, request, *arg, **kwargs):
        form = LoginForm(request.POST)
        return render(request, 'clothes/signin.html', {'form': form,})

def logout(LogoutView):
    return

def index(request):
    params ={
        'title':'Welcome to Close Cloth!!'
    }
    return render(request, 'clothes/index.html', params)

@login_required(login_url='/signin/')
def top(request):
    data = Post.objects.order_by('buying_date')
    user = request.user
    price = Post.objects.filter(owner=user).values_list('price', flat=True)
    sum_price = sum(price)
    params = {
        'title': 'all cloth',
        'data': data,
        'sum_price': sum_price,
        'login_user': user,
    }
    return render(request, 'clothes/top.html', params)

@login_required(login_url='/signin/')
def detail(request, num):
    user = request.user
    data = Post.objects.filter(owner=user).get(id=num)
    params = {
        'title': 'cloth detail',
        'data': data,
        'num': num,
        'login_user': user,
        
    }
    return render(request, 'clothes/detail.html', params)

@login_required(login_url='/signin/')
def post(request):
    user = request.user
    params = {
        'title': 'Post new cloth',
        'form': PostForm(), 
        'login_user': user,
    }
    if request.method == 'POST':
        owner = user
        name = request.POST['cloth_name']
        info = request.POST['item_info']
        brand_name = request.POST['brand_name']
        season = request.POST['season']
        cloth_size = request.POST['cloth_size']
        material = request.POST['material']
        price = request.POST['price']
        buying_place = request.POST['buying_place']
        buying_date = request.POST['buying_date']
        post_images = request.FILES['post_images']
        post = Post(owner=owner,cloth_name=name, item_info=info, brand_name=brand_name, season=season, cloth_size=cloth_size,\
            material=material, price=price, buying_place=buying_place, buying_date=buying_date, post_images=post_images)
        post.save()
        return redirect(to='/clothes/top')
    return render(request, 'clothes/post.html', params)

@login_required(login_url='/signin/')
def edit(request, num):
    obj = Post.objects.get(id=num)
    user = request.user
    if request.method == 'POST':
        post = PostForm(request.POST, request.FILES, instance=obj)
        post.save()
        return redirect(to='/clothes/top')
    params = {
        'title': 'Edit',
        'obj': obj,
        'id': num,
        'form': PostForm(instance=obj),
        'login_user': user,
    }
    return render(request, 'clothes/edit.html', params)

@login_required(login_url='/signin/')
def delete(request, num):
    post = Post.objects.get(id=num)
    user = request.user
    if request.method == 'POST':
        post.delete()
        return redirect(to='/clothes/top')
    params = {
        'title': 'Delete',
        'id': num,
        'obj': post,
        'login_user': user,
    }
    return render(request, 'clothes/delete.html', params)

@login_required(login_url='/signin/')
def search(request):
    user = request.user
    if request.method == 'POST':
        form = FindForm(request.POST)
        find = request.POST['find']
        data = Post.objects.filter(brand_name__icontains=find, owner=user)
        msg = 'Result:' + str(data.count())
        price = Post.objects.filter(brand_name__icontains=find, owner=user).values_list('price', flat=True)
        sum_price = sum(price)
    else:
        msg = 'Search words...'
        form = FindForm()
        data = Post.objects.filter(owner=user)
        price = Post.objects.filter(owner=user).values_list('price', flat=True)
        sum_price = sum(price)
    params = {
        'title':'Search some cloth',
        'message': msg,
        'form': form,
        'data': data,
        'sum_price': sum_price,
        'login_user': user,
    }
    return render(request, 'clothes/search.html', params)

@login_required(login_url='/signin/')
def wishlist(request):
    user = request.user
    data = Wanted.objects.filter(owner=user)
    price = Wanted.objects.filter(owner=user).values_list('wanted_price', flat=True)
    sum_price = sum(price)
    params = {
        'title': 'wishlist',
        'data': data,
        'sum_price':sum_price,
        'login_user': user,
    }
    return render(request, 'clothes/wishlist.html')

@login_required(login_url='/signin/')
def wishlist_add(request):
    user = request.user
    params = {
        'title': 'Add wishlist',
        'form': WantedForm(request.POST, request.FILES),
        'login_user': user,
    }
    if request.method == 'POST':
        owner = user
        name = request.POST['wanted_cloth_name']
        brand_name = request.POST['wanted_brand_name']
        season = request.POST['wanted_season']
        price = request.POST['wanted_price']
        priority = request.POST['priority']
        images = request.FILES['wanted_images']
        wanted = Wanted(wanted_cloth_name=name, wanted_brand_name=brand_name, wanted_season=season, \
            wanted_price=price, priority=priority, wanted_images=images)
        wanted.save()
        return redirect(to='/wishlist')
    return render(request, 'clothes/wishlist_add.html', params)

@login_required(login_url='/signin/')
def wishlist_edit(request, num):
    user = request.user
    obj = Wanted.objects.get(id=num)
    if request.method == 'POST':
        wanted = WantedForm(request.POST, request.FILES, instance=obj)
        wanted.save()
        return redirect(to='/wishlist')
    params = {
        'title': 'wishlist_edit',
        'id': num,
        'form': WantedForm(instance=obj),
        'login_user': user,
    }
    return render(request, 'clothes/wishlist_edit.html', params)

@login_required(login_url='/signin/')
def wishlist_delete(request, num):
    user = request.user
    wanted = Wanted.objects.get(id=num)
    if request.method == 'POST':
        wanted.delete()
        return redirect(to='/wishlist')
    params = {
        'title': 'wishlist_delete',
        'id': num,
        'obj': wanted,
        'login_user': user,
    }
    return render(request, 'clothes/wishlist_delete.html', params)



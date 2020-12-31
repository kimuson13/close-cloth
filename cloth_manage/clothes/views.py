from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
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
            return redirect('/')
        return render(request, 'signup.html', {'form': form,})
    def get(self, request, *args, **kwargs):
        form = UserCreateForm(request.POST)
        return render(request, 'signup.html', {'form':form,})

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

def logout_view(request):
    logout(request)

def index(request):
    params ={
        'title':'Welcome to Close Cloth!!'
    }
    return render(request, 'clothes/index.html', params)

@login_required(login_url='/signin/')
def top(request):
    data = Post.objects.order_by('buying_date').first()
    params = {
        'title': 'all cloth',
        'data': data,
        'sum_price': sum(Post.objects.value_list('price'))
    }
    return render(request, 'clothes/index/top.html')

@login_required(login_url='/signin/')
def detail(request, num):
    data = Post.objects.get(id=num)
    params = {
        'title': 'cloth detail',
        'data': data,
        'num': num,
    }
    return render(request, 'clothes/index/detail.html')

@login_required(login_url='/signin/')
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

@login_required(login_url='/signin/')
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

@login_required(login_url='/signin/')
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

@login_required(login_url='/signin/')
def search(request):
    if request.method == 'POST':
        form = FindForm(request.POST)
        find = request.POST['find']
        data = Post.objects.filter(brand_name__icontains=find)
        msg = 'Result:' + str(data.count())
        sum_price = sum(data.value_list('price'))
    else:
        msg = 'Search words...'
        form = FindForm()
        data = Post.objects.all()
        sum_price = sum(data.value_list('price'))
    params = {
        'title':'Search some cloth',
        'message': msg,
        'form': form,
        'data': data,
        'sum_price': sum_price,
    }
    return render(request, 'clothes/top/search.html')

@login_required(login_url='/signin/')
def wishlist(request):
    data = Wanted.objects.all()
    params = {
        'title': 'wishlist',
        'data': data,
        'sum_price':Wanted.objects.value_list('price')
    }
    return render(request, 'clothes/index/top/wishlist.html')

@login_required(login_url='/signin/')
def wishlist_add(request):
    params = {
        'title': 'Add wishlist',
        'form': WantedForm(),
    }
    if request.method == 'POST':
        name = request.POST['wanted_cloth_name']
        brand_name = request.POST['wanted_brand_name']
        season = request.POST['wanted_season']
        price = request.POST['wanted_price']
        priority = request.POST['priority']
        images = request.POST['wanted_images']
        wanted = Wanted(wanted_cloth_name=name, wanted_brand_name=brand_name, wanted_season=season, \
            wanted_price=price, priority=priority, wanted_images=images)
        wanted.save()
        return redirect(to='/wishlist')
    return render(request, 'clothes/index/top/wishlist/wishlist_add.html', params)

@login_required(login_url='/signin/')
def wishlist_edit(request, num):
    obj = Wanted.objects.get(id=num)
    if request.method == 'POST':
        wanted = WantedForm(request.POST, instance=obj)
        wanted.save()
        return redirect(to='/wishlist')
    params = {
        'title': 'wishlist_edit',
        'id': num,
        'form': WantedForm(instance=obj)
    }
    return render(request, 'clothes/index/top/wishlist/wishlist_edit.html', params)

@login_required(login_url='/signin/')
def wishlist_delete(request, num):
    wanted = Wanted.objects.get(id=num)
    if request.method == 'POST':
        wanted.delete()
        return redirect(to='/wishlist')
    params = {
        'title': 'wishlist_delete',
        'id': num,
        'obj': wanted
    }
    return render(request, 'clothes/index/top/wishlist/wishlist_delete.html', params)



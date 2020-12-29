from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.views.generic import CreateView
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

class Account_Login(View):
    def post(self, request, *args, **kwargs):
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            user = User.objects.get(username=username)
            login(request, user)
            return redirect(to='/top/')
        return render(request, 'signin.html', {'form': form,})
    def get(self, request, *arg, **kwargs):
        form = LoginForm(request.POST)
        return render(request, 'signin.html', {'form': form,})
account_login = Account_Login.as_view()


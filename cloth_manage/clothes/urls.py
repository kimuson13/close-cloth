from django.urls import path
from . import views
from .views import Create_account, Account_Login

urlpatterns = [
    path('', views.index, name='index'),
    path('signup', Create_account.as_view(), name='signup'),
    path('signin', Account_Login.as_view(), name='signin'),
    path('top/<int:num>', views.top, name='top'),
    path('detail', views.top, name='detail'),
    path('post', views.post, name='post'),
    path('edit/<int:num>', views.edit, name='edit'),
    path('delete/<int:num>', views.delete, name='delete'),
    path('search', views.search, name='search'),
    path('wishlist', views.wishlist, name='wishlist'),
    path('wishlist_add', views.wishlist_add, name='wishlist_add'),
    path('wishlist_edit/<int:num>', views.wishlist_edit, name='wishlist_edit'),
    path('wishlist_delete/<int:num>', views.wishlist_delete, name='wishlist_delete'),
    path('logout', views.logout_view, {'template_name': 'index.html'}, name='logout'),
]
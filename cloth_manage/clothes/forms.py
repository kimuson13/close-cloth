from django import forms
from .models import Post, Wanted
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
import bootstrap_datepicker_plus as datetimepicker
from django.contrib.auth.forms import AuthenticationForm

ITEM_CHOICES = [
    (1, 'Tops'),
    (2, 'Pants'),
    (3, 'Outers'),
    (4, 'SetUp'),
    (5, 'Coats'),
    (6, 'Shoes'),
    (7, 'Accessories'),
    (8, 'Belts'),
    (9, 'Bags'),
    (10, 'Others')
]

class UserCreateForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('cloth_name', 'item_info', 'brand_name', 'season', 'cloth_size', 'material', 'price', 'buying_place', 'buying_date', 'post_images')
        widgets = {
            'buying_date': datetimepicker.DatePickerInput(
                format='%Y-%m-%d',
                options={
                    'locale': 'ja',
                    'dayViewHeaderFormat': 'YYYY年 MMMM',
                }
            )
        }

class WantedForm(forms.ModelForm):
    class Meta:
        model = Wanted
        fields = ('owner', 'wanted_cloth_name', 'wanted_brand_name', 'wanted_season', 'wanted_price', 'priority', 'wanted_images')

class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['class'] = 'form-control'

class FindForm(forms.Form):
    item_info = forms.ChoiceField(choices=ITEM_CHOICES, required='False')
    brand_name = forms.CharField(label='ブランドを絞り込む', required='False', widget=forms.TextInput(attrs={'class':'form-control'}))
    buying_place = forms.CharField(label='購入場所を絞り込む', required='False', widget=forms.TextInput(attrs={'class':'form-control'}))
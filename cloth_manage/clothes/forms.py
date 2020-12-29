from django import forms
from .models import Post, Wanted
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
import bootstrap_datepicker_plus as datetimepicker
from django.contrib.auth.forms import AuthenticationForm

ITEM_CHOICES = [
    ('one', 'Tops'),
    ('two', 'Pants'),
    ('three', 'Outers'),
    ('four', 'SetUp'),
    ('five', 'Coats'),
    ('six', 'Shoes'),
    ('seven', 'Accessories'),
    ('eight', 'Belts'),
    ('nine', 'Bags'),
    ('ten', 'Others')
]

PRIORITY_CHOICES = [
    ('one', 'Priority_1'),
    ('two', 'Priority_2'),
    ('three', 'Priority_3'),
    ('four', 'Priority_4'),
    ('five', 'Priority_5')
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
        fields = ('owner', 'cloth_name', 'item_info', 'brand_name', 'season', 'cloth_size', 'material', 'price', 'buying_place', 'buying_date', 'post_images')
        widgets = {
            'item_info': forms.ChoiceField(choices=ITEM_CHOICES),
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
        widgets = {
            'priority': forms.ChoiceField(choices=PRIORITY_CHOICES)
        }

class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['class'] = 'form-control'

class FindForm(forms.Form):
    find = forms.CharField(label="検索", required=False, \
        widget=forms.TextInput(attrs={'class':'form-control'}))
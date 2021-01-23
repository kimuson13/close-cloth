from django import forms
from .models import Post, Wanted
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
import bootstrap_datepicker_plus as datetimepicker
from django.contrib.auth.forms import AuthenticationForm

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
        labels = {
            'cloth_name':'名称',
            'item_info':'種類',
            'brand_name':'ブランド名',
            'season':'シーズン',
            'cloth_size':'サイズ',
            'material':'素材',
            'price':'値段',
            'buying_place':'購入場所',
            'buying_date':'購入日時',
            'post_images':'服の写真',
        }

class WantedForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(WantedForm, self).__init__(*args, **kwargs)
        self.fields["wanted_price"].required = False
    class Meta:
        model = Wanted
        fields = ('wanted_cloth_name', 'wanted_brand_name', 'wanted_season', 'wanted_price', 'priority', 'wanted_images')
        labels = {
            'wanted_cloth_name':'名称',
            'wanted_brand_name':'ブランド名',
            'wanted_season':'シーズン',
            'wanted_price':'予想価格',
            'priority':'優先度',
            'wanted_images':'服の写真',
        }

class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['class'] = 'form-control'

class NameSearchForm(forms.Form):
    search = forms.CharField(label="ブランド名か購入場所、アイテムの種類を入力", required=True, \
        widget=forms.TextInput(attrs={'class':'form-control'}))
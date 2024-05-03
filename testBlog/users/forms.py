from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(
        label='Введите Email', 
        required=True, 
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'})
        )
    
    username = forms.CharField(
        label='Введите логин', 
        required=True, 
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Логин'}), 
        help_text='Нельзя вводить символы: @/./+/-/_')
    
    password1 = forms.CharField(
        label='Введите пароль', 
        required=True, 
        help_text='Пароль не должен быть меньше 8 символов', 
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Пароль'}),
        )
    
    password2 = forms.CharField(
        label='Подтвердите пароль', 
        required=True, 
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Подтвердите пароль'}),
        )

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class UserUpdateForm(forms.ModelForm):
    
    email = forms.EmailField(
        label='Введите Email', 
        required=True, 
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'})
        )
    
    username = forms.CharField(
        label='Введите логин', 
        required=True, 
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Логин'}), 
        help_text='Нельзя вводить символы: @/./+/-/_')
    
    class Meta:
        model = User
        fields = ["username", "email"]


class ProfileImageForm(forms.ModelForm):
    img = forms.ImageField(
        label = 'Изображение профиля',
        required = False,
        widget=forms.FileInput
    )
    
    class Meta:
        model = Profile
        fields = ["img"]
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

class UserForm(UserCreationForm):
    email = forms.EmailField(label='이메일')

    class Meta:
        model = get_user_model()
        fields = ['username', 'password1', 'password2', 'email'] # 사용자 이름, 비밀번호, 비밀번호대조값, 이메일주소

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ['username', 'first_name', 'last_name', 'email']
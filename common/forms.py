from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserForm(UserCreationForm):
    email = forms.EmailField(label='이메일')

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'email'] # 사용자 이름, 비밀번호, 비밀번호대조값, 이메일주소


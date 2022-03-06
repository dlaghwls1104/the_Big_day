from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout, get_user_model
from common.forms import UserForm, CustomUserChangeForm
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST

def signup(request):
    """
    계정생성
    """
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)  # 사용자 인증
            login(request, user)  # 로그인
            return redirect('qnaindex')
    else:
        form = UserForm()
    return render(request, 'common/signup.html', {'form': form})

def detail(request, username):
    User = get_user_model()
    user = get_object_or_404(User, username=username)
    context = {
        'user': user
    }
    return render(request, 'common/detail.html', context)

@login_required(login_url='common:login')
def update(request, username):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('common:detail', request.user.username)
    else:
        form = CustomUserChangeForm(instance = request.user)
        return render(request, 'common/update.html', {'form':form})


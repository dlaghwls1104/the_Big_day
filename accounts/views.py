from django.shortcuts import render, redirect
from django.contrib.auth import login as user_login
from django.contrib.auth.forms import UserCreationForm
# Django 프레임워크가 구현해 놓은 회원가입 폼을 import 한다.
from .forms import CustomUserCreationForm

def signup(request): # urls.py에 views.signup이 이 함수를 가리킨다.
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid(): # 회원가입 폼에서 적어 보낸 요청이 유효한지 검사한다.
            user = form.save() # 유효한 내용이면 이 회원 정보를 데이터베이스에 저장한다. 그 유저 정보를 리턴한다.
            user_login(request, user) # 유저 정보를 이용해 로그인한다.
        return redirect('accounts:signup')
    	# redirect 시 urls.py의 <app_name>:<name>으로 요청을 보낸다.
    else:
        form = CustomUserCreationForm() # 비어있는 회원가입 폼을 생성한다.
        return render(request, 'accounts/form.html', {'form': form})
    	# forms.html 파일을 렌더한다. 이때 위에서 생성한 회원가입 폼을 'form'이라는 이름으로 함께 보낸다.(딕셔너리)

# def login(request):
#     if request.method == 'POST':
#         form = AuthenticationForm(request, request.POST)
#         # 회원가입과 다르게 맨 앞의 인자로 request가 들어간다.
#         if form.is_valid():
#             user_login(request, form.get_user())
#             return redirect('posts:index')
#         return redirect('accounts:login')
#     else:
#         form = AuthenticationForm()
#         return render(request, 'accounts/form.html', {'form': form})

# def logout(request):
#     user_logout(request)
#     return redirect('posts:index')

def people(request, username): # urls.py에서 넘겨준 인자를 username으로 받는다.
    person = get_object_or_404(get_user_model(), username=username)
    context = {'person': person}
    return render(request, 'accounts/people.html', context)

def profile(request):
    if request.method == 'POST':
        user_change_form = CustomUserChangeForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if user_change_form.is_valid() and profile_form.is_valid():
            user = user_change_form.save()
            profile_form.save()
            return redirect('people', user.username)
        return redirect('accounts:profile')
    else:
        user_change_form = CustomUserChangeForm(instance=request.user)
        # 새롭게 추가하는 것이 아니라 수정하는 것이기 때문에
        # 기존의 정보를 가져오기 위해 instance를 지정해야 한다.
        profile, create = Profile.objects.get_or_create(user=request.user)
        # Profile 모델은 User 모델과 1:1 매칭이 되어있지만
        # User 모델에 새로운 인스턴스가 생성된다고 해서 그에 매칭되는 Profile 인스턴스가 생성되는 것은 아니기 때문에
        # 매칭되는 Profile 인스턴스가 있다면 그것을 가져오고, 아니면 새로 생성하도록 한다.
        profile_form = ProfileForm(instance=profile)
        return render(request, 'accounts/profile.html', {
            'user_change_form': user_change_form,
            'profile_form': profile_form
        })
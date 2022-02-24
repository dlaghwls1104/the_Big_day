from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

app_name = "accounts"
# view나 template에서 해당 이름을 이용해 url에 요청을 보낼 수 있다.

urlpatterns = [
    path('signup/', views.signup, name="signup"),
    # "<내 URL>/accounts/signup/" 주소로 요청이 오면 views.py 안에 signup이라는 함수를 찾아 실행한다.
    path('login/', auth_views.LoginView.as_view(), name="login"),
    path('logout/', auth_views.LogoutView.as_view(), name="logout"),
    path('signup/', views.signup, name="signup"),
    # path('profile/', views.profile, name="profile"),
]
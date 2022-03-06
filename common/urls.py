from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name ='common'

urlpatterns =[
    path('login/', auth_views.LoginView.as_view(template_name='common/login.html'), name= 'login'), # django 에서 제공하는 기본 로그인 뷰 사용
    path('logout/', auth_views.LogoutView.as_view(), name= 'logout'), 
    path('signup/', views.signup, name='signup'),
    path('<str:username>/', views.detail, name='detail'),
    path('update/<str:username>/', views.update, name='update'),
    path('delete/<str:username>/', views.update, name='delete'),
]
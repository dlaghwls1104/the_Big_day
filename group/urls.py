from django.urls import path,include

from . import views

app_name = 'group'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:recruit_id>/', views.detail, name='detail'),
    path('answer/create/<int:recruit_id>/', views.answer_create, name='answer_create'),
    path('recruit/create/', views.recruit_create, name='recruit_create'),
]
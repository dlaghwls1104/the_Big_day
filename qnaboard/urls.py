from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

app_name = "qnaboard"
# url name space = view나 template에서 해당 이름을 이용해 url에 요청을 보낼 수 있다.
# {% url 'qnaboard:detail' question.id %} < --- html에서 표현방식 

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('answer/create/<int:question_id>/', views.answer_create, name='answer_create'),
    path('question/create/', views.question_create, name='question_create'),
]
# URL링크의 구조가 변경되어도 링크 주소를 매핑하여 별칭을 사용할 수 있도록 하기 위해 name = 을 사용한다.
# html에서 {% url 'detail' question.id %} <-- url 'name' 을 입력해주면된다.
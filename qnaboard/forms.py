# 페이지에 요청시 전달되는 파라미터를 쉽게 관리하기 위한 클래스
# 폼은 필수 파라미터의 값이 누락되지 않았는지, 파라미터의 형식은 적절한지를 검증하는 목적으로 사용한다.
# 이외에도 HTML 자동 생성 또는 모델을 이용한 데이터 저장도 가능하다

from django import forms
from qnaboard.models import Question, Answer

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question # 사용할 모델
        fields = ['subject', 'content'] # QuestionForm 에서 사용할 Question 모델의 속성
        labels = {
            'subject':'제목',
            'content':'내용',
        }

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['content']
        labels = {
            'content': '답변내용',
        }
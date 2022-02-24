from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.utils import timezone
from qnaboard.models import Question
from django import forms
from .forms import Question, QuestionForm, AnswerForm

def index(request):
    """
    질문리스트 출력
    """
    question_List = Question.objects.order_by('-create_date')
    context = {'question_list': question_List
    }
    return render(request, 'qnaboard/question_list.html', context)

def detail(request, question_id):
    """
    질문내용 출력
    """
    question= get_object_or_404(Question, pk=question_id) # 해당 질문이 없으면 404 출력
    context = {'question': question}
    return render(request, 'qnaboard/question_detail.html', context)

def answer_create(request, question_id):
    """
    답변등록
    """
    question = get_object_or_404(Question, pk=question_id)
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.create_date = timezone.now()
            answer.question = question
            answer.save()
            return redirect('qnaboard:detail', question_id=question.id)
    else:
        form = AnswerForm()
    context = {'question': question, 'form': form}
    return render(request, 'qnaboard/question_detail.html', context) 


def question_create(request):
    """
    질문등록
    """
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.create_date = timezone.now()
            question.save()
            return redirect('qnaboard:index')
    else:
        form = QuestionForm()
    context = {'form': form}
    return render(request, 'qnaboard/question_form.html', context)

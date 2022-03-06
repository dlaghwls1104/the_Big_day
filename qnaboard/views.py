from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Question, Answer
from .forms import QuestionForm, AnswerForm
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
# Create your views here.

def qnaindex(request):
    """
    pybo 목록 출력
    """
    #입력파라미터
    page = request.GET.get('page','1')

    #조회
    question_list = Question.objects.order_by('-create_date')

    #페이징 처리
    paginator = Paginator(question_list, 10)
    page_obj = paginator.get_page(page)

    context = {'question_list': page_obj}
    
    return render(request, 'qnaboard/question_list.html', context)

def detail(request, question_id):
    """
    pybo 내용 출력
    """
    question = Question.objects.get(id=question_id)
    context = {'question': question}
    return render(request, 'qnaboard/question_detail.html', context)

@login_required(login_url='common:login') # 로그인을 어노테이션 - 로그인 상태에서 작동되게
def answer_create(request, question_id):
    """
    pybo 답변 등록
    """
    #answer_create함수의 매개변수를 URL 매핑으로 전달
    question = get_object_or_404(Question, pk=question_id)

    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.author = request.user # author 속성에 로그인 계정을 저장
            answer.create_date = timezone.now()
            answer.question = question
            answer.save()
            return redirect('qnaboard:detail', question_id=question.id)
    else:
        form = AnswerForm()
    context = {'question': question, 'form': form}
    return render(request, 'qnaboard/question_detail.html', context)  

@login_required(login_url='common:login') # 로그인을 어노테이션 - 로그인 상태에서 작동되게
def question_create(request):
    """
    pybo 질문등록
    """
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            # 데이터베이스에 저장하기 전에 commit=False는 임시저장, date를 생성하기 위해 잠시 기다리는 중
            question = form.save(commit=False)
            question.author = request.user
            question.create_date = timezone.now()
            question.save()
            # 저장이 끝나면 index(질문목록) 화면으로 돌아간다.
            return redirect('qnaboard:qnaindex')
    else:
        form = QuestionForm()
    context = {'form': form}
    return render(request, 'qnaboard/question_form.html', context)

@login_required(login_url='common:login') # 로그인을 어노테이션 - 로그인 상태에서 작동되게
def question_modify(request, question_id):
    """
    pybo 수정
    """
    question = get_object_or_404(Question, pk=question_id)
    if request.user != question.author:
        messages.error(request, '수정권한이 없습니다.')
        return redirect('qnaboard:detail', question_id=question_id)
    
    if request.method == "POST":
        form = QuestionForm(request.POST, instance=question)
        if form.is_valid():
            question = form.save(commit=False)
            question.modify_date = timezone.now()  # 수정일시 저장
            question.save()
            return redirect('qnaboard:detail', question_id=question.id)
    else:
        form = QuestionForm(instance=question)
    context = {'form': form}
    return render(request, 'qnaboard/question_form.html', context)

@login_required(login_url='common:login')
def question_delete(request, question_id):
    """
    pybo 질문삭제
    """
    question = get_object_or_404(Question, pk=question_id)
    if request.user != question.author:
        messages.error(request, '삭제권한이 없습니다')
        return redirect('qnaboard:detail', question_id=question.id)
    question.delete()
    return redirect('qnaboard:qnaindex')   


@login_required(login_url='common:login')
def answer_modify(request, answer_id):
    """
    pybo 답변수정
    """
    answer = get_object_or_404(Answer, pk=answer_id)
    if request.user != answer.author:
        messages.error(request, '수정권한이 없습니다')
        return redirect('qnaboard:detail', question_id=answer.question.id)

    if request.method == "POST":
        form = AnswerForm(request.POST, instance=answer)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.modify_date = timezone.now()
            answer.save()
            return redirect('qnaboard:detail', question_id=answer.question.id)
    else:
        form = AnswerForm(instance=answer)
    context = {'answer': answer, 'form': form}
    return render(request, 'qnaboard/answer_form.html', context)

@login_required(login_url='common:login')
def answer_delete(request, answer_id):
    """
    pybo 답변삭제
    """
    answer = get_object_or_404(Answer, pk=answer_id)
    if request.user != answer.author:
        messages.error(request, '삭제권한이 없습니다')
    else:
        answer.delete()
    return redirect('qnaboard:detail', question_id=answer.question.id)
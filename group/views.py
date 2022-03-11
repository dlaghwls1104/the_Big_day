from django.shortcuts import render, redirect
from .models import Recruit
from django.utils import timezone
from .forms import RecruitForm, ApplicantForm
from django.core.paginator import Paginator

def index(request):
    page = request.GET.get('page', '1')
    recruit_list = Recruit.objects.order_by('-create_date')
    paginator = Paginator(recruit_list, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)
    context = {'recruit_list' :   page_obj}
    return render(request, 'group/recruit_list.html', context)

def detail(request, recruit_id):
    recruit = Recruit.objects.get(id=recruit_id)
    context = {'recruit' : recruit }
    return render(request, 'group/recruit_detail.html', context)

def answer_create(request, recruit_id):
    recruit = Recruit.objects.get(id=recruit_id)
    if request.method == "POST":
        form = ApplicantForm(request.POST)
        if form.is_valid():
            applicant = form.save(commit=False)
            applicant.create_date = timezone.now()
            applicant.question = recruit
            applicant.save()
            return redirect('group:detail', recruit_id=recruit.id)
    else:
        form =ApplicantForm()
    context = {'recruit': recruit, 'form': form}
    return render(request, 'group/recruit_detail.html', context)

def recruit_create(request):
    if request.method == 'POST':
        form = RecruitForm(request.POST)
        if form.is_valid():
            recruit = form.save(commit=False)
            recruit.create_date = timezone.now()
            recruit.save()
            return redirect('group:index')
    else:
        form = RecruitForm()
    context = {'form' : form}
    return render(request, 'group/recruit_form.html', context )




from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import CheckPost
#from .forms import CheckPost
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

def guestindex(request):
    """
    목록 출력
    """
    #입력파라미터
    page = request.GET.get('page','1')

    #조회
    guest_list = CheckPost.objects.order_by('-create_date')

    #페이징 처리
    paginator = Paginator(guest_list, 10)
    page_obj = paginator.get_page(page)

    context = {'guest_list': page_obj}
    
    return render(request, 'guestapp/guest_list.html', context)

def create_post(request):


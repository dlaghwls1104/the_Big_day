from multiprocessing import context
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Visitor

def v_create(request):
    name = request.POST['name']
    memo = request.POST['memo']
    vdata = Visitor(name=name, memo=memo)
    vdata.save()
    return redirect("vR")

def v_read(request):
    page = request.Get.get('page',1)
    vlist = Visitor.objects.all()
    paginator = Paginator(vlist, 3)
    vlistpage = paginator.get_page(page)
    context = {'vlist': vlistpage}
    return render(request, 'visitor.html', context)


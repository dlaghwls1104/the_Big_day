from django.contrib import admin
from django.urls import path,include
from qnaboard import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bigday/', include('bigday.urls')),
    path('qnaboard/', include('qnaboard.urls')),
    path('common/', include('common.urls')),
    path('', views.qnaindex, name='qnaindex')
]

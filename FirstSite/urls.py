from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from accounts import views as accounts_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('bigday/', include('bigday.urls')),
    path('accounts/signin/', include('django.contrib.auth.urls')), 
    path('accounts/', include('accounts.urls')), 
    path('visitor/', include('visitor.urls')),
    path('qnaboard/', include('qnaboard.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

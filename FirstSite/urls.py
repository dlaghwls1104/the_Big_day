from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from accounts import views as accounts_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('bigday/', include('bigday.urls')),
    path('signin/', include('django.contrib.auth.urls')), 
    path('accounts/', include('accounts.urls')), 
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('qnaboard/', include('qnaboard.urls')),
    path('users/', include('users.urls')),
    path('challenges/', include('challenges.urls')),
    path('', include('bigday.urls')),
    path('study/', include('study.urls')),
    path('map/', include('map.urls')),
    path('competition/', include('competition.urls')),
    path('group/', include('group.urls')),
    path('ranking/', include('ranking.urls')),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

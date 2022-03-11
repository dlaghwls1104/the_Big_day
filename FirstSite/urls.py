from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bigday/', include('bigday.urls')),
    path('study/', include('study.urls')),
    path('map/', include('map.urls')),
    path('competition/', include('competition.urls')),
    path('group/', include('group.urls')),
]

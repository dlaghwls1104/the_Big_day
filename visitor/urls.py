from django.urls import path
from . import views

urlpatterns = [
    path("visitorC/", views.v_create, name="vC"),
    path("visitorR/", views.v_read, name="vR"),
    # path("visitorU/", views.v_update, name="vU"),
    # path("visitorD/", views.v_delete, name="vD"),
]
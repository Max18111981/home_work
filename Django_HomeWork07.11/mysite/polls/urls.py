from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='polls_list'),
    path('', views.multiplication_table, name='multiplication_table'),
]
from django.urls import path
from django.urls.resolvers import URLPattern

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('calculate/', views.make_math_print, name='calculate'),
    path('select/', views.select_problem, name='select')
]
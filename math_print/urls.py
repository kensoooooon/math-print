from django.urls import path
from django.urls.resolvers import URLPattern

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('calculate/', views.make_math_print, name='calculate'),
    path('print/', views.print_number_problem, name='number_print'),
    path('display/', views.display_number_problem, name="number_display")
]
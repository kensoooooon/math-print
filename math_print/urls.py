from django.urls import path
from django.urls.resolvers import URLPattern

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('calculate/', views.make_math_print, name='calculate'),
    path('nubmer_print/', views.print_number_problem, name='number_print'),
    path('number_display/', views.display_number_problem, name="number_display"),
    path('character_print/', views.print_character_problem, name="character_print"),
    path('character_display', views.display_character_problem, name="character_display"),
]
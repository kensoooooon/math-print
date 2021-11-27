from django.urls import path
from django.urls.resolvers import URLPattern

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('calculate/', views.make_math_print, name='calculate'),
    path('number/nubmer_print/', views.print_number_problem, name='number_print'),
    path('number/number_display/', views.display_number_problem, name="number_display"),
    path('character/character_print/', views.print_character_problem, name="character_print"),
    path('character/character_display', views.display_character_problem, name="character_display"),
    path('linear_equation/linear_equation_print/', views.print_linear_equation_problem, name="linear_equation_print"),
    path('linear_equation/linear_equation_display/', views.display_linear_equation_problem, name="linear_equation_display"),
    path('linear_equation/linear_equation_ax_equal_b_only_integer_print/',views.print_linear_equation_ax_equal_b_integer, name='linear_equation_ax_equal_b_integer_print'),
    path('linear_equation/linear_equation_ax_equal_b_only_integer_display/',views.display_linear_equation_ax_equal_b_integer, name='linear_equation_ax_equal_b_integer_display'),
]
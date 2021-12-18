from django.urls import path
from django.urls.resolvers import URLPattern

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('junior_highschool1/', views.show_junior_highschool1, name='junior_highschool1'),
    path('junior_highschool2/', views.show_junior_highschool2, name='junior_highschool2'),
    path('number/nubmer_print/', views.print_number_problem, name='number_print'),
    path('number/number_display/', views.display_number_problem, name="number_display"),
    path('character/character_print/', views.print_character_problem, name="character_print"),
    path('character/character_display', views.display_character_problem, name="character_display"),
    path('linear_equation/linear_equation_print/', views.print_linear_equation_problem, name="linear_equation_print"),
    path('linear_equation/linear_equation_display/', views.display_linear_equation_problem, name="linear_equation_display"),
    path('linear_equation/linear_equation_ax_equal_b_only_integer_print/',views.print_specific_linear_equation, name='specific_linear_equation_print'),
    path('linear_equation/linear_equation_ax_equal_b_only_integer_display/',views.display_specific_linear_equation, name='specific_linear_equation_display'),
    path('simultaneous_equations/simultaneous_equations_for_print/', views.print_simultaneous_equation, name='simultaneous_equation_print'),
    path('simultaneous_equations/simultaneous_equations_for_display/', views.display_simultaneous_equation, name='simultaneous_equation_display'),
]
from django.urls import path
from django.urls.resolvers import URLPattern

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('junior_highschool1/', views.show_junior_highschool1, name='junior_highschool1'),
    path('junior_highschool2/', views.show_junior_highschool2, name='junior_highschool2'),
    path('junior_highschool3/', views.show_junior_highschool3, name='junior_highschool3'),
    path('highschool1/', views.show_highschool1, name='highschool1'),
    path('number/print/', views.print_number_problem, name='number_print'),
    path('number/display/', views.display_number_problem, name="number_display"),
    path('character/print/', views.print_character_problem, name="character_print"),
    path('character/display', views.display_character_problem, name="character_display"),
    path('linear_equation/print/', views.print_linear_equation_problem, name="linear_equation_print"),
    path('linear_equation/display/', views.display_linear_equation_problem, name="linear_equation_display"),
    path('linear_equation/print/',views.print_specific_linear_equation, name='specific_linear_equation_print'),
    path('linear_equation/display/',views.display_specific_linear_equation, name='specific_linear_equation_display'),
    path('simultaneous_equations/print/', views.print_simultaneous_equation, name='simultaneous_equation_print'),
    path('simultaneous_equations/display/', views.display_simultaneous_equation, name='simultaneous_equation_display'),
    path('expand_equation/print/', views.print_expand_equation, name='expand_equation_print'),
    path('expand_equation/display/', views.display_expand_equation, name='expand_equation_display'),
    path('completing_the_square/print/', views.print_completing_the_square, name='completing_the_square_print'),
    path('completing_the_square/display/', views.display_completing_the_square, name='completing_the_square_display'),
]
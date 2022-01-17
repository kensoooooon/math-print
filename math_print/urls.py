from django.urls import path
from django.urls.resolvers import URLPattern

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    ##########################################
    ### 小5 ###
    path('elementary_school5/', views.show_elementary_school5, name='elementary_school5'),
    ### 約分 ###
    path('reduction/print/', views.print_reduction_problem, name='reduction_print'),
    path('reduction/display/', views.display_reduction_problem, name='reduction_display'),
    ### 小数と分数の変換 ###
    path('conversion_between_frac_and_decimal/print/', views.print_conversion_between_frac_and_decimal_problem, name='conversion_between_frac_and_decimal_print'),
    path('conversion_between_frac_and_decimal/display/', views.display_conversion_between_frac_and_decimal_problem, name='conversion_between_frac_and_decimal_display'),
    ##########################################
    ### 分数の計算 ###
    path('fraction_calculate/print/', views.print_fraction_calculate_problem, name='fraction_calculate_print'),
    path('fraction_calculate/display', views.display_fraction_calculate_problem, name='fraction_calculate_display'),
    ### 中1 ###
    path('junior_highschool1/', views.show_junior_highschool1, name='junior_highschool1'),
    # 数の計算
    path('number/print/', views.print_number_problem, name='number_print'),
    path('number/display/', views.display_number_problem, name="number_display"),
    # 文字の計算
    path('character/print/', views.print_character_problem, name="character_print"),
    path('character/display', views.display_character_problem, name="character_display"),
    # 形の決まっていない1次方程式の計算
    path('linear_equation/print/', views.print_linear_equation_problem, name="linear_equation_print"),
    path('linear_equation/display/', views.display_linear_equation_problem, name="linear_equation_display"),
    # 特定の形と解を持つ1次方程式の計算
    path('specific_linear_equation/print/',views.print_specific_linear_equation, name='specific_linear_equation_print'),
    path('specific_linear_equation/display/',views.display_specific_linear_equation, name='specific_linear_equation_display'),
    # 比例
    path('proportional_expression/print/', views.print_proportional_expression, name='proportional_expression_print'),
    path('proportional_expression/display/', views.display_proportional_expression, name='proportional_expression_display'),
    # 累乗の計算
    path('power/print/', views.print_power_calculate, name='power_print'),
    path('power/display/', views.display_power_calculate, name='power_display'),
    ###########################################
    ### 中2 ###
    path('junior_highschool2/', views.show_junior_highschool2, name='junior_highschool2'),
    # 連立方程式
    path('simultaneous_equations/print/', views.print_simultaneous_equation, name='simultaneous_equation_print'),
    path('simultaneous_equations/display/', views.display_simultaneous_equation, name='simultaneous_equation_display'),
    # 1次関数
    path('linear_function/print/', views.print_linear_function, name='linear_function_print'),
    path('linear_function/display/', views.display_linear_function, name='linear_function_display'),
    ##########################################
    ### 中3 ###
    path('junior_highschool3/', views.show_junior_highschool3, name='junior_highschool3'),
    # 展開
    path('expand_equation/print/', views.print_expand_equation, name='expand_equation_print'),
    path('expand_equation/display/', views.display_expand_equation, name='expand_equation_display'),
    # 2次関数
    path('quadratic_function/print/', views.print_quadratic_function, name='quadratic_function_print'),
    path('quadratic_function/display/', views.display_quadratic_function, name='quadratic_function_display'),
    #########################################
    ### 高1 ###
    path('highschool1/', views.show_highschool1, name='highschool1'),
    # 平方完成
    path('completing_the_square/print/', views.print_completing_the_square, name='completing_the_square_print'),
    path('completing_the_square/display/', views.display_completing_the_square, name='completing_the_square_display'),
]
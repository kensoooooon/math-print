from django.urls import path
from django.urls.resolvers import URLPattern

from . import views

urlpatterns = [
    ### 全体共通 ###
    path('', views.index, name='index'),
    ##########################################
    ### 小3 ###
    path('elementary_school3/', views.show_elementary_school3, name='elementary_school3'),
    ### 単位の変換 ###
    path('unit_conversion/print', views.print_unit_conversion_problem, name='unit_conversion_print'),
    path('unit_conversion/display', views.display_unit_conversion_problem, name='unit_conversion_display'),
    ##########################################
    ### 小5 ###
    path('elementary_school5/', views.show_elementary_school5, name='elementary_school5'),
    ### 約分 ###
    path('reduction/print/', views.print_reduction_problem, name='reduction_print'),
    path('reduction/display/', views.display_reduction_problem, name='reduction_display'),
    ### 小数と分数の変換 ###
    path('conversion_between_frac_and_decimal/print/', views.print_conversion_between_frac_and_decimal_problem, name='conversion_between_frac_and_decimal_print'),
    path('conversion_between_frac_and_decimal/display/', views.display_conversion_between_frac_and_decimal_problem, name='conversion_between_frac_and_decimal_display'),
    ### 分数の計算 ###
    path('fraction_calculate/print/', views.print_fraction_calculate_problem, name='fraction_calculate_print'),
    path('fraction_calculate/display', views.display_fraction_calculate_problem, name='fraction_calculate_display'),
    ### 最小公倍数と最大公約数 ###
    path('lcm_and_gcd/print/', views.print_lcm_and_gcd_problem, name='lcm_and_gcd_print'),
    path('lcm_and_gcd/display/', views.display_lcm_and_gcd_problem, name='lcm_and_gcd_display'),
    ##########################################
    ### 中1 ###
    path('junior_highschool1/', views.show_junior_highschool1, name='junior_highschool1'),
    # 数の計算
    path('number/print/', views.print_number_problem, name='number_print'),
    path('number/display/', views.display_number_problem, name="number_display"),
    # カッコなしの数の計算
    path('number_without_bracket/print/', views.print_number_without_bracket_problem, name='number_without_bracket_print'),
    path('number_without_bracket/display/', views.display_number_without_bracket_problem, name='number_without_bracket_display'),
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
    # おうぎ形
    path('sector/print/', views.print_sector_problem, name='sector_print'),
    path('sector/display/', views.display_sector_problem, name='sector_display'),
    # おうぎ形(図つき)
    path('sector_with_figure/print/', views.print_sector_with_figure_problem, name='sector_with_figure_print'),
    path('sector_with_figure/display/', views.display_sector_with_figure_problem, name='sector_with_figure_display'),
    ###########################################
    ### 中2 ###
    path('junior_highschool2/', views.show_junior_highschool2, name='junior_highschool2'),
    # 連立方程式
    path('simultaneous_equations/print/', views.print_simultaneous_equations, name='simultaneous_equations_print'),
    path('simultaneous_equations/display/', views.display_simultaneous_equations, name='simultaneous_equations_display'),
    # 1次関数
    path('linear_function/print/', views.print_linear_function, name='linear_function_print'),
    path('linear_function/display/', views.display_linear_function, name='linear_function_display'),
    # 等式の変形
    path('transformation_of_equation/print/', views.print_transformation_of_equation, name='transformation_of_equation_print'),
    path('transformation_of_equation/display/', views.display_transformation_of_equation, name='transformation_of_equation_display'),
    # 分数を使った文字の計算
    path('character_fraction/print/', views.print_character_fraction, name='character_fraction_print'),
    path('character_fraction/display/', views.display_character_fraction, name='character_fraction_display'),
    # 文字の計算
    path('jhs2_character/print/', views.jhs2_print_character_problem, name='jhs2_character_print'),
    path('jhs2_character/display/', views.jhs2_display_character_problem, name='jhs2_character_display'),
    # 平行線と図形の角
    path('parallel_lines_and_angle/print/', views.print_parallel_lines_and_angle, name='parallel_lines_and_angle_print'),
    path('parallel_lines_and_angle/display/', views.display_parallel_lines_and_angle, name='parallel_lines_and_angle_display'),
    ##########################################
    ### 中3 ###
    path('junior_highschool3/', views.show_junior_highschool3, name='junior_highschool3'),
    # 展開
    path('expand_equation/print/', views.print_expand_equation, name='expand_equation_print'),
    path('expand_equation/display/', views.display_expand_equation, name='expand_equation_display'),
    # 2次関数
    path('quadratic_function/print/', views.print_quadratic_function, name='quadratic_function_print'),
    path('quadratic_function/display/', views.display_quadratic_function, name='quadratic_function_display'),
    # 因数分解
    path('factorization/print/', views.print_factorization, name='factorization_print'),
    path('factorization/display/', views.display_factorization, name='factorization_display'),
    # 2次方程式
    path('quadratic_equation/print/', views.print_quadratic_equation, name='quadratic_equation_print'),
    path('quadratic_equation/display/', views.display_quadratic_equation, name='quadratic_equation_display'),
    #########################################
    ### 高1 ###
    path('highschool1/', views.show_highschool1, name='highschool1'),
    # 平方完成
    path('completing_the_square/print/', views.print_completing_the_square, name='completing_the_square_print'),
    path('completing_the_square/display/', views.display_completing_the_square, name='completing_the_square_display'),
    # 式の展開
    path('hs1_expand_equation/print', views.hs1_print_expand_equation, name='hs1_expand_equation_print'),
    path('hs1_expand_equation/display', views.hs1_display_expand_equation, name='hs1_expand_equation_display'),
    # 因数分解
    path('hs1_factorization/print', views.hs1_print_factorization, name='hs1_factorization_print'),
    path('hs1_factorization/display', views.hs1_display_factorization, name='hs1_factorization_display'),
    # 2次関数の決定
    path('hs1_quadratic_function/print', views.hs1_print_quadratic_function, name='hs1_quadratic_function_print'),
    path('hs1_quadratic_function/display', views.hs1_display_quadratic_function, name='hs1_quadratic_function_display'),
    # 2次関数の最大最小
    path('hs1_quadratic_function_max_min/print', views.hs1_print_quadratic_function_max_min, name='hs1_quadratic_function_max_min_print'),
    path('hs1_quadratic_function_max_min/display', views.hs1_display_quadratic_function_max_min, name='hs1_quadratic_function_max_min_display'),
    #########################################
    ### 高2 ###
    path('highschool2/', views.show_highschool2, name='highschool2'),
    # 対数の計算
    path('logarithm_calculate/print', views.print_logarithm_calculation, name='logarithm_calculation_print'),
    path('logarithm_calculate/display', views.display_logarithm_calculation, name='logarithm_calculation_display'),
    # 指数の計算
    path('exponent_calculate/print', views.print_exponent_calculation, name='exponent_calculation_print'),
    path('exponent_calculate/display', views.display_exponent_calculation, name='exponent_calculation_display'),
    # ベクトルの交点
    path('vector_cross_point/print', views.print_vector_cross_point, name='vector_cross_point_print'),
    path('vector_cross_point/display', views.display_vector_cross_point, name='vector_cross_point_display'),
]
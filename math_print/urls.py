from django.urls import path
from django.urls.resolvers import URLPattern

from . import views

urlpatterns = [
    ### 全体共通 ###
    path('', views.index, name='index'),
    ### サイト説明 ###
    path('about_me', views.about_me, name='about_me'),
    ### 更新情報 ###
    path('update_information/', views.update_information, name='update_information'),
    ##########################################
    ### 小2 ###
    path('elementary_school2/', views.show_elementary_school2, name='elementary_school2'),
    ### 時計 ###
    path('clock/print', views.print_clock, name='clock_print'),
    path('clock/display', views.display_clock, name='clock_display'),
    ##########################################
    ### 小3 ###
    path('elementary_school3/', views.show_elementary_school3, name='elementary_school3'),
    ### 単位の変換 ###
    path('unit_conversion/print', views.print_unit_conversion_problem, name='unit_conversion_print'),
    path('unit_conversion/display', views.display_unit_conversion_problem, name='unit_conversion_display'),
    ### 分母が同じ分数の計算 ###
    path('same_denominator_calculate/print', views.print_same_denominator_calculate_problem, name='same_denominator_calculate_print'),
    path('same_denominator_calculate/display', views.display_same_denominator_calculate_problem, name='same_denominator_calculate_display'),
    ### 割り算 ###
    path('division_for_elementary_school3/print', views.print_division_for_elementary_school3, name='division_for_elementary_school3_print'),
    path('division_for_elementary_school3/display', views.display_division_for_elementary_school3, name='division_for_elementary_school3_display'),
    ### 足し算と引き算 ###
    path('addition_and_subtraction_for_elementary_school3/print', views.print_addition_and_subtraction_for_elementary_school3, name='addition_and_subtraction_for_elementary_school3_print'),
    path('addition_and_subtraction_for_elementary_school3/display', views.display_addition_and_subtraction_for_elementary_school3, name='addition_and_subtraction_for_elementary_school3_display'),
    ### 掛け算 ###
    path('multiplication_for_elementary_school3/print', views.print_multiplication_for_elementary_school3, name='multiplication_for_elementary_school3_print'),
    path('multiplication_for_elementary_school3/display', views.display_multiplication_for_elementary_school3, name='multiplication_for_elementary_school3_display'),
    ##########################################
    ### 小4 ###
    path('elementary_school4/', views.show_elementary_school4, name='elementary_school4'),
    ### 1億を超える数の計算 ###
    path('calculation_of_big_number/print', views.print_calculation_of_big_number, name='calculation_of_big_number_print'),
    path('calculation_of_big_number/display', views.display_calculation_of_big_number, name='calculation_of_big_number_display'),
    ### 割り算 ###
    path('division_for_elementary_school4/print', views.print_division_for_elementary_school4, name='division_for_elementary_school4_print'),
    path('division_for_elementary_school4/display', views.display_division_for_elementary_school4, name='division_for_elementary_school4_display'),
    ### 小数の足し算・引き算 ###
    path('addition_and_subtraction_of_decimal_for_elementary_school4/print', views.print_addition_and_subtraction_of_decimal_for_elementary_school4, name='addition_and_subtraction_of_decimal_for_elementary_school4_print'),
    path('addition_and_subtraction_of_decimal_for_elementary_school4/display', views.display_addition_and_subtraction_of_decimal_for_elementary_school4, name='addition_and_subtraction_of_decimal_for_elementary_school4_display'),
    ### 小数のかけ算 ###
    path('multiplication_of_decimal_for_elementary_school4/print', views.print_multiplication_of_decimal_for_elementary_school4, name='multiplication_of_decimal_for_elementary_school4_print'),
    path('multiplication_of_decimal_for_elementary_school4/display', views.display_multiplication_of_decimal_for_elementary_school4, name='multiplication_of_decimal_for_elementary_school4_display'),
    ### 小数の割り算 ###
    path('division_of_decimal_for_elementary_school4/print', views.print_division_of_decimal_for_elementary_school4, name='division_of_decimal_for_elementary_school4_print'),
    path('division_of_decimal_for_elementary_school4/display', views.display_division_of_decimal_for_elementary_school4, name='division_of_decimal_for_elementary_school4_display'),
    ### 分数の足し算と引き算
    path('addition_and_subtraction_of_fraction_or_elementary_school4/print', views.print_addition_and_subtraction_of_fraction_for_elementary_school4, name='addition_and_subtraction_of_fraction_or_elementary_school4_print'),
    path('addition_and_subtraction_of_fraction_or_elementary_school4/display', views.display_addition_and_subtraction_of_fraction_for_elementary_school4, name='addition_and_subtraction_of_fraction_or_elementary_school4_display'),
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
    ### 扇形 ###
    path('elementary5_sector/print/', views.print_elementary5_sector_problem, name='elementary5_sector_print'),
    path('elementary5_sector/display/', views.display_elementary5_sector_problem, name='elementary5_sector_display'),
    ### 通分 ###
    path('common_denominator/print/', views.print_common_denominator_problem, name='common_denominator_print'),
    path('common_denominator/display/', views.display_common_denominator_problem, name='common_denominator_display'),
    ### 分数の倍, 割合 ###
    path('ratio/print', views.print_ratio, name='ratio_print'),
    path('ratio/display', views.display_ratio, name='ratio_display'),
    path('ratio/explanation/', views.explain_ratio, name='ratio_explain'),
    path('ratio/explanation_print/', views.explain_ratio_print, name='ratio_explain_print'),
    ##########################################
    ### 小6 ###
    path('elementary_school6/', views.show_elementary_school6, name='elementary_school6'),
    ### 穴埋め算 ###
    path('fill_in_the_square/print', views.print_fill_in_the_square_problem, name='fill_in_the_square_print'),
    path('fill_in_the_square/display', views.display_fill_in_the_square_problem, name='fill_in_the_square_display'),
    ### 分数と整数のかけ算・割り算 ###
    path('multiplication_and_division_of_fraction_and_integer/print', views.print_multiplication_and_division_of_fraction_and_integer, name='multiplication_and_division_of_fraction_and_integer_print'),
    path('multiplication_and_division_of_fraction_and_integer/display', views.display_multiplication_and_division_of_fraction_and_integer, name='multiplication_and_division_of_fraction_and_integer_display'),
    ### 文字を使った式 ###
    path('formula_with_symbol/print', views.print_formula_with_symbol, name='formula_with_symbol_print'),
    path('formula_with_symbol/display', views.display_formula_with_symbol, name='formula_with_symbol_display'),
    ##########################################
    ### 中1 ###
    path('junior_highschool1/', views.show_junior_highschool1, name='junior_highschool1'),
    # 数の計算
    path('number/print/', views.print_number_problem, name='number_print'),
    path('number/display/', views.display_number_problem, name="number_display"),
    # カッコなしの数の計算
    path('number_without_bracket/print/', views.print_number_without_bracket_problem, name='number_without_bracket_print'),
    path('number_without_bracket/display/', views.display_number_without_bracket_problem, name='number_without_bracket_display'),
    path('number_without_bracket/explanation/', views.explain_number_without_bracket, name='number_without_bracket_explain'),
    path('number_without_bracket/explanation_print/', views.explain_number_without_bracket_print, name='number_without_bracket_explain_print'),
    # 文字の計算
    path('character/print/', views.print_character_problem, name="character_print"),
    path('character/display', views.display_character_problem, name="character_display"),
    # 形の決まっていない1次方程式の計算
    path('linear_equation/print/', views.print_linear_equation_problem, name="linear_equation_print"),
    path('linear_equation/display/', views.display_linear_equation_problem, name="linear_equation_display"),
    # 特定の形と解を持つ1次方程式の計算
    path('specific_linear_equation/print/',views.print_specific_linear_equation, name='specific_linear_equation_print'),
    path('specific_linear_equation/display/',views.display_specific_linear_equation, name='specific_linear_equation_display'),
    path('specific_linear_equation/explanation', views.explain_specific_linear_equation, name='specific_linear_equation_explain'),
    path('specific_linear_equation/explanation_print', views.explain_specific_linear_equation_print, name='specific_linear_equation_explain_print'),
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
    # 直線と平面の位置関係
    path('line_and_flat_positional_relationship/print/', views.print_line_and_flat_positional_relationship, name="line_and_flat_positional_relationship_print"),
    path('line_and_flat_positional_relationship/display/', views.display_line_and_flat_positional_relationship, name="line_and_flat_positional_relationship_display"),
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
    # 1次関数とグラフ
    path('linear_function_with_graph/print/', views.print_linear_function_with_graph, name='linear_function_with_graph_print'),
    path('linear_function_with_graph/display/', views.display_linear_function_with_graph, name='linear_function_with_graph_display'),
    # 1次関数で囲まれた面積
    path('area_with_linear_function/print/', views.print_area_with_linear_function, name='area_with_linear_function_print'),
    path('area_with_linear_function/display/', views.display_area_with_linear_function, name='area_with_linear_function_display'),
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
    path('quadratic_equation/explain', views.explain_quadratic_equation, name='quadratic_equation_explain'),
    path('quadratic_equation/explain_print', views.explain_quadratic_equation_print, name='quadratic_equation_explain_print'),
    # 平方根を求める
    path('square_root/print/', views.print_square_root_problem, name='square_root_print'),
    path('square_root/display/', views.display_square_root_problem, name='square_root_display'),
    # 平方根を計算する
    path('square_root_calculate/print', views.print_square_root_calculate_problem, name='square_root_calculate_print'),
    path('square_root_calculate/display', views.display_square_root_calculate_problem, name='square_root_calculate_display'),
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
    # n進数
    path('base_n_numbers/print', views.print_base_n_numbers, name='base_n_numbers_print'),
    path('base_n_numbers/display', views.display_base_n_numbers, name='base_n_numbers_display'),
    # 三角比
    path('trigonometric_ratio/print', views.print_trigonometric_ratio, name='trigonometric_ratio_print'),
    path('trigonometric_ratio/display', views.display_trigonometric_ratio, name='trigonometric_ratio_display'),
    # 2次不等式
    path('quadratic_inequality/print', views.print_quadratic_inequality, name='quadratic_inequality_print'),
    path('quadratic_inequality/display', views.display_quadratic_inequality, name='quadratic_inequality_display'),
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
    # 数列の漸化式
    path('recurrence_relation/print', views.print_recurrence_relation, name='recurrence_relation_print'),
    path('recurrence_relation/display', views.display_recurrence_relation, name='recurrence_relation_display'),
    # 三角関数
    path('trigonometric_function/print', views.print_trigonometric_function, name='trigonometric_function_print'),
    path('trigonometric_function/display', views.display_trigonometric_function, name='trigonometric_function_display'),
    # 面積を求める積分
    path('calculate_area_by_integration/print', views.print_calculate_area_by_integration, name='calculate_area_by_integration_print'),
    path('calculate_area_by_integration/display', views.display_calculate_area_by_integration, name='calculate_area_by_integration_display'),
    path('calculate_area_by_integration/explanation_one_sixth', views.explain_one_sixth_calculate_area_by_integration, name='calculate_area_by_integration_explain_one_sixth'),
    path('calculate_area_by_integration/explanation_one_third', views.explain_one_third_calculate_area_by_integration, name='calculate_area_by_integration_explain_one_third'),
    path('calculate_area_by_integration/explanation_one_sixth_print', views.explain_one_sixth_calculate_area_by_integration_print, name='calculate_area_by_integration_explain_one_sixth_print'),
    path('calculate_area_by_integration/explanation_one_third_print', views.explain_one_third_calculate_area_by_integration_print, name='calculate_area_by_integration_explain_one_third_print'),
    # 対数方程式・不等式
    path('logarithmic_equation/print', views.print_logarithmic_equation, name='logarithmic_equation_print'),
    path('logarithmic_equation/display', views.display_logarithmic_equation, name='logarithmic_equation_display'),
    path('logarithmic_equation/explain', views.explain_logarithmic_equation, name='logarithmic_equation_explain'),
    path('logarithmic_equation/explain_print', views.explain_logarithmic_equation_print, name='logarithmic_equation_explain_print'),
    # 種々の数列の和
    path('series/print', views.print_series, name='series_print'),
    path('series/display', views.display_series, name='series_display'),
    #########################################
    ### 高3 ###
    path('highschool3/', views.show_highschool3, name='highschool3'),
    # 1次式の置換を用いる積分計算
    path('integration_calculation/print', views.print_integral_calculation_of_linear_function_replacement, name='hs3_integral_calculation_of_linear_function_replacement_print'),
    path('integration_calculation/display', views.display_integral_calculation_of_linear_function_replacement, name='hs3_integral_calculation_of_linear_function_replacement_display'),
]
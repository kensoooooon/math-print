import unicodedata
import pprint

from django.http import HttpResponse
from django.shortcuts import render
from sympy.geometry import line


from .math_process.character_calculate import CharacterMathProblem
from .math_process.linear_equation import LinearEquationProblem
from .math_process.number_calculate import NumberMathProblem
from .math_process.specific_linear_equation import SpecificLinearEquation
from .math_process.simultaneous_equations import SimultaneousEquations
from .math_process.expand_equation import ExpandEquationProblem
from .math_process.completing_the_square import CompletingTheSquareProblem
from .math_process.proportional_expression import ProportionalExpressionProblem
from .math_process.linear_function import LinearFunctionProblem
from .math_process.power_calculate import PowerCalculateProblem
from .math_process.completing_the_square import CompletingTheSquareProblem
from .math_process.reduction import ReductionProblem
from .math_process.conversion_between_frac_and_decimal import ConversionBetweenFracAndDecimalProblem
from .math_process.quadratic_function import QuadraticFunctionProblem
from .math_process.fraction_calculate import FractionCalculateProblem
from .math_process.number_without_bracket_calculate import NumberWithoutBracketCalculateProblem
from .math_process.sector import SectorProblem
from .math_process.factorization import FactorizationProblem
from .math_process.quadratic_equation import QuadraticEquationProblem
from .math_process.hs1_expand_equation import HS1ExpandEquationProblem
from .math_process.hs1_factorization import HS1FactorizationProblem
from .math_process.transformation_of_equation import TransformationOfEquationProblem
from .math_process.character_fraction import CharacterFractionProblem
from .math_process.hs1_quadratic_function import HS1QuadraticFunctionProblem
from .math_process.hs1_quadratic_function_max_min import HS1QuadraticFunctionMaxMinProblem
from .math_process.unit_conversion import UnitConversionProblem
from .math_process.sector_with_figure import SectorWithFigureProblem
from .math_process.logarithm_calculation import LogarithmCalculationProblem
from .math_process.exponent_calculation import ExponentCalculation
from .math_process.lcm_and_gcd import LCMAndGCD
from .math_process.vector_cross_point import VectorCrossPoint
from .math_process.elementary5_sector import Elementary5SectorWithFigureProblem
from .math_process.fill_in_the_square import FillInTheSquareProblem
from .math_process.common_denominator import CommonDenominatorProblem
from .math_process.recurrence_relation import RecurrenceRelationProblem
from .math_process.square_root import SquareRootProblem
from .math_process.square_root_calculate import SquareRootCalculateProblem
from .math_process.base_n_numbers import BaseNNumbersProblem
from .math_process.linear_function_with_graph import LinearFunctionWithGraphProblem
from .math_process.trigonometric_ratio import TrigonometricRatioProblem
from .math_process.trigonometric_function import TrigonometricFunctionProblem
from .math_process.quadratic_inequality import QuadraticInequality
from .math_process.same_denominator_calculate import SameDenominatorCalculate
from .math_process.line_and_flat_positional_relationship import LineAndFlatPositionalRelationship
from .math_process.calculate_area_by_integration import CalculateAreaByIntegration
from .math_process.logarithmic_equation import LogarithmicEquation
from .math_process.ratio_problem import RatioProblem
from .math_process.division_for_3rd_grade import DivisionFor3rdGrade
from .math_process.addition_and_subtraction_for_3rd_grade import AdditionAndSubtractionFor3rdGrade
from .math_process.multiplication_for_3rd_grade import MultiplicationFor3rdGrade
from .math_process.calculation_of_big_number import CalculationOfBigNumber
from .math_process.division_for_4th_grade import DivisionFor4thGrade
from .math_process.addition_and_subtraction_of_decimal_for_4th_grade import AdditionAndSubtractionOfDecimalFor4thGrade
from .math_process.multiplication_of_decimal_for_4th_grade import MultiplicationOfDecimalFor4thGrade
from .math_process.division_of_decimal_for_4th_grade import DivisionOfDecimalFor4thGrade
from .math_process.addition_and_subtraction_of_fraction_for_4th_grade import AdditionAndSubtractionOfFraction



def index(request):
    return render(request, 'math_print/index.html', {})


# for update information
def update_information(request):
    return render(request, 'math_print/update_information.html', {})

# for description about website
def about_me(request):
    return render(request, 'math_print/about_me.html', {})


# index
def show_elementary_school3(request):
    return render(request, 'math_print/elementary_school3/elementary_school3.html', {})

def show_elementary_school4(request):
    return render(request, 'math_print/elementary_school4/elementary_school4.html', {})

def show_elementary_school5(request):
    return render(request, 'math_print/elementary_school5/elementary_school5.html', {})

def show_elementary_school6(request):
    return render(request, 'math_print/elementary_school6/elementary_school6.html', {})

def show_junior_highschool1(request):
    return render(request, 'math_print/junior_highschool1/junior_highschool1.html', {})

def show_junior_highschool2(request):
    return render(request, 'math_print/junior_highschool2/junior_highschool2.html', {})

def show_junior_highschool3(request):
    return render(request, 'math_print/junior_highschool3/junior_highschool3.html', {})

def show_highschool1(request):
    return render(request, 'math_print/highschool1/highschool1.html', {})

def show_highschool2(request):
    return render(request, 'math_print/highschool2/highschool2.html', {})


# problem and explanation
## print section
def print_number_problem(request):
    PROBLEM_NUMBER = 20

    number_to_use = request.POST.getlist("number_number_to_use")
    operator_to_use = request.POST.getlist("number_operator_to_use")
    term_number = int(request.POST["term_number"])
    paper_number = int(request.POST["paper_number"])

    MAX_NUMBER_TO_FRAC = 10
    MIN_NUMBER_TO_FRAC = -10

    math_problem_list_of_list = []
    for _ in range(paper_number):
        math_problem_tuple_inner_list = []
        for _ in range(int(PROBLEM_NUMBER/2)):
            problem1 = NumberMathProblem(term_number, MAX_NUMBER_TO_FRAC, MIN_NUMBER_TO_FRAC, number_to_use, operator_to_use)
            problem2 = NumberMathProblem(term_number, MAX_NUMBER_TO_FRAC, MIN_NUMBER_TO_FRAC, number_to_use, operator_to_use)
            math_problem_tuple_inner_list.append((problem1, problem2))
        math_problem_list_of_list.append(math_problem_tuple_inner_list)

    return render(request, 'math_print/junior_highschool1/number/for_print.html', {'math_problem_list_of_list': math_problem_list_of_list})

def print_character_problem(request):
    PROBLEM_NUMBER = 20
    
    number_to_use = request.POST.getlist("character_number_to_use")
    operator_to_use = request.POST.getlist("character_operator_to_use")
    term_number = int(request.POST["term_number"])
    paper_number = int(request.POST["paper_number"])
    character_to_use = request.POST["character_to_use"]
    character_to_use_list = ["x"]
    if character_to_use == "2":
        character_to_use_list += ["y"]

    MAX_NUMBER_TO_FRAC = 10
    MIN_NUMBER_TO_FRAC = -10

    math_problem_list_of_list = []
    for _ in range(paper_number):
        math_problem_tuple_inner_list = []
        for _ in range(int(PROBLEM_NUMBER/2)):
            problem1 = CharacterMathProblem(
                term_number=term_number, max_number_to_frac=MAX_NUMBER_TO_FRAC,
                min_number_to_frac=MIN_NUMBER_TO_FRAC, used_number_type_list=number_to_use,
                used_operator_type_list=operator_to_use, used_character_type_list=character_to_use_list
                )
            problem2 = CharacterMathProblem(
                term_number=term_number, max_number_to_frac=MAX_NUMBER_TO_FRAC,
                min_number_to_frac=MIN_NUMBER_TO_FRAC, used_number_type_list=number_to_use,
                used_operator_type_list=operator_to_use, used_character_type_list=character_to_use_list
                )
            math_problem_tuple_inner_list.append((problem1, problem2))
        math_problem_list_of_list.append(math_problem_tuple_inner_list)

    return render(request, 'math_print/junior_highschool1/character/for_print.html', {'math_problem_list_of_list': math_problem_list_of_list})

def print_linear_equation_problem(request):
    PROBLEM_NUMBER = 20
    
    number_to_use = request.POST.getlist("number_to_use")
    operator_to_use = request.POST.getlist("operator_to_use")
    term_number = int(request.POST["term_number"])
    paper_number = int(request.POST["paper_number"])

    MAX_NUMBER_TO_FRAC = 10
    MIN_NUMBER_TO_FRAC = -10

    math_problem_list_of_list = []
    for _ in range(paper_number):
        math_problem_tuple_inner_list = []
        for _ in range(int(PROBLEM_NUMBER/2)):
            problem1 = LinearEquationProblem(
                term_number=term_number, max_number_to_frac=MAX_NUMBER_TO_FRAC,
                min_number_to_frac=MIN_NUMBER_TO_FRAC, used_number_type_list=number_to_use,
                used_operator_type_list=operator_to_use,
                )
            problem2 = LinearEquationProblem(
                term_number=term_number, max_number_to_frac=MAX_NUMBER_TO_FRAC,
                min_number_to_frac=MIN_NUMBER_TO_FRAC, used_number_type_list=number_to_use,
                used_operator_type_list=operator_to_use,
                )
            math_problem_tuple_inner_list.append((problem1, problem2))
        math_problem_list_of_list.append(math_problem_tuple_inner_list)

    return render(request, 'math_print/junior_highschool1/linear_equation/for_print.html', {'math_problem_list_of_list': math_problem_list_of_list})

def print_specific_linear_equation(request):
    PROBLEM_NUMBER = 20
    
    linear_equation_type_list = request.POST.getlist("linear_equation_type")
    if not(linear_equation_type_list):
        linear_equation_type_list.append("ax_equal_b_only_integer")
        linear_equation_type_list.append("ax_equal_b_all_number")
        linear_equation_type_list.append("ax_plus_b_equal_c_only_integer")
        linear_equation_type_list.append("ax_plus_b_equal_c_all_number")
        linear_equation_type_list.append("ax_plus_b_equal_cx_plus_d_only_integer")
        linear_equation_type_list.append("ax_plus_b_equal_cx_plus_d_all_number")
    number_to_use_list = request.POST.getlist("number_to_use")
    if not(number_to_use_list):
        number_to_use_list.append("integer")
        number_to_use_list.append("decimal")
        number_to_use_list.append("frac") 
    paper_number = int(request.POST["paper_number"])
    
    math_problem_list_of_list = []
    for _ in range(paper_number):
        math_problem_tuple_inner_list = []
        for _ in range(int(PROBLEM_NUMBER//2)):
            problem1 = SpecificLinearEquation(
                linear_equation_type_list=linear_equation_type_list, number_to_use_list=number_to_use_list
            )
            problem2 = SpecificLinearEquation(
                linear_equation_type_list=linear_equation_type_list, number_to_use_list=number_to_use_list
            )
            math_problem_tuple_inner_list.append((problem1, problem2))
        math_problem_list_of_list.append(math_problem_tuple_inner_list)
    
    return render(request, 'math_print/junior_highschool1/specific_linear_equation/for_print.html', {'math_problem_list_of_list': math_problem_list_of_list})

def print_simultaneous_equations(request):
    PROBLEM_NUMBER = 20
    
    used_coefficients = request.POST.getlist("used_coefficient")
    if not(used_coefficients):
        used_coefficients.append("integer")
        used_coefficients.append("decimal")
        used_coefficients.append("frac")
    equation_types = request.POST.getlist("equation_types")
    if not(equation_types):
        equation_types.append("ax+by=c")
        equation_types.append("ax+by=c+dx+ey")
        equation_types.append("ax+by=c+d(ex+fy)")
    answer_type = request.POST["answer_type"]
    paper_number = int(request.POST["paper_number"])

    math_problem_list_of_list = []
    for _ in range(paper_number):
        math_problem_tuple_inner_list = []
        for _ in range(int(PROBLEM_NUMBER//2)):
            problem1 = SimultaneousEquations(
                used_coefficients=used_coefficients, equation_types=equation_types,
                answer_type=answer_type
            )
            problem2 = SimultaneousEquations(
                used_coefficients=used_coefficients, equation_types=equation_types,
                answer_type=answer_type
            )
            math_problem_tuple_inner_list.append((problem1, problem2))
        math_problem_list_of_list.append(math_problem_tuple_inner_list)
    
    return render(request, "math_print/junior_highschool2/simultaneous_equations/for_print.html", {"math_problem_list_of_list": math_problem_list_of_list})

def print_expand_equation(request):
    PROBLEM_NUMBER = 20

    number_to_use = request.POST.getlist("number_to_use")
    expand_equation_type_list = request.POST.getlist("expand_equation_type")
    paper_number = int(request.POST["paper_number"])
    
    math_problem_list_of_list = []
    for _ in range(paper_number):
        math_problem_tuple_inner_list = []
        for _ in range(int(PROBLEM_NUMBER//2)):
            problem1 = ExpandEquationProblem(
                used_number_type_list=number_to_use, expand_equation_type_list=expand_equation_type_list
            )
            problem2 = ExpandEquationProblem(
                used_number_type_list=number_to_use, expand_equation_type_list=expand_equation_type_list
            )
            math_problem_tuple_inner_list.append((problem1, problem2))
        math_problem_list_of_list.append(math_problem_tuple_inner_list)
    
    return render(request, "math_print/junior_highschool3/expand_equation/for_print.html", {'math_problem_list_of_list': math_problem_list_of_list})

def print_completing_the_square(request):
    PROBLEM_NUMBER = 20
    
    number_to_use = request.POST.getlist("number_to_use")
    number_including_in_bracket = request.POST["number_including_in_bracket"]
    paper_number = int(request.POST["paper_number"])
    if request.POST["character_including_or_not"] == "including_character":
        include_character_in_coefficient = True
    else:
        include_character_in_coefficient = False
    
    math_problem_list_of_list = []
    for _ in range(paper_number):
        math_problem_tuple_inner_list = []
        for _ in range(int(PROBLEM_NUMBER//2)):
            problem1 = CompletingTheSquareProblem(
                used_number_type_list=number_to_use, number_including_in_bracket=number_including_in_bracket,
                include_character_in_coefficient=include_character_in_coefficient
            )
            problem2 = CompletingTheSquareProblem(
                used_number_type_list=number_to_use, number_including_in_bracket=number_including_in_bracket,
                include_character_in_coefficient=include_character_in_coefficient
            )
            math_problem_tuple_inner_list.append((problem1, problem2))
        math_problem_list_of_list.append(math_problem_tuple_inner_list)
    
    return render(request, "math_print/highschool1/completing_the_square/for_print.html", {'math_problem_list_of_list': math_problem_list_of_list})

def print_proportional_expression(request):

    PROBLEM_NUMBER = 20
    
    number_to_use = request.POST.getlist("number_to_use")
    proportional_expression_type = request.POST["proportional_expression_type"]
    paper_number = int(request.POST["paper_number"])
    
    math_problem_list_of_list = []
    for _ in range(paper_number):
        math_problem_tuple_inner_list = []
        for _ in range(int(PROBLEM_NUMBER//2)):
            problem1 = ProportionalExpressionProblem(
                used_number_type_list=number_to_use, proportional_expression_type=proportional_expression_type
            )
            problem2 = ProportionalExpressionProblem(
                used_number_type_list=number_to_use, proportional_expression_type=proportional_expression_type
            )
            math_problem_tuple_inner_list.append((problem1, problem2))
        math_problem_list_of_list.append(math_problem_tuple_inner_list)
    
    return render(request, "math_print/junior_highschool1/proportional_expression/for_print.html", {'math_problem_list_of_list': math_problem_list_of_list})

def print_linear_function(request):
    PROBLEM_NUMBER = 20
    
    number_to_use_list = request.POST.getlist("number_to_use")
    given_information_list = request.POST.getlist("given_information")
    paper_number = int(request.POST["paper_number"])
    
    math_problem_list_of_list = []
    for _ in range(paper_number):
        math_problem_tuple_inner_list = []
        for _ in range(int(PROBLEM_NUMBER//2)):
            problem1 = LinearFunctionProblem(
                number_to_use_list=number_to_use_list, given_information_list=given_information_list
            )
            problem2 = LinearFunctionProblem(
                number_to_use_list=number_to_use_list, given_information_list=given_information_list
            )
            math_problem_tuple_inner_list.append((problem1, problem2))
        math_problem_list_of_list.append(math_problem_tuple_inner_list)
    
    return render(request, "math_print/junior_highschool2/linear_function/for_print.html", {'math_problem_list_of_list': math_problem_list_of_list})

def print_power_calculate(request):
    PROBLEM_NUMBER = 20
    
    number_to_use = request.POST.getlist("power_number_to_use")
    calculate_type = request.POST.getlist("power_calculate_type")
    paper_number = int(request.POST["paper_number"])
    
    math_problem_list_of_list = []
    for _ in range(paper_number):
        math_problem_tuple_inner_list = []
        for _ in range(int(PROBLEM_NUMBER//2)):
            problem1 = PowerCalculateProblem(
                number_to_use=number_to_use, calculate_type=calculate_type
            )
            problem2 = PowerCalculateProblem(
                number_to_use=number_to_use, calculate_type=calculate_type
            )
            math_problem_tuple_inner_list.append((problem1, problem2))
        math_problem_list_of_list.append(math_problem_tuple_inner_list)
    
    return render(request, "math_print/junior_highschool1/power/for_print.html", {'math_problem_list_of_list': math_problem_list_of_list})

def print_reduction_problem(request):

    def decide_max_and_min_number(max_number_in_post, min_number_in_post):
        """POSTから送られた計算の設定に用いる数字の最大値最小値を処理

        Args:
            max_number_in_post (str): POSTに格納されている最大値。空欄の可能性あり
            min_number_in_post (str): POSTに格納されている最小値。空欄の可能性あり 

        Returns:
            max_number (int): 用いる最大値
            min_number (int): 用いる最小値
        Considering:
            全角数字が入力された場合や、文字が入力された場合を想定するのであれば、処理させるのはここになる可能性がある
        """
        
        if bool(max_number_in_post):
            max_number = int(unicodedata.normalize("NFKD", max_number_in_post))
        else:
            max_number = 6
        
        if bool(min_number_in_post):
            min_number = int(unicodedata.normalize("NFKD", min_number_in_post))
        else:
            min_number = 2
            
        if max_number < min_number:
            max_number, min_number = min_number, max_number
        
        if max_number == 0:
            max_number += 2
        if min_number == 0:
            min_number += 1

        return max_number, min_number
    
    PROBLEM_NUMBER = 20
    paper_number = int(request.POST["paper_number"])
    fraction_type_list = request.POST.getlist("fraction_type")
    
    max_number_to_denominator, min_number_to_denominator = decide_max_and_min_number(request.POST["max_number_to_denominator"], request.POST["min_number_to_denominator"])
    max_number_to_numerator, min_number_to_numerator = decide_max_and_min_number(request.POST["max_number_to_numerator"], request.POST["min_number_to_numerator"])
    max_number_on_the_left_of_frac, min_number_on_the_left_of_frac = decide_max_and_min_number(request.POST["max_number_on_the_left_of_frac"], request.POST["min_number_on_the_left_of_frac"])
    max_number_to_reduction, min_number_to_reduction = decide_max_and_min_number(request.POST["max_number_to_reduction"], request.POST["min_number_to_reduction"])
    
    math_problem_list_of_list = []
    for _ in range(paper_number):
        math_problem_tuple_inner_list = []
        for _ in range(int(PROBLEM_NUMBER//2)):
            problem1 = ReductionProblem(
                fraction_type_list=fraction_type_list,
            min_number_to_denominator=min_number_to_denominator, max_number_to_denominator=max_number_to_denominator,
            min_number_to_numerator=min_number_to_numerator, max_number_to_numerator=max_number_to_numerator,
            min_number_on_the_left_of_frac=min_number_on_the_left_of_frac, max_number_on_the_left_of_frac=max_number_on_the_left_of_frac,
            min_number_to_reduction=min_number_to_reduction, max_number_to_reduction=max_number_to_reduction
            )
            problem2 = ReductionProblem(
                fraction_type_list=fraction_type_list,
            min_number_to_denominator=min_number_to_denominator, max_number_to_denominator=max_number_to_denominator,
            min_number_to_numerator=min_number_to_numerator, max_number_to_numerator=max_number_to_numerator,
            min_number_on_the_left_of_frac=min_number_on_the_left_of_frac, max_number_on_the_left_of_frac=max_number_on_the_left_of_frac,
            min_number_to_reduction=min_number_to_reduction, max_number_to_reduction=max_number_to_reduction
            )
            math_problem_tuple_inner_list.append((problem1, problem2))
        math_problem_list_of_list.append(math_problem_tuple_inner_list)
    
    return render(request, 'math_print/elementary_school5/reduction/for_print.html', {'math_problem_list_of_list': math_problem_list_of_list})

def print_conversion_between_frac_and_decimal_problem(request):
    PROBLEM_NUMBER = 20
    
    conversion_type_list = request.POST.getlist("conversion_type")
    below_the_decimal_point_with_string = request.POST.getlist("below_the_decimal_point")
    below_the_decimal_point_with_int = [int(num) for num in below_the_decimal_point_with_string]
    paper_number = int(request.POST["paper_number"])
    
    math_problem_list_of_list = []
    for _ in range(paper_number):
        math_problem_tuple_inner_list = []
        for _ in range(int(PROBLEM_NUMBER//2)):
            problem1 = ConversionBetweenFracAndDecimalProblem(
                conversion_type_list=conversion_type_list, below_the_decimal_point_list=below_the_decimal_point_with_int
            )
            problem2 = ConversionBetweenFracAndDecimalProblem(
                conversion_type_list=conversion_type_list, below_the_decimal_point_list=below_the_decimal_point_with_int
            )
            math_problem_tuple_inner_list.append((problem1, problem2))
        math_problem_list_of_list.append(math_problem_tuple_inner_list)
    
    return render(request, 'math_print/elementary_school5/conversion_between_frac_and_decimal/for_print.html', {'math_problem_list_of_list': math_problem_list_of_list})

def print_quadratic_function(request):
    PROBLEM_NUMBER = 20
    
    problem_type_list = request.POST.getlist("problem_type")
    used_point_number_type_list = request.POST.getlist("used_point_number_type")
    used_coefficient_number_type_list = request.POST.getlist("used_coefficient_number_type")
    paper_number = int(request.POST["paper_number"])
    
    math_problem_list_of_list = []
    for _ in range(paper_number):
        math_problem_tuple_inner_list = []
        for _ in range(int(PROBLEM_NUMBER//2)):
            problem1 = QuadraticFunctionProblem(
                problem_type_list=problem_type_list, used_point_number_type_list=used_point_number_type_list,
                used_coefficient_number_type_list=used_coefficient_number_type_list
            )
            problem2 = QuadraticFunctionProblem(
                problem_type_list=problem_type_list, used_point_number_type_list=used_point_number_type_list,
                used_coefficient_number_type_list=used_coefficient_number_type_list
            )
            math_problem_tuple_inner_list.append((problem1, problem2))
        math_problem_list_of_list.append(math_problem_tuple_inner_list)
    
    return render(request, 'math_print/junior_highschool3/quadratic_function/for_print.html', {'math_problem_list_of_list': math_problem_list_of_list})

def print_fraction_calculate_problem(request):
    PROBLEM_NUMBER = 20
    def decide_max_and_min_number(max_number_in_post, min_number_in_post):
        """POSTから送られた計算の設定に用いる数字の最大値最小値を処理

        Args:
            max_number_in_post (str): POSTに格納されている最大値。空欄の可能性あり
            min_number_in_post (str): POSTに格納されている最小値。空欄の可能性あり 

        Returns:
            max_number (int): 用いる最大値
            min_number (int): 用いる最小値
        Considering:
            全角数字が入力された場合や、文字が入力された場合を想定するのであれば、処理させるのはここになる可能性がある
        """
        
        if bool(max_number_in_post):
            max_number = int(unicodedata.normalize("NFKD", max_number_in_post))
        else:
            max_number = 6
        
        if bool(min_number_in_post):
            min_number = int(unicodedata.normalize("NFKD", min_number_in_post))
        else:
            min_number = 2
            
        if max_number < min_number:
            max_number, min_number = min_number, max_number
        
        if max_number == 0:
            max_number += 2
        if min_number == 0:
            min_number += 1

        return max_number, min_number
    
    fraction_type_list = request.POST.getlist("fraction_type_for_calculate")
    PROBLEM_NUMBER = 20
    
    max_number_to_denominator, min_number_to_denominator = decide_max_and_min_number(request.POST["max_number_to_denominator"], request.POST["min_number_to_denominator"])
    max_number_to_numerator, min_number_to_numerator = decide_max_and_min_number(request.POST["max_number_to_numerator"], request.POST["min_number_to_numerator"])
    max_number_on_the_left_of_frac, min_number_on_the_left_of_frac = decide_max_and_min_number(request.POST["max_number_on_the_left_of_frac"], request.POST["min_number_on_the_left_of_frac"])
    
    calculate_type_list = request.POST.getlist("fraction_calculate_type")
    fraction_type_list = request.POST.getlist("fraction_type_for_calculate")
    term_number = int(request.POST["term_number_for_fraction_calculate"])
    paper_number = int(request.POST["paper_number"])
    
    math_problem_list_of_list = []
    for _ in range(paper_number):
        math_problem_tuple_inner_list = []
        for _ in range(int(PROBLEM_NUMBER//2)):
            problem1 = FractionCalculateProblem(
                calculate_type_list=calculate_type_list, fraction_type_list=fraction_type_list,
                term_number=term_number,
                min_number_to_denominator=min_number_to_denominator, max_number_to_denominator=max_number_to_denominator,
                min_number_to_numerator=min_number_to_numerator, max_number_to_numerator=max_number_to_numerator,
                min_number_on_the_left_of_frac=min_number_on_the_left_of_frac, max_number_on_the_left_of_frac=max_number_on_the_left_of_frac
            )
            problem2 = FractionCalculateProblem(
                calculate_type_list=calculate_type_list, fraction_type_list=fraction_type_list,
                term_number=term_number,
                min_number_to_denominator=min_number_to_denominator, max_number_to_denominator=max_number_to_denominator,
                min_number_to_numerator=min_number_to_numerator, max_number_to_numerator=max_number_to_numerator,
                min_number_on_the_left_of_frac=min_number_on_the_left_of_frac, max_number_on_the_left_of_frac=max_number_on_the_left_of_frac
            )
            math_problem_tuple_inner_list.append((problem1, problem2))
        math_problem_list_of_list.append(math_problem_tuple_inner_list)
    
    return render(request, 'math_print/elementary_school5/fraction_calculate/for_print.html', {'math_problem_list_of_list': math_problem_list_of_list})

def print_number_without_bracket_problem(request):
    PROBLEM_NUMBER = 20
    
    operators_to_use = request.POST.getlist("number_without_bracket_operator_to_use")
    if not(operators_to_use):
        operators_to_use.append("plus")
        operators_to_use.append("minus")
    numbers_to_use = request.POST.getlist("number_without_bracket_number_to_use")
    if not(numbers_to_use):
        numbers_to_use.append("one_digit_integer")
        numbers_to_use.append("two_digit_integer")
        numbers_to_use.append("frac")
        numbers_to_use.append("decimal")
    term_numbers = request.POST.getlist("number_without_bracket_term_number")
    if not(term_numbers):
        term_numbers.append("2")
        term_numbers.append("3")
        term_numbers.append("4")
        term_numbers.append("5")
        term_numbers.append("6")
    paper_number = int(request.POST["paper_number"])
    
    math_problem_list_of_list = []
    for _ in range(paper_number):
        math_problem_tuple_inner_list = []
        for _ in range(int(PROBLEM_NUMBER//2)):
            problem1 = NumberWithoutBracketCalculateProblem(
                operators_to_use=operators_to_use, numbers_to_use=numbers_to_use,
                term_numbers=term_numbers
            )
            problem2 = NumberWithoutBracketCalculateProblem(
                operators_to_use=operators_to_use, numbers_to_use=numbers_to_use,
                term_numbers=term_numbers
            )
            math_problem_tuple_inner_list.append((problem1, problem2))
        math_problem_list_of_list.append(math_problem_tuple_inner_list)
    
    return render(request, 'math_print/junior_highschool1/number_without_bracket/for_print.html', {'math_problem_list_of_list': math_problem_list_of_list})

    
def print_sector_problem(request):
    PROBLEM_NUMBER = 20
    
    problem_type_list = request.POST.getlist("sector_problem_type")
    paper_number = int(request.POST["paper_number"])
    
    if request.POST["show_formula"] == "show_sector_formula":
        is_show_formula = True
    else:
        is_show_formula = False
    
    math_problem_list_of_list = []
    for _ in range(paper_number):
        math_problem_tuple_inner_list = []
        for _ in range(int(PROBLEM_NUMBER//2)):
            problem1 = SectorProblem(problem_type_list=problem_type_list)
            problem2 = SectorProblem(problem_type_list=problem_type_list)
            math_problem_tuple_inner_list.append((problem1, problem2))
        math_problem_list_of_list.append(math_problem_tuple_inner_list)
    
    return render(request, 'math_print/junior_highschool1/sector/for_print.html', {'math_problem_list_of_list': math_problem_list_of_list, 'is_show_formula': is_show_formula})

def print_factorization(request):
    PROBLEM_NUMBER = 20
    used_coefficient = request.POST["coefficient_used_for_factorization"]
    paper_number = int(request.POST["paper_number"])

    factorization_type_list = request.POST.getlist("factorization_type")
    if not(factorization_type_list):
        factorization_type_list.append('ax+ab=a(x+b)')
        factorization_type_list.append('x^2+2ax+a^2=(x+a)^2')
        factorization_type_list.append('x^2-2ax+a^2=(x-a)^2')
        factorization_type_list.append('x^2+(a+b)x+ab=(x+a)(x+b)')
        factorization_type_list.append('x^2-a^2=(x+a)(x-a)')
    
    used_formula_list = []
    if request.POST["show_formula"] == "show_factorization_formula":
        if "ax+ab=a(x+b)" in factorization_type_list:
            used_formula_list.append("\( ax + ab = a(x + b) \)")
        if "x^2+2ax+a^2=(x+a)^2" in factorization_type_list:
            used_formula_list.append("\( x^2 + 2ax + a^2 = (x + a)^2 \)")
        if "x^2-2ax+a^2=(x-a)^2" in factorization_type_list:
            used_formula_list.append("\( x^2 - 2ax + a^2 = (x - a)^2 \)")
        if "x^2+(a+b)x+ab=(x+a)(x+b)" in factorization_type_list:
            used_formula_list.append("\( x^2 + (a + b)x + ab = (x + a)(x + b) \)")
        if "x^2-a^2=(x+a)(x-a)" in factorization_type_list:
            used_formula_list.append("\( x^2 - a^2 = (x + a)(x - a) \)")

    # divide used_formula_list
    used_formula_tuple_in_list = []
    formula_list_length = len(used_formula_list)
    for index in range(0, formula_list_length, 2):
        if (index + 1) >= formula_list_length:
            inner_tuple = (used_formula_list[index],)
        else:
            inner_tuple = (used_formula_list[index], used_formula_list[index+1])
        used_formula_tuple_in_list.append(inner_tuple)
    
    math_problem_list_of_list = []
    for _ in range(paper_number):
        math_problem_tuple_inner_list = []
        for _ in range(int(PROBLEM_NUMBER//2)):
            problem1 = FactorizationProblem(factorization_type_list=factorization_type_list, used_coefficient=used_coefficient)
            problem2 = FactorizationProblem(factorization_type_list=factorization_type_list, used_coefficient=used_coefficient)
            math_problem_tuple_inner_list.append((problem1, problem2))
        math_problem_list_of_list.append(math_problem_tuple_inner_list)
    
    context = {}
    context["math_problem_list_of_list"] = math_problem_list_of_list
    context["used_formula_tuple_in_list"] = used_formula_tuple_in_list

    return render(request, 'math_print/junior_highschool3/factorization/for_print.html', context)

def print_quadratic_equation(request):
    PROBLEM_NUMBER = 20
    
    quadratic_equation_type_list = request.POST.getlist("quadratic_equation_type")
    if not(quadratic_equation_type_list):
        quadratic_equation_type_list.append("x^2=k")
        quadratic_equation_type_list.append("x^2+2ax+a^2=(x+a)^2")
        quadratic_equation_type_list.append("x^2-2ax+a^2=(x-a)^2")
        quadratic_equation_type_list.append("x^2+(a+b)x+ab=(x+a)(x+b)")
        quadratic_equation_type_list.append("x^2-a^2=(x+a)(x-a)")
        quadratic_equation_type_list.append("quadratic_formula")
    paper_number = int(request.POST["paper_number"])
    if request.POST["organization_coefficient_or_not"] == "organization_coefficient":
        organization_coefficient = True
    else:
        organization_coefficient = False
    
    used_formula_list = []
    if quadratic_equation_type_list:
        if "x^2=k" in quadratic_equation_type_list:
            used_formula_list.append("\( x^2 = k \Leftrightarrow x = \pm \sqrt{{k}} \)")
        if "x^2+2ax+a^2=(x+a)^2" in quadratic_equation_type_list:
            used_formula_list.append("\( x^2 + 2ax + a^2 = (x + a)^2 \)")
        if "x^2-2ax+a^2=(x-a)^2" in quadratic_equation_type_list:
            used_formula_list.append("\( x^2 - 2ax + a^2 = (x - a)^2 \)")
        if "x^2+(a+b)x+ab=(x+a)(x+b)" in quadratic_equation_type_list:
            used_formula_list.append("\( x^2+(a+b)x+ab=(x+a)(x+b) \)")
        if "x^2-a^2=(x+a)(x-a)" in quadratic_equation_type_list:
            used_formula_list.append("\( x^2-a^2=(x+a)(x-a) \)")
        if "quadratic_formula" in quadratic_equation_type_list:
            used_formula_list.append("\( ax^2 + bx + c = 0 \Leftrightarrow x = \\frac{-b\pm\sqrt{b^2-4ac}}{2a} \)")
    else:
        used_formula_list.append("\( x^2 = k \Leftrightarrow x = \pm \sqrt{{k}} \)")
        used_formula_list.append("\( x^2 + 2ax + a^2 = (x + a)^2 \)")
        used_formula_list.append("\( x^2 - 2ax + a^2 = (x - a)^2 \)")
        used_formula_list.append("\( x^2+(a+b)x+ab=(x+a)(x+b) \)")
        used_formula_list.append("\( x^2-a^2=(x+a)(x-a) \)")
        used_formula_list.append("\( ax^2 + bx + c = 0 \Leftrightarrow x = \\frac{-b\pm\sqrt{b^2-4ac}}{2a} \)")
        
    math_problem_list_of_list = []
    for _ in range(paper_number):
        math_problem_tuple_inner_list = []
        for _ in range(int(PROBLEM_NUMBER//2)):
            problem1 = QuadraticEquationProblem(
                quadratic_equation_type_list=quadratic_equation_type_list, organization_coefficient=organization_coefficient
            )
            problem2 = QuadraticEquationProblem(
                quadratic_equation_type_list=quadratic_equation_type_list, organization_coefficient=organization_coefficient
            )
            math_problem_tuple_inner_list.append((problem1, problem2))
        math_problem_list_of_list.append(math_problem_tuple_inner_list)
    
    context = {}
    context["math_problem_list_of_list"] = math_problem_list_of_list
    context["used_formula_list"] = used_formula_list

    return render(request, 'math_print/junior_highschool3/quadratic_equation/for_print.html', context)

def hs1_print_expand_equation(request):
    PROBLEM_NUMBER = 20
    paper_number = int(request.POST["paper_number"])
    """
    '(a+b)^2=a^2+2ab+b^2', '(a-b)^2=a^2-2ab+b^2',
    '(a+b)(a-b)=a^2-b^2',
    '(ax+b)(cx+d)=acx^2+(ad+bc)x+ab', '(a+b+c)^2=a^2+b^2+c^2+2ab+2bc+2ca',
    '(a+b)^3=a^3+3a^2b+3ab^2+b^3', '(a-b)^3=a^3-3a^2b+3ab^2-b^3',
    '(a+b)(a^2-ab+b^2)=a^3+b^3', '(a-b)(a^2+ab+b^2)=a^3-b^3'
    """
    expand_equation_type_list = request.POST.getlist("used_formula_for_expand")
    if not(expand_equation_type_list):
        expand_equation_type_list.append('(a+b)^2=a^2+2ab+b^2')
        expand_equation_type_list.append('(a-b)^2=a^2-2ab+b^2')
        expand_equation_type_list.append('(a+b)(a-b)=a^2-b^2')
        expand_equation_type_list.append('(ax+b)(cx+d)=acx^2+(ad+bc)x+ab')
        expand_equation_type_list.append('(a+b+c)^2=a^2+b^2+c^2+2ab+2bc+2ca')
        expand_equation_type_list.append('(a+b)^3=a^3+3a^2b+3ab^2+b^3')
        expand_equation_type_list.append('(a-b)^3=a^3-3a^2b+3ab^2-b^3')
        expand_equation_type_list.append('(a+b)(a^2-ab+b^2)=a^3+b^3')
        expand_equation_type_list.append('(a-b)(a^2+ab+b^2)=a^3-b^3')
    
    used_formula_list = []
    if request.POST["show_formula"] == "show_expansion_formula":
        if '(a+b)^2=a^2+2ab+b^2' in expand_equation_type_list:
            used_formula_list.append("\( (a+b)^2=a^2+2ab+b^2 \)")
        if '(a-b)^2=a^2-2ab+b^2' in expand_equation_type_list:
            used_formula_list.append("\( (a-b)^2=a^2-2ab+b^2 \)")
        if '(a+b)(a-b)=a^2-b^2' in expand_equation_type_list:
            used_formula_list.append("\( (a+b)(a-b)=a^2-b^2 \)")
        if '(ax+b)(cx+d)=acx^2+(ad+bc)x+ab' in expand_equation_type_list:
            used_formula_list.append("\( (ax+b)(cx+d)=acx^2+(ad+bc)x+ab \)")
        if '(a+b+c)^2=a^2+b^2+c^2+2ab+2bc+2ca' in expand_equation_type_list:
            used_formula_list.append("\( (a+b+c)^2=a^2+b^2+c^2+2ab+2bc+2ca \)")
        if '(a+b)^3=a^3+3a^2b+3ab^2+b^3' in expand_equation_type_list:
            used_formula_list.append("\( (a+b)^3=a^3+3a^2b+3ab^2+b^3 \)")
        if '(a-b)^3=a^3-3a^2b+3ab^2-b^3' in expand_equation_type_list:
            used_formula_list.append("\( (a-b)^3=a^3-3a^2b+3ab^2-b^3 \)")
        if '(a+b)(a^2-ab+b^2)=a^3+b^3' in expand_equation_type_list:
            used_formula_list.append("\( (a+b)(a^2-ab+b^2)=a^3+b^3 \)")
        if '(a-b)(a^2+ab+b^2)=a^3-b^3' in expand_equation_type_list:
            used_formula_list.append("\( (a-b)(a^2+ab+b^2)=a^3-b^3 \)")
    
    # divide used_formula_list
    used_formula_tuple_in_list = []
    formula_list_length = len(used_formula_list)
    for index in range(0, formula_list_length, 2):
        if (index + 1) >= formula_list_length:
            inner_tuple = (used_formula_list[index],)
        else:
            inner_tuple = (used_formula_list[index], used_formula_list[index+1])
        used_formula_tuple_in_list.append(inner_tuple)            

    if request.POST["another_character_exists_or_not"] == "exist":
        another_character_existence = True
    else:
        another_character_existence = False

    math_problem_list_of_list = []
    for _ in range(paper_number):
        math_problem_tuple_inner_list = []
        for _ in range(int(PROBLEM_NUMBER//2)):
            problem1 = HS1ExpandEquationProblem(
                expand_equation_type_list=expand_equation_type_list, another_character_existence=another_character_existence
            )
            problem2 = HS1ExpandEquationProblem(
                expand_equation_type_list=expand_equation_type_list, another_character_existence=another_character_existence
            )
            math_problem_tuple_inner_list.append((problem1, problem2))
        math_problem_list_of_list.append(math_problem_tuple_inner_list)
    
    context = {}
    context["math_problem_list_of_list"] = math_problem_list_of_list
    context["used_formula_tuple_in_list"] = used_formula_tuple_in_list

    return render(request, 'math_print/highschool1/expand_equation/for_print.html', context)


def hs1_print_factorization(request):
    PROBLEM_NUMBER = 20
    paper_number = int(request.POST["paper_number"])

    factorization_type_list = request.POST.getlist("used_formula_for_factorization")
    if not(factorization_type_list):
        factorization_type_list.append('a^2+2ab+b^2=(a+b)^2')
        factorization_type_list.append('a^2-2ab+b^2=(a-b)^2')
        factorization_type_list.append('a^2-b^2=(a+b)(a-b)')
        factorization_type_list.append('acx^2+(ad+bc)x+ab=(ax+b)(cx+d)')
        factorization_type_list.append('a^2+b^2+c^2+2ab+2bc+2ca=(a+b+c)^2')
        factorization_type_list.append('a^3+3a^2b+3ab^2+b^3=(a+b)^3')
        factorization_type_list.append('a^3-3a^2b+3ab^2-b^3=(a-b)^3')
        factorization_type_list.append('a^3+b^3=(a+b)(a^2-ab+b^2)')
        factorization_type_list.append('a^3-b^3=(a-b)(a^2+ab+b^2)')
    
    used_formula_list = []
    if request.POST["show_formula"] == "show_factorization_formula":
        if 'a^2+2ab+b^2=(a+b)^2' in factorization_type_list:
            used_formula_list.append("\( a^2+2ab+b^2=(a+b)^2 \)")
        if 'a^2-2ab+b^2=(a-b)^2' in factorization_type_list:
            used_formula_list.append("\( a^2-2ab+b^2=(a-b)^2 \)")
        if 'a^2-b^2=(a+b)(a-b)' in factorization_type_list:
            used_formula_list.append("\( a^2-b^2=(a+b)(a-b) \)")
        if 'acx^2+(ad+bc)x+ab=(ax+b)(cx+d)' in factorization_type_list:
            used_formula_list.append("\( acx^2+(ad+bc)x+ab=(ax+b)(cx+d) \)")
        if 'a^2+b^2+c^2+2ab+2bc+2ca=(a+b+c)^2' in factorization_type_list:
            used_formula_list.append("\( a^2+b^2+c^2+2ab+2bc+2ca=(a+b+c)^2 \)")
        if 'a^3+3a^2b+3ab^2+b^3=(a+b)^3' in factorization_type_list:
            used_formula_list.append("\( a^3+3a^2b+3ab^2+b^3=(a+b)^3 \)")
        if 'a^3-3a^2b+3ab^2-b^3=(a-b)^3' in factorization_type_list:
            used_formula_list.append("\( a^3-3a^2b+3ab^2-b^3=(a-b)^3 \)")
        if 'a^3+b^3=(a+b)(a^2-ab+b^2)' in factorization_type_list:
            used_formula_list.append("\( a^3+b^3=(a+b)(a^2-ab+b^2) \)")
        if 'a^3-b^3=(a-b)(a^2+ab+b^2)' in factorization_type_list:
            used_formula_list.append("\( a^3-b^3=(a-b)(a^2+ab+b^2) \)")
    
    # divide used_formula_list
    used_formula_tuple_in_list = []
    formula_list_length = len(used_formula_list)
    for index in range(0, formula_list_length, 2):
        if (index + 1) >= formula_list_length:
            inner_tuple = (used_formula_list[index],)
        else:
            inner_tuple = (used_formula_list[index], used_formula_list[index+1])
        used_formula_tuple_in_list.append(inner_tuple)            

    if request.POST["another_character_exists_or_not"] == "exist":
        another_character_existence = True
    else:
        another_character_existence = False

    math_problem_list_of_list = []
    for _ in range(paper_number):
        math_problem_tuple_inner_list = []
        for _ in range(int(PROBLEM_NUMBER//2)):
            problem1 = HS1FactorizationProblem(
                factorization_type_list=factorization_type_list, another_character_existence=another_character_existence
            )
            problem2 = HS1FactorizationProblem(
                factorization_type_list=factorization_type_list, another_character_existence=another_character_existence
            )
            math_problem_tuple_inner_list.append((problem1, problem2))
        math_problem_list_of_list.append(math_problem_tuple_inner_list)
    
    context = {}
    context["math_problem_list_of_list"] = math_problem_list_of_list
    context["used_formula_tuple_in_list"] = used_formula_tuple_in_list

    return render(request, 'math_print/highschool1/factorization/for_print.html', context)


def print_transformation_of_equation(request):
    PROBLEM_NUMBER = 20
    
    paper_number = int(request.POST["paper_number"])
    calculate_types = request.POST.getlist("calculate_type")
    if not(calculate_types):
        calculate_types.append("addition_and_subtraction")
        calculate_types.append("multiplication_and_division")
        calculate_types.append("mixed")
    
    math_problem_list_of_list = []
    for _ in range(paper_number):
        math_problem_tuple_inner_list = []
        for _ in range(int(PROBLEM_NUMBER//2)):
            problem1 = TransformationOfEquationProblem(calculate_types=calculate_types)
            problem2 = TransformationOfEquationProblem(calculate_types=calculate_types)
            math_problem_tuple_inner_list.append((problem1, problem2))
        math_problem_list_of_list.append(math_problem_tuple_inner_list)
    
    context = {}
    context["math_problem_list_of_list"] = math_problem_list_of_list

    return render(request, 'math_print/junior_highschool2/transformation_of_equation/for_print.html', context)

def print_character_fraction(request):
    PROBLEM_NUMBER = 20
    
    term_number = int(request.POST["term_number"])
    paper_number = int(request.POST["paper_number"])
    
    math_problem_list_of_list = []
    for _ in range(paper_number):
        math_problem_tuple_inner_list = []
        for _ in range(int(PROBLEM_NUMBER//2)):
            problem1 = CharacterFractionProblem(term_number=term_number)
            problem2 = CharacterFractionProblem(term_number=term_number)
            math_problem_tuple_inner_list.append((problem1, problem2))
        math_problem_list_of_list.append(math_problem_tuple_inner_list)
    
    context = {}
    context["math_problem_list_of_list"] = math_problem_list_of_list
    
    return render(request, 'math_print/junior_highschool2/character_fraction/for_print.html', context)

def hs1_print_quadratic_function(request):
    PROBLEM_NUMBER = 20
    given_information_list = request.POST.getlist("given_information")
    if not(given_information_list):
        given_information_list.append("vertex_and_one_point")
        given_information_list.append("three_points")
        given_information_list.append("the_axis_of_symmetry_and_two_points")
        given_information_list.append("before_parabora_and_line_or_parabora_containing_vertex_and_one_point")

    paper_number = int(request.POST["paper_number"])
    
    math_problem_list_of_list = []
    for _ in range(paper_number):
        math_problem_tuple_inner_list = []
        for _ in range(int(PROBLEM_NUMBER//2)):
            problem1 = HS1QuadraticFunctionProblem(given_information_list=given_information_list)
            problem2 = HS1QuadraticFunctionProblem(given_information_list=given_information_list)
            math_problem_tuple_inner_list.append((problem1, problem2))
        math_problem_list_of_list.append(math_problem_tuple_inner_list)
    
    context = {}
    context["math_problem_list_of_list"] = math_problem_list_of_list
    
    return render(request, 'math_print/highschool1/quadratic_function/for_print.html', context)

def jhs2_print_character_problem(request):
    PROBLEM_NUMBER = 20
    
    number_to_use = request.POST.getlist("character_number_to_use")
    operator_to_use = request.POST.getlist("character_operator_to_use")
    term_number = int(request.POST["term_number"])
    paper_number = int(request.POST["paper_number"])
    character_to_use = request.POST["character_to_use"]
    character_to_use_list = ["x"]
    if character_to_use == "2":
        character_to_use_list += ["y"]

    MAX_NUMBER_TO_FRAC = 10
    MIN_NUMBER_TO_FRAC = -10

    math_problem_list_of_list = []
    for _ in range(paper_number):
        math_problem_tuple_inner_list = []
        for _ in range(int(PROBLEM_NUMBER//2)):
            problem1 = CharacterMathProblem(
                term_number=term_number, max_number_to_frac=MAX_NUMBER_TO_FRAC,
                min_number_to_frac=MIN_NUMBER_TO_FRAC, used_number_type_list=number_to_use,
                used_operator_type_list=operator_to_use, used_character_type_list=character_to_use_list
                )
            problem2 = CharacterMathProblem(
                term_number=term_number, max_number_to_frac=MAX_NUMBER_TO_FRAC,
                min_number_to_frac=MIN_NUMBER_TO_FRAC, used_number_type_list=number_to_use,
                used_operator_type_list=operator_to_use, used_character_type_list=character_to_use_list
                )
            math_problem_tuple_inner_list.append((problem1, problem2))
        math_problem_list_of_list.append(math_problem_tuple_inner_list)

    return render(request, 'math_print/junior_highschool2/character/for_print.html', {'math_problem_list_of_list': math_problem_list_of_list})

def hs1_print_quadratic_function_max_min(request):
    PROBLEM_NUMBER = 14
    
    moving_part_list = request.POST.getlist("moving_part")
    if not(moving_part_list):
        moving_part_list.append("the_axis_of_symmetry")
        moving_part_list.append("domain")
    max_min_list = request.POST.getlist("max_min")
    if not(max_min_list):
        max_min_list.append("max")
        max_min_list.append("min")
    paper_number = int(request.POST["paper_number"])
    
    math_problem_list_of_list = []
    for _ in range(paper_number):
        math_problem_tuple_inner_list = []
        for _ in range(int(PROBLEM_NUMBER//2)):
            problem1 = HS1QuadraticFunctionMaxMinProblem(moving_part_list=moving_part_list, max_min_list=max_min_list)
            problem2 = HS1QuadraticFunctionMaxMinProblem(moving_part_list=moving_part_list, max_min_list=max_min_list)
            math_problem_tuple_inner_list.append((problem1, problem2))
        math_problem_list_of_list.append(math_problem_tuple_inner_list)
    
    context = {}
    context["math_problem_list_of_list"] = math_problem_list_of_list
    
    return render(request, 'math_print/highschool1/quadratic_function_max_min/for_print.html', context)

def print_parallel_lines_and_angle(request):
    import random
    from typing import NamedTuple
    
    class ProblemTypeAndAnswerAngle(NamedTuple):
        problem_type: str
        angle: int

    PROBLEM_NUMBER = 10
    paper_number = int(request.POST["paper_number"])
    used_information_list = request.POST.getlist("used_information")
    if not(used_information_list):
        used_information_list.append("corresponding_and_alternate_angle")
        used_information_list.append("vertical_angle")
        used_information_list.append("multiple_corresponding_and_alternate_angle")
    math_problem_list_of_list = []
    for _ in range(paper_number):
        math_problem_tuple_inner_list = []
        for _ in range(int(PROBLEM_NUMBER//2)):
            problem_type1 = random.choice(used_information_list)
            answer_angle1 = random.randint(40, 120)
            problem_type_and_answer_angle1 = ProblemTypeAndAnswerAngle(problem_type1, answer_angle1)
            problem_type2 = random.choice(used_information_list)
            answer_angle2 = random.randint(40, 120)
            problem_type_and_answer_angle2 = ProblemTypeAndAnswerAngle(problem_type2, answer_angle2)
            math_problem_tuple_inner_list.append((problem_type_and_answer_angle1, problem_type_and_answer_angle2))
        math_problem_list_of_list.append(math_problem_tuple_inner_list)
    context = {}
    context["math_problem_list_of_list"] = math_problem_list_of_list
    return render(request, 'math_print/junior_highschool2/parallel_lines_and_angle/for_print.html', context)

def print_unit_conversion_problem(request):
    PROBLEM_NUMBER = 20
    
    paper_number = int(request.POST["paper_number"])
    used_unit_list = request.POST.getlist("unit_type")
    if not(used_unit_list):
        used_unit_list.append("length")
        used_unit_list.append("weight")
        used_unit_list.append("area")
        used_unit_list.append("volume")
        used_unit_list.append("time")
    
    math_problem_list_of_list = []
    for _ in range(paper_number):
        math_problem_tuple_inner_list = []
        for _ in range(int(PROBLEM_NUMBER//2)):
            problem1 = UnitConversionProblem(used_unit_list=used_unit_list)
            problem2 = UnitConversionProblem(used_unit_list=used_unit_list)
            math_problem_tuple_inner_list.append((problem1, problem2))
        math_problem_list_of_list.append(math_problem_tuple_inner_list)
    
    context = {}
    context["math_problem_list_of_list"] = math_problem_list_of_list
    
    return render(request, 'math_print/elementary_school3/unit_conversion/for_print.html', context)

def print_sector_with_figure_problem(request):
    PROBLEM_NUMBER = 10
    
    problem_type_list = request.POST.getlist("sector_problem_type")
    paper_number = int(request.POST["paper_number"])
    
    math_problem_list_of_list = []
    for _ in range(paper_number):
        math_problem_tuple_inner_list = []
        for _ in range(int(PROBLEM_NUMBER//2)):
            problem1 = SectorWithFigureProblem(problem_type_list=problem_type_list)
            problem2 = SectorWithFigureProblem(problem_type_list=problem_type_list)
            math_problem_tuple_inner_list.append((problem1, problem2))
        math_problem_list_of_list.append(math_problem_tuple_inner_list)
    
    return render(request, 'math_print/junior_highschool1/sector_with_figure/for_print.html', {'math_problem_list_of_list': math_problem_list_of_list})

def print_logarithm_calculation(request):
    PROBLEM_NUMBER = 20
    
    problem_type_list = request.POST.getlist("logarithm_calculation_type")
    if not(problem_type_list):
        problem_type_list.append("change_of_base_formula")
        problem_type_list.append("add_and_subtraction_without_change_of_base_formula")
    paper_number = int(request.POST["paper_number"])
    
    math_problem_list_of_list = []
    for _ in range(paper_number):
        math_problem_tuple_inner_list = []
        for _ in range(int(PROBLEM_NUMBER//2)):
            problem1 = LogarithmCalculationProblem(problem_type_list=problem_type_list)
            problem2 = LogarithmCalculationProblem(problem_type_list=problem_type_list)
            math_problem_tuple_inner_list.append((problem1, problem2))
        math_problem_list_of_list.append(math_problem_tuple_inner_list)
    
    return render(request, 'math_print/highschool2/logarithm_calculate/for_print.html', {'math_problem_list_of_list': math_problem_list_of_list})

def print_exponent_calculation(request):
    PROBLEM_NUMBER = 20
    
    calculation_type = request.POST["exponent_calculation_type"]

    base_type_list = request.POST.getlist("exponent_base_type")
    if not(base_type_list):
        base_type_list.append("number")
        base_type_list.append("character")
    
    paper_number = int(request.POST["paper_number"])
    
    math_problem_list_of_list = []
    for _ in range(paper_number):
        math_problem_tuple_inner_list = []
        for _ in range(int(PROBLEM_NUMBER//2)):
            problem1 = ExponentCalculation(calculation_type=calculation_type, base_type_list=base_type_list)
            problem2 = ExponentCalculation(calculation_type=calculation_type, base_type_list=base_type_list)
            math_problem_tuple_inner_list.append((problem1, problem2))
        math_problem_list_of_list.append(math_problem_tuple_inner_list)
    
    
    return render(request, 'math_print/highschool2/exponent_calculate/for_print.html', {'math_problem_list_of_list': math_problem_list_of_list})

def print_lcm_and_gcd_problem(request):
    PROBLEM_NUMBER = 20
    problem_type_list = request.POST.getlist("problem_type")
    if not(problem_type_list):
        problem_type_list.append("lcm")
        problem_type_list.append("gcd")
    max_problem_number_in_post = request.POST["max_problem_number"]
    if bool(max_problem_number_in_post):
        max_problem_number = int(unicodedata.normalize("NFKD", max_problem_number_in_post))
    else:
        max_problem_number = 100
    paper_number = int(request.POST["paper_number"])
    
    math_problem_list_of_list = []
    for _ in range(paper_number):
        math_problem_tuple_inner_list = []
        for _ in range(int(PROBLEM_NUMBER//2)):
            problem1 = LCMAndGCD(problem_type_list=problem_type_list, max_problem_number=max_problem_number)
            problem2 = LCMAndGCD(problem_type_list=problem_type_list, max_problem_number=max_problem_number)
            math_problem_tuple_inner_list.append((problem1, problem2))
        math_problem_list_of_list.append(math_problem_tuple_inner_list)
    
    return render(request, 'math_print/elementary_school5/lcm_and_gcd/for_print.html', {'math_problem_list_of_list': math_problem_list_of_list})

def print_vector_cross_point(request):
    PROBLEM_NUMBER = 2
    problem_type_list = request.POST.getlist("problem_type")
    if not(problem_type_list):
        problem_type_list.append("cross_point_of_two_line")
        problem_type_list.append("cross_point_of_plane_and_line")
    paper_number = int(request.POST["paper_number"])
    
    math_problem_list_of_list = []
    for _ in range(paper_number):
        math_problem_tuple_inner_list = []
        for _ in range(int(PROBLEM_NUMBER//2)):
            problem1 = VectorCrossPoint(problem_type_list=problem_type_list)
            problem2 = VectorCrossPoint(problem_type_list=problem_type_list)
            math_problem_tuple_inner_list.append((problem1, problem2))
        math_problem_list_of_list.append(math_problem_tuple_inner_list)
    
    return render(request, 'math_print/highschool2/vector_cross_point/for_print.html', {'math_problem_list_of_list': math_problem_list_of_list})


def print_elementary5_sector_problem(request):
    PROBLEM_NUMBER = 10
    
    problem_type_list = request.POST.getlist("problem_type")
    if not(problem_type_list):
        problem_type_list.append("standard_sector")
        problem_type_list.append("baumkuchen")
        problem_type_list.append("in_star")
        problem_type_list.append("out_star")
        problem_type_list.append("in_rugby")
        problem_type_list.append("out_rugby")
        problem_type_list.append("in_seed_and_flower")
        problem_type_list.append("out_seed_and_flower")
    paper_number = int(request.POST["paper_number"])
    
    math_problem_list_of_list = []
    for _ in range(paper_number):
        math_problem_tuple_inner_list = []
        for _ in range(int(PROBLEM_NUMBER//2)):
            problem1 = Elementary5SectorWithFigureProblem(problem_type_list=problem_type_list)
            problem2 = Elementary5SectorWithFigureProblem(problem_type_list=problem_type_list)
            math_problem_tuple_inner_list.append((problem1, problem2))
        math_problem_list_of_list.append(math_problem_tuple_inner_list)
    
    return render(request, 'math_print/elementary_school5/sector/for_print.html', {'math_problem_list_of_list': math_problem_list_of_list})

def print_fill_in_the_square_problem(request):
    PROBLEM_NUMBER = 20
    
    calculation_type_list = request.POST.getlist("calculation_type")
    if not(calculation_type_list):
        calculation_type_list.append("addition_only")
        calculation_type_list.append("subtraction_only")
        calculation_type_list.append("multiplication_only")
        calculation_type_list.append("division_only")
        calculation_type_list.append("addition_and_subtraction")
        calculation_type_list.append("multiplication_and_division")
        calculation_type_list.append("all_calculations")
    paper_number = int(request.POST["paper_number"])
    used_symbol = request.POST["used_symbol"]
    used_number_list = request.POST.getlist("used_number")
    if not(used_number_list):
        used_number_list.append("integer")
        used_number_list.append("frac")
        used_number_list.append("decimal")
    math_problem_list_of_list = []
    for _ in range(paper_number):
        math_problem_tuple_inner_list = []
        for _ in range(int(PROBLEM_NUMBER//2)):
            problem1 = FillInTheSquareProblem(
                calculation_type_list=calculation_type_list, used_symbol=used_symbol,
                used_number_list=used_number_list
                )
            problem2 = FillInTheSquareProblem(
                calculation_type_list=calculation_type_list, used_symbol=used_symbol,
                used_number_list=used_number_list)
            math_problem_tuple_inner_list.append((problem1, problem2))
        math_problem_list_of_list.append(math_problem_tuple_inner_list)
    
    return render(request, 'math_print/elementary_school6/fill_in_the_square/for_print.html', {'math_problem_list_of_list': math_problem_list_of_list, 'used_symbol': used_symbol})
  
def print_common_denominator_problem(request):
    PROBLEM_NUMBER = 20
    
    fraction_type_list = request.POST.getlist("fraction_type_for_common_denominator")
    if not(fraction_type_list):
        fraction_type_list.append("proper_fraction")
        fraction_type_list.append("improper_fraction")
        fraction_type_list.append("mixed_fraction")
    fraction_numbers_list = request.POST.getlist("fraction_numbers")
    if not(fraction_numbers_list):
        fraction_numbers_list.append(2)
        fraction_numbers_list.append(3)
    else:
        fraction_numbers_list = [int(number_str) for number_str in fraction_numbers_list]
    paper_number = int(request.POST["paper_number"])

    math_problem_list_of_list = []
    for _ in range(paper_number):
        math_problem_tuple_inner_list = []
        for _ in range(int(PROBLEM_NUMBER//2)):
            problem1 = CommonDenominatorProblem(fraction_type_list=fraction_type_list, fraction_numbers_list=fraction_numbers_list)
            problem2 = CommonDenominatorProblem(fraction_type_list=fraction_type_list, fraction_numbers_list=fraction_numbers_list)
            math_problem_tuple_inner_list.append((problem1, problem2))
        math_problem_list_of_list.append(math_problem_tuple_inner_list)
    
    return render(request, 'math_print/elementary_school5/common_denominator/for_print.html', {'math_problem_list_of_list': math_problem_list_of_list})

def print_recurrence_relation(request):
    PROBLEM_NUMBER = 4
    
    problem_type_list = request.POST.getlist("recurrence_relation_type")
    if not(problem_type_list):
        problem_type_list.append("arithmetic_progression")
        problem_type_list.append("geometric_progression")
        problem_type_list.append("progression_of_differences")
        problem_type_list.append("harmonic_progression")
        problem_type_list.append("linear_characteristic_equation")
        problem_type_list.append("coefficient_comparison_to_geometric_progression")
        problem_type_list.append("exponent_to_linear_characteristic_equation")
        problem_type_list.append("three_adjacent_terms")
    paper_number = int(request.POST["paper_number"])
    
    math_problem_list_of_list = []
    for _ in range(paper_number):
        math_problem_tuple_inner_list = []
        for _ in range(int(PROBLEM_NUMBER//2)):
            problem1 = RecurrenceRelationProblem(problem_type_list=problem_type_list)
            problem2 = RecurrenceRelationProblem(problem_type_list=problem_type_list)
            math_problem_tuple_inner_list.append((problem1, problem2))
        math_problem_list_of_list.append(math_problem_tuple_inner_list)
    
    return render(request, 'math_print/highschool2/recurrence_relation/for_print.html', {'math_problem_list_of_list': math_problem_list_of_list})

def print_square_root_problem(request):
    PROBLEM_NUMBER = 20
    problem_types = request.POST.getlist("problem_type")
    if not(problem_types):
        problem_types.append("write_square_root_not_using_radical_sign_only_with_integer")
        problem_types.append("write_square_root_not_using_radical_sign")
        problem_types.append("write_square_root_using_radical_sign_only_with_integer")
        problem_types.append("write_square_root_using_radical_sign")
        problem_types.append("put_coefficient_into_radical_sign")
        problem_types.append("take_out_coefficient_from_radical_sign_inside")
        problem_types.append("rationalize")
    paper_number = int(request.POST["paper_number"])
    math_problem_list_of_list = []
    for _ in range(paper_number):
        math_problem_tuple_inner_list = []
        for _ in range(int(PROBLEM_NUMBER//2)):
            problem1 = SquareRootProblem(problem_types=problem_types)
            problem2 = SquareRootProblem(problem_types=problem_types)
            math_problem_tuple_inner_list.append((problem1, problem2))
        math_problem_list_of_list.append(math_problem_tuple_inner_list)
    
    return render(request, 'math_print/junior_highschool3/square_root/for_print.html', {'math_problem_list_of_list': math_problem_list_of_list})

def print_square_root_calculate_problem(request):
    PROBLEM_NUMBER = 20
    calculation_types = request.POST.getlist("calculation_type")
    if not(calculation_types):
        calculation_types.append("addition_and_subtraction_only")
        calculation_types.append("multiplication_and_division_only")
        calculation_types.append("using_expand_formula")
    paper_number = int(request.POST["paper_number"])
    math_problem_list_of_list = []
    for _ in range(paper_number):
        math_problem_tuple_inner_list = []
        for _ in range(int(PROBLEM_NUMBER//2)):
            problem1 = SquareRootCalculateProblem(calculation_types=calculation_types)
            problem2 = SquareRootCalculateProblem(calculation_types=calculation_types)
            math_problem_tuple_inner_list.append((problem1, problem2))
        math_problem_list_of_list.append(math_problem_tuple_inner_list)
    
    return render(request, 'math_print/junior_highschool3/square_root_calculate/for_print.html', {'math_problem_list_of_list': math_problem_list_of_list})

def print_base_n_numbers(request):
    PROBLEM_NUMBER = 20
    convert_from_to_types = request.POST.getlist("convert_from_to_type")
    if not(convert_from_to_types):
        convert_from_to_types.append("from_n_base_to_ten_base")
        convert_from_to_types.append("from_ten_base_to_n_base")
    numbers_to_convert = request.POST.getlist("number_to_convert")
    if not(numbers_to_convert):
        numbers_to_convert.append("integer")
        numbers_to_convert.append("decimal")
    paper_number = int(request.POST["paper_number"])
    math_problem_list_of_list = []
    for _ in range(paper_number):
        math_problem_tuple_inner_list = []
        for _ in range(int(PROBLEM_NUMBER//2)):
            problem1 = BaseNNumbersProblem(convert_from_to_types=convert_from_to_types, numbers_to_convert=numbers_to_convert)
            problem2 = BaseNNumbersProblem(convert_from_to_types=convert_from_to_types, numbers_to_convert=numbers_to_convert)
            math_problem_tuple_inner_list.append((problem1, problem2))
        math_problem_list_of_list.append(math_problem_tuple_inner_list)
    
    return render(request, 'math_print/highschool1/base_n_numbers/for_print.html', {'math_problem_list_of_list': math_problem_list_of_list}) 

def print_linear_function_with_graph(request):
    PROBLEM_NUMBER = 10
    
    problem_types = request.POST.getlist("problem_type")
    if not(problem_types):
        problem_types.append("with_grid_to_linear_function")
        problem_types.append("without_grid_to_linear_function")
        problem_types.append("linear_function_to_with_grid")
        problem_types.append("coefficient_and_intercept_to_with_grid")
    paper_number = int(request.POST["paper_number"])
    
    math_problem_list_of_list = []
    for _ in range(paper_number):
        math_problem_tuple_inner_list = []
        for _ in range(int(PROBLEM_NUMBER//2)):
            problem1 = LinearFunctionWithGraphProblem(problem_types=problem_types)
            problem2 = LinearFunctionWithGraphProblem(problem_types=problem_types)
            math_problem_tuple_inner_list.append((problem1, problem2))
        math_problem_list_of_list.append(math_problem_tuple_inner_list)
    
    return render(request, 'math_print/junior_highschool2/linear_function_with_graph/for_print.html', {'math_problem_list_of_list': math_problem_list_of_list})


def print_trigonometric_ratio(request):
    PROBLEM_NUMBER = 10
    
    problem_types = request.POST.getlist("problem_type")
    if not(problem_types):
        problem_types.append("value_to_degree")
        problem_types.append("degree_to_value")
        problem_types.append("mutual_relationships")
    
    used_trigonometric_ratios = request.POST.getlist("used_trigonometric_ratio")
    if not(used_trigonometric_ratios):
        used_trigonometric_ratios.append("sin")
        used_trigonometric_ratios.append("cos")
        used_trigonometric_ratios.append("tan")
    
    degree_range = request.POST["degree_range"]  
    
    paper_number = int(request.POST["paper_number"])
    
    math_problem_list_of_list = []
    for _ in range(paper_number):
        math_problem_tuple_inner_list = []
        for _ in range(int(PROBLEM_NUMBER//2)):
            problem1 = TrigonometricRatioProblem(
                problem_types=problem_types, used_trigonometric_ratios=used_trigonometric_ratios,
                degree_range=degree_range)
            problem2 = TrigonometricRatioProblem(
                problem_types=problem_types, used_trigonometric_ratios=used_trigonometric_ratios,
                degree_range=degree_range)
            math_problem_tuple_inner_list.append((problem1, problem2))
        math_problem_list_of_list.append(math_problem_tuple_inner_list)
    
    return render(request, 'math_print/highschool1/trigonometric_ratio/for_print.html', {'math_problem_list_of_list': math_problem_list_of_list})


def print_trigonometric_function(request):
    PROBLEM_NUMBER = 10
    
    problem_types = request.POST.getlist("trigonometric_function_problem_type")
    if not(problem_types):
        problem_types.append("value_to_radian")
        problem_types.append("radian_to_value")
        problem_types.append("mutual_relationships")
    
    radian_range = request.POST["radian_range"]
    
    used_trigonometric_functions = request.POST.getlist("used_trigonometric_function")
    if not(used_trigonometric_functions):
        used_trigonometric_functions.append("sin")
        used_trigonometric_functions.append("cos")
        used_trigonometric_functions.append("tan")
    
    paper_number = int(request.POST["paper_number"])
    
    math_problem_list_of_list = []
    for _ in range(paper_number):
        math_problem_tuple_inner_list = []
        for _ in range(int(PROBLEM_NUMBER//2)):
            problem1 = TrigonometricFunctionProblem(
                problem_types=problem_types, used_trigonometric_functions=used_trigonometric_functions,
                radian_range=radian_range)
            problem2 = TrigonometricFunctionProblem(
                problem_types=problem_types, used_trigonometric_functions=used_trigonometric_functions,
                radian_range=radian_range)
            math_problem_tuple_inner_list.append((problem1, problem2))
        math_problem_list_of_list.append(math_problem_tuple_inner_list)
    
    return render(request, 'math_print/highschool2/trigonometric_function/for_print.html', {'math_problem_list_of_list': math_problem_list_of_list})


def print_quadratic_inequality(request):
    PROBLEM_NUMBER = 20
    used_quadratic_equation = request.POST.getlist("used_quadratic_equation")
    if not(used_quadratic_equation):
        used_quadratic_equation.append("two_different_answer")
        used_quadratic_equation.append("same_answer")
        used_quadratic_equation.append("no_answer")
    used_answer_in_quadratic_equation = request.POST.getlist("used_answer_in_quadratic_equation")
    if not(used_answer_in_quadratic_equation):
        used_answer_in_quadratic_equation.append("integer")
        used_answer_in_quadratic_equation.append("frac")
    paper_number = int(request.POST["paper_number"])
    math_problem_list_of_list = []
    for _ in range(paper_number):
        math_problem_tuple_inner_list = []
        for _ in range(int(PROBLEM_NUMBER // 2)):
            problem1 = QuadraticInequality(used_quadratic_equation=used_quadratic_equation, used_answer_in_quadratic_equation=used_answer_in_quadratic_equation)
            problem2 = QuadraticInequality(used_quadratic_equation=used_quadratic_equation, used_answer_in_quadratic_equation=used_answer_in_quadratic_equation)
            math_problem_tuple_inner_list.append((problem1, problem2))
        math_problem_list_of_list.append(math_problem_tuple_inner_list)
    return render(request, 'math_print/highschool1/quadratic_inequality/for_print.html', {'math_problem_list_of_list': math_problem_list_of_list})


def print_same_denominator_calculate_problem(request):
    PROBLEM_NUMBER = 20
    calculate_type = request.POST.getlist("same_denominator_calculate_type")
    if not(calculate_type):
        calculate_type.append("addition")
        calculate_type.append("subtraction")
    paper_number = int(request.POST["paper_number"])
    term_number = request.POST.getlist("term_number")
    if not(term_number):
        term_number.append("2")
        term_number.append("3")
        term_number.append("4")
    math_problem_list_of_list = []
    for _ in range(paper_number):
        math_problem_tuple_inner_list = []
        for _ in range(int(PROBLEM_NUMBER // 2)):
            problem1 = SameDenominatorCalculate(calculate_type=calculate_type, term_number=term_number)
            problem2 = SameDenominatorCalculate(calculate_type=calculate_type, term_number=term_number)
            math_problem_tuple_inner_list.append((problem1, problem2))
        math_problem_list_of_list.append(math_problem_tuple_inner_list)
    return render(request, 'math_print/elementary_school3/same_denominator_calculate/for_print.html', {'math_problem_list_of_list': math_problem_list_of_list})


def print_line_and_flat_positional_relationship(request):
    """印刷用の直線と平面の位置関係の問題のリクエスト受信と問題出力と担当。
    
    Args:
        request (django.core.handlers.wsgi.WSGIRequest): 送信されたリクエスト
    
    Returns:
        math_problem_tuple_list (list): 2問ずつ問題が格納されたタプルのリスト
    """
    PROBLEM_NUMBER = 6
    paper_number = int(request.POST["paper_number"])
    question_format = request.POST["question_format"]
    used_problems = request.POST.getlist("used_problem")
    if not(used_problems):
        used_problems.append("line_and_line")
        used_problems.append("line_and_flat")
        used_problems.append("flat_and_flat")
    used_solid_bodies = request.POST.getlist("used_solid_body")
    if not(used_solid_bodies):
        used_solid_bodies.append("quadrangular_prism")
        used_solid_bodies.append("triangular_prism")
    math_problem_list_of_list = []
    for _ in range(paper_number):
        math_problem_tuple_inner_list = []
        for _ in range(int(PROBLEM_NUMBER // 2)):
            problem1 = LineAndFlatPositionalRelationship(used_problems=used_problems, used_solid_bodies=used_solid_bodies, question_format=question_format)
            problem2 = LineAndFlatPositionalRelationship(used_problems=used_problems, used_solid_bodies=used_solid_bodies, question_format=question_format)
            math_problem_tuple_inner_list.append((problem1, problem2))
        math_problem_list_of_list.append(math_problem_tuple_inner_list)
    return render(request, 'math_print/junior_highschool1/line_and_flat_positional_relationship/for_print.html', {'math_problem_list_of_list': math_problem_list_of_list})


def print_calculate_area_by_integration(request):
    PROBLEM_NUMBER = 2
    paper_number = int(request.POST["paper_number"])
    problem_types = []
    problem_types += request.POST.getlist("one_sixth_problem_type")
    problem_types += request.POST.getlist("one_third_problem_type")
    problem_types += request.POST.getlist("one_twelfth_problem_type")
    if not (problem_types):
        problem_types.append("between_quadratic_function_and_x_axis")
        problem_types.append("between_quadratic_function_and_line")
        problem_types.append("between_quadratic_functions")
        problem_types.append("between_cubic_functions")
        problem_types.append("between_quadratic_function_and_tangent_and_parallel_line_with_y_axis")
        problem_types.append("between_two_quadratic_functions_that_touch_each_other_and_parallel_line_with_y_axis")
        problem_types.append("between_quadratic_function_and_two_tangents")
    math_problem_list_of_list = []
    for _ in range(paper_number):
        math_problem_tuple_inner_list = []
        for _ in range(int(PROBLEM_NUMBER//2)):
            problem1 = CalculateAreaByIntegration(problem_types=problem_types)
            problem2 = CalculateAreaByIntegration(problem_types=problem_types)
            math_problem_tuple_inner_list.append((problem1, problem2))
        math_problem_list_of_list.append(math_problem_tuple_inner_list)
    return render(request, 'math_print/highschool2/calculate_area_by_integration/for_print.html', {'math_problem_list_of_list': math_problem_list_of_list})


def print_logarithmic_equation(request):
    """印刷用対数方程式の問題のリクエスト受信と問題出力を担当

    Args:
        request (django.core.handlers.wsgi.WSGIRequest): 送信されたリクエスト

    Returns:
        render (django.http.response.HttpResponse): Httpでページを表示するための諸要素
    """
    paper_number = int(request.POST["paper_number"])
    PROBLEM_NUMBER = 4
    problem_types = request.POST.getlist("logarithmic_equation_type")
    if not(problem_types):
        problem_types.append("only_with_calculation")
        problem_types.append("with_calculation_and_change_base_of_formula")
        problem_types.append("with_replacement")
    math_problem_list_of_list = []
    for _ in range(paper_number):
        math_problem_tuple_inner_list = []
        for _ in range(int(PROBLEM_NUMBER//2)):
            problem1 = LogarithmicEquation(problem_types=problem_types)
            problem2 = LogarithmicEquation(problem_types=problem_types)
            math_problem_tuple_inner_list.append((problem1, problem2))
        math_problem_list_of_list.append(math_problem_tuple_inner_list)
    return render(request, 'math_print/highschool2/logarithmic_equation/for_print.html', {"math_problem_list_of_list": math_problem_list_of_list})


def print_ratio(request):
    """割合の問題のリクエスト受信と問題出力を担当

    Args:
        request (django.core.handlers.wsgi.WSGIRequest): 送信されたリクエスト

    Returns:
        render (django.http.response.HttpResponse): Httpでページを表示するための諸要素
    """
    PROBLEM_NUMBER = 8
    paper_number = int(request.POST["paper_number"])
    problem_types = request.POST.getlist("problem_type")
    if not(problem_types):
        problem_types.append("amount_to_compare")
        problem_types.append("standard_amount")
        problem_types.append("ratio")
    used_numbers_for_ratio = request.POST.getlist("used_number_for_ratio")
    if not(used_numbers_for_ratio):
        used_numbers_for_ratio.append("decimal")
        used_numbers_for_ratio.append("percentage")
        used_numbers_for_ratio.append("japanese_percentage")
    unit_change = request.POST["unit_change"]
    if unit_change == "yes":
        used_unit_change = True
    elif unit_change == "no":
        used_unit_change = False
    digit_under_the_decimal_point = [int(num_str) for num_str in request.POST.getlist("digit_under_the_decimal_point")]
    if not(digit_under_the_decimal_point):
        digit_under_the_decimal_point.append(1)
        digit_under_the_decimal_point.append(2)
        digit_under_the_decimal_point.append(3)
    math_problem_list_of_list = []
    for _ in range(paper_number):
        math_problem_tuple_inner_list = []
        for _ in range(int(PROBLEM_NUMBER//2)):
            problem1 = RatioProblem(
                problem_types=problem_types, used_numbers_for_ratio=used_numbers_for_ratio,
                used_unit_change=used_unit_change, digit_under_the_decimal_point=digit_under_the_decimal_point
            )
            problem2 = RatioProblem(
                problem_types=problem_types, used_numbers_for_ratio=used_numbers_for_ratio,
                used_unit_change=used_unit_change, digit_under_the_decimal_point=digit_under_the_decimal_point
            )
            math_problem_tuple_inner_list.append((problem1, problem2))
        math_problem_list_of_list.append(math_problem_tuple_inner_list)
    return render(request, 'math_print/elementary_school5/ratio/for_print.html', {"math_problem_list_of_list": math_problem_list_of_list})


def print_division_for_elementary_school3(request):
    """小学3年生用の割り算のプリントの出力を担当

    Args:
        request (django.core.handlers.wsgi.WSGIRequest): 送信されたリクエスト

    Returns:
        render (django.http.response.HttpResponse): Httpでページを表示するための諸要素
    """
    PROBLEM_NUMBER = 20
    paper_number = int(request.POST["paper_number"])
    remainder_types = request.POST.getlist("remainder_type")
    if not(remainder_types):
        remainder_types.append("without_remainder")
        remainder_types.append("with_remainder")
    digit_of_divided_numbers = request.POST.getlist("digit_of_divided_number")
    if not(digit_of_divided_numbers):
        digit_of_divided_numbers.append("1")
        digit_of_divided_numbers.append("2")
    math_problem_list_of_list = []
    for _ in range(paper_number):
        math_problem_tuple_inner_list = []
        for _ in range(int(PROBLEM_NUMBER // 2)):
            problem1 = DivisionFor3rdGrade(remainder_types=remainder_types, digit_of_divided_numbers=digit_of_divided_numbers)
            problem2 = DivisionFor3rdGrade(remainder_types=remainder_types, digit_of_divided_numbers=digit_of_divided_numbers)
            math_problem_tuple_inner_list.append((problem1, problem2))
        math_problem_list_of_list.append(math_problem_tuple_inner_list)
    return render(request, 'math_print/elementary_school3/division/for_print.html', {"math_problem_list_of_list": math_problem_list_of_list})


def print_addition_and_subtraction_for_elementary_school3(request):
    """小学3年生用の足し算引き算の問題のプリント表示を担当

    Args:
        request (django.core.handlers.wsgi.WSGIRequest): 送信されたリクエスト

    Returns:
        render (django.http.response.HttpResponse): Httpでページを表示するための諸要素    
    """
    PROBLEM_NUMBER = 20
    paper_number = int(request.POST["paper_number"])
    used_calculations = request.POST.getlist("used_calculation")
    if not(used_calculations):
        used_calculations.append("addition")
        used_calculations.append("subtraction")
    digits_of_number = request.POST.getlist("digit_of_number")
    if not(digits_of_number):
        digits_of_number.append("3")
        digits_of_number.append("4")
        digits_of_number.append("5")
    math_problem_list_of_list = []
    for _ in range(paper_number):
        math_problem_tuple_inner_list = []
        for _ in range(int(PROBLEM_NUMBER // 2)):
            problem1 = AdditionAndSubtractionFor3rdGrade(used_calculations=used_calculations, digits_of_number=digits_of_number)
            problem2 = AdditionAndSubtractionFor3rdGrade(used_calculations=used_calculations, digits_of_number=digits_of_number)
            math_problem_tuple_inner_list.append((problem1, problem2))
        math_problem_list_of_list.append(math_problem_tuple_inner_list)
    return render(request, 'math_print/elementary_school3/addition_and_subtraction/for_print.html', {"math_problem_list_of_list": math_problem_list_of_list})


def print_multiplication_for_elementary_school3(request):
    """小学3年生用の掛け算の問題のプリント表示を担当

    Args:
        request (django.core.handlers.wsgi.WSGIRequest): 送信されたリクエスト

    Returns:
        render (django.http.response.HttpResponse): Httpでページを表示するための諸要素    
    """
    PROBLEM_NUMBER = 20
    paper_number = int(request.POST["paper_number"])
    digits_of_multiplied_number = request.POST.getlist("digit_of_multiplied_number")
    if not(digits_of_multiplied_number):
        digits_of_multiplied_number.append("2")
        digits_of_multiplied_number.append("3")
        digits_of_multiplied_number.append("4")
        digits_of_multiplied_number.append("5")
    digits_of_multiplying_number = request.POST.getlist("digit_of_multiplying_number")
    if not(digits_of_multiplying_number):
        digits_of_multiplying_number.append("2")
        digits_of_multiplying_number.append("3")
        digits_of_multiplying_number.append("4")
        digits_of_multiplying_number.append("5")
    math_problem_list_of_list = []
    for _ in range(paper_number):
        math_problem_tuple_inner_list = []
        for _ in range(PROBLEM_NUMBER // 2):
            problem1 = MultiplicationFor3rdGrade(digits_of_multiplied_number=digits_of_multiplied_number, digits_of_multiplying_number=digits_of_multiplying_number)
            problem2 = MultiplicationFor3rdGrade(digits_of_multiplied_number=digits_of_multiplied_number, digits_of_multiplying_number=digits_of_multiplying_number)
            math_problem_tuple_inner_list.append((problem1, problem2))
        math_problem_list_of_list.append(math_problem_tuple_inner_list)
    return render(request, 'math_print/elementary_school3/multiplication/for_print.html', {"math_problem_list_of_list": math_problem_list_of_list})


def print_calculation_of_big_number(request):
    """1億を超える数を用いた計算問題のプリント表示を担当

    Args:
        request (django.core.handlers.wsgi.WSGIRequest): 送信されたリクエスト

    Returns:
        render (django.http.response.HttpResponse): Httpでページを表示するための諸要素    
    """
    PROBLEM_NUMBER = 20
    paper_number = int(request.POST["paper_number"])
    units_of_used_number = request.POST.getlist("unit_of_used_number")
    if not(units_of_used_number):
        units_of_used_number.append("billion")
        units_of_used_number.append("trillion")
        units_of_used_number.append("ten_quadrillion")
    problem_types = request.POST.getlist("problem_type")
    if not(problem_types):
        problem_types.append("conversion_from_chinese_numerical_to_alphanumeric")
        problem_types.append("conversion_from_alphanumeric_to_chinese_numerical")
        problem_types.append("unite_numbers")
        problem_types.append("addition")
        problem_types.append("subtraction")
        problem_types.append("multiplication")
        problem_types.append("division")
    math_problem_list_of_list = []
    for _ in range(paper_number):
        math_problem_tuple_inner_list = []
        for _ in range(PROBLEM_NUMBER // 2):
            problem1 = CalculationOfBigNumber(units_of_used_number=units_of_used_number, problem_types=problem_types)
            problem2 = CalculationOfBigNumber(units_of_used_number=units_of_used_number, problem_types=problem_types)
            math_problem_tuple_inner_list.append((problem1, problem2))
        math_problem_list_of_list.append(math_problem_tuple_inner_list)
    return render(request, 'math_print/elementary_school4/calculation_of_big_number/for_print.html', {'math_problem_list_of_list': math_problem_list_of_list})

def print_division_for_elementary_school4(request):
    """小学4年生用の割り算のプリントの出力を担当

    Args:
        request (django.core.handlers.wsgi.WSGIRequest): 送信されたリクエスト

    Returns:
        render (django.http.response.HttpResponse): Httpでページを表示するための諸要素
    """
    PROBLEM_NUMBER = 20
    paper_number = int(request.POST["paper_number"])
    remainder_types = request.POST.getlist("remainder_type")
    if not(remainder_types):
        remainder_types.append("without_remainder")
        remainder_types.append("with_remainder")
    digits_of_divided_number = request.POST.getlist("digit_of_divided_number")
    if not(digits_of_divided_number):
        digits_of_divided_number.append("1")
        digits_of_divided_number.append("2")
        digits_of_divided_number.append("3")
    digits_of_dividing_number = request.POST.getlist("digit_of_dividing_number")
    if not(digits_of_dividing_number):
        digits_of_dividing_number.append("1")
        digits_of_dividing_number.append("2")
        digits_of_dividing_number.append("3")
    math_problem_list_of_list = []
    for _ in range(paper_number):
        math_problem_tuple_inner_list = []
        for _ in range(int(PROBLEM_NUMBER // 2)):
            problem1 = DivisionFor4thGrade(
                remainder_types=remainder_types,
                digits_of_divided_number=digits_of_divided_number, digits_of_dividing_number=digits_of_dividing_number)
            problem2 = DivisionFor4thGrade(
                remainder_types=remainder_types,
                digits_of_divided_number=digits_of_divided_number, digits_of_dividing_number=digits_of_dividing_number)
            math_problem_tuple_inner_list.append((problem1, problem2))
        math_problem_list_of_list.append(math_problem_tuple_inner_list)
    return render(request, 'math_print/elementary_school4/division/for_print.html', {"math_problem_list_of_list": math_problem_list_of_list})


def print_addition_and_subtraction_of_decimal_for_elementary_school4(request):
    """小学4年生用の小数の足し算と引き算の問題のプリント用表示を担当

    Args:
        request (django.core.handlers.wsgi.WSGIRequest): 送信されたリクエスト

    Returns:
        render (django.http.response.HttpResponse): Httpでページを表示するための諸要素    
    """
    PROBLEM_NUMBER = 20
    paper_number = int(request.POST["paper_number"])
    calculation_types = request.POST.getlist("calculation_type")
    if not(calculation_types):
        calculation_types.append("addition")
        calculation_types.append("subtraction")
    numbers_of_decimal_places = request.POST.getlist("number_of_decimal_places")
    if not(numbers_of_decimal_places):
        numbers_of_decimal_places.append("1")
        numbers_of_decimal_places.append("2")
        numbers_of_decimal_places.append("3")
    math_problem_list_of_list = []
    for _ in range(paper_number):
        math_problem_tuple_inner_list = []
        for _ in range(PROBLEM_NUMBER // 2):
            problem1 = AdditionAndSubtractionOfDecimalFor4thGrade(calculation_types=calculation_types, numbers_of_decimal_places=numbers_of_decimal_places)
            problem2 = AdditionAndSubtractionOfDecimalFor4thGrade(calculation_types=calculation_types, numbers_of_decimal_places=numbers_of_decimal_places)
            math_problem_tuple_inner_list.append((problem1, problem2))
        math_problem_list_of_list.append(math_problem_tuple_inner_list)
    return render(request, 'math_print/elementary_school4/addition_and_subtraction_of_decimal/for_print.html', {'math_problem_list_of_list': math_problem_list_of_list})


def print_multiplication_of_decimal_for_elementary_school4(request):
    """小学4年生用の小数の足し算と引き算の問題のプリント用表示を担当

    Args:
        request (django.core.handlers.wsgi.WSGIRequest): 送信されたリクエスト

    Returns:
        render (django.http.response.HttpResponse): Httpでページを表示するための諸要素    
    """
    PROBLEM_NUMBER = 20
    paper_number = int(request.POST["paper_number"])
    multiplied_numbers_of_decimal_places = request.POST.getlist("multiplied_number_of_decimal_places")
    if not(multiplied_numbers_of_decimal_places):
        multiplied_numbers_of_decimal_places.append("0")
        multiplied_numbers_of_decimal_places.append("1")
        multiplied_numbers_of_decimal_places.append("2")
        multiplied_numbers_of_decimal_places.append("3")
    multiplying_numbers_of_decimal_places = request.POST.getlist("multiplying_number_of_decimal_places")
    if not(multiplying_numbers_of_decimal_places):
        multiplying_numbers_of_decimal_places.append("0")
        multiplying_numbers_of_decimal_places.append("1")
        multiplying_numbers_of_decimal_places.append("2")
        multiplying_numbers_of_decimal_places.append("3")
    math_problem_list_of_list = []
    for _ in range(paper_number):
        math_problem_tuple_inner_list = []
        for _ in range(PROBLEM_NUMBER // 2):
            problem1 = MultiplicationOfDecimalFor4thGrade(multiplied_numbers_of_decimal_places=multiplied_numbers_of_decimal_places, multiplying_numbers_of_decimal_places=multiplying_numbers_of_decimal_places)
            problem2 = MultiplicationOfDecimalFor4thGrade(multiplied_numbers_of_decimal_places=multiplied_numbers_of_decimal_places, multiplying_numbers_of_decimal_places=multiplying_numbers_of_decimal_places)
            math_problem_tuple_inner_list.append((problem1, problem2))
        math_problem_list_of_list.append(math_problem_tuple_inner_list)
    return render(request, 'math_print/elementary_school4/multiplication_of_decimal/for_print.html', {'math_problem_list_of_list': math_problem_list_of_list})


def print_division_of_decimal_for_elementary_school4(request):
    """小学4年生用の小数の割り算の問題のプリント用表示を担当

    Args:
        request (django.core.handlers.wsgi.WSGIRequest): 送信されたリクエスト

    Returns:
        render (django.http.response.HttpResponse): Httpでページを表示するための諸要素    
    """
    PROBLEM_NUMBER = 10
    paper_number = int(request.POST["paper_number"])
    remainder_types = request.POST.getlist("remainder_type")
    if not(remainder_types):
        remainder_types.append("without_remainder")
        remainder_types.append("with_remainder")
    decimal_places_of_divided_number = request.POST.getlist("decimal_places_of_divided_number")
    if not(decimal_places_of_divided_number):
        decimal_places_of_divided_number.append("0")
        decimal_places_of_divided_number.append("1")
        decimal_places_of_divided_number.append("2")
        decimal_places_of_divided_number.append("3")
    decimal_places_of_dividing_number = request.POST.getlist("decimal_places_of_dividing_number")
    if not(decimal_places_of_dividing_number):
        decimal_places_of_dividing_number.append("0")
        decimal_places_of_dividing_number.append("1")
        decimal_places_of_dividing_number.append("2")
        decimal_places_of_dividing_number.append("3")
    decimal_places_of_quotient = request.POST.getlist("decimal_places_of_quotient")
    if not(decimal_places_of_quotient):
        decimal_places_of_quotient.append("1")
        decimal_places_of_quotient.append("2")
        decimal_places_of_quotient.append("3")
    math_problem_list_of_list = []
    for _ in range(paper_number):
        math_problem_tuple_inner_list = []
        for _ in range(PROBLEM_NUMBER // 2):
            problem1 = DivisionOfDecimalFor4thGrade(
                remainder_types=remainder_types,
                decimal_places_of_divided_number=decimal_places_of_divided_number,
                decimal_places_of_dividing_number=decimal_places_of_dividing_number,
                decimal_places_of_quotient=decimal_places_of_quotient
                )
            problem2 = DivisionOfDecimalFor4thGrade(
                remainder_types=remainder_types,
                decimal_places_of_divided_number=decimal_places_of_divided_number,
                decimal_places_of_dividing_number=decimal_places_of_dividing_number,
                decimal_places_of_quotient=decimal_places_of_quotient
                )          
            math_problem_tuple_inner_list.append((problem1, problem2))
        math_problem_list_of_list.append(math_problem_tuple_inner_list)
    return render(request, 'math_print/elementary_school4/division_of_decimal/for_print.html', {'math_problem_list_of_list': math_problem_list_of_list})


def print_addition_and_subtraction_of_fraction_for_elementary_school4(request):
    """小学4年生用の分数の足し算と引き算の問題のプリント用表示を担当

    Args:
        request (django.core.handlers.wsgi.WSGIRequest): 送信されたリクエスト

    Returns:
        render (django.http.response.HttpResponse): Httpでページを表示するための諸要素    
    """
    PROBLEM_NUMBER = 20
    paper_number = int(request.POST["paper_number"])
    used_calculations = request.POST.getlist("used_calculation")
    if not(used_calculations):
        used_calculations.append("from_improper_fraction_to_mixed_number_or_integer")
        used_calculations.append("from_mixed_number_to_improper_fraction")
        used_calculations.append("addition")
        used_calculations.append("subtraction")
        used_calculations.append("fill_in_the_square")
    integer_part = request.POST.getlist("integer_part")
    if not(integer_part):
        integer_part.append("with_integer_part")
        integer_part.append("without_integer_part")
    math_problem_list_of_list = []
    for _ in range(paper_number):
        math_problem_tuple_inner_list = []
        for _ in range(PROBLEM_NUMBER // 2):
            problem1 = AdditionAndSubtractionOfFraction(used_calculations=used_calculations, integer_part=integer_part)
            problem2 = AdditionAndSubtractionOfFraction(used_calculations=used_calculations, integer_part=integer_part)
            math_problem_tuple_inner_list.append((problem1, problem2))
        math_problem_list_of_list.append(math_problem_tuple_inner_list)
    return render(request, 'math_print/elementary_school4/addition_and_subtraction_of_fraction/for_print.html', {'math_problem_list_of_list': math_problem_list_of_list})


def print_multiplication_and_division_of_decimal_and_integer(request):
    return render(request, 'math_print/elementary_school6/multiplication_and_division_of_decimal_and_integer/for_print.html', {})

# display section


def display_number_problem(request):
    PROBLEM_NUMBER = 20

    number_to_use = request.POST.getlist("number_number_to_use")
    operator_to_use = request.POST.getlist("number_operator_to_use")
    term_number = int(request.POST["term_number"])

    MAX_NUMBER_TO_FRAC = 10
    MIN_NUMBER_TO_FRAC = -10

    math_problem_tuple_list = []
    for _ in range(int(PROBLEM_NUMBER/2)):
        problem1 = NumberMathProblem(term_number, MAX_NUMBER_TO_FRAC, MIN_NUMBER_TO_FRAC, number_to_use, operator_to_use)
        problem2 = NumberMathProblem(term_number, MAX_NUMBER_TO_FRAC, MIN_NUMBER_TO_FRAC, number_to_use, operator_to_use)
        math_problem_tuple_list.append((problem1, problem2))

    return render(request, 'math_print/junior_highschool1/number/for_display.html', {'math_problem_tuple_list': math_problem_tuple_list})

def display_character_problem(request):
    PROBLEM_NUMBER = 20
    
    number_to_use = request.POST.getlist("character_number_to_use")
    operator_to_use = request.POST.getlist("character_operator_to_use")
    term_number = int(request.POST["term_number"])
    character_to_use = request.POST["character_to_use"]
    character_to_use_list = ["x"]
    if character_to_use == "2":
        character_to_use_list += ["y"]

    MAX_NUMBER_TO_FRAC = 10
    MIN_NUMBER_TO_FRAC = -10

    math_problem_tuple_list = []
    for _ in range(int(PROBLEM_NUMBER/2)):
        problem1 = CharacterMathProblem(
            term_number=term_number, max_number_to_frac=MAX_NUMBER_TO_FRAC,
            min_number_to_frac=MIN_NUMBER_TO_FRAC, used_number_type_list=number_to_use,
            used_operator_type_list=operator_to_use, used_character_type_list=character_to_use_list
            )
        problem2 = CharacterMathProblem(
            term_number=term_number, max_number_to_frac=MAX_NUMBER_TO_FRAC,
            min_number_to_frac=MIN_NUMBER_TO_FRAC, used_number_type_list=number_to_use,
            used_operator_type_list=operator_to_use, used_character_type_list=character_to_use_list
            )
        math_problem_tuple_list.append((problem1, problem2))
    
    return render(request, 'math_print/junior_highschool1/character/for_display.html', {'math_problem_tuple_list': math_problem_tuple_list})

def display_linear_equation_problem(request):
    PROBLEM_NUMBER = 20
    
    number_to_use = request.POST.getlist("number_to_use")
    operator_to_use = request.POST.getlist("operator_to_use")
    term_number = int(request.POST["term_number"])

    MAX_NUMBER_TO_FRAC = 10
    MIN_NUMBER_TO_FRAC = -10

    math_problem_tuple_list = []
    for _ in range(int(PROBLEM_NUMBER/2)):
        problem1 = LinearEquationProblem(
            term_number=term_number, max_number_to_frac=MAX_NUMBER_TO_FRAC,
            min_number_to_frac=MIN_NUMBER_TO_FRAC, used_number_type_list=number_to_use,
            used_operator_type_list=operator_to_use,
            )
        problem2 = LinearEquationProblem(
            term_number=term_number, max_number_to_frac=MAX_NUMBER_TO_FRAC,
            min_number_to_frac=MIN_NUMBER_TO_FRAC, used_number_type_list=number_to_use,
            used_operator_type_list=operator_to_use,
            )
        math_problem_tuple_list.append((problem1, problem2))
    
    return render(request, 'math_print/junior_highschool1/linear_equation/for_display.html', {'math_problem_tuple_list': math_problem_tuple_list})

def display_specific_linear_equation(request):
    PROBLEM_NUMBER = 20
    
    linear_equation_type_list = request.POST.getlist("linear_equation_type")
    if not(linear_equation_type_list):
        linear_equation_type_list.append("ax_equal_b_only_integer")
        linear_equation_type_list.append("ax_equal_b_all_number")
        linear_equation_type_list.append("ax_plus_b_equal_c_only_integer")
        linear_equation_type_list.append("ax_plus_b_equal_c_all_number")
        linear_equation_type_list.append("ax_plus_b_equal_cx_plus_d_only_integer")
        linear_equation_type_list.append("ax_plus_b_equal_cx_plus_d_all_number")
    number_to_use_list = request.POST.getlist("number_to_use")
    if not(number_to_use_list):
        number_to_use_list.append("integer")
        number_to_use_list.append("decimal")
        number_to_use_list.append("frac") 
    
    math_problem_tuple_list = []
    for _ in range(int(PROBLEM_NUMBER//2)):
        problem1 = SpecificLinearEquation(
            linear_equation_type_list=linear_equation_type_list, number_to_use_list=number_to_use_list
        )
        problem2 = SpecificLinearEquation(
            linear_equation_type_list=linear_equation_type_list, number_to_use_list=number_to_use_list
        )
        math_problem_tuple_list.append((problem1, problem2))
    
    return render(request, 'math_print/junior_highschool1/specific_linear_equation/for_display.html', {'math_problem_tuple_list': math_problem_tuple_list})

def display_simultaneous_equations(request):
    PROBLEM_NUMBER = 20
    
    used_coefficients = request.POST.getlist("used_coefficient")
    if not(used_coefficients):
        used_coefficients.append("integer")
        used_coefficients.append("decimal")
        used_coefficients.append("frac")
    equation_types = request.POST.getlist("equation_types")
    if not(equation_types):
        equation_types.append("ax+by=c")
        equation_types.append("ax+by=c+dx+ey")
        equation_types.append("ax+by=c+d(ex+fy)")
    answer_type = request.POST["answer_type"]
    
    math_problem_tuple_list = []
    for _ in range(int(PROBLEM_NUMBER//2)):
        problem1 = SimultaneousEquations(
            used_coefficients=used_coefficients, equation_types=equation_types,
            answer_type=answer_type
        )
        problem2 = SimultaneousEquations(
            used_coefficients=used_coefficients, equation_types=equation_types,
            answer_type=answer_type
        )
        math_problem_tuple_list.append((problem1, problem2))
    
    return render(request, 'math_print/junior_highschool2/simultaneous_equations/for_display.html', {'math_problem_tuple_list': math_problem_tuple_list})

def display_expand_equation(request):
    PROBLEM_NUMBER = 20

    number_to_use = request.POST.getlist("number_to_use")
    expand_equation_type_list = request.POST.getlist("expand_equation_type")

    math_problem_tuple_list = []
    for _ in range(int(PROBLEM_NUMBER/2)):
        problem1 = ExpandEquationProblem(
            used_number_type_list = number_to_use, expand_equation_type_list=expand_equation_type_list
        )
        problem2 = ExpandEquationProblem(
            used_number_type_list = number_to_use, expand_equation_type_list=expand_equation_type_list
        )
        math_problem_tuple_list.append((problem1, problem2))
    
    return render(request, 'math_print/junior_highschool3/expand_equation/for_display.html', {'math_problem_tuple_list': math_problem_tuple_list})

def display_completing_the_square(request):
    PROBLEM_NUMBER = 20
    
    number_to_use = request.POST.getlist("number_to_use")
    number_including_in_bracket = request.POST["number_including_in_bracket"]
    if request.POST["character_including_or_not"] == "including_character":
        include_character_in_coefficient = True
    else:
        include_character_in_coefficient = False
    
    math_problem_tuple_list = []
    for _ in range(int(PROBLEM_NUMBER//2)):
        problem1 = CompletingTheSquareProblem(
            used_number_type_list=number_to_use, number_including_in_bracket=number_including_in_bracket,
            include_character_in_coefficient=include_character_in_coefficient
        )
        problem2 = CompletingTheSquareProblem(
            used_number_type_list=number_to_use, number_including_in_bracket=number_including_in_bracket,
            include_character_in_coefficient=include_character_in_coefficient
        )
        math_problem_tuple_list.append((problem1, problem2))
    
    return render(request, 'math_print/highschool1/completing_the_square/for_display.html', {'math_problem_tuple_list': math_problem_tuple_list})

def display_proportional_expression(request):
    PROBLEM_NUMBER = 20
    
    number_to_use = request.POST.getlist("number_to_use")
    proportional_expression_type = request.POST["proportional_expression_type"]
    
    math_problem_tuple_list = []
    for _ in range(int(PROBLEM_NUMBER//2)):
        problem1 = ProportionalExpressionProblem(
            used_number_type_list=number_to_use, proportional_expression_type=proportional_expression_type
        )
        problem2 = ProportionalExpressionProblem(
            used_number_type_list=number_to_use, proportional_expression_type=proportional_expression_type
        )
        math_problem_tuple_list.append((problem1, problem2))
    
    return render(request, 'math_print/junior_highschool1/proportional_expression/for_display.html', {'math_problem_tuple_list': math_problem_tuple_list})

def display_linear_function(request):
    PROBLEM_NUMBER = 20
    
    number_to_use_list = request.POST.getlist("number_to_use")
    given_information_list = request.POST.getlist("given_information")
    
    math_problem_tuple_list = []
    for _ in range(int(PROBLEM_NUMBER//2)):
        problem1 = LinearFunctionProblem(
            number_to_use_list=number_to_use_list, given_information_list=given_information_list
        )
        problem2 = LinearFunctionProblem(
            number_to_use_list=number_to_use_list, given_information_list=given_information_list
        )
        math_problem_tuple_list.append((problem1, problem2))
    
    return render(request, 'math_print/junior_highschool2/linear_function/for_display.html', {'math_problem_tuple_list': math_problem_tuple_list})
    
def display_power_calculate(request):
    PROBLEM_NUMBER = 20
    
    number_to_use = request.POST.getlist("power_number_to_use")
    calculate_type = request.POST.getlist("power_calculate_type")
    
    math_problem_tuple_list = []
    for _ in range(int(PROBLEM_NUMBER//2)):
        problem1 = PowerCalculateProblem(
            number_to_use=number_to_use, calculate_type=calculate_type
        )
        problem2 = PowerCalculateProblem(
            number_to_use=number_to_use, calculate_type=calculate_type
        )
        math_problem_tuple_list.append((problem1, problem2))
    
    return render(request, 'math_print/junior_highschool1/power/for_display.html', {'math_problem_tuple_list': math_problem_tuple_list})

def display_reduction_problem(request):
    PROBLEM_NUMBER = 20
    
    def decide_max_and_min_number(max_number_in_post, min_number_in_post):
        """POSTから送られた計算の設定に用いる数字の最大値最小値を処理

        Args:
            max_number_in_post (str): POSTに格納されている最大値。空欄の可能性あり
            min_number_in_post (str): POSTに格納されている最小値。空欄の可能性あり 

        Returns:
            max_number (int): 用いる最大値
            min_number (int): 用いる最小値
        Considering:
            全角数字が入力された場合や、文字が入力された場合を想定するのであれば、処理させるのはここになる可能性がある
        """
        
        if bool(max_number_in_post):
            max_number = int(unicodedata.normalize("NFKD", max_number_in_post))
        else:
            max_number = 6
        
        if bool(min_number_in_post):
            min_number = int(unicodedata.normalize("NFKD", min_number_in_post))
        else:
            min_number = 2
            
        if max_number < min_number:
            max_number, min_number = min_number, max_number
        
        if max_number == 0:
            max_number += 2
        if min_number == 0:
            min_number += 1

        return max_number, min_number

    max_number_to_denominator, min_number_to_denominator = decide_max_and_min_number(request.POST["max_number_to_denominator"], request.POST["min_number_to_denominator"])
    max_number_to_numerator, min_number_to_numerator = decide_max_and_min_number(request.POST["max_number_to_numerator"], request.POST["min_number_to_numerator"])
    max_number_on_the_left_of_frac, min_number_on_the_left_of_frac = decide_max_and_min_number(request.POST["max_number_on_the_left_of_frac"], request.POST["min_number_on_the_left_of_frac"])
    max_number_to_reduction, min_number_to_reduction = decide_max_and_min_number(request.POST["max_number_to_reduction"], request.POST["min_number_to_reduction"])

    fraction_type_list = request.POST.getlist("fraction_type")

    math_problem_tuple_list = []
    for _ in range(int(PROBLEM_NUMBER//2)):
        problem1 = ReductionProblem(
            fraction_type_list=fraction_type_list,
            min_number_to_denominator=min_number_to_denominator, max_number_to_denominator=max_number_to_denominator,
            min_number_to_numerator=min_number_to_numerator, max_number_to_numerator=max_number_to_numerator,
            min_number_on_the_left_of_frac=min_number_on_the_left_of_frac, max_number_on_the_left_of_frac=max_number_on_the_left_of_frac,
            min_number_to_reduction=min_number_to_reduction, max_number_to_reduction=max_number_to_reduction
        )
        problem2 = ReductionProblem(
            fraction_type_list=fraction_type_list,
            min_number_to_denominator=min_number_to_denominator, max_number_to_denominator=max_number_to_denominator,
            min_number_to_numerator=min_number_to_numerator, max_number_to_numerator=max_number_to_numerator,
            min_number_on_the_left_of_frac=min_number_on_the_left_of_frac, max_number_on_the_left_of_frac=max_number_on_the_left_of_frac,
            min_number_to_reduction=min_number_to_reduction, max_number_to_reduction=max_number_to_reduction
        )
        math_problem_tuple_list.append((problem1, problem2))
    
    return render(request, 'math_print/elementary_school5/reduction/for_display.html', {'math_problem_tuple_list': math_problem_tuple_list})

def display_conversion_between_frac_and_decimal_problem(request):
    PROBLEM_NUMBER = 20
    
    conversion_type_list = request.POST.getlist("conversion_type")
    below_the_decimal_point_with_string = request.POST.getlist("below_the_decimal_point")
    below_the_decimal_point_with_int = [int(num) for num in below_the_decimal_point_with_string]

    math_problem_tuple_list = []
    for _ in range(int(PROBLEM_NUMBER//2)):
        problem1 = ConversionBetweenFracAndDecimalProblem(
            conversion_type_list=conversion_type_list, below_the_decimal_point_list=below_the_decimal_point_with_int
        )
        problem2 = ConversionBetweenFracAndDecimalProblem(
            conversion_type_list=conversion_type_list, below_the_decimal_point_list=below_the_decimal_point_with_int
        )
        math_problem_tuple_list.append((problem1, problem2))
    
    return render(request, 'math_print/elementary_school5/conversion_between_frac_and_decimal/for_display.html', {'math_problem_tuple_list': math_problem_tuple_list})

def display_quadratic_function(request):
    PROBLEM_NUMBER = 20
    
    problem_type_list = request.POST.getlist("problem_type")
    used_point_number_type_list = request.POST.getlist("used_point_number_type")
    used_coefficient_number_type_list = request.POST.getlist("used_coefficient_number_type")
    
    math_problem_tuple_list = []
    for _ in range(int(PROBLEM_NUMBER//2)):
        problem1 = QuadraticFunctionProblem(
            problem_type_list=problem_type_list, used_point_number_type_list=used_point_number_type_list,
            used_coefficient_number_type_list=used_coefficient_number_type_list
        )
        problem2 = QuadraticFunctionProblem(
            problem_type_list=problem_type_list, used_point_number_type_list=used_point_number_type_list,
            used_coefficient_number_type_list=used_coefficient_number_type_list
        )
        math_problem_tuple_list.append((problem1, problem2))
    
    return render(request, 'math_print/junior_highschool3/quadratic_function/for_display.html', {'math_problem_tuple_list': math_problem_tuple_list})
        
def display_fraction_calculate_problem(request):
    
    def decide_max_and_min_number(max_number_in_post, min_number_in_post):
        """POSTから送られた計算の設定に用いる数字の最大値最小値を処理

        Args:
            max_number_in_post (str): POSTに格納されている最大値。空欄の可能性あり
            min_number_in_post (str): POSTに格納されている最小値。空欄の可能性あり 

        Returns:
            max_number (int): 用いる最大値
            min_number (int): 用いる最小値
        Considering:
            全角数字が入力された場合や、文字が入力された場合を想定するのであれば、処理させるのはここになる可能性がある
        """
        
        if bool(max_number_in_post):
            max_number = int(unicodedata.normalize("NFKD", max_number_in_post))
        else:
            max_number = 6
        
        if bool(min_number_in_post):
            min_number = int(unicodedata.normalize("NFKD", min_number_in_post))
        else:
            min_number = 2
            
        if max_number < min_number:
            max_number, min_number = min_number, max_number
        
        if max_number == 0:
            max_number += 2
        if min_number == 0:
            min_number += 1

        return max_number, min_number
    
    fraction_type_list = request.POST.getlist("fraction_type_for_calculate")
    PROBLEM_NUMBER = 20
    
    max_number_to_denominator, min_number_to_denominator = decide_max_and_min_number(request.POST["max_number_to_denominator"], request.POST["min_number_to_denominator"])
    max_number_to_numerator, min_number_to_numerator = decide_max_and_min_number(request.POST["max_number_to_numerator"], request.POST["min_number_to_numerator"])
    max_number_on_the_left_of_frac, min_number_on_the_left_of_frac = decide_max_and_min_number(request.POST["max_number_on_the_left_of_frac"], request.POST["min_number_on_the_left_of_frac"])
    
    calculate_type_list = request.POST.getlist("fraction_calculate_type")
    term_number = int(request.POST["term_number_for_fraction_calculate"])

    math_problem_tuple_list = []
    for _ in range(int(PROBLEM_NUMBER//2)):
        problem1 = FractionCalculateProblem(
            calculate_type_list=calculate_type_list, fraction_type_list=fraction_type_list,
            term_number=term_number,
            min_number_to_denominator=min_number_to_denominator, max_number_to_denominator=max_number_to_denominator,
            min_number_to_numerator=min_number_to_numerator, max_number_to_numerator=max_number_to_numerator,
            min_number_on_the_left_of_frac=min_number_on_the_left_of_frac, max_number_on_the_left_of_frac=max_number_on_the_left_of_frac
        )
        problem2 = FractionCalculateProblem(
            calculate_type_list=calculate_type_list, fraction_type_list=fraction_type_list,
            term_number=term_number,
            min_number_to_denominator=min_number_to_denominator, max_number_to_denominator=max_number_to_denominator,
            min_number_to_numerator=min_number_to_numerator, max_number_to_numerator=max_number_to_numerator,
            min_number_on_the_left_of_frac=min_number_on_the_left_of_frac, max_number_on_the_left_of_frac=max_number_on_the_left_of_frac
        )
        math_problem_tuple_list.append((problem1, problem2))

    return render(request, 'math_print/elementary_school5/fraction_calculate/for_display.html', {'math_problem_tuple_list': math_problem_tuple_list})

def display_number_without_bracket_problem(request):
    PROBLEM_NUMBER = 20
    
    operators_to_use = request.POST.getlist("number_without_bracket_operator_to_use")
    if not(operators_to_use):
        operators_to_use.append("plus")
        operators_to_use.append("minus")
    numbers_to_use = request.POST.getlist("number_without_bracket_number_to_use")
    if not(numbers_to_use):
        numbers_to_use.append("one_digit_integer")
        numbers_to_use.append("two_digit_integer")
        numbers_to_use.append("frac")
        numbers_to_use.append("decimal")
    term_numbers = request.POST.getlist("number_without_bracket_term_number")
    if not(term_numbers):
        term_numbers.append("2")
        term_numbers.append("3")
        term_numbers.append("4")
        term_numbers.append("5")
        term_numbers.append("6")
    
    math_problem_tuple_list = []
    for _ in range(int(PROBLEM_NUMBER//2)):
        problem1 = NumberWithoutBracketCalculateProblem(
            operators_to_use=operators_to_use, numbers_to_use=numbers_to_use,
            term_numbers=term_numbers
        )
        problem2 = NumberWithoutBracketCalculateProblem(
            operators_to_use=operators_to_use, numbers_to_use=numbers_to_use,
            term_numbers=term_numbers
        )
        math_problem_tuple_list.append((problem1, problem2))
    
    return render(request, 'math_print/junior_highschool1/number_without_bracket/for_display.html', {'math_problem_tuple_list': math_problem_tuple_list})


def display_sector_problem(request):
    PROBLEM_NUMBER = 20
    
    problem_type_list = request.POST.getlist("sector_problem_type")
    
    math_problem_tuple_list = []
    for _ in range(int(PROBLEM_NUMBER//2)):
        problem1 = SectorProblem(problem_type_list=problem_type_list)
        problem2 = SectorProblem(problem_type_list=problem_type_list)
        math_problem_tuple_list.append((problem1, problem2))
    
    return render(request, 'math_print/junior_highschool1/sector/for_display.html', {'math_problem_tuple_list': math_problem_tuple_list})

def display_factorization(request):
    PROBLEM_NUMBER = 20

    factorization_type_list = request.POST.getlist("factorization_type")
    used_coefficient = request.POST["coefficient_used_for_factorization"]
    
    used_formula_list = []
    
    if factorization_type_list:
        if "ax+ab=a(x+b)" in factorization_type_list:
            used_formula_list.append("\( ax + ab = a(x + b) \)")
        
        if "x^2+2ax+a^2=(x+a)^2" in factorization_type_list:
            used_formula_list.append("\( x^2 + 2ax + a^2 = (x + a)^2 \)")
        
        if "x^2-2ax+a^2=(x-a)^2" in factorization_type_list:
            used_formula_list.append("\( x^2 - 2ax + a^2 = (x - a)^2 \)")
        
        if "x^2+(a+b)x+ab=(x+a)(x+b)" in factorization_type_list:
            used_formula_list.append("\( x^2 + (a + b)x + ab = (x + a)(x + b) \)")
        
        if "x^2-a^2=(x+a)(x-a)" in factorization_type_list:
            used_formula_list.append("\( x^2 - a^2 = (x + a)(x - a) \)")
    else:
        used_formula_list.append("\( ax + ab = a(x + b) \)")
        used_formula_list.append("\( x^2 + 2ax + a^2 = (x + a)^2 \)")
        used_formula_list.append("\( x^2 - 2ax + a^2 = (x - a)^2 \)")
        used_formula_list.append("\( x^2 + (a + b)x + ab = (x + a)(x + b) \)")
        used_formula_list.append("\( x^2 - a^2 = (x + a)(x - a) \)")
        
    
    math_problem_tuple_list = []
    for _ in range(int(PROBLEM_NUMBER//2)):
        problem1 = FactorizationProblem(factorization_type_list=factorization_type_list, used_coefficient=used_coefficient)
        problem2 = FactorizationProblem(factorization_type_list=factorization_type_list, used_coefficient=used_coefficient)
        math_problem_tuple_list.append((problem1, problem2))
    
    context = {}
    context["math_problem_tuple_list"] = math_problem_tuple_list
    context["used_formula_list"] = used_formula_list
    return render(request, 'math_print/junior_highschool3/factorization/for_display.html', context)

def display_quadratic_equation(request):
    PROBLEM_NUMBER = 20

    quadratic_equation_type_list = request.POST.getlist("quadratic_equation_type")
    if request.POST["organization_coefficient_or_not"] == "organization_coefficient":
        organization_coefficient = True
    else:
        organization_coefficient = False
    
    used_formula_list = []
    if quadratic_equation_type_list:
        if "x^2=k" in quadratic_equation_type_list:
            used_formula_list.append("\( x^2 = k \Leftrightarrow x = \pm \sqrt{{k}} \)")
        if "x^2+2ax+a^2=(x+a)^2" in quadratic_equation_type_list:
            used_formula_list.append("\( x^2 + 2ax + a^2 = (x + a)^2 \)")
        if "x^2-2ax+a^2=(x-a)^2" in quadratic_equation_type_list:
            used_formula_list.append("\( x^2 - 2ax + a^2 = (x - a)^2 \)")
        if "x^2+(a+b)x+ab=(x+a)(x+b)" in quadratic_equation_type_list:
            used_formula_list.append("\( x^2+(a+b)x+ab=(x+a)(x+b) \)")
        if "x^2-a^2=(x+a)(x-a)" in quadratic_equation_type_list:
            used_formula_list.append("\( x^2-a^2=(x+a)(x-a) \)")
        if "quadratic_formula" in quadratic_equation_type_list:
            used_formula_list.append("\( ax^2 + bx + c = 0 \Leftrightarrow x = \\frac{-b\pm\sqrt{b^2-4ac}}{2a} \)")
    else:
        used_formula_list.append("\( x^2 = k \Leftrightarrow x = \pm \sqrt{{k}} \)")
        used_formula_list.append("\( x^2 + 2ax + a^2 = (x + a)^2 \)")
        used_formula_list.append("\( x^2 - 2ax + a^2 = (x - a)^2 \)")
        used_formula_list.append("\( x^2+(a+b)x+ab=(x+a)(x+b) \)")
        used_formula_list.append("\( x^2-a^2=(x+a)(x-a) \)")
        used_formula_list.append("\( ax^2 + bx + c = 0 \Leftrightarrow x = \\frac{-b\pm\sqrt{b^2-4ac}}{2a} \)")

    math_problem_tuple_list = []
    for _ in range(int(PROBLEM_NUMBER//2)):
        problem1 = QuadraticEquationProblem(
            quadratic_equation_type_list=quadratic_equation_type_list, organization_coefficient=organization_coefficient
        )
        problem2 = QuadraticEquationProblem(
            quadratic_equation_type_list=quadratic_equation_type_list, organization_coefficient=organization_coefficient
        )
        math_problem_tuple_list.append((problem1, problem2))
    
    context = {}
    context["math_problem_tuple_list"] = math_problem_tuple_list
    context["used_formula_list"] = used_formula_list
    return render(request, 'math_print/junior_highschool3/quadratic_equation/for_display.html', context)

def hs1_display_expand_equation(request):
    PROBLEM_NUMBER = 20
    """
    '(a+b)^2=a^2+2ab+b^2', '(a-b)^2=a^2-2ab+b^2',
    '(a+b)(a-b)=a^2-b^2',
    '(ax+b)(cx+d)=acx^2+(ad+bc)x+ab', '(a+b+c)^2=a^2+b^2+c^2+2ab+2bc+2ca',
    '(a+b)^3=a^3+3a^2b+3ab^2+b^3', '(a-b)^3=a^3-3a^2b+3ab^2-b^3',
    '(a+b)(a^2-ab+b^2)=a^3+b^3', '(a-b)(a^2+ab+b^2)=a^3-b^3'
    """
    expand_equation_type_list = request.POST.getlist("used_formula")
    if not(expand_equation_type_list):
        expand_equation_type_list.append('(a+b)^2=a^2+2ab+b^2')
        expand_equation_type_list.append('(a-b)^2=a^2-2ab+b^2')
        expand_equation_type_list.append('(a+b)(a-b)=a^2-b^2')
        expand_equation_type_list.append('(ax+b)(cx+d)=acx^2+(ad+bc)x+ab')
        expand_equation_type_list.append('(a+b+c)^2=a^2+b^2+c^2+2ab+2bc+2ca')
        expand_equation_type_list.append('(a+b)^3=a^3+3a^2b+3ab^2+b^3')
        expand_equation_type_list.append('(a-b)^3=a^3-3a^2b+3ab^2-b^3')
        expand_equation_type_list.append('(a+b)(a^2-ab+b^2)=a^3+b^3')
        expand_equation_type_list.append('(a-b)(a^2+ab+b^2)=a^3-b^3')
    
    used_formula_list = []
    if '(a+b)^2=a^2+2ab+b^2' in expand_equation_type_list:
        used_formula_list.append("\( (a+b)^2=a^2+2ab+b^2 \)")
    if '(a-b)^2=a^2-2ab+b^2' in expand_equation_type_list:
        used_formula_list.append("\( (a-b)^2=a^2-2ab+b^2 \)")
    if '(a+b)(a-b)=a^2-b^2' in expand_equation_type_list:
        used_formula_list.append("\( (a+b)(a-b)=a^2-b^2 \)")
    if '(ax+b)(cx+d)=acx^2+(ad+bc)x+ab' in expand_equation_type_list:
        used_formula_list.append("\( (ax+b)(cx+d)=acx^2+(ad+bc)x+ab \)")
    if '(a+b+c)^2=a^2+b^2+c^2+2ab+2bc+2ca' in expand_equation_type_list:
        used_formula_list.append("\( (a+b+c)^2=a^2+b^2+c^2+2ab+2bc+2ca \)")
    if '(a+b)^3=a^3+3a^2b+3ab^2+b^3' in expand_equation_type_list:
        used_formula_list.append("\( (a+b)^3=a^3+3a^2b+3ab^2+b^3 \)")
    if '(a-b)^3=a^3-3a^2b+3ab^2-b^3' in expand_equation_type_list:
        used_formula_list.append("\( (a-b)^3=a^3-3a^2b+3ab^2-b^3 \)")
    if '(a+b)(a^2-ab+b^2)=a^3+b^3' in expand_equation_type_list:
        used_formula_list.append("\( (a+b)(a^2-ab+b^2)=a^3+b^3 \)")
    if '(a-b)(a^2+ab+b^2)=a^3-b^3' in expand_equation_type_list:
        used_formula_list.append("\( (a-b)(a^2+ab+b^2)=a^3-b^3 \)")

    if request.POST["another_character_exists_or_not"] == "exist":
        another_character_existence = True
    else:
        another_character_existence = False
    
    math_problem_tuple_list = []
    for _ in range(int(PROBLEM_NUMBER//2)):
        problem1 = HS1ExpandEquationProblem(
            expand_equation_type_list=expand_equation_type_list, another_character_existence=another_character_existence
        )
        problem2 = HS1ExpandEquationProblem(
            expand_equation_type_list=expand_equation_type_list, another_character_existence=another_character_existence
        )
        math_problem_tuple_list.append((problem1, problem2))

    context = {}
    context["math_problem_tuple_list"] = math_problem_tuple_list
    context["used_formula_list"] = used_formula_list
    return render(request, 'math_print/highschool1/expand_equation/for_display.html', context)

def hs1_display_factorization(request):
    PROBLEM_NUMBER = 20

    factorization_type_list = request.POST.getlist("used_formula_for_factorization")
    if not(factorization_type_list):
        factorization_type_list.append('a^2+2ab+b^2=(a+b)^2')
        factorization_type_list.append('a^2-2ab+b^2=(a-b)^2')
        factorization_type_list.append('a^2-b^2=(a+b)(a-b)')
        factorization_type_list.append('acx^2+(ad+bc)x+ab=(ax+b)(cx+d)')
        factorization_type_list.append('a^2+b^2+c^2+2ab+2bc+2ca=(a+b+c)^2')
        factorization_type_list.append('a^3+3a^2b+3ab^2+b^3=(a+b)^3')
        factorization_type_list.append('a^3-3a^2b+3ab^2-b^3=(a-b)^3')
        factorization_type_list.append('a^3+b^3=(a+b)(a^2-ab+b^2)')
        factorization_type_list.append('a^3-b^3=(a-b)(a^2+ab+b^2)')
    
    used_formula_list = []
    if 'a^2+2ab+b^2=(a+b)^2' in factorization_type_list:
        used_formula_list.append("\( a^2+2ab+b^2=(a+b)^2 \)")
    if '(a^2-2ab+b^2=(a-b)^2' in factorization_type_list:
        used_formula_list.append("\( a^2-2ab+b^2=(a-b)^2 \)")
    if 'a^2-b^2=(a+b)(a-b)' in factorization_type_list:
        used_formula_list.append("\( a^2-b^2=(a+b)(a-b) \)")
    if 'acx^2+(ad+bc)x+ab=(ax+b)(cx+d)' in factorization_type_list:
        used_formula_list.append("\( acx^2+(ad+bc)x+ab=(ax+b)(cx+d) \)")
    if 'a^2+b^2+c^2+2ab+2bc+2ca=(a+b+c)^2' in factorization_type_list:
        used_formula_list.append("\( a^2+b^2+c^2+2ab+2bc+2ca=(a+b+c)^2 \)")
    if 'a^3+3a^2b+3ab^2+b^3=(a+b)^3' in factorization_type_list:
        used_formula_list.append("\( a^3+3a^2b+3ab^2+b^3=(a+b)^3 \)")
    if 'a^3-3a^2b+3ab^2-b^3=(a-b)^3' in factorization_type_list:
        used_formula_list.append("\( a^3-3a^2b+3ab^2-b^3=(a-b)^3 \)")
    if 'a^3+b^3=(a+b)(a^2-ab+b^2)' in factorization_type_list:
        used_formula_list.append("\( a^3+b^3=(a+b)(a^2-ab+b^2) \)")
    if 'a^3-b^3=(a-b)(a^2+ab+b^2)' in factorization_type_list:
        used_formula_list.append("\( a^3-b^3=(a-b)(a^2+ab+b^2) \)")          
    

    if request.POST["another_character_exists_or_not"] == "exist":
        another_character_existence = True
    else:
        another_character_existence = False

    math_problem_tuple_list = []
    for _ in range(int(PROBLEM_NUMBER//2)):
        problem1 = HS1FactorizationProblem(
            factorization_type_list=factorization_type_list, another_character_existence=another_character_existence
        )
        problem2 = HS1FactorizationProblem(
            factorization_type_list=factorization_type_list, another_character_existence=another_character_existence
        )
        math_problem_tuple_list.append((problem1, problem2))
    
    context = {}
    context["math_problem_tuple_list"] = math_problem_tuple_list
    context["used_formula_list"] = used_formula_list

    return render(request, 'math_print/highschool1/factorization/for_display.html', context)

def display_transformation_of_equation(request):
    PROBLEM_NUMBER = 20
    calculate_types = request.POST.getlist("calculate_type")
    if not(calculate_types):
        calculate_types.append("addition_and_subtraction")
        calculate_types.append("multiplication_and_division")
        calculate_types.append("mixed")
    
    math_problem_tuple_list = []
    for _ in range(int(PROBLEM_NUMBER//2)):
        problem1 = TransformationOfEquationProblem(calculate_types=calculate_types)
        problem2 = TransformationOfEquationProblem(calculate_types=calculate_types)
        math_problem_tuple_list.append((problem1, problem2))
    
    context = {}
    context["math_problem_tuple_list"] = math_problem_tuple_list
    
    return render(request, 'math_print/junior_highschool2/transformation_of_equation/for_display.html', context)

def display_character_fraction(request):
    PROBLEM_NUMBER = 20
    term_number = int(request.POST["term_number"])
    
    math_problem_tuple_list = []
    for _ in range(int(PROBLEM_NUMBER//2)):
        problem1 = CharacterFractionProblem(term_number=term_number)
        problem2 = CharacterFractionProblem(term_number=term_number)
        math_problem_tuple_list.append((problem1, problem2))
    
    context = {}
    context["math_problem_tuple_list"] = math_problem_tuple_list
    
    return render(request, 'math_print/junior_highschool2/character_fraction/for_display.html', context)

def hs1_display_quadratic_function(request):
    PROBLEM_NUMBER = 14
    given_information_list = request.POST.getlist("given_information")
    if not(given_information_list):
        given_information_list.append("vertex_and_one_point")
        given_information_list.append("three_points")
        given_information_list.append("the_axis_of_symmetry_and_two_points")
        given_information_list.append("before_parabora_and_line_or_parabora_containing_vertex_and_one_point")
    
    math_problem_tuple_list = []
    for _ in range(int(PROBLEM_NUMBER//2)):
        problem1 = HS1QuadraticFunctionProblem(given_information_list=given_information_list)
        problem2 = HS1QuadraticFunctionProblem(given_information_list=given_information_list)
        math_problem_tuple_list.append((problem1, problem2))
    
    context = {}
    context["math_problem_tuple_list"] = math_problem_tuple_list
    
    return render(request, 'math_print/highschool1/quadratic_function/for_display.html', context)

def jhs2_display_character_problem(request):
    PROBLEM_NUMBER = 20

    number_to_use = request.POST.getlist("character_number_to_use")
    operator_to_use = request.POST.getlist("character_operator_to_use")
    term_number = int(request.POST["term_number"])
    character_to_use = request.POST["character_to_use"]
    character_to_use_list = ["x"]
    if character_to_use == "2":
        character_to_use_list += ["y"]

    MAX_NUMBER_TO_FRAC = 10
    MIN_NUMBER_TO_FRAC = -10

    math_problem_tuple_list = []
    for _ in range(int(PROBLEM_NUMBER//2)):
        problem1 = CharacterMathProblem(
            term_number=term_number, max_number_to_frac=MAX_NUMBER_TO_FRAC,
            min_number_to_frac=MIN_NUMBER_TO_FRAC, used_number_type_list=number_to_use,
            used_operator_type_list=operator_to_use, used_character_type_list=character_to_use_list
            )
        problem2 = CharacterMathProblem(
            term_number=term_number, max_number_to_frac=MAX_NUMBER_TO_FRAC,
            min_number_to_frac=MIN_NUMBER_TO_FRAC, used_number_type_list=number_to_use,
            used_operator_type_list=operator_to_use, used_character_type_list=character_to_use_list
            )
        math_problem_tuple_list.append((problem1, problem2))
    
    return render(request, 'math_print/junior_highschool2/character/for_display.html', {'math_problem_tuple_list': math_problem_tuple_list})

def hs1_display_quadratic_function_max_min(request):
    PROBLEM_NUMBER = 14
    
    moving_part_list = request.POST.getlist("moving_part")
    if not(moving_part_list):
        moving_part_list.append("the_axis_of_symmetry")
        moving_part_list.append("domain")
    max_min_list = request.POST.getlist("max_min")
    if not(max_min_list):
        max_min_list.append("max")
        max_min_list.append("min")
    
    math_problem_tuple_list = []
    for _ in range(int(PROBLEM_NUMBER//2)):
        problem1 = HS1QuadraticFunctionMaxMinProblem(moving_part_list=moving_part_list, max_min_list=max_min_list)
        problem2 = HS1QuadraticFunctionMaxMinProblem(moving_part_list=moving_part_list, max_min_list=max_min_list)
        math_problem_tuple_list.append((problem1, problem2))
    
    context = {}
    context["math_problem_tuple_list"] = math_problem_tuple_list
    
    return render(request, 'math_print/highschool1/quadratic_function_max_min/for_display.html', context)


def display_parallel_lines_and_angle(request):
    import random
    from typing import NamedTuple
    
    class ProblemTypeAndAnswerAngle(NamedTuple):
        problem_type: str
        angle: int
    
    used_information_list = request.POST.getlist("used_information")
    if not(used_information_list):
        used_information_list.append("corresponding_and_alternate_angle")
        used_information_list.append("multiple_corresponding_and_alternate_angle")
        used_information_list.append("vertical_angle")
    
    problem_type_and_answer_angle_tuple_list = []
    for _ in range(20//2):
        problem_type1 = random.choice(used_information_list)
        answer_angle1 = random.randint(40, 120)
        problem_type_and_answer_angle1 = ProblemTypeAndAnswerAngle(problem_type1, answer_angle1)
        problem_type2 = random.choice(used_information_list)
        answer_angle2 = random.randint(40, 120)
        problem_type_and_answer_angle2 = ProblemTypeAndAnswerAngle(problem_type2, answer_angle2)   
        problem_type_and_answer_angle_tuple_list.append((problem_type_and_answer_angle1, problem_type_and_answer_angle2))
        
    context = {}
    context["problem_type_and_answer_angle_tuple_list"] = problem_type_and_answer_angle_tuple_list

    return render(request, 'math_print/junior_highschool2/parallel_lines_and_angle/for_display.html', context)

def display_unit_conversion_problem(request):
    PROBLEM_NUMBER = 20
    
    used_unit_list = request.POST.getlist("unit_type")
    if not(used_unit_list):
        used_unit_list.append("length")
        used_unit_list.append("weight")
        used_unit_list.append("area")
        used_unit_list.append("volume")
        used_unit_list.append("time")
        
    math_problem_tuple_list = []
    for _ in range(int(PROBLEM_NUMBER//2)):
        problem1 = UnitConversionProblem(used_unit_list=used_unit_list)
        problem2 = UnitConversionProblem(used_unit_list=used_unit_list)
        math_problem_tuple_list.append((problem1, problem2))
    
    context = {}
    context["math_problem_tuple_list"] = math_problem_tuple_list
    
    return render(request, 'math_print/elementary_school3/unit_conversion/for_display.html', context)

def display_sector_with_figure_problem(request):      
    PROBLEM_NUMBER = 20
    
    problem_type_list = request.POST.getlist("sector_problem_type")
    
    math_problem_tuple_list = []
    for _ in range(int(PROBLEM_NUMBER//2)):
        problem1 = SectorWithFigureProblem(problem_type_list=problem_type_list)
        problem2 = SectorWithFigureProblem(problem_type_list=problem_type_list)
        math_problem_tuple_list.append((problem1, problem2))
    
    return render(request, 'math_print/junior_highschool1/sector_with_figure/for_display.html', {'math_problem_tuple_list': math_problem_tuple_list})

def display_logarithm_calculation(request):
    PROBLEM_NUMBER = 20
    
    problem_type_list = request.POST.getlist("logarithm_calculation_type")
    if not(problem_type_list):
        problem_type_list.append("change_of_base_formula")
        problem_type_list.append("add_and_subtraction_without_change_of_base_formula")
    
    math_problem_tuple_list = []
    for _ in range(int(PROBLEM_NUMBER//2)):
        problem1 = LogarithmCalculationProblem(problem_type_list=problem_type_list)
        problem2 = LogarithmCalculationProblem(problem_type_list=problem_type_list)
        math_problem_tuple_list.append((problem1, problem2))
    
    return render(request, 'math_print/highschool2/logarithm_calculate/for_display.html', {'math_problem_tuple_list': math_problem_tuple_list})

def display_exponent_calculation(request):
    PROBLEM_NUMBER = 20
    
    calculation_type = request.POST["exponent_calculation_type"]

    base_type_list = request.POST.getlist("exponent_base_type")
    if not(base_type_list):
        base_type_list.append("number")
        base_type_list.append("character")
    
    math_problem_tuple_list = []
    for _ in range(int(PROBLEM_NUMBER//2)):
        problem1 = ExponentCalculation(calculation_type=calculation_type, base_type_list=base_type_list)
        problem2 = ExponentCalculation(calculation_type=calculation_type, base_type_list=base_type_list)
        math_problem_tuple_list.append((problem1, problem2))
    
    return render(request, 'math_print/highschool2/exponent_calculate/for_display.html', {'math_problem_tuple_list': math_problem_tuple_list})

def display_lcm_and_gcd_problem(request):
    PROBLEM_NUMBER = 20

    problem_type_list = request.POST.getlist("problem_type")
    if not(problem_type_list):
        problem_type_list.append("lcm")
        problem_type_list.append("gcd")
    max_problem_number_in_post = request.POST["max_problem_number"]
    if bool(max_problem_number_in_post):
        max_problem_number = int(unicodedata.normalize("NFKD", max_problem_number_in_post))
    else:
        max_problem_number = 100
    
    math_problem_tuple_list = []
    for _ in range(int(PROBLEM_NUMBER//2)):
        problem1 = LCMAndGCD(problem_type_list=problem_type_list, max_problem_number=max_problem_number)
        problem2 = LCMAndGCD(problem_type_list=problem_type_list, max_problem_number=max_problem_number)
        math_problem_tuple_list.append((problem1, problem2))
    
    return render(request, 'math_print/elementary_school5/lcm_and_gcd/for_display.html', {'math_problem_tuple_list': math_problem_tuple_list})

def display_vector_cross_point(request):
    PROBLEM_NUMBER = 6

    problem_type_list = request.POST.getlist("problem_type")
    if not(problem_type_list):
        problem_type_list.append("cross_point_of_two_line")
        problem_type_list.append("cross_point_of_plane_and_line")
    
    math_problem_tuple_list = []
    for _ in range(int(PROBLEM_NUMBER//2)):
        problem1 = VectorCrossPoint(problem_type_list=problem_type_list)
        problem2 = VectorCrossPoint(problem_type_list=problem_type_list)
        math_problem_tuple_list.append((problem1, problem2))
    
    return render(request, 'math_print/highschool2/vector_cross_point/for_display.html', {'math_problem_tuple_list': math_problem_tuple_list})


def display_elementary5_sector_problem(request):
    PROBLEM_NUMBER = 20
    
    problem_type_list = request.POST.getlist("problem_type")
    if not(problem_type_list):
        problem_type_list.append("standard_sector")
        problem_type_list.append("baumkuchen")
        problem_type_list.append("in_star")
        problem_type_list.append("out_star")
        problem_type_list.append("in_rugby")
        problem_type_list.append("out_rugby")
        problem_type_list.append("in_seed_and_flower")
        problem_type_list.append("out_seed_and_flower")
    
    math_problem_tuple_list = []
    for _ in range(int(PROBLEM_NUMBER//2)):
        problem1 = Elementary5SectorWithFigureProblem(problem_type_list=problem_type_list)
        problem2 = Elementary5SectorWithFigureProblem(problem_type_list=problem_type_list)
        math_problem_tuple_list.append((problem1, problem2))
    
    return render(request, 'math_print/elementary_school5/sector/for_display.html', {'math_problem_tuple_list': math_problem_tuple_list})

def display_fill_in_the_square_problem(request):
    PROBLEM_NUMBER = 20
    
    calculation_type_list = request.POST.getlist("calculation_type")
    if not(calculation_type_list):
        calculation_type_list.append("addition_only")
        calculation_type_list.append("subtraction_only")
        calculation_type_list.append("multiplication_only")
        calculation_type_list.append("division_only")
        calculation_type_list.append("addition_and_subtraction")
        calculation_type_list.append("multiplication_and_division")
        calculation_type_list.append("all_calculations")
    used_symbol = request.POST["used_symbol"]
    used_number_list = request.POST.getlist("used_number")
    if not(used_number_list):
        used_number_list.append("integer")
        used_number_list.append("frac")
        used_number_list.append("decimal")
    math_problem_tuple_list = []
    for _ in range(int(PROBLEM_NUMBER//2)):
        problem1 = FillInTheSquareProblem(
            calculation_type_list=calculation_type_list, used_symbol=used_symbol,
            used_number_list=used_number_list
            )
        problem2 = FillInTheSquareProblem(
            calculation_type_list=calculation_type_list, used_symbol=used_symbol,
            used_number_list=used_number_list)
        math_problem_tuple_list.append((problem1, problem2))
    
    return render(request, 'math_print/elementary_school6/fill_in_the_square/for_display.html', {'math_problem_tuple_list': math_problem_tuple_list, 'used_symbol': used_symbol})

def display_common_denominator_problem(request):
    PROBLEM_NUMBER = 20
    
    fraction_type_list = request.POST.getlist("fraction_type_for_common_denominator")
    if not(fraction_type_list):
        fraction_type_list.append("proper_fraction")
        fraction_type_list.append("improper_fraction")
        fraction_type_list.append("mixed_fraction")
    fraction_numbers_list = request.POST.getlist("fraction_numbers")
    if not(fraction_numbers_list):
        fraction_numbers_list.append(2)
        fraction_numbers_list.append(3)
    else:
        fraction_numbers_list = [int(number_str) for number_str in fraction_numbers_list]
    
    math_problem_tuple_list = []
    for _  in range(int(PROBLEM_NUMBER//2)):
        problem1 = CommonDenominatorProblem(fraction_type_list=fraction_type_list, fraction_numbers_list=fraction_numbers_list)
        problem2 = CommonDenominatorProblem(fraction_type_list=fraction_type_list, fraction_numbers_list=fraction_numbers_list)
        math_problem_tuple_list.append((problem1, problem2))
    
    return render(request, 'math_print/elementary_school5/common_denominator/for_display.html', {'math_problem_tuple_list': math_problem_tuple_list})

def display_recurrence_relation(request):
    PROBLEM_NUMBER = 20
    
    problem_type_list = request.POST.getlist("recurrence_relation_type")
    if not(problem_type_list):
        problem_type_list.append("arithmetic_progression")
        problem_type_list.append("geometric_progression")
        problem_type_list.append("progression_of_differences")
        problem_type_list.append("harmonic_progression")
        problem_type_list.append("linear_characteristic_equation")
        problem_type_list.append("coefficient_comparison_to_geometric_progression")
        problem_type_list.append("three_adjacent_terms")
    
    math_problem_tuple_list = []
    for _ in range(int(PROBLEM_NUMBER//2)):
        problem1 = RecurrenceRelationProblem(problem_type_list=problem_type_list)
        problem2 = RecurrenceRelationProblem(problem_type_list=problem_type_list)
        math_problem_tuple_list.append((problem1, problem2))
    
    return render(request, 'math_print/highschool2/recurrence_relation/for_display.html', {'math_problem_tuple_list': math_problem_tuple_list})

def display_square_root_problem(request):
    PROBLEM_NUMBER = 20
    problem_types = request.POST.getlist("problem_type")
    if not(problem_types):
        problem_types.append("write_square_root_not_using_radical_sign_only_with_integer")
        problem_types.append("write_square_root_not_using_radical_sign")
        problem_types.append("write_square_root_using_radical_sign_only_with_integer")
        problem_types.append("write_square_root_using_radical_sign")
        problem_types.append("put_coefficient_into_radical_sign")
        problem_types.append("take_out_coefficient_from_radical_sign_inside")
        problem_types.append("rationalize")
    math_problem_tuple_list = []
    for _ in range(int(PROBLEM_NUMBER//2)):
        problem1 = SquareRootProblem(problem_types=problem_types)
        problem2 = SquareRootProblem(problem_types=problem_types)
        math_problem_tuple_list.append((problem1, problem2))
    return render(request, 'math_print/junior_highschool3/square_root/for_display.html', {'math_problem_tuple_list': math_problem_tuple_list})

def display_square_root_calculate_problem(request):
    PROBLEM_NUMBER = 20
    calculation_types = request.POST.getlist("calculation_type")
    if not(calculation_types):
        calculation_types.append("addition_and_subtraction_only")
        calculation_types.append("multiplication_and_division_only")
        calculation_types.append("using_expand_formula")
    math_problem_tuple_list = []
    for _ in range(int(PROBLEM_NUMBER//2)):
        problem1 = SquareRootCalculateProblem(calculation_types=calculation_types)
        problem2 = SquareRootCalculateProblem(calculation_types=calculation_types)
        math_problem_tuple_list.append((problem1, problem2))
    return render(request, 'math_print/junior_highschool3/square_root_calculate/for_display.html', {'math_problem_tuple_list': math_problem_tuple_list})

def display_base_n_numbers(request):
    PROBLEM_NUMBER = 20
    convert_from_to_types = request.POST.getlist("convert_from_to_type")
    if not(convert_from_to_types):
        convert_from_to_types.append("from_n_base_to_ten_base")
        convert_from_to_types.append("from_ten_base_to_n_base")
    numbers_to_convert = request.POST.getlist("number_to_convert")
    if not(numbers_to_convert):
        numbers_to_convert.append("integer")
        numbers_to_convert.append("decimal")
    math_problem_tuple_list = []
    for _ in range(int(PROBLEM_NUMBER//2)):
        problem1 = BaseNNumbersProblem(convert_from_to_types=convert_from_to_types, numbers_to_convert=numbers_to_convert)
        problem2 = BaseNNumbersProblem(convert_from_to_types=convert_from_to_types, numbers_to_convert=numbers_to_convert)
        math_problem_tuple_list.append((problem1, problem2))
    return render(request, 'math_print/highschool1/base_n_numbers/for_display.html', {'math_problem_tuple_list': math_problem_tuple_list})

def display_linear_function_with_graph(request):      
    PROBLEM_NUMBER = 20
    
    problem_types = request.POST.getlist("problem_type")
    if not(problem_types):
        problem_types.append("with_grid_to_linear_function")
        problem_types.append("without_grid_to_linear_function")
        problem_types.append("linear_function_to_with_grid")
        problem_types.append("coefficient_and_intercept_to_with_grid")
    
    math_problem_tuple_list = []
    for _ in range(int(PROBLEM_NUMBER//2)):
        problem1 = LinearFunctionWithGraphProblem(problem_types=problem_types)
        problem2 = LinearFunctionWithGraphProblem(problem_types=problem_types)
        math_problem_tuple_list.append((problem1, problem2))
    
    return render(request, 'math_print/junior_highschool2/linear_function_with_graph/for_display.html', {'math_problem_tuple_list': math_problem_tuple_list})

def display_trigonometric_ratio(request):
    PROBLEM_NUMBER = 10
    
    problem_types = request.POST.getlist("problem_type")
    if not(problem_types):
        problem_types.append("value_to_degree")
        problem_types.append("degree_to_value")
        problem_types.append("mutual_relationships")
        
    used_trigonometric_ratios = request.POST.getlist("used_trigonometric_ratio")
    if not(used_trigonometric_ratios):
        used_trigonometric_ratios.append("sin")
        used_trigonometric_ratios.append("cos")
        used_trigonometric_ratios.append("tan")
    
    degree_range = request.POST["degree_range"]
        
    math_problem_tuple_list = []
    for _ in range(int(PROBLEM_NUMBER // 2)):
        problem1 = TrigonometricRatioProblem(
            problem_types=problem_types, used_trigonometric_ratios=used_trigonometric_ratios,
            degree_range=degree_range
            )
        problem2 = TrigonometricRatioProblem(
            problem_types=problem_types, used_trigonometric_ratios=used_trigonometric_ratios,
            degree_range=degree_range)
        math_problem_tuple_list.append((problem1, problem2))
    return render(request, 'math_print/highschool1/trigonometric_ratio/for_display.html', {'math_problem_tuple_list': math_problem_tuple_list})

def display_trigonometric_function(request):
    PROBLEM_NUMBER = 10
    
    problem_types = request.POST.getlist("trigonometric_function_problem_type")
    if not(problem_types):
        problem_types.append("value_to_radian")
        problem_types.append("radian_to_value")
        problem_types.append("mutual_relationships")
    
    radian_range = request.POST["radian_range"]
    
    used_trigonometric_functions = request.POST.getlist("used_trigonometric_function")
    if not(used_trigonometric_functions):
        used_trigonometric_functions.append("sin")
        used_trigonometric_functions.append("cos")
        used_trigonometric_functions.append("tan")
    
    math_problem_tuple_list = []
    for _ in range(int(PROBLEM_NUMBER // 2)):
        problem1 = TrigonometricFunctionProblem(
            problem_types=problem_types, used_trigonometric_functions=used_trigonometric_functions,
            radian_range=radian_range
        )
        problem2 = TrigonometricFunctionProblem(
            problem_types=problem_types, used_trigonometric_functions=used_trigonometric_functions,
            radian_range=radian_range
        )
        math_problem_tuple_list.append((problem1, problem2))
    return render(request, 'math_print/highschool2/trigonometric_function/for_display.html', {'math_problem_tuple_list': math_problem_tuple_list})


def display_quadratic_inequality(request):
    PROBLEM_NUMBER = 20
    used_quadratic_equation = request.POST.getlist("used_quadratic_equation")
    if not(used_quadratic_equation):
        used_quadratic_equation.append("two_different_answer")
        used_quadratic_equation.append("same_answer")
        used_quadratic_equation.append("no_answer")
    used_answer_in_quadratic_equation = request.POST.getlist("used_answer_in_quadratic_equation")
    if not(used_answer_in_quadratic_equation):
        used_answer_in_quadratic_equation.append("integer")
        used_answer_in_quadratic_equation.append("frac")
    math_problem_tuple_list = []
    for _ in range(int(PROBLEM_NUMBER // 2)):
        problem1 = QuadraticInequality(used_quadratic_equation=used_quadratic_equation, used_answer_in_quadratic_equation=used_answer_in_quadratic_equation)
        problem2 = QuadraticInequality(used_quadratic_equation=used_quadratic_equation, used_answer_in_quadratic_equation=used_answer_in_quadratic_equation)
        math_problem_tuple_list.append((problem1, problem2))
    return render(request, 'math_print/highschool1/quadratic_inequality/for_display.html', {'math_problem_tuple_list': math_problem_tuple_list})


def display_same_denominator_calculate_problem(request):
    PROBLEM_NUMBER = 20
    calculate_type = request.POST.getlist("same_denominator_calculate_type")
    if not(calculate_type):
        calculate_type.append("addition")
        calculate_type.append("subtraction")
    term_number = request.POST.getlist("term_number")
    if not(term_number):
        term_number.append("2")
        term_number.append("3")
        term_number.append("4")
    math_problem_tuple_list = []
    for _ in range(int(PROBLEM_NUMBER // 2)):
        problem1 = SameDenominatorCalculate(calculate_type=calculate_type, term_number=term_number)
        problem2 = SameDenominatorCalculate(calculate_type=calculate_type, term_number=term_number)
        math_problem_tuple_list.append((problem1, problem2))
    return render(request, 'math_print/elementary_school3/same_denominator_calculate/for_display.html', {'math_problem_tuple_list': math_problem_tuple_list})


def display_line_and_flat_positional_relationship(request):
    """画面用の直線と平面の位置関係の問題のリクエスト受信と問題出力を担当。
    
    Args:
        request (django.core.handlers.wsgi.WSGIRequest): 送信されたリクエスト
    
    Returns:
        render (django.http.response.HttpResponse): Httpでページを表示するための諸要素    
    """
    PROBLEM_NUMBER = 10
    question_format = request.POST["question_format"]
    used_problems = request.POST.getlist("used_problem")
    if not(used_problems):
        used_problems.append("line_and_line")
        used_problems.append("line_and_flat")
        used_problems.append("flat_and_flat")
    used_solid_bodies = request.POST.getlist("used_solid_body")
    if not(used_solid_bodies):
        used_solid_bodies.append("quadrangular_prism")
        used_solid_bodies.append("triangular_prism")
    math_problem_tuple_list = []
    for _ in range(int(PROBLEM_NUMBER // 2)):
        problem1 = LineAndFlatPositionalRelationship(used_problems=used_problems, used_solid_bodies=used_solid_bodies, question_format=question_format)
        problem2 = LineAndFlatPositionalRelationship(used_problems=used_problems, used_solid_bodies=used_solid_bodies, question_format=question_format)
        math_problem_tuple_list.append((problem1, problem2))
    return render(request, 'math_print/junior_highschool1/line_and_flat_positional_relationship/for_display.html', {'math_problem_tuple_list': math_problem_tuple_list})


def display_calculate_area_by_integration(request):
    """平面上の面積を、積分の各種公式を使って求める問題のリクエスト受信と問題出力を担当。

    Args:
        request (django.core.handlers.wsgi.WSGIRequest): 送信されたリクエスト
    
    Returns:
        render (django.http.response.HttpResponse): Httpでページを表示するための諸要素
    """
    # PROBLEM_NUMBER = 4
    PROBLEM_NUMBER = 20
    problem_types = []
    problem_types += request.POST.getlist("one_sixth_problem_type")
    problem_types += request.POST.getlist("one_third_problem_type")
    problem_types += request.POST.getlist("one_twelfth_problem_type")
    if not (problem_types):
        problem_types.append("between_quadratic_function_and_x_axis")
        problem_types.append("between_quadratic_function_and_line")
        problem_types.append("between_quadratic_functions")
        problem_types.append("between_cubic_functions")
        problem_types.append("between_quadratic_function_and_tangent_and_parallel_line_with_y_axis")
        problem_types.append("between_two_quadratic_functions_that_touch_each_other_and_parallel_line_with_y_axis")
        problem_types.append("between_quadratic_function_and_two_tangents")
    math_problem_tuple_list = []
    for _ in range(int(PROBLEM_NUMBER // 2)):
        problem1 = CalculateAreaByIntegration(problem_types=problem_types)
        problem2 = CalculateAreaByIntegration(problem_types=problem_types)
        math_problem_tuple_list.append((problem1, problem2))
    return render(request, 'math_print/highschool2/calculate_area_by_integration/for_display.html', {'math_problem_tuple_list': math_problem_tuple_list})


def display_logarithmic_equation(request):
    """対数方程式の問題のリクエスト受信と問題出力を担当

    Args:
        request (django.core.handlers.wsgi.WSGIRequest): 送信されたリクエスト

    Returns:
        render (django.http.response.HttpResponse): Httpでページを表示するための諸要素
    """
    PROBLEM_NUMBER = 4
    problem_types = request.POST.getlist("logarithmic_equation_type")
    if not(problem_types):
        problem_types.append("only_with_calculation")
        problem_types.append("with_calculation_and_change_base_of_formula")
        problem_types.append("with_replacement")
    math_problem_tuple_list = []
    for _ in range(int(PROBLEM_NUMBER // 2)):
        problem1 = LogarithmicEquation(problem_types=problem_types)
        problem2 = LogarithmicEquation(problem_types=problem_types)
        math_problem_tuple_list.append((problem1, problem2))
    return render(request, 'math_print/highschool2/logarithmic_equation/for_display.html', {'math_problem_tuple_list': math_problem_tuple_list})


def display_ratio(request):
    """分数の倍や割合を求める問題のリクエスト受信と問題出力を担当
    
    Args:
        request (django.core.handlers.wsgi.WSGIRequest): 送信されたリクエスト

    Returns:
        render (django.http.response.HttpResponse): Httpでページを表示するための諸要素    
    """
    PROBLEM_NUMBER = 8
    problem_types = request.POST.getlist("problem_type")
    if not(problem_types):
        problem_types.append("amount_to_compare")
        problem_types.append("standard_amount")
        problem_types.append("ratio")
    used_numbers_for_ratio = request.POST.getlist("used_number_for_ratio")
    if not(used_numbers_for_ratio):
        used_numbers_for_ratio.append("decimal")
        used_numbers_for_ratio.append("percentage")
        used_numbers_for_ratio.append("japanese_percentage")
    unit_change = request.POST["unit_change"]
    if unit_change == "yes":
        used_unit_change = True
    elif unit_change == "no":
        used_unit_change = False
    digit_under_the_decimal_point = [int(num_str) for num_str in request.POST.getlist("digit_under_the_decimal_point")]
    if not(digit_under_the_decimal_point):
        digit_under_the_decimal_point.append(1)
        digit_under_the_decimal_point.append(2)
        digit_under_the_decimal_point.append(3)
    math_problem_tuple_list = []
    for _ in range(int(PROBLEM_NUMBER // 2)):
        problem1 = RatioProblem(
            problem_types=problem_types, used_numbers_for_ratio=used_numbers_for_ratio,
            used_unit_change=used_unit_change, digit_under_the_decimal_point=digit_under_the_decimal_point
        )
        problem2 = RatioProblem(
            problem_types=problem_types, used_numbers_for_ratio=used_numbers_for_ratio,
            used_unit_change=used_unit_change, digit_under_the_decimal_point=digit_under_the_decimal_point
        )
        math_problem_tuple_list.append((problem1, problem2))
    return render(request, 'math_print/elementary_school5/ratio/for_display.html', {"math_problem_tuple_list": math_problem_tuple_list})

def display_division_for_elementary_school3(request):
    """小学3年生用の割り算の問題の表示を担当

    Args:
        request (django.core.handlers.wsgi.WSGIRequest): 送信されたリクエスト

    Returns:
        render (django.http.response.HttpResponse): Httpでページを表示するための諸要素    
    """
    PROBLEM_NUMBER = 20
    remainder_types = request.POST.getlist("remainder_type")
    if not(remainder_types):
        remainder_types.append("without_remainder")
        remainder_types.append("with_remainder")
    digit_of_divided_numbers = request.POST.getlist("digit_of_divided_number")
    if not(digit_of_divided_numbers):
        digit_of_divided_numbers.append("1")
        digit_of_divided_numbers.append("2")
    math_problem_tuple_list = []
    for _ in range(int(PROBLEM_NUMBER // 2)):
        problem1 = DivisionFor3rdGrade(remainder_types=remainder_types, digit_of_divided_numbers=digit_of_divided_numbers)
        problem2 = DivisionFor3rdGrade(remainder_types=remainder_types, digit_of_divided_numbers=digit_of_divided_numbers)
        math_problem_tuple_list.append((problem1, problem2))
    return render(request, 'math_print/elementary_school3/division/for_display.html', {"math_problem_tuple_list": math_problem_tuple_list})


def display_addition_and_subtraction_for_elementary_school3(request):
    """小学3年生用の足し算引き算の問題の表示を担当

    Args:
        request (django.core.handlers.wsgi.WSGIRequest): 送信されたリクエスト

    Returns:
        render (django.http.response.HttpResponse): Httpでページを表示するための諸要素    
    """
    PROBLEM_NUMBER = 20
    used_calculations = request.POST.getlist("used_calculation")
    if not(used_calculations):
        used_calculations.append("addition")
        used_calculations.append("subtraction")
    digits_of_number = request.POST.getlist("digit_of_number")
    if not(digits_of_number):
        digits_of_number.append("3")
        digits_of_number.append("4")
        digits_of_number.append("5")
    math_problem_tuple_list = []
    for _ in range(PROBLEM_NUMBER // 2):
        problem1 = AdditionAndSubtractionFor3rdGrade(used_calculations=used_calculations, digits_of_number=digits_of_number)
        problem2 = AdditionAndSubtractionFor3rdGrade(used_calculations=used_calculations, digits_of_number=digits_of_number)
        math_problem_tuple_list.append((problem1, problem2))
    return render(request, 'math_print/elementary_school3/addition_and_subtraction/for_display.html', {"math_problem_tuple_list": math_problem_tuple_list})

def display_multiplication_for_elementary_school3(request):
    """小学生用の掛け算の問題の表示を担当

    Args:
        request (django.core.handlers.wsgi.WSGIRequest): 送信されたリクエスト

    Returns:
        render (django.http.response.HttpResponse): Httpでページを表示するための諸要素 
    """
    PROBLEM_NUMBER = 20
    digits_of_multiplied_number = request.POST.getlist("digit_of_multiplied_number")
    if not(digits_of_multiplied_number):
        digits_of_multiplied_number.append("2")
        digits_of_multiplied_number.append("3")
        digits_of_multiplied_number.append("4")
        digits_of_multiplied_number.append("5")
    digits_of_multiplying_number = request.POST.getlist("digit_of_multiplying_number")
    if not(digits_of_multiplying_number):
        digits_of_multiplying_number.append("2")
        digits_of_multiplying_number.append("3")
        digits_of_multiplying_number.append("4")
        digits_of_multiplying_number.append("5")
    math_problem_tuple_list = []
    for _ in range(PROBLEM_NUMBER // 2):
        problem1 = MultiplicationFor3rdGrade(digits_of_multiplied_number=digits_of_multiplied_number, digits_of_multiplying_number=digits_of_multiplying_number)
        problem2 = MultiplicationFor3rdGrade(digits_of_multiplied_number=digits_of_multiplied_number, digits_of_multiplying_number=digits_of_multiplying_number)
        math_problem_tuple_list.append((problem1, problem2))
    return render(request, 'math_print/elementary_school3/multiplication/for_display.html', {"math_problem_tuple_list": math_problem_tuple_list})


def display_calculation_of_big_number(request):
    """1億を超える数を用いた計算問題の表示を担当
    
    Args:
        request (django.core.handlers.wsgi.WSGIRequest): 送信されたリクエスト

    Returns:
        render (django.http.response.HttpResponse): Httpでページを表示するための諸要素 
    """
    PROBLEM_NUMBER = 20
    units_of_used_number = request.POST.getlist("unit_of_used_number")
    if not(units_of_used_number):
        units_of_used_number.append("hundred_million")
        units_of_used_number.append("trillion")
        units_of_used_number.append("ten_quadrillion")
    problem_types = request.POST.getlist("problem_type")
    if not(problem_types):
        problem_types.append("conversion_from_chinese_numerical_to_alphanumeric")
        problem_types.append("conversion_from_alphanumeric_to_chinese_numerical")
        problem_types.append("unite_numbers")
        problem_types.append("addition")
        problem_types.append("subtraction")
        problem_types.append("multiplication")
        problem_types.append("division")
    math_problem_tuple_list = []
    for _ in range(PROBLEM_NUMBER // 2):
        problem1 = CalculationOfBigNumber(units_of_used_number=units_of_used_number, problem_types=problem_types)
        problem2 = CalculationOfBigNumber(units_of_used_number=units_of_used_number, problem_types=problem_types)
        math_problem_tuple_list.append((problem1, problem2))
    return render(request, 'math_print/elementary_school4/calculation_of_big_number/for_display.html', {'math_problem_tuple_list': math_problem_tuple_list})

def display_division_for_elementary_school4(request):
    """小学4年生用の割り算の問題の表示を担当

    Args:
        request (django.core.handlers.wsgi.WSGIRequest): 送信されたリクエスト

    Returns:
        render (django.http.response.HttpResponse): Httpでページを表示するための諸要素    
    """
    PROBLEM_NUMBER = 20
    remainder_types = request.POST.getlist("remainder_type")
    if not(remainder_types):
        remainder_types.append("without_remainder")
        remainder_types.append("with_remainder")
    digits_of_divided_number = request.POST.getlist("digit_of_divided_number")
    if not(digits_of_divided_number):
        digits_of_divided_number.append("1")
        digits_of_divided_number.append("2")
        digits_of_divided_number.append("3")
    digits_of_dividing_number = request.POST.getlist("digit_of_dividing_number")
    if not(digits_of_dividing_number):
        digits_of_dividing_number.append("1")
        digits_of_dividing_number.append("2")
        digits_of_dividing_number.append("3")
    math_problem_tuple_list = []
    for _ in range(int(PROBLEM_NUMBER // 2)):
        problem1 = DivisionFor4thGrade(
            remainder_types=remainder_types,
            digits_of_divided_number=digits_of_divided_number, digits_of_dividing_number=digits_of_dividing_number)
        problem2 = DivisionFor4thGrade(
            remainder_types=remainder_types,
            digits_of_divided_number=digits_of_divided_number, digits_of_dividing_number=digits_of_dividing_number)
        math_problem_tuple_list.append((problem1, problem2))
    return render(request, 'math_print/elementary_school4/division/for_display.html', {"math_problem_tuple_list": math_problem_tuple_list})

def display_addition_and_subtraction_of_decimal_for_elementary_school4(request):
    """小学4年生用の小数の足し算と引き算の問題の表示を担当

    Args:
        request (django.core.handlers.wsgi.WSGIRequest): 送信されたリクエスト

    Returns:
        render (django.http.response.HttpResponse): Httpでページを表示するための諸要素    
    """
    PROBLEM_NUMBER = 20
    calculation_types = request.POST.getlist("calculation_type")
    if not(calculation_types):
        calculation_types.append("addition")
        calculation_types.append("subtraction")
    numbers_of_decimal_places = request.POST.getlist("number_of_decimal_places")
    if not(numbers_of_decimal_places):
        numbers_of_decimal_places.append("1")
        numbers_of_decimal_places.append("2")
        numbers_of_decimal_places.append("3")
    math_problem_tuple_list = []
    for _ in range(PROBLEM_NUMBER // 2):
        problem1 = AdditionAndSubtractionOfDecimalFor4thGrade(calculation_types=calculation_types, numbers_of_decimal_places=numbers_of_decimal_places)
        problem2 = AdditionAndSubtractionOfDecimalFor4thGrade(calculation_types=calculation_types, numbers_of_decimal_places=numbers_of_decimal_places)
        math_problem_tuple_list.append((problem1, problem2))
    return render(request, 'math_print/elementary_school4/addition_and_subtraction_of_decimal/for_display.html', {'math_problem_tuple_list': math_problem_tuple_list})
    

def display_multiplication_of_decimal_for_elementary_school4(request):
    """小学4年生用の小数のかけ算の問題の表示を担当

    Args:
        request (django.core.handlers.wsgi.WSGIRequest): 送信されたリクエスト

    Returns:
        render (django.http.response.HttpResponse): Httpでページを表示するための諸要素    
    """
    PROBLEM_NUMBER = 20
    multiplied_numbers_of_decimal_places = request.POST.getlist("multiplied_number_of_decimal_places")
    if not(multiplied_numbers_of_decimal_places):
        multiplied_numbers_of_decimal_places.append("0")
        multiplied_numbers_of_decimal_places.append("1")
        multiplied_numbers_of_decimal_places.append("2")
        multiplied_numbers_of_decimal_places.append("3")
    multiplying_numbers_of_decimal_places = request.POST.getlist("multiplying_number_of_decimal_places")
    if not(multiplying_numbers_of_decimal_places):
        multiplying_numbers_of_decimal_places.append("0")
        multiplying_numbers_of_decimal_places.append("1")
        multiplying_numbers_of_decimal_places.append("2")
        multiplying_numbers_of_decimal_places.append("3")
    math_problem_tuple_list = []
    for _ in range(PROBLEM_NUMBER // 2):
        problem1 = MultiplicationOfDecimalFor4thGrade(multiplied_numbers_of_decimal_places=multiplied_numbers_of_decimal_places, multiplying_numbers_of_decimal_places=multiplying_numbers_of_decimal_places)
        problem2 = MultiplicationOfDecimalFor4thGrade(multiplied_numbers_of_decimal_places=multiplied_numbers_of_decimal_places, multiplying_numbers_of_decimal_places=multiplying_numbers_of_decimal_places)
        math_problem_tuple_list.append((problem1, problem2))
    return render(request, 'math_print/elementary_school4/multiplication_of_decimal/for_display.html', {'math_problem_tuple_list': math_problem_tuple_list})


def display_division_of_decimal_for_elementary_school4(request):
    """小学4年生用の小数の割り算の問題の表示を担当

    Args:
        request (django.core.handlers.wsgi.WSGIRequest): 送信されたリクエスト

    Returns:
        render (django.http.response.HttpResponse): Httpでページを表示するための諸要素    
    """
    PROBLEM_NUMBER = 10
    remainder_types = request.POST.getlist("remainder_type")
    if not(remainder_types):
        remainder_types.append("without_remainder")
        remainder_types.append("with_remainder")
    decimal_places_of_divided_number = request.POST.getlist("decimal_places_of_divided_number")
    if not(decimal_places_of_divided_number):
        decimal_places_of_divided_number.append("0")
        decimal_places_of_divided_number.append("1")
        decimal_places_of_divided_number.append("2")
        decimal_places_of_divided_number.append("3")
    decimal_places_of_dividing_number = request.POST.getlist("decimal_places_of_dividing_number")
    if not(decimal_places_of_dividing_number):
        decimal_places_of_dividing_number.append("0")
        decimal_places_of_dividing_number.append("1")
        decimal_places_of_dividing_number.append("2")
        decimal_places_of_dividing_number.append("3")
    decimal_places_of_quotient = request.POST.getlist("decimal_places_of_quotient")
    if not(decimal_places_of_quotient):
        decimal_places_of_quotient.append("1")
        decimal_places_of_quotient.append("2")
        decimal_places_of_quotient.append("3")
    math_problem_tuple_list = []
    for _ in range(PROBLEM_NUMBER // 2):
        problem1 = DivisionOfDecimalFor4thGrade(
            remainder_types=remainder_types,
            decimal_places_of_divided_number=decimal_places_of_divided_number,
            decimal_places_of_dividing_number=decimal_places_of_dividing_number,
            decimal_places_of_quotient=decimal_places_of_quotient
            )
        problem2 = DivisionOfDecimalFor4thGrade(
            remainder_types=remainder_types,
            decimal_places_of_divided_number=decimal_places_of_divided_number,
            decimal_places_of_dividing_number=decimal_places_of_dividing_number,
            decimal_places_of_quotient=decimal_places_of_quotient
            )
        math_problem_tuple_list.append((problem1, problem2))
    return render(request, 'math_print/elementary_school4/division_of_decimal/for_display.html', {'math_problem_tuple_list': math_problem_tuple_list})


def display_addition_and_subtraction_of_fraction_for_elementary_school4(request):
    """小学4年生用の分数の足し算と引き算の問題の表示を担当

    Args:
        request (django.core.handlers.wsgi.WSGIRequest): 送信されたリクエスト

    Returns:
        render (django.http.response.HttpResponse): Httpでページを表示するための諸要素    
    """
    PROBLEM_NUMBER = 20
    used_calculations = request.POST.getlist("used_calculation")
    if not(used_calculations):
        used_calculations.append("from_improper_fraction_to_mixed_number_or_integer")
        used_calculations.append("from_mixed_number_to_improper_fraction")
        used_calculations.append("addition")
        used_calculations.append("subtraction")
        used_calculations.append("fill_in_the_square")
    integer_part = request.POST.getlist("integer_part")
    if not(integer_part):
        integer_part.append("with_integer_part")
        integer_part.append("without_integer_part")
    math_problem_tuple_list = []
    for _ in range(PROBLEM_NUMBER // 2):
        problem1 = AdditionAndSubtractionOfFraction(used_calculations=used_calculations, integer_part=integer_part)
        problem2 = AdditionAndSubtractionOfFraction(used_calculations=used_calculations, integer_part=integer_part)
        math_problem_tuple_list.append((problem1, problem2))
    return render(request, 'math_print/elementary_school4/addition_and_subtraction_of_fraction/for_display.html', {'math_problem_tuple_list': math_problem_tuple_list})


def display_multiplication_and_division_of_decimal_and_integer(request):
    return render(request, 'math_print/elementary_school6/multiplication_and_division_of_decimal_and_integer/for_display.html', {})


# explain section
def explain_one_sixth_calculate_area_by_integration(request):
    """平面上の面積を、1/6公式を使って求める問題の解き方の解説を担当。
    
    Args:
        request (django.core.handlers.wsgi.WSGIRequest): 送信されたリクエスト
    
    Returns:
        returned_render (django.http.response.HttpResponse): 描画のもろもろ
    """
    returned_render = render(request, 'math_print/highschool2/calculate_area_by_integration/for_explain_one_sixth.html', {})
    return returned_render

def explain_one_sixth_calculate_area_by_integration_print(request):
    """平面上の面積を、1/6公式を使って求める問題の解き方の解説プリントの出力を担当。
    
    Args:
        request (django.core.handlers.wsgi.WSGIRequest): 送信されたリクエスト
    
    Returns:
        returned_render (django.http.response.HttpResponse): 描画のもろもろ
    """
    returned_render = render(request, 'math_print/highschool2/calculate_area_by_integration/for_explain_one_sixth_print.html', {})
    return returned_render

def explain_one_third_calculate_area_by_integration(request):
    """平面上の面積を、1/3公式を使って求める問題の解き方の解説を担当。
    
    Args:
        request (django.core.handlers.wsgi.WSGIRequest): 送信されたリクエスト
    
    Returns:
        returned_render (django.http.response.HttpResponse): 描画のもろもろ
    """
    returned_render = render(request, 'math_print/highschool2/calculate_area_by_integration/for_explain_one_third.html', {})
    return returned_render

def explain_one_third_calculate_area_by_integration_print(request):
    """平面上の面積を、1/3公式を使って求める問題の解き方の解説プリントの出力を担当。
    
    Args:
        request (django.core.handlers.wsgi.WSGIRequest): 送信されたリクエスト
    
    Returns:
        returned_render (django.http.response.HttpResponse): 描画のもろもろ
    """
    returned_render = render(request, 'math_print/highschool2/calculate_area_by_integration/for_explain_one_third_print.html', {})
    return returned_render

def explain_number_without_bracket(request):
    """カッコなしの正負の計算の解き方の解説を担当。
    
    Args:
        request (django.core.handlers.wsgi.WSGIRequest): 送信されたリクエスト
    
    Returns:
        returned_render (django.http.response.HttpResponse): 描画のもろもろ
    """
    returned_render = render(request, 'math_print/junior_highschool1/number_without_bracket/for_explain.html', {})
    return returned_render


def explain_number_without_bracket_print(request):
    """カッコなしの正負の計算の解き方の解説プリントを担当。
    
    Args:
        request (django.core.handlers.wsgi.WSGIRequest): 送信されたリクエスト
    
    Returns:
        returned_render (django.http.response.HttpResponse): 描画のもろもろ
    """
    returned_render = render(request, 'math_print/junior_highschool1/number_without_bracket/for_explain_print.html', {})
    return returned_render


def explain_specific_linear_equation(request):
    """特定の形の1次方程式の解き方の解説を担当。
    
    Args:
        request (django.core.handlers.wsgi.WSGIRequest): 送信されたリクエスト
    
    Returns:
        returned_render (django.http.response.HttpResponse): 描画のもろもろ
    """
    returned_render = render(request, 'math_print/junior_highschool1/specific_linear_equation/for_explain.html', {})
    return returned_render


def explain_specific_linear_equation_print(request):
    """特定の形の1次方程式の解き方の解説プリントを担当。
    
    Args:
        request (django.core.handlers.wsgi.WSGIRequest): 送信されたリクエスト
    
    Returns:
        returned_render (django.http.response.HttpResponse): 描画のもろもろ
    """
    returned_render = render(request, 'math_print/junior_highschool1/specific_linear_equation/for_explain_print.html', {})
    return returned_render


def explain_logarithmic_equation(request):
    """対数方程式の解き方の解説を担当
    
    Args:
        request (django.core.handlers.wsgi.WSGIRequest): 送信されたリクエスト
    
    Returns:
        returned_render (django.http.response.HttpResponse): 描画のもろもろ
    """
    returned_render = render(request, 'math_print/highschool2/logarithmic_equation/for_explain.html', {})
    return returned_render


def explain_logarithmic_equation_print(request):
    """対数方程式の解き方の解説プリント出力を担当
    
    Args:
        request (django.core.handlers.wsgi.WSGIRequest): 送信されたリクエスト
    
    Returns:
        returned_render (django.http.response.HttpResponse): 描画のもろもろ
    """
    returned_render = render(request, 'math_print/highschool2/logarithmic_equation/for_explain_print.html', {})
    return returned_render


def explain_quadratic_equation(request):
    """2次方程式の解き方の解説を担当
    
    Args:
        request (django.core.handlers.wsgi.WSGIRequest): 送信されたリクエスト
    
    Returns:
        returned_render (django.http.response.HttpResponse): 描画のもろもろ
    """
    returned_render = render(request, 'math_print/junior_highschool3/quadratic_equation/for_explain.html', {})
    return returned_render


def explain_quadratic_equation_print(request):
    """2次方程式の解き方の解説プリント出力を担当
    
    Args:
        request (django.core.handlers.wsgi.WSGIRequest): 送信されたリクエスト
    
    Returns:
        returned_render (django.http.response.HttpResponse): 描画のもろもろ
    """
    returned_render = render(request, 'math_print/junior_highschool3/quadratic_equation/for_explain_print.html', {})
    return returned_render


def explain_ratio(request):
    """割合・百分率・歩合の問題の解き方の表示を担当
    
    Args:
        request (django.core.handlers.wsgi.WSGIRequest): 送信されたリクエスト
    
    Returns:
        returned_render (django.http.response.HttpResponse): 描画のもろもろ    
    """
    returned_render = render(request, 'math_print/elementary_school5/ratio/for_explain.html', {})
    return returned_render

def explain_ratio_print(request):
    """割合・百分率・歩合の問題の解き方の印刷用表示を担当
    
    Args:
        request (django.core.handlers.wsgi.WSGIRequest): 送信されたリクエスト
    
    Returns:
        returned_render (django.http.response.HttpResponse): 描画のもろもろ    
    """
    returned_render = render(request, 'math_print/elementary_school5/ratio/for_explain_print.html', {})
    return returned_render

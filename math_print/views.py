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


def index(request):
    return render(request, 'math_print/index.html', {})

# for graphic sample
def graphic_sample(request):
    return render(request, 'math_print/result.html', {})

def show_elementary_school3(request):
    return render(request, 'math_print/elementary_school3/elementary_school3.html', {})

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
    
    return render(request, 'math_print/junior_highschool1/linear_equation/for_print.html', {'math_problem_list_of_list': math_problem_list_of_list})

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
    
    operator_to_use_list = request.POST.getlist("operator_to_use")
    number_to_use_list = request.POST.getlist("number_to_use_without_bracket_problem")
    term_number = int(request.POST["term_number"])
    paper_number = int(request.POST["paper_number"])
    
    math_problem_list_of_list = []
    for _ in range(paper_number):
        math_problem_tuple_inner_list = []
        for _ in range(int(PROBLEM_NUMBER//2)):
            problem1 = NumberWithoutBracketCalculateProblem(
                operator_to_use_list=operator_to_use_list, number_to_use_list=number_to_use_list,
                term_number=term_number
            )
            problem2 = NumberWithoutBracketCalculateProblem(
                operator_to_use_list=operator_to_use_list, number_to_use_list=number_to_use_list,
                term_number=term_number
            )
            math_problem_tuple_inner_list.append((problem1, problem2))
        math_problem_list_of_list.append(math_problem_tuple_inner_list)
    
    return render(request, 'math_print/junior_highschool1/number/for_print.html', {'math_problem_list_of_list': math_problem_list_of_list})
    
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
    paper_number = int(request.POST["paper_number"])
    if request.POST["organization_coefficient_or_not"] == "organization_coefficient":
        organization_coefficient = True
    else:
        organization_coefficient = False
    
    used_formula_list = []
    if quadratic_equation_type_list:
        if "x^2+2ax+a^2=(x+a)^2" in quadratic_equation_type_list:
            used_formula_list.append("\( x^2 + 2ax + a^2 = (x + a)^2 \)")
        if "x^2-2ax+a^2=(x-a)^2" in quadratic_equation_type_list:
            used_formula_list.append("\( x^2 - 2ax + a^2 = (x - a)^2 \)")
        if "x^2+(a+b)x+ab=(x+a)(x+b)" in quadratic_equation_type_list:
            used_formula_list.append("\( x^2+(a+b)x+ab=(x+a)(x+b) \)")
        if "x^2-a^2=(x+a)(x-a)" in quadratic_equation_type_list:
            used_formula_list.append("\( x^2-a^2=(x+a)(x-a) \)")
        if "quadratic_formula" in quadratic_equation_type_list:
            used_formula_list.append("\( x = \\frac{-b\pm\sqrt{b^2-4ac}}{2a} \)")
    else:
        used_formula_list.append("\( x^2 + 2ax + a^2 = (x + a)^2 \)")
        used_formula_list.append("\( x^2 - 2ax + a^2 = (x - a)^2 \)")
        used_formula_list.append("\( x^2+(a+b)x+ab=(x+a)(x+b) \)")
        used_formula_list.append("\( x^2-a^2=(x+a)(x-a) \)")
        used_formula_list.append("\( x = \\frac{-b\pm\sqrt{b^2-4ac}}{2a} \)")
        
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
    # pprint.pprint(math_problem_list_of_list)

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
    
    math_problem_list_of_list = []
    for _ in range(paper_number):
        math_problem_tuple_inner_list = []
        for _ in range(int(PROBLEM_NUMBER//2)):
            problem1 = FillInTheSquareProblem(calculation_type_list=calculation_type_list)
            problem2 = FillInTheSquareProblem(calculation_type_list=calculation_type_list)
            math_problem_tuple_inner_list.append((problem1, problem2))
        math_problem_list_of_list.append(math_problem_tuple_inner_list)
    
    return render(request, 'math_print/elementary_school6/fill_in_the_square/for_print.html', {'math_problem_list_of_list': math_problem_list_of_list})
  
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
    
    problem_type_list = request.POST.getlist("problem_type")
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
            problem1 = SquareRootProblem(problem_type_list=problem_type_list)
            problem2 = SquareRootProblem(problem_type_list=problem_type_list)
            math_problem_tuple_inner_list.append((problem1, problem2))
        math_problem_list_of_list.append(math_problem_tuple_inner_list)
    
    return render(request, 'math_print/junior_highschool3/square_root/for_print.html', {'math_problem_list_of_list': math_problem_list_of_list})

def print_square_root_problem(request):
    PROBLEM_NUMBER = 20
    problem_types = request.POST.getlist("problem_type")
    if not(problem_types):
        problem_types.append("write_square_root_not_using_radical_sign")
        problem_types.append("write_square_root_using_radical_sign")
        problem_types.append("put_coefficient_into_radical_sign")
        problem_types.append("take_out_coefficient_from_radical_sign_inside")
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
    print(f"number_to_use: {number_to_use}")
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
    
    return render(request, 'math_print/junior_highschool1/linear_equation/for_display.html', {'math_problem_tuple_list': math_problem_tuple_list})

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
    
    operator_to_use_list = request.POST.getlist("number_without_bracket_operator_to_use")
    number_to_use_list = request.POST.getlist("number_to_use_without_bracket_problem")
    term_number = int(request.POST["term_number"])
    
    math_problem_tuple_list = []
    for _ in range(int(PROBLEM_NUMBER//2)):
        problem1 = NumberWithoutBracketCalculateProblem(
            term_number=term_number, operator_to_use_list=operator_to_use_list,
            number_to_use_list=number_to_use_list
        )
        problem2 = NumberWithoutBracketCalculateProblem(
            term_number=term_number, operator_to_use_list=operator_to_use_list,
            number_to_use_list=number_to_use_list
        )
        math_problem_tuple_list.append((problem1, problem2))
    
    return render(request, 'math_print/junior_highschool1/number/for_display.html', {'math_problem_tuple_list': math_problem_tuple_list})

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
        if "x^2+2ax+a^2=(x+a)^2" in quadratic_equation_type_list:
            used_formula_list.append("\( x^2 + 2ax + a^2 = (x + a)^2 \)")
        if "x^2-2ax+a^2=(x-a)^2" in quadratic_equation_type_list:
            used_formula_list.append("\( x^2 - 2ax + a^2 = (x - a)^2 \)")
        if "x^2+(a+b)x+ab=(x+a)(x+b)" in quadratic_equation_type_list:
            used_formula_list.append("\( x^2+(a+b)x+ab=(x+a)(x+b) \)")
        if "x^2-a^2=(x+a)(x-a)" in quadratic_equation_type_list:
            used_formula_list.append("\( x^2-a^2=(x+a)(x-a) \)")
        if "quadratic_formula" in quadratic_equation_type_list:
            used_formula_list.append("\( x = \\frac{-b\pm\sqrt{b^2-4ac}}{2a} \)")
    else:
        used_formula_list.append("\( x^2 + 2ax + a^2 = (x + a)^2 \)")
        used_formula_list.append("\( x^2 - 2ax + a^2 = (x - a)^2 \)")
        used_formula_list.append("\( x^2+(a+b)x+ab=(x+a)(x+b) \)")
        used_formula_list.append("\( x^2-a^2=(x+a)(x-a) \)")
        used_formula_list.append("\( x = \\frac{-b\pm\sqrt{b^2-4ac}}{2a} \)")

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
    
    print(f"request: {request}")
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

    problem_type_list = request.POST.getlist("problem")
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
        calculation_type_list.append("exponent_to_linear_characteristic_equation")
    
    math_problem_tuple_list = []
    for _ in range(int(PROBLEM_NUMBER//2)):
        problem1 = FillInTheSquareProblem(calculation_type_list=calculation_type_list)
        problem2 = FillInTheSquareProblem(calculation_type_list=calculation_type_list)
        math_problem_tuple_list.append((problem1, problem2))
    
    return render(request, 'math_print/elementary_school6/fill_in_the_square/for_display.html', {'math_problem_tuple_list': math_problem_tuple_list})

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
    
    problem_type_list = request.POST.getlist("problem_type")
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
        problem_types.append("write_square_root_not_using_radical_sign")
        problem_types.append("write_square_root_using_radical_sign")
        problem_types.append("put_coefficient_into_radical_sign")
        problem_types.append("take_out_coefficient_from_radical_sign_inside")
    math_problem_tuple_list = []
    for _ in range(int(PROBLEM_NUMBER//2)):
        problem1 = SquareRootProblem(problem_types=problem_types)
        problem2 = SquareRootProblem(problem_types=problem_types)
        math_problem_tuple_list.append((problem1, problem2))
    return render(request, 'math_print/junior_highschool3/square_root/for_display.html', {'math_problem_tuple_list': math_problem_tuple_list})

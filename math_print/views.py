"""
Fixing
4/1
------
数の範囲を入力する際に、数字が誤って消されてしまうと、(おそらく)ValueErrorを吐いてしまうことの修正
->分数計算のなかでも約分と計算で発生する模様
おそらく原因は、
min_number_to_denominator = int(request.POST["min_number_to_denominator"])
でnoneやそれに準じるなにかをintで読み込もうとしている点っぽい
→int の前に、if is not Noneをはさむことで解決するとおもわれ
"""
import unicodedata

from django.http import HttpResponse
from django.shortcuts import render
from sympy.geometry import line

from .math_process.character_calculate import CharacterMathProblem
from .math_process.linear_equation import LinearEquationProblem
from .math_process.number_calculate import NumberMathProblem
from .math_process.specific_linear_equation import SpecificLinearEquation
from .math_process.simultaneous_equation import SimultaneousEquation
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


# Create your views here.
def index(request):
    return render(request, 'math_print/index.html', {})

def show_elementary_school5(request):
    return render(request, 'math_print/elementary_school5/elementary_school5.html', {})

def show_junior_highschool1(request):
    return render(request, 'math_print/junior_highschool1/junior_highschool1.html', {})

def show_junior_highschool2(request):
    return render(request, 'math_print/junior_highschool2/junior_highschool2.html', {})

def show_junior_highschool3(request):
    return render(request, 'math_print/junior_highschool3/junior_highschool3.html', {})

def show_highschool1(request):
    return render(request, 'math_print/highschool1/highschool1.html', {})

def print_number_problem(request):
    PROBLEM_NUMBER = 20

    result = request.POST
    print(f"result: {result}")
    number_to_use = request.POST.getlist("number_to_use")
    print(f"number_to_use: {number_to_use} \n type: {type(number_to_use)}")
    operator_to_use = request.POST.getlist("operator_to_use")
    print(f"operator_to_use: {operator_to_use} \n type; {type(operator_to_use)}")
    term_number = int(request.POST["term_number"])
    print(f"term_number: {term_number} \n type: {type(term_number)}")
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

    result = request.POST
    print(f"result: {result}")
    number_to_use = request.POST.getlist("number_to_use")
    print(f"number_to_use: {number_to_use} \n type: {type(number_to_use)}")
    operator_to_use = request.POST.getlist("operator_to_use")
    print(f"operator_to_use: {operator_to_use} \n type; {type(operator_to_use)}")
    term_number = int(request.POST["term_number"])
    print(f"term_number: {term_number} \n type: {type(term_number)}")
    paper_number = int(request.POST["paper_number"])
    print(f"paper_number: {paper_number}")
    character_to_use = request.POST["character_to_use"]
    print(f"character_to_use: {character_to_use}")
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
    
    result = request.POST
    # print(f"result: {result}")
    number_to_use = request.POST.getlist("number_to_use")
    # print(f"number_to_use: {number_to_use} \n type: {type(number_to_use)}")
    operator_to_use = request.POST.getlist("operator_to_use")
    # print(f"operator_to_use: {operator_to_use} \n type: {type(operator_to_use)}")
    term_number = int(request.POST["term_number"])
    # print(f"term_number: {term_number} \n type: {type(term_number)}")
    paper_number = int(request.POST["paper_number"])
    # print(f"paper_number: {paper_number}")

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
    number_to_use = request.POST.getlist("number_to_use")
    paper_number = int(request.POST["paper_number"])
    
    math_problem_list_of_list = []
    for _ in range(paper_number):
        math_problem_tuple_inner_list = []
        for _ in range(int(PROBLEM_NUMBER//2)):
            problem1 = SpecificLinearEquation(
                used_number_type_list=number_to_use, linear_equation_type_list=linear_equation_type_list
            )
            problem2 = SpecificLinearEquation(
                used_number_type_list=number_to_use, linear_equation_type_list=linear_equation_type_list
            )
            math_problem_tuple_inner_list.append((problem1, problem2))
        math_problem_list_of_list.append(math_problem_tuple_inner_list)
    
    return render(request, 'math_print/junior_highschool1/linear_equation/for_print.html', {'math_problem_list_of_list': math_problem_list_of_list})

def print_simultaneous_equation(request):
    PROBLEM_NUMBER = 20
    
    simultaneous_equation_type = request.POST["simultaneous_equation_type"]
    number_to_use = request.POST.getlist("number_to_use")
    paper_number = int(request.POST["paper_number"])

    math_problem_list_of_list = []
    for _ in range(paper_number):
        math_problem_tuple_inner_list = []
        for _ in range(int(PROBLEM_NUMBER//2)):
            problem1 = SimultaneousEquation(
                used_number_type_list=number_to_use, simultaneous_equation_type=simultaneous_equation_type
            )
            problem2 = SimultaneousEquation(
                used_number_type_list=number_to_use, simultaneous_equation_type=simultaneous_equation_type
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
    
    math_problem_list_of_list = []
    for _ in range(paper_number):
        math_problem_tuple_inner_list = []
        for _ in range(int(PROBLEM_NUMBER//2)):
            problem1 = CompletingTheSquareProblem(
                used_number_type_list=number_to_use, number_including_in_bracket=number_including_in_bracket
            )
            problem2 = CompletingTheSquareProblem(
                used_number_type_list=number_to_use, number_including_in_bracket=number_including_in_bracket
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
    
    number_to_use = request.POST.getlist("number_to_use")
    calculate_type = request.POST.getlist("calculate_type")
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
    
    # print(f"post: {request.POST}")
    
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
    
    factorization_type_list = request.POST.getlist("factorization_type")
    used_coefficient = request.POST["coefficient_used_for_factorization"]
    paper_number = int(request.POST["paper_number"])
    
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
    
    """
    使用される公式
    ax+ab=a(x+b)
    \( ax + ab = a(x + b) \)
    
    x^2+2ax+a^2=(x+a)^2
    \( x^2 + 2ax + a^2 = (x + a)^2 \)

    x^2-2ax+a^2=(x-a)^2
    \( x^2 - 2ax + a^2 = (x - a)^2 \)

    x^2+(a+b)x+ab=(x+a)(x+b)
    \( x^2 + (a + b)x + ab = (x + a)(x + b) \)
    """
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
    context["used_formula_list"] = used_formula_list

    return render(request, 'math_print/junior_highschool3/factorization/for_print.html', context)

def print_quadratic_equation(request):
    PROBLEM_NUMBER = 20
    
    quadratic_equation_type_list = request.POST.getlist("quadratic_equation_type")
    paper_number = int(request.POST["paper_number"])
    if request.POST["factor_out_or_not"] == "factor_out":
        factor_out = True
    else:
        factor_out = False
    
    used_formula_list = []
    if "x^2+2ax+a^2=(x+a)^2" in quadratic_equation_type_list:
        used_formula_list.append("\( x^2 + 2ax + a^2 = (x + a)^2 \)")
    if "x^2-2ax+a^2=(x-a)^2" in quadratic_equation_type_list:
        used_formula_list.append("\( x^2 - 2ax + a^2 = (x - a)^2 \)")
    if "x^2+(a+b)x+ab=(x+a)(x+b)" in quadratic_equation_type_list:
        used_formula_list.append("\( x^2+(a+b)x+ab=(x+a)(x+b) \)")
    if "x^2-a^2=(x+a)(x-a)" in quadratic_equation_type_list:
        used_formula_list.append("\( x^2-a^2=(x+a)(x-a) \)")
    if "quadratic_formula" in quadratic_equation_type_list:
        used_formula_list.append("\( x = \frac{-b\pm\sqrt{b^2-4ac}}{2a} \)")
        
    math_problem_list_of_list = []
    for _ in range(paper_number):
        math_problem_tuple_inner_list = []
        for _ in range(int(PROBLEM_NUMBER//2)):
            problem1 = QuadraticEquationProblem(
                quadratic_equation_type_list=quadratic_equation_type_list, factor_out=factor_out
            )
            problem2 = QuadraticEquationProblem(
                quadratic_equation_type_list=quadratic_equation_type_list, factor_out=factor_out
            )
            math_problem_tuple_inner_list.append((problem1, problem2))
        math_problem_list_of_list.append(math_problem_tuple_inner_list)
    
    context = {}
    context["math_problem_list_of_list"] = math_problem_list_of_list
    context["used_formula_list"] = used_formula_list

    return render(request, 'math_print/junior_highschool3/quadratic_equation/for_print.html', context)

def display_number_problem(request):
    PROBLEM_NUMBER = 20

    result = request.POST
    print(f"result: {result}")
    number_to_use = request.POST.getlist("number_to_use")
    print(f"number_to_use: {number_to_use} \n type: {type(number_to_use)}")
    operator_to_use = request.POST.getlist("operator_to_use")
    print(f"operator_to_use: {operator_to_use} \n type: {type(operator_to_use)}")
    term_number = int(request.POST["term_number"])
    print(f"term_number: {term_number} \n type: {type(term_number)}")

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

    result = request.POST
    print(f"result: {result}")
    number_to_use = request.POST.getlist("number_to_use")
    print(f"number_to_use: {number_to_use} \n type: {type(number_to_use)}")
    operator_to_use = request.POST.getlist("operator_to_use")
    print(f"operator_to_use: {operator_to_use} \n type; {type(operator_to_use)}")
    term_number = int(request.POST["term_number"])
    print(f"term_number: {term_number} \n type: {type(term_number)}")
    paper_number = int(request.POST["paper_number"])
    print(f"paper_number: {paper_number}")
    character_to_use = request.POST["character_to_use"]
    print(f"character_to_use: {character_to_use}")
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
    
    result = request.POST
    # print(f"result: {result}")
    number_to_use = request.POST.getlist("number_to_use")
    # print(f"number_to_use: {number_to_use} \n type: {type(number_to_use)}")
    operator_to_use = request.POST.getlist("operator_to_use")
    # print(f"operator_to_use: {operator_to_use} \n type: {type(operator_to_use)}")
    term_number = int(request.POST["term_number"])
    # print(f"term_number: {term_number} \n type: {type(term_number)}")
    character_to_use_list = ["x"]
    # print(f"character_to_use_list: {character_to_use_list} \n type: {type(character_to_use_list)}")

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
    number_to_use = request.POST.getlist("number_to_use")
    
    math_problem_tuple_list = []
    for _ in range(int(PROBLEM_NUMBER//2)):
        problem1 = SpecificLinearEquation(
            used_number_type_list=number_to_use, linear_equation_type_list=linear_equation_type_list
            )
        problem2 = SpecificLinearEquation(
            used_number_type_list=number_to_use, linear_equation_type_list=linear_equation_type_list
        )
        math_problem_tuple_list.append((problem1, problem2))
    
    return render(request, 'math_print/junior_highschool1/linear_equation/for_display.html', {'math_problem_tuple_list': math_problem_tuple_list})

def display_simultaneous_equation(request):
    PROBLEM_NUMBER = 20
    
    simultaneous_equation_type = request.POST["simultaneous_equation_type"]
    used_number_type_list = request.POST.getlist("number_to_use")
    print(f"used_number_type_list: {used_number_type_list}")
    
    math_problem_tuple_list = []
    for _ in range(int(PROBLEM_NUMBER//2)):
        problem1 = SimultaneousEquation(
            used_number_type_list=used_number_type_list, simultaneous_equation_type=simultaneous_equation_type
        )
        problem2 = SimultaneousEquation(
            used_number_type_list=used_number_type_list, simultaneous_equation_type=simultaneous_equation_type
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
    
    math_problem_tuple_list = []
    for _ in range(int(PROBLEM_NUMBER//2)):
        problem1 = CompletingTheSquareProblem(
            used_number_type_list=number_to_use, number_including_in_bracket=number_including_in_bracket
        )
        problem2 = CompletingTheSquareProblem(
            used_number_type_list=number_to_use, number_including_in_bracket=number_including_in_bracket
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
    
    number_to_use = request.POST.getlist("number_to_use")
    calculate_type = request.POST.getlist("calculate_type")
    
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
    
    operator_to_use_list = request.POST.getlist("operator_to_use")
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
    if "ax+ab=a(x+b)" in factorization_type_list:
        used_formula_list.append("\( ax + ab = a(x + b) \)")
    
    if "x^2+2ax+a^2=(x+a)^2" in factorization_type_list:
        used_formula_list.append("\( x^2 + 2ax + a^2 = (x + a)^2 \)")
    
    if "x^2-2ax+a^2=(x-a)^2" in factorization_type_list:
        used_formula_list.append("\( x^2 - 2ax + a^2 = (x - a)^2 \)")
    
    if "x^2+(a+b)x+ab=(x+a)(x+b)" in factorization_type_list:
        used_formula_list.append("\( x^2 + (a + b)x + ab = (x + a)(x + b) \)")
    
    print(f"used_formula_list: {used_formula_list}")
    
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
    if request.POST["factor_out_or_not"] == "factor_out":
        factor_out = True
    else:
        factor_out = False
    
    used_formula_list = []
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

    math_problem_tuple_list = []
    for _ in range(int(PROBLEM_NUMBER//2)):
        problem1 = QuadraticEquationProblem(
            quadratic_equation_type_list=quadratic_equation_type_list, factor_out=factor_out
        )
        problem2 = QuadraticEquationProblem(
            quadratic_equation_type_list=quadratic_equation_type_list, factor_out=factor_out
        )
        math_problem_tuple_list.append((problem1, problem2))
    
    context = {}
    context["math_problem_tuple_list"] = math_problem_tuple_list
    context["used_formula_list"] = used_formula_list
    return render(request, 'math_print/junior_highschool3/quadratic_equation/for_display.html', context)

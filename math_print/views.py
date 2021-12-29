from django.http import HttpResponse
from django.shortcuts import render
from sympy.geometry import line

from math_print.math_process.completing_the_square import CompletingTheSquareProblem

from .math_process.character_calculate import CharacterMathProblem
from .math_process.linear_equation import LinearEquationProblem
from .math_process.number_calculate import NumberMathProblem
from .math_process.specific_linear_equation import SpecificLinearEquation
from .math_process.simultaneous_equation import SimultaneousEquation
from .math_process.expand_equation import ExpandEquationProblem
from .math_process.completing_the_square import CompletingTheSquareProblem
from .math_process.proportional_expression import ProportionalExpressionProblem
from .math_process.linear_function import LinearFunctionProblem


# Create your views here.
def index(request):
    return render(request, 'math_print/index.html', {})

def make_math_print(request):
    math_problem_tuple_list = []
    NUMBER_OF_PROBLEM = 10
    MAX_NUMBER_TO_FRAC = 10
    MIN_NUMBER_TO_FRAC = -10
    TERM_NUMBER = 3
    for _ in range(NUMBER_OF_PROBLEM):
        problem1 = NumberMathProblem(TERM_NUMBER, MAX_NUMBER_TO_FRAC, MIN_NUMBER_TO_FRAC)
        problem2 = NumberMathProblem(TERM_NUMBER, MAX_NUMBER_TO_FRAC, MIN_NUMBER_TO_FRAC)
        math_problem_tuple_list.append((problem1, problem2))

    return render(request, 'math_print/calculate.html', {'math_problem_tuple_list': math_problem_tuple_list})

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

    return render(request, 'math_print/junior_highschool1/number/number_for_print.html', {'math_problem_list_of_list': math_problem_list_of_list})

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
    """
    elif character_to_use == "3":
        character_to_use_list += ["y", "z"]
    """

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

    return render(request, 'math_print/junior_highschool1/character/character_for_print.html', {'math_problem_list_of_list': math_problem_list_of_list})

def print_linear_equation_problem(request):
    PROBLEM_NUMBER = 20
    
    result = request.POST
    print(f"result: {result}")
    number_to_use = request.POST.getlist("number_to_use")
    print(f"number_to_use: {number_to_use} \n type: {type(number_to_use)}")
    operator_to_use = request.POST.getlist("operator_to_use")
    print(f"operator_to_use: {operator_to_use} \n type: {type(operator_to_use)}")
    term_number = int(request.POST["term_number"])
    print(f"term_number: {term_number} \n type: {type(term_number)}")
    paper_number = int(request.POST["paper_number"])
    print(f"paper_number: {paper_number}")
    """
    character_to_use_list = ["x"]
    print(f"character_to_use_list: {character_to_use_list} \n type: {type(character_to_use_list)}")
    """

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

    return render(request, 'math_print/junior_highschool1/linear_equation/linear_equation_for_print.html', {'math_problem_list_of_list': math_problem_list_of_list})

def print_specific_linear_equation(request):
    PROBLEM_NUMBER = 20
    
    linear_equation_type = request.POST["linear_equation_type"]
    number_to_use = request.POST.getlist("number_to_use")
    paper_number = int(request.POST["paper_number"])
    
    math_problem_list_of_list = []
    for _ in range(paper_number):
        math_problem_tuple_inner_list = []
        for _ in range(int(PROBLEM_NUMBER//2)):
            problem1 = SpecificLinearEquation(
                used_number_type_list=number_to_use, linear_equation_type=linear_equation_type
            )
            problem2 = SpecificLinearEquation(
                used_number_type_list=number_to_use, linear_equation_type=linear_equation_type
            )
            math_problem_tuple_inner_list.append((problem1, problem2))
        math_problem_list_of_list.append(math_problem_tuple_inner_list)
    
    return render(request, 'math_print/junior_highschool1/linear_equation/linear_equation_for_print.html', {'math_problem_list_of_list': math_problem_list_of_list})

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
    
    return render(request, "math_print/junior_highschool2/simultaneous_equations/simultaneous_equations_for_print.html", {"math_problem_list_of_list": math_problem_list_of_list})

def print_expand_equation(request):
    PROBLEM_NUMBER = 20

    number_to_use = request.POST.getlist("number_to_use")
    expand_equation_type = request.POST["expand_equation_type"]
    paper_number = int(request.POST["paper_number"])
    
    math_problem_list_of_list = []
    for _ in range(paper_number):
        math_problem_tuple_inner_list = []
        for _ in range(int(PROBLEM_NUMBER//2)):
            problem1 = ExpandEquationProblem(
                used_number_type_list=number_to_use, expand_equation_type=expand_equation_type
            )
            problem2 = ExpandEquationProblem(
                used_number_type_list=number_to_use, expand_equation_type=expand_equation_type
            )
            math_problem_tuple_inner_list.append((problem1, problem2))
        math_problem_list_of_list.append(math_problem_tuple_inner_list)
    
    return render(request, "math_print/junior_highschool3/expand_equation/expand_equation_for_print.html", {'math_problem_list_of_list': math_problem_list_of_list})

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
    
    return render(request, "math_print/highschool1/completing_the_square/completing_the_square_for_print.html", {'math_problem_list_of_list': math_problem_list_of_list})

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
    
    return render(request, "math_print/junior_highschool1/proportional_expression/proportional_expression_for_print.html", {'math_problem_list_of_list': math_problem_list_of_list})

def print_linear_function(request):
    PROBLEM_NUMBER = 20
    
    number_to_use = request.POST.getlist("number_to_use")
    given_information = request.POST["given_information"]
    paper_number = int(request.POST["paper_number"])
    
    math_problem_list_of_list = []
    for _ in range(paper_number):
        math_problem_tuple_inner_list = []
        for _ in range(int(PROBLEM_NUMBER//2)):
            problem1 = LinearFunctionProblem(
                number_to_use=number_to_use, given_information=given_information
            )
            problem2 = LinearFunctionProblem(
                number_to_use=number_to_use, given_information=given_information
            )
            math_problem_tuple_inner_list.append((problem1, problem2))
        math_problem_list_of_list.append(math_problem_tuple_inner_list)
    
    return render(request, "math_print/junior_highschool2/linear_function/linear_function_for_print.html", {'math_problem_list_of_list': math_problem_list_of_list})
        

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

    return render(request, 'math_print/junior_highschool1/number/number_for_display.html', {'math_problem_tuple_list': math_problem_tuple_list})

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
    
    return render(request, 'math_print/junior_highschool1/character/character_for_display.html', {'math_problem_tuple_list': math_problem_tuple_list})

def display_linear_equation_problem(request):
    PROBLEM_NUMBER = 20
    
    result = request.POST
    print(f"result: {result}")
    number_to_use = request.POST.getlist("number_to_use")
    print(f"number_to_use: {number_to_use} \n type: {type(number_to_use)}")
    operator_to_use = request.POST.getlist("operator_to_use")
    print(f"operator_to_use: {operator_to_use} \n type: {type(operator_to_use)}")
    term_number = int(request.POST["term_number"])
    print(f"term_number: {term_number} \n type: {type(term_number)}")
    character_to_use_list = ["x"]
    print(f"character_to_use_list: {character_to_use_list} \n type: {type(character_to_use_list)}")

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
    
    return render(request, 'math_print/junior_highschool1/linear_equation/linear_equation_for_display.html', {'math_problem_tuple_list': math_problem_tuple_list})

def display_specific_linear_equation(request):
    PROBLEM_NUMBER = 20
    
    linear_equation_type = request.POST["linear_equation_type"]
    number_to_use = request.POST.getlist("number_to_use")
    
    math_problem_tuple_list = []
    for _ in range(int(PROBLEM_NUMBER//2)):
        problem1 = SpecificLinearEquation(
            used_number_type_list=number_to_use, linear_equation_type=linear_equation_type
            )
        problem2 = SpecificLinearEquation(
            used_number_type_list=number_to_use, linear_equation_type=linear_equation_type
        )
        math_problem_tuple_list.append((problem1, problem2))
    
    return render(request, 'math_print/junior_highschool1/linear_equation/linear_equation_for_display.html', {'math_problem_tuple_list': math_problem_tuple_list})

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
    
    return render(request, 'math_print/junior_highschool2/simultaneous_equations/simultaneous_equations_for_display.html', {'math_problem_tuple_list': math_problem_tuple_list})

def display_expand_equation(request):
    PROBLEM_NUMBER = 20

    number_to_use = request.POST.getlist("number_to_use")
    expand_equation_type = request.POST["expand_equation_type"]

    math_problem_tuple_list = []
    for _ in range(int(PROBLEM_NUMBER/2)):
        problem1 = ExpandEquationProblem(
            used_number_type_list = number_to_use, expand_equation_type=expand_equation_type
        )
        problem2 = ExpandEquationProblem(
            used_number_type_list = number_to_use, expand_equation_type=expand_equation_type
        )
        math_problem_tuple_list.append((problem1, problem2))
    
    return render(request, 'math_print/junior_highschool3/expand_equation/expand_equation_for_display.html', {'math_problem_tuple_list': math_problem_tuple_list})

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
    
    return render(request, 'math_print/highschool1/completing_the_square/completing_the_square_for_display.html', {'math_problem_tuple_list': math_problem_tuple_list})

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
    
    return render(request, 'math_print/junior_highschool2/linear_function/linear_function_for_display.html', {'math_problem_tuple_list': math_problem_tuple_list})

def display_linear_function(request):
    PROBLEM_NUMBER = 20
    
    number_to_use = request.POST.getlist("number_to_use")
    given_information = request.POST["given_information"]
    
    math_problem_tuple_list = []
    for _ in range(int(PROBLEM_NUMBER//2)):
        problem1 = LinearFunctionProblem(
            number_to_use=number_to_use, given_information=given_information
        )
        problem2 = LinearFunctionProblem(
            number_to_use=number_to_use, given_information=given_information
        )
        math_problem_tuple_list.append((problem1, problem2))
    
    return render(request, 'math_print/junior_highschool2/linear_function/linear_function_for_display.html', {'math_problem_tuple_list': math_problem_tuple_list})
    

from django.http import HttpResponse
from django.shortcuts import render

from .math_calculate import MathProblem



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
        problem1 = MathProblem(TERM_NUMBER, MAX_NUMBER_TO_FRAC, MIN_NUMBER_TO_FRAC)
        problem2 = MathProblem(TERM_NUMBER, MAX_NUMBER_TO_FRAC, MIN_NUMBER_TO_FRAC)
        math_problem_tuple_list.append((problem1, problem2))

    return render(request, 'math_print/calculate.html', {'math_problem_tuple_list': math_problem_tuple_list})

def print_problem(request):
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
            problem1 = MathProblem(term_number, MAX_NUMBER_TO_FRAC, MIN_NUMBER_TO_FRAC, number_to_use, operator_to_use)
            problem2 = MathProblem(term_number, MAX_NUMBER_TO_FRAC, MIN_NUMBER_TO_FRAC, number_to_use, operator_to_use)
            math_problem_tuple_inner_list.append((problem1, problem2))
        math_problem_list_of_list.append(math_problem_tuple_inner_list)

    # print(f"ren of math_problem_tuple_list: {len(math_problem_tuple_inner_list)}")
    return render(request, 'math_print/for_print.html', {'math_problem_list_of_list': math_problem_list_of_list})

def display_problem(request):
    PROBLEM_NUMBER = 20

    result = request.POST
    print(f"result: {result}")
    number_to_use = request.POST.getlist("number_to_use")
    print(f"number_to_use: {number_to_use} \n type: {type(number_to_use)}")
    term_number = int(request.POST["term_number"])
    print(f"term_number: {term_number} \n type: {type(term_number)}")
    paper_number = int(request.POST["paper_number"])

    MAX_NUMBER_TO_FRAC = 10
    MIN_NUMBER_TO_FRAC = -10

    math_problem_list_of_list = []
    for _ in range(paper_number):
        math_problem_tuple_inner_list = []
        for _ in range(int(PROBLEM_NUMBER/2)):
            problem1 = MathProblem(term_number, MAX_NUMBER_TO_FRAC, MIN_NUMBER_TO_FRAC, number_to_use)
            problem2 = MathProblem(term_number, MAX_NUMBER_TO_FRAC, MIN_NUMBER_TO_FRAC, number_to_use)
            math_problem_tuple_inner_list.append((problem1, problem2))
        math_problem_list_of_list.append(math_problem_tuple_inner_list)
    return HttpResponse("This is dummy page for solving on display page!")

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

def select_problem(request):
    result = request.POST
    return render(request, 'math_print/result.html', {'result': result})

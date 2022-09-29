from random import choice


import sympy as sy


class SquareRootProblem:
    
    def __init__(self, **settings):
        self._problem_types = settings["problem_types"]
        self.latex_answer, self.latex_problem = self._make_problem()
    
    def _make_problem(self):
        selected_problem_type = choice(self._problem_types)
        if selected_problem_type == "write_square_root":
            latex_answer, latex_problem = self._make_write_square_root_problem()
        
        return latex_answer, latex_problem

    def _make_write_square_root_problem(self):
        latex_answer = "dummmmyyyyannsnsnsnswer"
        latex_problem = "dummummuuyyuproropoboelem"
        
        return latex_answer, latex_problem
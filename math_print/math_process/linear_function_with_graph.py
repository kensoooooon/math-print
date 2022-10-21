import sympy as sy


class LinearFunctionWithGraphProblem:
    
    def __init__(self, **settings):
        self.graph_to_use_list = settings["graph_to_use_list"]
        self.latex_answer, self.latex_problem = self._make_problem()
    
    def _make_problem(self):
        latex_answer = "dummy answer"
        latex_problem = "dummy problem"
        return latex_answer, latex_problem

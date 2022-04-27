from random import choice, randint, random

import sympy as sy

class CharacterFractionProblem:
    
    def __init__(self, **settings):
        self._term_number = settings["term_number"]
        self._character = {}
        characters = choice([("a", "b"), ("x", "y")])
        for index, character in enumerate(characters):
            self._character[f"character{index}"] = sy.Symbol(character, real=True)
        self.latex_answer, self.latex_problem = self._make_problem()
    
    def _make_problem(self):
        # (ka+lb)/num + ....
        c0 = self._character["character0"]
        c1 = self._character["character1"]
        problem = 0
        for index in range(self._term_number):
            denominator_of_term = randint(2, 6)
            numerator_of_term = self._make_random_number() * c0 + self._make_random_number() * c1
            term = sy.Rational(1, denominator_of_term) * numerator_of_term
            if random() > 0.5:
                problem += sy.factor(term)
            else:
                problem -= sy.factor(term)

        latex_problem = sy.latex(problem)
        answer = sy.simplify(problem)
        latex_answer = f"= {sy.latex(answer)}"       
        
        return latex_answer, latex_problem

    def _make_random_number(self, positive_or_negative=None):
        number = sy.Integer(randint(1, 6))
        
        if positive_or_negative is None:
            if random() > 0.5:
                number = -1 * number
        elif positive_or_negative == "negative":
            number = -1 * number
        elif positive_or_negative == "positive":
            pass
        
        return number
    
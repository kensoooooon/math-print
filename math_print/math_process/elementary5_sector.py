from random import choice, randint, random
from typing import NamedTuple

import sympy as sy


class Elementary5SectorWithFigureProblem:
    
    def __init__(self, **settings):
        sy.init_printing(order='grevlex')
        self._problem_type_list = settings["problem_type_list"]
        self.selected_problem_type, self.latex_answer, self.sector = self._make_problem()
    
    def _make_problem(self):
        selected_problem_type = choice(self._problem_type_list)
        
        if selected_problem_type == "basic":
            latex_answer, sector = self._make_basic_problem()
        elif selected_problem_type == "advance":
            pass
        # print(f"selected_problem_type: {selected_problem_type}, latex_answer: {latex_answer}, sector: {sector}")

        return selected_problem_type, latex_answer, sector
    
    def _make_basic_problem(self):
        sector = self._decide_sector_status()
        latex_answer =f"面積: \( {sy.latex(sector.area)} \\mathrm{{ cm^2 }} \)".replace("\\", "\\\\")
        return latex_answer, sector
    
    def _decide_sector_status(self):
        class Sector(NamedTuple):
            radius: str
            area: str
            central_angle: str

        # radius = randint(1, 10)
        if random() > 0.5:
            central_angle = 30 * randint(1, 11)
        else:
            central_angle = 45 * randint(1, 7)
        ratio_by_circle = sy.Rational(central_angle, 360)
        radius = ratio_by_circle.denominator
        area = str(sy.Integer(radius**2) * sy.Rational(central_angle, 360) * 3.14).replace("0", "")
        central_angle = str(central_angle)
        radius = str(radius)
        sector = Sector(radius=radius, area=area, central_angle=central_angle)
        return sector     
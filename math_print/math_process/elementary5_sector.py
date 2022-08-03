from random import choice, randint, random
from typing import NamedTuple

import sympy as sy
from sympy.parsing.sympy_parser import _add_factorial_tokens

class SectorWithFigureProblem:
    
    def __init__(self, **settings):
        sy.init_printing(order='grevlex')
        self._problem_type_list = settings["problem_type_list"]
        self.selected_problem_type, self.latex_answer, self.sector = self._make_problem()
    
    def _make_problem(self):
        selected_problem_type = choice(selected_problem_type)
        
        if selected_problem_type == "baumkuchen":
            latex_answer, sector = self._make_baumkuchen_problem()

        return selected_problem_type, latex_answer, sector
    
    def _make_baumkuchen_problem(self):
        return 115423

    def _make_radius_and_central_angle_to_arc_length_and_area_problem(self):
        sector = self._decide_sector_status()
        
        # latex_problem = f"半径{sector.radius_latex}、中心角{sector.central_angle_latex}のおうぎ形の弧の長さと面積"
        latex_answer = f"弧の長さ: \( {sy.latex(sector.coefficient_of_arc_length)} \\pi \\mathrm{{ cm }} \)、"\
            f"面積: \( {sy.latex(sector.coefficient_of_area)} \\pi \\mathrm{{ cm^2 }} \)".replace("\\", "\\\\")

        return latex_answer, sector
    
    def _decide_sector_status(self):
        
        class Sector(NamedTuple):
            radius: str
            coefficient_of_arc_length : str
            coefficient_of_area: str
            central_angle: str
            
        radius = randint(1, 10)
        if random() > 0.5:
            central_angle = str(30 * randint(1, 11))
        else:
            central_angle = str(45 * randint(1, 7))
        coefficient_of_arc_length = str(sy.Integer(2) * sy.Rational(central_angle, 360) * sy.Integer(radius))
        coefficient_of_area = str(sy.Integer(radius**2) * sy.Rational(central_angle, 360))
        
        sector = Sector(radius=radius, coefficient_of_arc_length=coefficient_of_arc_length,
                        coefficient_of_area=coefficient_of_area, central_angle=central_angle)
        
        return sector    
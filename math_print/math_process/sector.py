from random import choice, randint, random
from typing import NamedTuple

import sympy as sy
from sympy.parsing.sympy_parser import _add_factorial_tokens


"""
from typing import NamedTuple

class PathContainer(NamedTuple):
    root: str
    document: str
    exe: str

path_container = PathContainer("root_path","document_path","exe_path")
"""
    

class SectorProblem:
    
    def __init__(self, **settings):
        sy.init_printing(order='grevlex')
        self._problem_type_list = settings["problem_type_list"]
        self.latex_answer, self.latex_problem = self._make_problem()
    
    def _make_problem(self):
        selected_problem_type = choice(self._problem_type_list)
        
        if selected_problem_type == "radius_and_central_angle_to_arc_length_and_area":
            latex_answer, latex_problem = self._make_radius_and_central_angle_to_arc_length_and_area_problem()
        elif selected_problem_type == "radius_and_arc_length_to_area":
            latex_answer, latex_problem = self._make_radius_and_arc_length_to_area_problem()
        elif selected_problem_type == "radius_and_area_to_arc_length":
            latex_answer, latex_problem = self._make_radius_and_area_to_arc_length_problem()
        elif selected_problem_type == "radius_and_area_to_central_angle":
            latex_answer, latex_problem = self._make_radius_and_area_to_central_angle_problem()

        return latex_answer, latex_problem

    def _make_radius_and_central_angle_to_arc_length_and_area_problem(self):
        sector = self._decide_sector_status()
        
        latex_problem = f"半径{sector.radius_latex}、中心角{sector.central_angle_latex}のおうぎ形の弧の長さと面積"
        latex_answer = f"弧の長さ: {sector.arc_length_latex}、面積: {sector.area_latex}"

        return latex_answer, latex_problem
    
    def _make_radius_and_arc_length_to_area_problem(self):
        sector = self._decide_sector_status()
        
        latex_problem = f"半径{sector.radius_latex}、弧の長さ{sector.arc_length_latex}のおうぎ形の面積"
        latex_answer = f"面積: {sector.area_latex}"
        
        return latex_answer, latex_problem
    
    def _make_radius_and_area_to_arc_length_problem(self):
        sector = self._decide_sector_status()
        
        latex_problem = f"半径{sector.radius_latex}、面積{sector.area_latex}のおうぎ形の弧の長さ"
        latex_answer = f"弧の長さ: {sector.arc_length_latex}"
        
        return latex_answer, latex_problem
    
    def _make_radius_and_area_to_central_angle_problem(self):
        sector = self._decide_sector_status()
        
        latex_problem = f"半径{sector.radius_latex}、面積{sector.area_latex}のおうぎ形の中心角"
        latex_answer = f"中心角{sector.central_angle_latex}"
        
        return latex_answer, latex_problem
    
    def _decide_sector_status(self):
        
        class Sector(NamedTuple):
            radius_latex: str
            arc_length_latex: str
            central_angle_latex: str
            area_latex: str
        
        radius = randint(1, 10)
        radius_latex = f"\( {sy.latex(radius)} \\mathrm{{ cm }} \)"
        
        if random() > 0.5:
            central_angle = 30 * randint(1, 11)
        else:
            central_angle = 45 * randint(1, 7)
        central_angle_latex = f"\( {sy.latex(central_angle)} ^{{ \circ }} \)"

        coefficient_of_arc_length = sy.Integer(2) * sy.Rational(central_angle, 360) * sy.Integer(radius)
        arc_length_latex = f"\( {sy.latex(coefficient_of_arc_length)} \\pi \\mathrm{{ cm }} \)"
        
        coefficient_of_area = sy.Integer(radius**2) * sy.Rational(central_angle, 360)
        area_latex = f"\( {sy.latex(coefficient_of_area)} \\pi \\mathrm{{ cm^2 }} \)"
        
        sector = Sector(radius_latex, arc_length_latex, central_angle_latex, area_latex)
        
        return sector
    
        
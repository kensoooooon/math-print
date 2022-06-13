import math
from random import choice, randint, random
from typing import NamedTuple

import sympy as sy

class UnitConversionProblem:
    
    def __init__(self, **settings):
        sy.init_printing(order='grevlex')
        self._used_unit_list = settings["unit_type"]
        self.latex_answer, self.latex_problem = self._make_problem()
        
        def _make_problem(self):
            selected_unit_type = choice(self._used_unit_list)
        
            if selected_unit_type == "length":
                latex_answer, latex_problem = self._make_length_problem()
        
        def _make_length_problem(self):
            
            class LengthUnit(NamedTuple):
                unit: str
                ratio_to_kilometer : int

            kilometer_unit = LengthUnit(unit="km", ratio_to_kilometer=1)
            meter_unit = LengthUnit(unit="m", ratio_to_kilometer=1000)
            centimeter_unit = LengthUnit(unit="cm", ratio_to_kilometer=100000)
            millimeter_unit = LengthUnit(unit="mm", ratio_to_kilometer=1000000)
            unit_list = [kilometer_unit, meter_unit, centimeter_unit, millimeter_unit]
            larger_index, smaller_index = sorted(random.sample(range(len(unit_list)), k=2))
            larger_unit = unit_list[larger_index]
            smaller_unit = unit_list[smaller_index]
            larger_unit_coefficient = random.randint(1, 15)
            larger_value = larger_unit.ratio_to_kilometer * larger_unit_coefficient
            print(f"larger_value: {larger_value}{larger_unit.unit}")
            smaller_value = larger_value * (smaller_unit.ratio_to_kilometer / larger_unit.ratio_to_kilometer)
            print(f"smaller_value: {smaller_value}{smaller_unit.unit}")
            
            return latex_answer, latex_problem
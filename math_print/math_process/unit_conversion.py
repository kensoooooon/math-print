from random import choice, randint, random
from typing import NamedTuple

import sympy as sy

class UnitConversionProblem:
    
    def __init__(self, **settings):
        sy.init_printing(order='grevlex')
        self._used_unit_list = settings["used_unit_list"]
        self.latex_answer, self.latex_problem = self._make_problem()
        
    def _make_problem(self):
        selected_unit_type = choice(self._used_unit_list)
    
        if selected_unit_type == "length":
            latex_answer, latex_problem = self._make_length_problem()
        elif selected_unit_type == "weight":
            latex_answer, latex_problem = self._make_weight_problem()
        elif selected_unit_type == "area":
            latex_answer, latex_problem = self._make_area_problem()
        elif selected_unit_type == "volume":
            latex_answer, latex_problem = self._make_volume_problem()
        elif selected_unit_type == "time":
            latex_answer, latex_problem = self._make_time_problem()
                
        return latex_answer, latex_problem
    
    def _make_length_problem(self):
        
        class LengthUnit(NamedTuple):
            unit: str
            ratio_to_kilometer : int

        kilometer_unit = LengthUnit(unit="km", ratio_to_kilometer=1)
        meter_unit = LengthUnit(unit="m", ratio_to_kilometer=10**3)
        centimeter_unit = LengthUnit(unit="cm", ratio_to_kilometer=10**5)
        millimeter_unit = LengthUnit(unit="mm", ratio_to_kilometer=10**6)
        unit_list = [kilometer_unit, meter_unit, centimeter_unit, millimeter_unit]
        # larger_index, smaller_index = sorted(sample(range(len(unit_list)), k=2))
        larger_index = randint(0, len(unit_list) - 2)
        smaller_index = larger_index + randint(1, 2)
        if smaller_index > (len(unit_list) - 1):
            smaller_index = len(unit_list) - 1
        larger_unit = unit_list[larger_index]
        smaller_unit = unit_list[smaller_index]
        larger_unit_coefficient = randint(1, 15)
        larger_value = larger_unit_coefficient
        # print(f"larger_value: {larger_value}{larger_unit.unit}")
        smaller_value = int(larger_value * (smaller_unit.ratio_to_kilometer / larger_unit.ratio_to_kilometer))
        # print(f"smaller_value: {smaller_value}{smaller_unit.unit}")
        
        if random() > 0.5:
            latex_problem = f"{sy.latex(larger_value)} \mathrm{{{larger_unit.unit}}} = \square \mathrm{{{smaller_unit.unit}}}"
            latex_answer = f"{sy.latex(smaller_value)} \mathrm{{{smaller_unit.unit}}}"
        else:
            latex_problem = f"{sy.latex(smaller_value)} \mathrm{{{smaller_unit.unit}}} = \square \mathrm{{{larger_unit.unit}}}"
            latex_answer = f"{sy.latex(larger_value)}  \mathrm{{{larger_unit.unit}}}"
        
        # print(f"latex_answer: {latex_problem}")
        # print(f"latex_problem: {latex_problem}")
        
        return latex_answer, latex_problem

    def _make_weight_problem(self):
        
        class LengthUnit(NamedTuple):
            unit: str
            ratio_to_ton : int

        ton_unit = LengthUnit(unit="t", ratio_to_ton=1)
        kilogram_unit = LengthUnit(unit="kg", ratio_to_ton=10**3)
        gram_unit = LengthUnit(unit="g", ratio_to_ton=10**6)
        milligram_unit = LengthUnit(unit="mg", ratio_to_ton=10**9)
        unit_list = [ton_unit, kilogram_unit, gram_unit, milligram_unit]
        # larger_index, smaller_index = sorted(sample(range(len(unit_list)), k=2))
        larger_index = randint(0, len(unit_list) - 2)
        smaller_index = larger_index + randint(1, 2)
        if smaller_index > (len(unit_list) - 1):
            smaller_index = len(unit_list) - 1
        larger_unit = unit_list[larger_index]
        smaller_unit = unit_list[smaller_index]
        larger_unit_coefficient = randint(1, 15)
        larger_value = larger_unit_coefficient
        # print(f"larger_value: {larger_value}{larger_unit.unit}")
        smaller_value = int(larger_value * (smaller_unit.ratio_to_ton / larger_unit.ratio_to_ton))
        # print(f"smaller_value: {smaller_value}{smaller_unit.unit}")
        
        if random() > 0.5:
            latex_problem = f"{sy.latex(larger_value)} \mathrm{{{larger_unit.unit}}} = \square \mathrm{{{smaller_unit.unit}}}"
            latex_answer = f"{sy.latex(smaller_value)} \mathrm{{{smaller_unit.unit}}}"
        else:
            latex_problem = f"{sy.latex(smaller_value)} \mathrm{{{smaller_unit.unit}}} = \square \mathrm{{{larger_unit.unit}}}"
            latex_answer = f"{sy.latex(larger_value)}  \mathrm{{{larger_unit.unit}}}"
        
        # print(f"latex_answer: {latex_problem}")
        # print(f"latex_problem: {latex_problem}")
        
        return latex_answer, latex_problem

    def _make_area_problem(self):
        
        class AreaUnit(NamedTuple):
            unit: str
            ratio_to_square_kilometer : int

        square_kilometer_unit = AreaUnit(unit="km^2", ratio_to_square_kilometer=1)
        hectare_unit = AreaUnit("ha", ratio_to_square_kilometer=10**2)
        are_unit = AreaUnit("a", ratio_to_square_kilometer=10**4)
        square_meter_unit = AreaUnit(unit="m^2", ratio_to_square_kilometer=10**6)
        square_centimeter_unit = AreaUnit(unit="cm^2", ratio_to_square_kilometer=10**10)
        square_millimeter_unit = AreaUnit(unit="mm^2", ratio_to_square_kilometer=10**12)
        unit_list = [square_kilometer_unit, hectare_unit, are_unit, 
                     square_meter_unit, square_centimeter_unit, square_millimeter_unit,
                     ]
        # larger_index, smaller_index = sorted(sample(range(len(unit_list)), k=2))
        larger_index = randint(0, len(unit_list) - 2)
        smaller_index = larger_index + randint(1, 2)
        if smaller_index > (len(unit_list) - 1):
            smaller_index = len(unit_list) - 1
        larger_unit = unit_list[larger_index]
        smaller_unit = unit_list[smaller_index]
        larger_unit_coefficient = randint(1, 15)
        larger_value = larger_unit_coefficient
        # print(f"larger_value: {larger_value}{larger_unit.unit}")
        smaller_value = int(larger_value * (smaller_unit.ratio_to_square_kilometer / larger_unit.ratio_to_square_kilometer))
        # print(f"smaller_value: {smaller_value}{smaller_unit.unit}")
        
        if random() > 0.5:
            latex_problem = f"{sy.latex(larger_value)} \mathrm{{{larger_unit.unit}}} = \square \mathrm{{{smaller_unit.unit}}}"
            latex_answer = f"{sy.latex(smaller_value)} \mathrm{{{smaller_unit.unit}}}"
        else:
            latex_problem = f"{sy.latex(smaller_value)} \mathrm{{{smaller_unit.unit}}} = \square \mathrm{{{larger_unit.unit}}}"
            latex_answer = f"{sy.latex(larger_value)}  \mathrm{{{larger_unit.unit}}}"
        
        # print(f"latex_answer: {latex_problem}")
        # print(f"latex_problem: {latex_problem}")
        
        return latex_answer, latex_problem
    
    def _make_volume_problem(self):
        
        class VolumeUnit(NamedTuple):
            unit: str
            ratio_to_cubic_kilometer: int
        
        cubic_kilometer_unit = VolumeUnit(unit="km^3", ratio_to_cubic_kilometer=1)
        cubic_meter_unit = VolumeUnit(unit="m^3", ratio_to_cubic_kilometer=10**9)
        liter_unit = VolumeUnit(unit="L", ratio_to_cubic_kilometer=10**12)
        deciliter_unit = VolumeUnit(unit="dL", ratio_to_cubic_kilometer=10**13)
        cubic_centimeter_unit = VolumeUnit(unit="cm^3", ratio_to_cubic_kilometer=10**15)
        milliliter_unit = VolumeUnit(unit="mL", ratio_to_cubic_kilometer=10**15)
        cubic_millimeter_unit = VolumeUnit(unit="mm^3", ratio_to_cubic_kilometer=10**18)
        unit_list = [cubic_kilometer_unit, cubic_meter_unit,
                     liter_unit, deciliter_unit,
                     cubic_centimeter_unit, milliliter_unit,
                     cubic_millimeter_unit]
        # larger_index, smaller_index = sorted(sample(range(len(unit_list)), k=2))
        larger_index = randint(0, len(unit_list) - 2)
        smaller_index = larger_index + 1
        if smaller_index > (len(unit_list) - 1):
            smaller_index = len(unit_list) - 1
        larger_unit = unit_list[larger_index]
        smaller_unit = unit_list[smaller_index]
        larger_unit_coefficient = randint(1, 15)
        larger_value = larger_unit_coefficient
        # print(f"larger_value: {larger_value}{larger_unit.unit}")
        smaller_value = int(larger_value * (smaller_unit.ratio_to_cubic_kilometer / larger_unit.ratio_to_cubic_kilometer))
        # print(f"smaller_value: {smaller_value}{smaller_unit.unit}")
        
        if random() > 0.5:
            latex_problem = f"{sy.latex(larger_value)} \mathrm{{{larger_unit.unit}}} = \square \mathrm{{{smaller_unit.unit}}}"
            latex_answer = f"{sy.latex(smaller_value)} \mathrm{{{smaller_unit.unit}}}"
        else:
            latex_problem = f"{sy.latex(smaller_value)} \mathrm{{{smaller_unit.unit}}} = \square \mathrm{{{larger_unit.unit}}}"
            latex_answer = f"{sy.latex(larger_value)}  \mathrm{{{larger_unit.unit}}}"
        
        # print(f"latex_answer: {latex_problem}")
        # print(f"latex_problem: {latex_problem}")
        
        return latex_answer, latex_problem
    
    def _make_time_problem(self):
        
        from datetime import timedelta
        import re

        def get_hours_minutes_seconds(timedelta_value):
            minutes, seconds = divmod(timedelta_value.seconds, 60)
            hours, minutes = divmod(minutes, 60)
            return hours, minutes, seconds
        
        seconds = randint(1, 10000)
        seconds_str = f"{sy.latex(seconds)}秒"
        
        hours, minutes, seconds = get_hours_minutes_seconds(timedelta(seconds=seconds))
        hours_minutes_seconds_str = ""
        if hours:
            hours_minutes_seconds_str += f"{sy.latex(hours)}時間"
        if minutes:
            hours_minutes_seconds_str += f"{sy.latex(minutes)}分"
        if seconds:
            hours_minutes_seconds_str += f"{sy.latex(seconds)}秒"
        
        if random() > 0.5:
            replaced_hours_minutes_seconds_str = re.sub(r"\d+", r"\\square", hours_minutes_seconds_str)
            latex_problem = f"{seconds_str} = {replaced_hours_minutes_seconds_str}"
            latex_answer = hours_minutes_seconds_str
        else:
            replaced_seconds_str = re.sub(r"\d+", r"\\square", seconds_str)
            latex_problem = f"{hours_minutes_seconds_str} = {replaced_seconds_str}"
            latex_answer = seconds_str
        
        return latex_answer, latex_problem

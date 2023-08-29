from random import choice, randint, random, shuffle

import sympy as sy


class ExponentCalculation:
    
    def __init__(self, **settings):
        # times, division, power, root
        self._calculation_type = settings["calculation_type"]
        # number, character
        self._base_type_list = settings["base_type_list"]
        
        self.latex_answer, self.latex_problem = self._make_problem()
        
    def _make_problem(self):
        if self._calculation_type == "only_times_and_division":
            latex_answer, latex_problem = self._make_only_times_and_division_problem()
        elif self._calculation_type == "include_power":
            latex_answer, latex_problem = self._make_include_power_problem()
        elif self._calculation_type == "include_power_and_root":
            latex_answer, latex_problem = self._make_include_power_and_root_problem()
        return latex_answer, latex_problem

    def _make_only_times_and_division_problem(self):
        def exp(base, index):
            """
            if isinstance(base, int):
                exp_num = sy.Rational(base ** index)
            elif isinstance(base, sy.core.symbol.Symbol):
                exp_num = base ** index
            """
            exp_num = sy.Pow(base, index)
            exp_num_latex = f"{base}^{{{index}}}"
            return exp_num, exp_num_latex
        
        selected_base_type = choice(self._base_type_list)
        
        if selected_base_type == "character":
            base = sy.Symbol("a", real=True)
            index1 = self._random_index_without_zero_and_one(min_num=-8, max_num=8)
            index2 = self._random_index_without_zero_and_one(min_num=-8, max_num=8)
            index3 = self._random_index_without_zero_and_one(min_num=-8, max_num=8)
            index4 = self._random_index_without_zero_and_one(min_num=-8, max_num=8)
            index_list = [index1, index2, index3, index4]
            
            first_index = index_list.pop()
            first_num, first_latex = exp(base, first_index)
            answer = first_num
            latex_problem = first_latex
            for index in index_list:
                num, num_latex = exp(base, index)
                if random() > 0.5:
                    answer *= num
                    latex_problem += f"\\times {num_latex}"
                else:
                    answer /= num
                    latex_problem += f"\\div {num_latex}"
            
            latex_answer = f"= {sy.latex(answer)}"
            
            return latex_answer, latex_problem
            
        elif selected_base_type == "number":
            base = choice([2, 3, 5, 7])
            # redefine 2->6, 3->5, 4->4, 5->3: 
            final_index = self._random_index_without_zero_and_one(min_num=-(8 - base), max_num=8 - base)
            index1 = self._random_index_without_zero_and_one(min_num=-6, max_num=6)
            index2 = self._random_index_without_zero_and_one(min_num=-6, max_num=6)
            index3 = final_index - (index1 + index2)
            index_list = [index1, index2, index3]
            shuffle(index_list)
            
            first_index = index_list.pop()
            first_num, first_latex = exp(base, first_index)
            answer = first_num
            latex_problem = first_latex
            
            for index in index_list:
                if random() > 0.5: # add as times
                    num, num_latex = exp(base, index)
                    answer *= num
                    latex_problem += f" \\times {num_latex}"
                else: # add as division
                    num, num_latex = exp(base, -index)
                    answer /= num
                    latex_problem += f" \\div {num_latex}"

            latex_answer = f"= {sy.latex(answer)}"
        
            return latex_answer, latex_problem

    def _make_include_power_problem(self):
        def exp(base, inner_index=1, outer_index=1):
            if (inner_index == 1) and (outer_index == 1):
                exp_num = sy.Pow(base, 1)
                exp_num_latex = f"{base}"
            elif (inner_index == 1) and (outer_index != 1):
                exp_num = sy.Pow(base, outer_index)
                exp_num_latex = f"{base}^{{{outer_index}}}"
            elif (inner_index != 1) and (outer_index == 1):
                exp_num = sy.Pow(base, inner_index)
                exp_num_latex = f"{base}^{{{inner_index}}}"
            else:
                exp_num = sy.Pow(base, inner_index * outer_index)
                exp_num_latex = f"\\left( {base}^{{{inner_index}}} \\right)^{{{outer_index}}}"
            return exp_num, exp_num_latex
        
        selected_base_type = choice(self._base_type_list)
        
        if selected_base_type == "character":
            base = sy.Symbol("a", real=True)
            inner_index1 = self._random_index_without_zero_and_one(min_num=-3, max_num=3)
            outer_index1 = self._random_index_without_zero_and_one(min_num=-3, max_num=3)
            index1 = (inner_index1, outer_index1)
            inner_index2 = self._random_index_without_zero_and_one(min_num=-3, max_num=3)
            outer_index2 = self._random_index_without_zero_and_one(min_num=-3, max_num=3)
            index2 = (inner_index2, outer_index2)
            inner_index3 = self._random_index_without_zero_and_one(min_num=-3, max_num=3)
            outer_index3 = self._random_index_without_zero_and_one(min_num=-3, max_num=3)
            index3 = (inner_index3, outer_index3)
            inner_index4 = self._random_index_without_zero_and_one(min_num=-3, max_num=3)
            outer_index4 = self._random_index_without_zero_and_one(min_num=-3, max_num=3)
            index4 = (inner_index4, outer_index4)
            index_list = [index1, index2, index3, index4]
            
            first_inner_index, first_outer_index = index_list.pop()
            first_num, first_latex = exp(base, inner_index=first_inner_index, outer_index=first_outer_index)
            answer = first_num
            latex_problem = first_latex
            for inner_index, outer_index in index_list:
                num, num_latex = exp(base, inner_index=inner_index, outer_index=outer_index)
                if random() > 0.5:
                    answer *= num
                    latex_problem += f"\\times {num_latex}"
                else:
                    answer /= num
                    latex_problem += f"\\div {num_latex}"
            
            latex_answer = f"= {sy.latex(answer)}"

            return latex_answer, latex_problem

        elif selected_base_type == "number":
            base = choice([2, 3, 5, 7])
            final_index = self._random_index_without_zero_and_one(min_num=-(8 - base), max_num=8 - base)
            inner_index1 = self._random_index_without_zero_and_one(min_num=-3, max_num=3)
            outer_index1 = self._random_index_without_zero_and_one(min_num=-3, max_num=3)
            index1 = (inner_index1, outer_index1)
            inner_index2 = self._random_index_without_zero_and_one(min_num=-3, max_num=3)
            outer_index2 = self._random_index_without_zero_and_one(min_num=-3, max_num=3)
            index2 = (inner_index2, outer_index2)
            coordinate_index = final_index - (inner_index1 * outer_index1 + inner_index2 * outer_index2)
            if coordinate_index > 0:
                for num_for_div in range(coordinate_index - 1, 1, -1):
                    if (coordinate_index % num_for_div == 0):
                        inner_index3 = num_for_div
                        outer_index3 = int(coordinate_index / num_for_div)
                        break
                else:
                    inner_index3 = 1
                    outer_index3 = coordinate_index
            elif coordinate_index < 0:
                for num_for_div in range(coordinate_index + 1, -1, 1):
                    if (coordinate_index % num_for_div == 0):
                        inner_index3 = num_for_div
                        outer_index3 = int(coordinate_index / num_for_div)
                        break
                else:
                    inner_index3 = 1
                    outer_index3 = coordinate_index
            else:
                inner_index3 = 1
                outer_index3 = 0
            index3 = (inner_index3, outer_index3)
            index_list = [index1, index2, index3]
            shuffle(index_list)
            
            first_inner_index, first_outer_index = index_list.pop()
            first_num, first_latex = exp(base, inner_index=first_inner_index, outer_index=first_outer_index)
            answer = first_num
            latex_problem = first_latex
            
            for inner_index, outer_index in index_list:
                if random() > 0.5:  # add as times
                    if random() > 0.5:
                        num, num_latex = exp(base, inner_index=inner_index, outer_index=outer_index)
                    else:
                        num, num_latex = exp(base, inner_index=-inner_index, outer_index=-outer_index)
                    answer *= num
                    latex_problem += f" \\times {num_latex}"
                else:  # add as division
                    if random() > 0.5:
                        num, num_latex = exp(base, inner_index=-inner_index, outer_index=outer_index)
                    else: 
                        num, num_latex = exp(base, inner_index=inner_index, outer_index=-outer_index)
                    answer /= num
                    latex_problem += f"\\div {num_latex}"
                
            latex_answer = f"= {sy.latex(answer)}"
            return latex_answer, latex_problem
        
    def _make_include_power_and_root_problem(self):
        def exp(base, index_numerator=1, index_denominator1=1, index_denominator2=1):
            # a^{n/m} = \root[m]{a^n}
            index = sy.Rational(index_numerator, index_denominator1 * index_denominator2)
            exp_num = sy.Pow(base, index)
            
            base_latex = sy.latex(base)
            index_latex = sy.latex(index)
            index_numerator_latex = sy.latex(index_numerator)
            index_denominator1_latex = sy.latex(index_denominator1)
            index_denominator2_latex = sy.latex(index_denominator2)
            
            if (index_denominator1 == 1) and (index_denominator2 == 1):
                if random() > 0.5:
                    # a^m
                    exp_num_latex = f"{base_latex}^{{{index_numerator_latex}}}"
                else:
                    # (a^m)
                    exp_num_latex = f"{sy.latex(sy.Pow(base, index_numerator))}"
            elif (index_denominator1 != 1) and (index_denominator2 == 1):
                type_checker = random()
                if type_checker < 0.33:
                    # a ^ {n/m}
                    exp_num_latex = f"{base_latex}^{{{index_latex}}}"
                elif (0.33 <= type_checker) and (type_checker < 0.66):
                    # m√a^n
                    exp_num_latex = f"\\sqrt[{index_denominator1_latex}]{{{base_latex}^{{{index_numerator_latex}}}}}"
                else:
                    # m√(a^n)
                    exp_num_latex = f"\\sqrt[{index_denominator1_latex}]{{{sy.latex(sy.Pow(base, index_numerator))}}}"
            elif (index_denominator1 == 1) and (index_denominator2 != 1):
                type_checker = random()
                if type_checker < 0.33:
                    # a ^ {n/m}
                    exp_num_latex = f"{base_latex}^{{{index_latex}}}"
                elif (0.33 <= type_checker) and (type_checker < 0.66):
                    # m√a^n
                    exp_num_latex = f"\\sqrt[{index_denominator2_latex}]{{{base_latex}^{{{index_numerator_latex}}}}}"
                else:
                    # m√(a^n)
                    exp_num_latex = f"\\sqrt[{index_denominator2_latex}]{{{sy.latex(sy.Pow(base, index_numerator))}}}"
            else:
                type_checker = random()
                if type_checker < 0.33:
                    # a ^ {n/(d1*d2)}
                    exp_num_latex = f"{base_latex}^{{{index_latex}}}"
                elif (0.33 <= type_checker) and (type_checker < 0.66):
                    # \\sqrt[d1*d2]{a^n}
                    exp_num_latex = f"\\sqrt[{sy.latex(index_denominator1 * index_denominator2)}]{{{sy.latex(sy.Pow(base, index_numerator))}}}"
                else:
                    # \\sqrt[d1]{\\sqrt[d2]}{a^n}
                    exp_num_latex = f"\\sqrt[{index_denominator1}]{{\\sqrt[{index_denominator2}]{{{sy.latex(sy.Pow(base, index_numerator))}}}}}"
            return exp_num, exp_num_latex
        
        selected_base_type = choice(self._base_type_list)
        
        if selected_base_type == "character":
            base = sy.Symbol("a", real=True)
            index_list = []
            for _ in range(4):
                index_numerator = self._random_index_without_zero_and_one(min_num=-8, max_num=8)
                index_denominator1 = self._random_index_without_zero_and_one(min_num=2, max_num=6)
                # index_denominator2 = self._random_index_without_zero_and_one(min_num=2, max_num=6)
                index_denominator2 = 1
                index = (index_numerator, index_denominator1, index_denominator2)
                index_list.append(index)
            
            first_index_numerator, first_denominator1, first_denominator2 = index_list.pop()
            first_num, first_latex = exp(base, index_numerator=first_index_numerator, index_denominator1=first_denominator1, index_denominator2=first_denominator2)
            answer = first_num
            latex_problem = first_latex
            for index_numerator, index_denominator1, index_denominator2 in index_list:
                num, num_latex = exp(base, index_numerator=index_numerator, index_denominator1=index_denominator1, index_denominator2=index_denominator2)
                if random() > 0.5:
                    answer *= num
                    latex_problem += f"\\times {num_latex}"
                else:
                    answer /= num
                    latex_problem += f"\\div {num_latex}"
            
            latex_answer = f"= {sy.latex(answer)}"

            return latex_answer, latex_problem

        elif selected_base_type == "number":
            base = choice([2, 3, 5, 7])
            final_index = self._random_index_without_zero_and_one(min_num=-(8 - base), max_num=8 - base)
            final_index = sy.Rational(final_index, 1)
            index1_numerator = self._random_index_without_zero_and_one(min_num=-3, max_num=3)
            if random() > 0.7:
                index1_denominator1 = self._random_index_without_zero_and_one(min_num=2, max_num=3)
                index1_denominator2 = self._random_index_without_zero_and_one(min_num=2, max_num=3)
            else:
                index1_denominator1 = 1
                index1_denominator2 = 1
            index1 = (index1_numerator, index1_denominator1, index1_denominator2)
            
            index2_numerator = self._random_index_without_zero_and_one(min_num=-3, max_num=3)
            if random() > 0.7:
                index2_denominator1 = self._random_index_without_zero_and_one(min_num=2, max_num=3)
                index2_denominator2 = self._random_index_without_zero_and_one(min_num=2, max_num=3)
            else:
                index2_denominator1 = 1
                index2_denominator2 = 1
            index2 = (index2_numerator, index2_denominator1, index2_denominator2)
            
            coordinate_index = final_index - (sy.Rational(index1_numerator, index1_denominator1 * index1_denominator2) + sy.Rational(index2_numerator, index2_denominator1 * index2_denominator2))
            index_denominator1 = 1
            index_denominator2 = 1
            index3 = (coordinate_index, index_denominator1, index_denominator2)
            index_list = [index1, index2, index3]
            shuffle(index_list)
            
            first_index_numerator, first_index_denominator1, first_index_denominator2 = index_list.pop()
            first_num, first_latex = exp(base, index_numerator=first_index_numerator, index_denominator1=first_index_denominator1, index_denominator2=first_index_denominator2)
            answer = first_num
            latex_problem = first_latex
            
            for index_numerator, index_denominator1, index_denominator2 in index_list:
                if random() > 0.5:  # add as times
                    num, num_latex = exp(base, index_numerator=index_numerator, index_denominator1=index_denominator1, index_denominator2=index_denominator2)
                    answer *= num
                    latex_problem += f" \\times {num_latex}"
                else:  # add as division
                    num, num_latex = exp(base, index_numerator=-index_numerator, index_denominator1=index_denominator1, index_denominator2=index_denominator2)
                    answer /= num
                    latex_problem += f"\\div {num_latex}"
                
            latex_answer = f"= {sy.latex(answer)}"
            return latex_answer, latex_problem
    
    def _random_index_without_zero_and_one(self, min_num=-5, max_num=5):
        index = randint(min_num, max_num)
        if index == 0:
            if random() > 0.5:
                index = 2
            else:
                index = -2
        elif index == -1:
            index -= 1
        elif index == 1:
            index += 1
        return index
"""
developing from 4/25
--------------------
4/25
    each character appears in equation at once?
"""

from random import choice, randint, random, sample, shuffle

import sympy as sy


class TransformationOfEquationProblem:
    
    def __init__(self, **settings):
        sy.init_printing(order='grevlex')
        self._calculate_types_list = settings["calculate_types"]
        self._character = {}
        character_candidate = [("a", "b", "c"), ("x", "y", "z"), ("l", "m", "n")]
        selected_character_candidate = choice(character_candidate)
        for index, letter in enumerate(selected_character_candidate):
            character = sy.Symbol(letter, real=True)
            self._character[f"character{index}"] = character
        self.latex_answer, self.latex_problem = self._make_problem()
    
    def _make_problem(self):
        selected_calculate_type = choice(self._calculate_types_list)
        if selected_calculate_type == "addition_and_subtraction":
            latex_answer, latex_problem = self._make_addition_or_subtraction_problem()
        elif selected_calculate_type == "multiplication_and_division":
            latex_answer, latex_problem = self._make_multiplication_and_division_problem()
        elif selected_calculate_type == "mixed":
            latex_answer, latex_problem = self._make_mixed_problem()

        return latex_answer, latex_problem
    
    def _make_addition_or_subtraction_problem(self):
        c0 = self._character["character0"]
        c1 = self._character["character1"]
        c2 = self._character["character2"]
        add_object_to_equation = [c0, c1, c2]
        # need select character to answer at first?
        character_to_answer_index = randint(0, len(add_object_to_equation)-1)
        character_to_answer = add_object_to_equation.pop(character_to_answer_index)
        if random() > 0.4:
            add_object_to_equation.append(self._make_random_number())
        shuffle(add_object_to_equation)
        
        left = 0
        right = 0
        for object in add_object_to_equation:
            if random() > 0.5:
                left += object
            else:
                right += object
        
        # add character_to_answer later!
        if left == 0:
            right += character_to_answer
        elif right == 0:
            left += character_to_answer
        else:
            if random() > 0.5:
                left += character_to_answer
            else:
                right += character_to_answer
        
        answer = sy.solve(left-right, character_to_answer)[0]
        latex_answer = f"{sy.latex(character_to_answer)} = {sy.latex(answer)}"
        latex_problem = f"{sy.latex(left)} = {sy.latex(right)} \\quad [{sy.latex(character_to_answer)}]"
        
        return latex_answer, latex_problem
    
    def _make_multiplication_and_division_problem(self):
        c0 = self._character["character0"]
        c1 = self._character["character1"]
        c2 = self._character["character2"]
        add_object_to_equation = [c0, c1, c2]
        # need select character to answer at first?
        character_to_answer_index = randint(0, len(add_object_to_equation)-1)
        character_to_answer = add_object_to_equation.pop(character_to_answer_index)
        if random() > 0.4:
            add_object_to_equation.append(self._make_random_number())
        shuffle(add_object_to_equation)
        
        left = 1
        right = 1
        
        for object in add_object_to_equation:
            if random() > 0.5:
                left *= object
            else:
                right *= object
        
        # add character_to_answer later!
        if left == 1:
            right *= character_to_answer
        elif right == 1:
            left *= character_to_answer
        else:
            if random() > 0.5:
                left *= character_to_answer
            else:
                right *= character_to_answer

        answer = sy.solve(left-right, character_to_answer)[0]
        latex_answer = f"{sy.latex(character_to_answer)} = {sy.latex(answer)}"
        latex_problem = f"{sy.latex(left)} = {sy.latex(right)} \\quad [{sy.latex(character_to_answer)}]"
        
        return latex_answer, latex_problem
    
    def _make_mixed_problem(self):
        """
        now making
        
        can't use operator -
        -> change set and subtract?
        may need information about character not used.
        """
        c0 = self._character["character0"]
        c1 = self._character["character1"]
        c2 = self._character["character2"]
        characters= [c0, c1, c2]
        shuffled_characters_for_left = sample(characters, 3)
        shuffled_characters_for_right = sample(characters, 3)
        # left and right is composed of fraction
        
        left_denominator = randint(2, 6)
        left_numerator = 0
        # add -> multiplication
        # add
        left_numerator += (self._make_random_number() * shuffled_characters_for_left.pop())
        if random() > 0.5:
            left_numerator += (self._make_random_number() * shuffled_characters_for_left.pop())
        else:
            left_numerator += self._make_random_number()
        # multiplication
        if random() > 0.5:
            if random() > 0.5:
                left_numerator *= (self._make_random_number() * shuffled_characters_for_left.pop())
            else:
                left_numerator *= self._make_random_number()
        
        right_denominator = randint(2, 6)
        right_numerator = 0
        right_numerator += (self._make_random_number() * shuffled_characters_for_right.pop())
        if random() > 0.5:
            right_numerator += (self._make_random_number() * shuffled_characters_for_right.pop())
        else:
            right_numerator += self._make_random_number()
        if random() > 0.5:
            if random() > 0.5:
                right_numerator *= (self._make_random_number() * shuffled_characters_for_right.pop())
            else:
                right_numerator += self._make_random_number()
        
        left = left_numerator / left_denominator
        # print(f"left: {left}")
        right = right_numerator / right_denominator
        # print(f"right: {right}")    
        # the phase of selecting character for answer.
        remained_characters_set = set(shuffled_characters_for_left) & set(shuffled_characters_for_right)
        # print(f"remained_characters_set: {remained_characters_set}, type:{type(remained_characters_set)}")
        characters_set = set(characters)
        # print(f"characters_set: {characters_set}")
        characters_for_answer = set(characters) - remained_characters_set
        # print(f"characters_for_answer: {characters_for_answer}")
        character_for_answer = choice(list(characters_for_answer))
        # print(f"character_for_answer: {character_for_answer}")
        latex_problem = f"{sy.latex(left)} = {sy.latex(right)} \\quad [{sy.latex(character_for_answer)}]" 
        answer = sy.solve(left-right, character_for_answer)[0]
        # print(f"answer: {answer}")
        ## expanded_answer = sy.expand(answer)
        # print(f"expanded_answer: {expanded_answer}")
        simplified_answer = sy.simplify(answer)
        latex_answer = f"{sy.latex(character_for_answer)} = {sy.latex(simplified_answer)}"
        print("---------------------------------")
        
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

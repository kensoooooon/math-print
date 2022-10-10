from random import choice, randint, random

import sympy as sy

class FillInTheSquareProblem:
    """穴埋め算の問題を出力する
    
    Attributes:
        _calculation_type_list (list): 選択される演算の候補が格納されている
        latex_answer (str): latex形式で記述された解答
        latex_problem (str): latex形式で記述された問題
    """
    def __init__(self, **settings):
        """初期化
        
        Args:
            settings (dict): 問題の設定が格納されている
        """
        sy.init_printing(order='grevlex')
        self._calculation_type_list = settings["calculation_type_list"]
        self._used_symbol = settings["used_symbol"]
        self._used_number_list = settings["used_number_list"]
        self.latex_answer, self.latex_problem = self._make_problem()
    
    def _make_problem(self):
        """候補となる演算からランダムに選択を行い、それに応じた問題と解答を出力する
        
        Returns:
            latex_answer (str): latex形式で記述された解答
            latex_problem (str): latex形式で記述された問題
        Raises:
            ValueError: 選択された問題形式が正しくないときに挙上される
        """
        selected_calculation_type = choice(self._calculation_type_list)
        if selected_calculation_type == "addition_only":
            latex_answer, latex_problem = self._make_addition_only_problem()
        elif selected_calculation_type == "subtraction_only":
            latex_answer, latex_problem = self._make_subtraction_only_problem()
        elif selected_calculation_type == "multiplication_only":
            latex_answer, latex_problem = self._make_multiplication_only_problem()
        elif selected_calculation_type == "division_only":
            latex_answer, latex_problem = self._make_division_only_problem()
        elif selected_calculation_type == "addition_and_subtraction":
            latex_answer, latex_problem = self._make_addition_and_subtraction_problem()
        elif selected_calculation_type == "multiplication_and_division":
            latex_answer, latex_problem = self._make_multiplication_and_division_problem()
        elif selected_calculation_type == "all_calculations":
            latex_answer, latex_problem = self._make_all_calculations_problem()
        else:
            raise ValueError(f"selected_calculation_type is {selected_calculation_type}. This may be wrong type.")
        if self._used_symbol == "x":
            latex_answer = latex_answer.replace("\\square", "x")
            latex_problem = latex_problem.replace("\\square", "x")
        return latex_answer, latex_problem
    
    def _make_addition_only_problem(self):
        """足し算のみが用いられた穴埋め算の問題を出力

        Returns:
            latex_answer (str): latex形式で記述された解答
            latex_problem (str): latex形式で記述された問題
        
        Note:
            □+a=c, a+□=cの2タイプ
            a,c,xともに正である。
        """
        square_value, square_value_latex = self._make_random_number()
        latex_answer = f"\\square = {square_value_latex}"
        a, a_latex = self._make_random_number()
        c = square_value + a
        c_latex = self._float_display_checker(c)
        if random() > 0.5:  # □+a=c
            latex_problem = f"\\square + {a_latex} = {c_latex}"
        else:  # a+□=c
            latex_problem = f"{a_latex} + \\square = {c_latex}"
        return latex_answer, latex_problem

    def _make_subtraction_only_problem(self):
        """引き算のみが用いられた穴埋め算の問題を出力

        Returns:
            latex_answer (str): latex形式で記述された解答
            latex_problem (str): latex形式で記述された問題
        
        Notes:
            □-a=c, a-□=cの2タイプ
            小さいほうから値を決定して、負の値が出ないようにしている
            どちらでも正しく答えが出る場合は、random経由で決定
        """
        if random() > 0.5:  # □-a=c
            if random() > 0.5:  # a>c(□>a>c>0)
                c, c_latex = self._make_random_number()
                delta_for_a, _ = self._make_random_number(max_num=5)
                a = c + delta_for_a
                a_latex = self._float_display_checker(a)
            else:  # c>a(□>c>a>0)
                a, a_latex = self._make_random_number()
                delta_for_c, _ = self._make_random_number(max_num=5)
                c = a + delta_for_c
                c_latex = self._float_display_checker(c)
            square_value = a + c
            square_value_latex = self._float_display_checker(square_value)
            latex_problem = f"\\square - {a_latex} = {c_latex}"
        else:  # a-□=c
            if random() > 0.5:  # □>c(a>□>c>0)
                c, c_latex = self._make_random_number(max_num=5)
                delta_for_square_value, _ = self._make_random_number(max_num=5)
                square_value = c + delta_for_square_value
                square_value_latex = self._float_display_checker(square_value)
            else:  # c>□(a>c>□>0)
                square_value, square_value_latex = self._make_random_number(max_num=5)
                delta_for_c, _ = self._make_random_number(max_num=5)
                c = square_value + delta_for_c
                c_latex = self._float_display_checker(c)
            a = square_value + c
            a_latex = self._float_display_checker(a)
            latex_problem = f"{a_latex} - \\square = {c_latex}"
        latex_answer = f"\\square = {square_value_latex}"
        return latex_answer, latex_problem

    def _make_multiplication_only_problem(self):
        """かけ算のみが用いられた穴埋め算の問題を出力

        Returns:
            latex_answer (str): latex形式で記述された解答
            latex_problem (str): latex形式で記述された問題
        
        Notes:
            □×a=c, a×□=cの2タイプ
        """
        if random() > 0.5:  # □×a=c
            square_value, square_value_latex = self._make_random_number(min_num=2)
            a, a_latex = self._make_random_number(min_num=2)
            c = square_value * a
            c_latex = self._float_display_checker(c)
            latex_problem = f"\\square \\times {a_latex} = {c_latex}"
        else:  # a×□=c
            a, a_latex = self._make_random_number(min_num=2)
            square_value, square_value_latex = self._make_random_number(min_num=2)
            c = a * square_value
            c_latex = self._float_display_checker(c)
            latex_problem = f"{a_latex} \\times \\square = {c_latex}"
        latex_answer = f"\\square = {square_value_latex}"
        return latex_answer, latex_problem

    def _make_division_only_problem(self):
        """割り算のみが用いられた穴埋め算の問題を出力

        Returns:
            latex_answer (str): latex形式で記述された解答
            latex_problem (str): latex形式で記述された問題
        
        Notes:
            □÷a=c, a÷□=cの2タイプ
        """
        if random() > 0.5:  # □÷a=c
            a, a_latex = self._make_random_number(min_num=2)
            c, c_latex = self._make_random_number(min_num=2)
            square_value = c * a
            square_value_latex = self._float_display_checker(square_value)
            latex_problem = f"\\square \\div {a_latex} = {c_latex}"
        else:  # a÷□=c
            square_value, square_value_latex = self._make_random_number(min_num=2)
            c, c_latex = self._make_random_number(min_num=2)
            a = c * square_value
            a_latex = self._float_display_checker(a)
            latex_problem = f"{a_latex} \\div \\square = {c_latex}"
        latex_answer = f"\\square = {square_value_latex}"
        return latex_answer, latex_problem

    def _make_addition_and_subtraction_problem(self):
        """足し算と引き算が用いられた穴埋め算の問題を出力

        Returns:
            latex_answer (str): latex形式で記述された解答
            latex_problem (str): latex形式で記述された問題
        
        Notes:
            □+a-b=c, a+□-b=c 
            □-a+b=c, b-a+□=c
        """
        square_value, square_value_latex = self._make_random_number()
        if random() < 0.5:  # □+a-b=c or a+□-b=c, □+a>b
            b, b_latex = self._make_random_number()
            if random() > 0.5:  # b->square(random a)
                delta_for_square, _ = self._make_random_number()
                square_value = b + delta_for_square
                square_value_latex = self._float_display_checker(square_value)
                a, a_latex = self._make_random_number()
            else:  # b->a(random square)
                delta_for_a, _ = self._make_random_number()
                a = b + delta_for_a
                a_latex = self._float_display_checker(a)
                square_value, _ = self._make_random_number()
                square_value_latex = self._float_display_checker(square_value)
            c = square_value + a - b
            c_latex = self._float_display_checker(c)
            if random() > 0.5:  # □+a-b=c
                latex_problem = f"\\square + {a_latex} - {b_latex} = {c_latex}"
            else:  # a+□-b=c
                latex_problem = f"{a_latex} + \\square - {b_latex} = {c_latex}"
        else:  # □-a+b=c and b-a+□=c, □+b>a
            if random() > 0.5:  # a->square(random b)
                a, a_latex = self._make_random_number()
                delta_for_square, _ = self._make_random_number()
                square_value = a + delta_for_square
                square_value_latex = self._float_display_checker(square_value)
                b, b_latex = self._make_random_number()
            else:  # a->b(random square)
                a, a_latex = self._make_random_number()
                delta_for_b, _ = self._make_random_number()
                b = a + delta_for_b
                b_latex = self._float_display_checker(b)
                square_value, _ = self._make_random_number()
                square_value_latex = self._float_display_checker(square_value)
            c = square_value - a + b
            c_latex = self._float_display_checker(c)
            if random() > 0.5:  # □-a+b=c
                latex_problem = f"\\square - {a_latex} + {b_latex} = {c_latex}"
            else:  # b-a+□=c
                latex_problem = f"{b_latex} - {a_latex} + \\square = {c_latex}"
        latex_answer = f"\\square = {square_value_latex}"
        return latex_answer, latex_problem

    def _make_multiplication_and_division_problem(self):
        """かけ算と割り算が用いられた穴埋め算の問題を出力

        Returns:
            latex_answer (str): latex形式で記述された解答
            latex_problem (str): latex形式で記述された問題
        
        Notes:
            それぞれ分数にならないように設計
        
        Developing:
            何が支配的?
        """
        problem_type_checker = random()
        if problem_type_checker < 0.25:  # □×a×b=c, a×□×b=c, a×b×□=c
            square_value, _ = self._make_random_number(min_num=2)
            square_value_latex = self._float_display_checker(square_value)
            a, a_latex = self._make_random_number(min_num=2)
            b, b_latex = self._make_random_number(min_num=2)
            c = a * b * square_value
            c_latex = sy.latex(c)
            display_type_checker = random()
            if display_type_checker < 0.33:  # □×a×b=c
                latex_problem = f"\\square \\times {a_latex} \\times {b_latex} = {c_latex}"
            elif 0.33 <= display_type_checker < 0.66:  # a×□×b=c
                latex_problem = f"{a_latex} \\times \\square \\times {b_latex} = {c_latex}"
            else:  # a×b×□=c
                latex_problem = f"{a_latex} \\times {b_latex} \\times \\square = {c_latex}"
        elif 0.25 <= problem_type_checker < 0.5:  # □×a÷b=c, a×□÷b=c, a÷b×□=c
            b, b_latex = self._make_random_number(max_num=10, min_num=2)
            c, c_latex = self._make_random_number(max_num=10, min_num=2)
            if self._used_number_list == ["integer"]:
                a = 1
                for base, index in sy.factorint(b * c).items():
                    if random() > 0.3:
                        a *= (base ** randint(1, index))
                a_latex = self._float_display_checker(a)
            else:
                a, a_latex = self._make_random_number()
            square_value = sy.Rational(b * c, a)
            square_value_latex = self._float_display_checker(square_value)
            display_type_checker = random()
            if display_type_checker < 0.33:  # □×a÷b=c
                latex_problem = f"\\square \\times {a_latex} \\div {b_latex} = {c_latex}"
            elif 0.33 <= display_type_checker < 0.66:  # a×□÷b=c
                latex_problem = f"{a_latex} \\times \\square \\div {b_latex} = {c_latex}"
            else:  # a÷b×□=c
                latex_problem = f"{a_latex} \\div {b_latex} \\times \\square = {c_latex}"
        elif 0.5 <= problem_type_checker < 0.75:  # □÷a×b=c, b×□÷a=c, b÷a×□=c
            a, a_latex = self._make_random_number(max_num=10, min_num=2)
            c, c_latex = self._make_random_number(max_num=10, min_num=2)
            if self._used_number_list == ["integer"]:
                b = 1
                for base, index in sy.factorint(a * c).items():
                    if random() > 0.3:
                        b *= (base ** randint(1, index))
                b_latex = self._float_display_checker(b)
            else:
                b, b_latex = self._make_random_number()
            square_value = sy.Rational(a * c, b)
            square_value_latex = self._float_display_checker(square_value)
            display_type_checker = random()
            if display_type_checker < 0.33:  # □÷a×b=c
                latex_problem = f"\\square \\div {a_latex} \\times {b_latex} = {c_latex}"
            elif 0.33 <= display_type_checker < 0.66:  # b×□÷a=c
                latex_problem = f"{b_latex} \\times \\square \\div {a_latex} = {c_latex}"
            else:  # b÷a×□=c
                latex_problem = f"{b_latex} \\div {a_latex} \\times \\square = {c_latex}"
        else:  # □÷a÷b=c
            a, a_latex = self._make_random_number(max_num=10, min_num=2)
            b, b_latex = self._make_random_number(max_num=10, min_num=2)
            c, c_latex = self._make_random_number(max_num=10, min_num=2)
            square_value = a * b * c
            square_value_latex = self._float_display_checker(square_value)
            # latex_answer = f"\\square = {square_value_latex}"
            latex_problem = f"\\square \\div {a_latex} \\div {b_latex} = {c_latex}"     
        latex_answer = f"\\square = {square_value_latex}"  
        return latex_answer, latex_problem
    
    def _make_all_calculations_problem(self):
        """四則演算全てが用いられた穴埋め算の問題を出力

        Returns:
            latex_answer (str): latex形式で記述された解答
            latex_problem (str): latex形式で記述された問題
        
        Developing:
            □×a+b=c, a×□+b=c, b+□×a=c, b+a×□=c
            □÷a+b=c, b+□÷a=c
            a÷□+b=c, b+a÷□=c
            □÷a-b=c
            a÷□-b=c
            (□+a)×b=c, (a+□)×b=c
            (□-a)×b=c
            (□-a)÷b=c
            (a-□)×b=c
            (a-□)÷b=c
            (a+b)×□=c, □×(a+b)=c
            (a+b)÷□=c
            □÷(a+b)=c
        """
        problem_type_checker = random()
        if problem_type_checker < sy.Rational(1, 13):  # □×a+b=c, a×□+b=c, b+□×a=c, b+a×□=c
            square_value, square_value_latex = self._make_random_number()
            # latex_answer = f"\\square = {square_value_latex}"
            a, a_latex = self._make_random_number()
            b, b_latex = self._make_random_number()
            c = square_value * a + b
            c_latex = self._float_display_checker(c)
            display_type_checker = random()
            if display_type_checker < 0.25:  # □×a+b=c
                latex_problem = f"\\square \\times {a_latex} + {b_latex} = {c_latex}"
            elif 0.25 <= display_type_checker < 0.5:  # a×□+b=c
                latex_problem = f"{a_latex} \\times \\square + {b_latex} = {c_latex}"
            elif 0.5 <= display_type_checker < 0.75:  # b+□×a=c
                latex_problem = f"{b_latex} + \\square \\times {a_latex} = {c_latex}"
            else:
                latex_problem = f"{b_latex} + {a_latex} \\times \\square = {c_latex}"
        elif sy.Rational(1, 13) <= problem_type_checker < sy.Rational(2, 13):  # □÷a+b=c, b+□÷a=c
            b, b_latex = self._make_random_number()
            delta_for_c, _ = self._make_random_number()
            c = b + delta_for_c
            c_latex = self._float_display_checker(c)
            a, a_latex = self._make_random_number()
            square_value = a * (c - b)
            square_value_latex = self._float_display_checker(square_value)
            if random() > 0.5:  # □÷a+b=c
                latex_problem = f"\\square \\div {a_latex} + {b_latex} = {c_latex}"
            else:  # b+□÷a=c  
                latex_problem = f"{b_latex} + \\square \\div {a_latex} = {c_latex}"
        elif sy.Rational(2, 13) <= problem_type_checker < sy.Rational(3, 13):  # a÷□+b=c, b+a÷□=c
            b, b_latex = self._make_random_number()
            delta_for_c, _ = self._make_random_number()
            c = b + delta_for_c
            c_latex = self._float_display_checker(c)
            square_value, square_value_latex = self._make_random_number()
            a = square_value * (c - b)
            a_latex = self._float_display_checker(a)
            if random() > 0.5:  # a÷□+b=c
                latex_problem = f"{a_latex} \\div \\square + {b_latex} = {c_latex}"
            else:  # b+a÷□=c
                latex_problem = f"{b_latex} + {a_latex} \\div \\square = {c_latex}"
        elif sy.Rational(3, 13) <= problem_type_checker < sy.Rational(4, 13):  # □÷a-b=c
            b, b_latex = self._make_random_number()
            c, c_latex = self._make_random_number()
            a, a_latex = self._make_random_number()
            square_value = a * (b + c)
            square_value_latex = self._float_display_checker(square_value)
            latex_problem = f"\\square \\div {a_latex} - {b_latex} = {c_latex}"
        elif sy.Rational(4, 13) <= problem_type_checker < sy.Rational(5, 13):  # a÷□-b=c
            b, b_latex = self._make_random_number()
            c, c_latex = self._make_random_number()
            square_value, square_value_latex = self._make_random_number()
            a = square_value * (b + c)
            a_latex = self._float_display_checker(a)
            latex_problem = f"{a_latex} \\div \\square - {b_latex} = {c_latex}"
        elif sy.Rational(5, 13) <= problem_type_checker < sy.Rational(6, 13):  # (□+a)×b=c, (a+□)×b=c
            square_value, square_value_latex = self._make_random_number()
            a, a_latex = self._make_random_number()
            b, b_latex = self._make_random_number()
            c = (square_value + a) * b
            c_latex = self._float_display_checker(c)
            if random() > 0.5:  # (□+a)×b=c
                latex_problem = f"(\\square + {a_latex}) \\times {b_latex} = {c_latex}"
            else:  # (a+□)×b=c
                latex_problem = f"({a_latex} + \\square) \\times {b_latex} = {c_latex}"
        elif sy.Rational(6, 13) <= problem_type_checker < sy.Rational(7, 13):  # (□-a)×b=c
            a, a_latex = self._make_random_number()
            delta_for_square_value, _ = self._make_random_number()
            square_value = a + delta_for_square_value
            square_value_latex = self._float_display_checker(square_value)
            b, b_latex = self._make_random_number()
            c = (square_value - a) * b
            c_latex = self._float_display_checker(c)
            latex_problem = f"(\\square - {a_latex}) \\times {b_latex} = {c_latex}"
        elif sy.Rational(7, 13) <= problem_type_checker < sy.Rational(8, 13):  # (□-a)÷b=c
            a, a_latex = self._make_random_number()
            square_value = a + randint(1, 10)
            square_value_latex = self._float_display_checker(square_value)
            # latex_answer = f"\\square = {square_value_latex}"
            if self._used_number_list == ["integer"]:
                b = 1
                for base, index in sy.factorint(square_value - a).items():
                    if random() > 0.3:
                        b *= (base ** randint(1, index))
                b_latex = self._float_display_checker(b)
            else:
                b, b_latex = self._make_random_number()
            c = sy.Rational(square_value - a, b)
            c_latex = self._float_display_checker(c)
            latex_problem = f"(\\square - {a_latex}) \\div {b_latex} = {c_latex}"
        elif sy.Rational(8, 13) <= problem_type_checker < sy.Rational(9, 13):  # (a-□)×b=c
            square_value, square_value_latex = self._make_random_number()
            delta_for_a, _ = self._make_random_number()
            a = square_value + delta_for_a
            a_latex = self._float_display_checker(a)
            b, b_latex = self._make_random_number()
            c = (a - square_value) * b
            c_latex = self._float_display_checker(c)
            latex_problem = f"({a_latex} - \\square) \\times {b_latex} = {c_latex}"
        elif sy.Rational(9, 13) <= problem_type_checker < sy.Rational(10, 13):  # (a-□)÷b=c
            square_value, square_value_latex = self._make_random_number()
            delta_for_a, _ = self._make_random_number()
            a = square_value + delta_for_a
            a_latex = self._float_display_checker(a)
            if self._used_number_list == ["integer"]:
                b = 1
                for base, index in sy.factorint(a - square_value).items():
                    if random() > 0.3:
                        b *= (base ** randint(1, index))
                b_latex = sy.latex(b)
            else:
                b, b_latex = self._make_random_number()
            c = sy.Rational(a - square_value, b)
            c_latex = self._float_display_checker(c)
            latex_problem = f"({a_latex} - \\square) \\div {b_latex} = {c_latex}"
        elif sy.Rational(10, 13) <= problem_type_checker < sy.Rational(11, 13):  # (a+b)×□=c, □×(a+b)=c
            a, a_latex = self._make_random_number()
            b, b_latex = self._make_random_number()
            square_value, square_value_latex = self._make_random_number()
            c = (a + b) * square_value
            c_latex = self._float_display_checker(c)
            if random() > 0.5:  # (a+b)×□=c
                latex_problem = f"({a_latex} + {b_latex}) \\times \\square = {c_latex}"
            else:  # □×(a+b)=c
                latex_problem = f"\\square \\times ({a_latex} + {b_latex}) = {c_latex}"
        elif sy.Rational(11, 13) <= problem_type_checker < sy.Rational(12, 13):  # (a+b)÷□=c
            a, a_latex = self._make_random_number()
            b, b_latex = self._make_random_number()
            if self._used_number_list == ["integer"]:
                square_value = 1
                for base, index in sy.factorint(a + b).items():
                    if random() > 0.3:
                        square_value *= (base ** randint(1, index))
                square_value_latex =sy.latex(square_value)
            else:
                square_value, square_value_latex = self._make_random_number()
            c = sy.Rational(a + b, square_value)
            c_latex = self._float_display_checker(c)
            latex_problem = f"({a_latex} + {b_latex}) \\div \\square = {c_latex}"
        else:  # □÷(a+b)=c
            a, a_latex = self._make_random_number()
            b, b_latex = self._make_random_number()
            c, c_latex = self._make_random_number()
            square_value = (a + b) * c
            square_value_latex = self._float_display_checker(square_value)
            latex_problem = f"\\square \\div ({a_latex} + {b_latex}) = {c_latex}"
        latex_answer = f"\\square = {square_value_latex}"
        return latex_answer, latex_problem
    
    def _make_random_number(self, max_num=10, min_num=1, number_type=None):
        """選択された数の種類に応じて、ランダムな値を出力する

        Args:
            max_num (int, optional): 使用される数の最大値。デフォルトは10
            min_num (int, optional): 使用される数の最小値。デフォルトは1
            number_type (Union[str, NoneType], optional): 数の種類(integer, frac, decimal)
        
        Returns:
            number (Union[sy.Integer, sy.Rational, sy.Float]): 計算に用いられる数
            number_latex (str): 表示に用いられるlatex形式の数
        """
    
        def _make_random_integer(max_num, min_num):
            """ランダムな自然数とそのlatexを生成する

            Args:
                max_num (int): 生成される数の最大値
                min_num (int): 生成される数の最小値
            
            Returns:
                integer (sy.Integer): 計算に用いられる自然数
                integer_latex (str): 表示に用いられるlatex形式の自然数
            """
            integer = sy.Integer(randint(min_num, max_num))
            integer_latex = sy.latex(integer)
            return integer, integer_latex
        
        def _make_random_frac(max_num, min_num):
            """ランダムな分数とそのlatexを生成
            
            Args:
                max_num (int): 使用される数の最大値
                min_num (int): 使用される数の最小値
            
            Returns:
                frac (sy.Rational): 計算に用いられる分数
                frac_latex (str): 表示に用いられるlatex形式の分数
            """
            denominator = randint(2, max_num)
            numerator = randint(min_num, max_num)
            frac = sy.Rational(numerator, denominator)
            frac_latex = sy.latex(frac)
            return frac, frac_latex
        
        def _make_random_decimal(max_num, min_num):
            """ランダムな小数とそのlatexを生成

            Args:
                max_num (int): 使用される数の最大値
                min_num (int): 使用される数の最小値
            
            Returns:
                frac (sy.Rational): 計算に用いられる小数
                decimal_latex (str): 表示に用いられるlatex形式の小数
            
            Developing:
                計算はRationalで、表示はFloat
            """
            numerator = randint(min_num, max_num)
            denominator = 10
            if numerator % 10 == 0:
                numerator += randint(1, 9)
            frac = sy.Rational(numerator, denominator)
            decimal_latex = sy.latex(sy.Float(frac))
            return frac, decimal_latex
        
        if number_type is None:
            selected_number_type = choice(self._used_number_list)
        else:
            selected_number_type = number_type
        if selected_number_type == "integer":
            number, number_latex = _make_random_integer(max_num, min_num)
        elif selected_number_type == "frac":
            number, number_latex = _make_random_frac(max_num, min_num)
        elif selected_number_type == "decimal":
            number, number_latex = _make_random_decimal(max_num, min_num)
        else:
            raise ValueError(f"selected_number_type is {selected_number_type}. This may be wrong.")
        return number, number_latex
    
    def _float_display_checker(self, frac):
        """使用される数に分数が入っておらず、かつ整数でもないとき、かつ有限小数に小数表示に切り替える
        
        Args:
            frac (Union[sy.Integer, sy.Rational]): 変換対象の数
        
        Return:
            number_latex (str): チェックを経たlatex形式で表示された数
        """
        def _is_finite_decimal(rational_number):
            """有限小数か否かを判定

            Args:
                rational_number (sy.Rational): 判定したい分数

            Returns:
                (bool): 有限小数ならTrue, 無限小数ならFalse
            """
            denominator_list = list(sy.factorint(rational_number.denominator).keys())
            denominator_set = set(denominator_list)
            if denominator_set == set():
                return True
            elif denominator_set == {2}:
                return True
            elif denominator_set == {5}:
                return True
            elif denominator_set == {2, 5}:
                return True
            else:
                return False
        
        if ("frac" not in self._used_number_list) and (frac.denominator != 1) and (_is_finite_decimal(frac)):
            number_latex = sy.latex(sy.Float(frac))
        else:
            number_latex = sy.latex(frac)
        return number_latex
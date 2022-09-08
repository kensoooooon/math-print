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
        self.latex_answer, self.latex_problem = self._make_problem()
    
    def _make_problem(self):
        """選択された演算の形式に応じて、問題と解答を出力する
        
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
        return latex_answer, latex_problem
    
    def _make_addition_only_problem(self):
        """足し算のみが用いられた穴埋め算の問題を出力

        Returns:
            latex_answer (str): latex形式で記述された解答
            latex_problem (str): latex形式で記述された問題
        
        Note:
            解も係数も整数で統一。要望があれば分数の設定等も追加予定
        Developing:
            要するにx+a=c, a+x=c型の方程式と考え方は同じ
            a,c,xともに正である。
        """
        square_value, square_value_latex = self._make_random_integer()
        latex_answer = f"\\square = {square_value_latex}"
        a, a_latex = self._make_random_integer()
        c = square_value + a
        c_latex = sy.latex(c)
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
            小さいほうから値を決定している
            どちらでも正しく答えが出る場合は、random経由で決定
        """
        if random() > 0.5:  # □-a=c
            if random() > 0.5:  # a>c(□>a>c>0)
                c, c_latex = self._make_random_integer()
                a = c + sy.Integer(randint(1, 5))
                a_latex = sy.latex(a)
                square_value = a + c
                square_value_latex = sy.latex(square_value)
            else:  # c>a(□>c>a>0)
                a, a_latex = self._make_random_integer()
                c = a + sy.Integer(randint(1, 5))
                c_latex = sy.latex(c)
                square_value = a + c
                square_value_latex = sy.latex(square_value)
            latex_answer = f"\\square = {square_value_latex}"
            latex_problem = f"\\square - {a_latex} = {c_latex}"
        else:  # a-□=c
            if random() > 0.5:  # □>c(a>□>c>0)
                c, c_latex = self._make_random_integer()
                square_value = c + sy.Integer(randint(1, 5))
                square_value_latex = sy.latex(square_value)
                a = square_value + c
                a_latex = sy.latex(a)
            else:  # c>□(a>c>□>0)
                square_value, square_value_latex = self._make_random_integer()
                c = square_value + sy.Integer(randint(1, 5))
                c_latex = sy.latex(c)
                a = square_value + c
                a_latex = sy.latex(a)
            latex_answer = f"\\square = {square_value_latex}"
            latex_problem = f"{a_latex} - \\square = {c_latex}"
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
            square_value, square_value_latex = self._make_random_integer()
            latex_answer = f"\\square = {square_value_latex}"
            a, a_latex = self._make_random_integer()
            c = square_value * a
            c_latex = sy.latex(c)
            latex_problem = f"\\square \\times {a_latex} = {c_latex}"
        else:  # a×□=c
            a, a_latex = self._make_random_integer()
            square_value, square_value_latex = self._make_random_integer()
            latex_answer = f"\\square = {square_value_latex}"
            c = a * square_value
            c_latex = sy.latex(c)
            latex_problem = f"{a_latex} \\times \\square = {c_latex}"
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
            a, a_latex = self._make_random_integer()
            c, c_latex = self._make_random_integer()
            square_value = c * a
            square_value_latex = sy.latex(square_value)
            latex_answer = f"\\square = {square_value_latex}"
            latex_problem = f"\\square \\div {a_latex} = {c_latex}"
        else:  # a÷□=c
            square_value, square_value_latex = self._make_random_integer()
            latex_answer = f"\\square = {square_value_latex}"
            c, c_latex = self._make_random_integer()
            a = c * square_value
            a_latex = sy.latex(a)
            latex_problem = f"{a_latex} \\div \\square = {c_latex}"
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
        square_value, square_value_latex = self._make_random_integer()
        latex_answer = f"\\square = {square_value_latex}"
        if random() < 0.5:  # □+a-b=c or a+□-b=c, □+a>b
            a, a_latex = self._make_random_integer()
            b = sy.Integer(randint(1, square_value + a - 1))
            b_latex = sy.latex(b)
            c = square_value + a - b
            c_latex = sy.latex(c)
            if random() > 0.5:  # □+a-b=c
                latex_problem = f"\\square + {a_latex} - {b_latex} = {c_latex}"
            else:  # a+□-b=c
                latex_problem = f"{a_latex} + \\square - {b_latex} = {c_latex}"
        else:  # □-a+b=c and b-a+□=c, □+b>a
            b, b_latex = self._make_random_integer()
            a = sy.Integer(randint(1, square_value + b - 1))
            a_latex = sy.latex(a)
            c = square_value - a + b
            c_latex = sy.latex(c)
            if random() > 0.5:  # □-a+b=c
                latex_problem = f"\\square - {a_latex} + {b_latex} = {c_latex}"
            else:  # b-a+□=c
                latex_problem = f"{b_latex} - {a_latex} + \\square = {c_latex}"
        return latex_answer, latex_problem

    def _make_multiplication_and_division_problem(self):
        """かけ算と割り算が用いられた穴埋め算の問題を出力

        Returns:
            latex_answer (str): latex形式で記述された解答
            latex_problem (str): latex形式で記述された問題
        
        Notes:
            それぞれ分数にならないように設計
        """
        problem_type_checker = random()
        if problem_type_checker < 0.25:  # □×a×b=c, a×□×b=c, a×b×□=c
            square_value, square_value_latex = self._make_random_integer(max_num=10, min_num=2)
            latex_answer = f"\\square = {square_value_latex}"
            a, a_latex = self._make_random_integer(max_num=10, min_num=2)
            b, b_latex = self._make_random_integer(max_num=10, min_num=2)
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
            b, b_latex = self._make_random_integer(max_num=10, min_num=2)
            c, c_latex = self._make_random_integer(max_num=10, min_num=2)
            a = 1
            for base, index in sy.factorint(b * c).items():
                if random() > 0.3:
                    a *= (base ** randint(1, index))
            a_latex = sy.latex(a)
            square_value = sy.Rational(b * c, a)
            square_value_latex = sy.latex(square_value)
            latex_answer = f"\\square = {square_value_latex}"
            display_type_checker = random()
            if display_type_checker < 0.33:  # □×a÷b=c
                latex_problem = f"\\square \\times {a_latex} \\div {b_latex} = {c_latex}"
            elif 0.33 <= display_type_checker < 0.66:  # a×□÷b=c
                latex_problem = f"{a_latex} \\times \\square \\div {b_latex} = {c_latex}"
            else:  # a÷b×□=c
                latex_problem = f"{a_latex} \\div {b_latex} \\times \\square = {c_latex}"
        elif 0.5 <= problem_type_checker < 0.75:  # □÷a×b=c, b×□÷a=c, b÷a×□=c
            a, a_latex = self._make_random_integer(max_num=10, min_num=2)
            c, c_latex = self._make_random_integer(max_num=10, min_num=2)
            b = 1
            for base, index in sy.factorint(a * c).items():
                if random() > 0.3:
                    b *= (base ** randint(1, index))
            b_latex = sy.latex(b)
            square_value = sy.Rational(a * c, b)
            square_value_latex = sy.latex(square_value)
            latex_answer = f"\\square = {square_value_latex}"
            display_type_checker = random()
            if display_type_checker < 0.33:  # □÷a×b=c
                latex_problem = f"\\square \\div {a_latex} \\times {b_latex} = {c_latex}"
            elif 0.33 <= display_type_checker < 0.66:  # b×□÷a=c
                latex_problem = f"{b_latex} \\times \\square \\div {a_latex} = {c_latex}"
            else:  # b÷a×□=c
                latex_problem = f"{b_latex} \\div {a_latex} \\times \\square = {c_latex}"
        else:  # □÷a÷b=c
            a, a_latex = self._make_random_integer(max_num=10, min_num=2)
            b, b_latex = self._make_random_integer(max_num=10, min_num=2)
            c, c_latex = self._make_random_integer(max_num=10, min_num=2)
            square_value = a * b * c
            square_value_latex = sy.latex(square_value)
            latex_answer = f"\\square = {square_value_latex}"
            latex_problem = f"\\square \\div {a_latex} \\div {b_latex} = {c_latex}"            
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
            square_value, square_value_latex = self._make_random_integer()
            latex_answer = f"\\square = {square_value_latex}"
            a, a_latex = self._make_random_integer()
            b, b_latex = self._make_random_integer()
            c = square_value * a + b
            c_latex = sy.latex(c)
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
            b, b_latex = self._make_random_integer()
            c = b + randint(1, 10)
            c_latex = sy.latex(c)
            a, a_latex = self._make_random_integer()
            square_value = a * (c - b)
            square_value_latex = sy.latex(square_value)
            latex_answer = f"\\square = {square_value_latex}"
            if random() > 0.5:  # □÷a+b=c
                latex_problem = f"\\square \\div {a_latex} + {b_latex} = {c_latex}"
            else:  # b+□÷a=c  
                latex_problem = f"{b_latex} + \\square \\div {a_latex} = {c_latex}"
        elif sy.Rational(2, 13) <= problem_type_checker < sy.Rational(3, 13):  # a÷□+b=c, b+a÷□=c
            b, b_latex = self._make_random_integer()
            c = b + randint(1, 10)
            c_latex = sy.latex(c)
            square_value, square_value_latex = self._make_random_integer()
            latex_answer = f"\\square = {square_value_latex}"
            a = square_value * (c - b)
            a_latex = sy.latex(a)
            if random() > 0.5:  # a÷□+b=c
                latex_problem = f"{a_latex} \\div \\square + {b_latex} = {c_latex}"
            else:  # b+a÷□=c
                latex_problem = f"{b_latex} + {a_latex} \\div \\square = {c_latex}"
        elif sy.Rational(3, 13) <= problem_type_checker < sy.Rational(4, 13):  # □÷a-b=c
            b, b_latex = self._make_random_integer()
            c, c_latex = self._make_random_integer()
            a, a_latex = self._make_random_integer()
            square_value = a * (b + c)
            square_value_latex = sy.latex(square_value)
            latex_answer = f"\\square = {square_value_latex}"
            latex_problem = f"\\square \\div {a_latex} - {b_latex} = {c_latex}"
        elif sy.Rational(4, 13) <= problem_type_checker < sy.Rational(5, 13):  # a÷□-b=c
            b, b_latex = self._make_random_integer()
            c, c_latex = self._make_random_integer()
            square_value, square_value_latex = self._make_random_integer()
            latex_answer = f"\\square = {square_value_latex}"
            a = square_value * (b + c)
            a_latex = sy.latex(a)
            latex_problem = f"{a_latex} \\div \\square - {b_latex} = {c_latex}"
        elif sy.Rational(5, 13) <= problem_type_checker < sy.Rational(6, 13):  # (□+a)×b=c, (a+□)×b=c
            square_value, square_value_latex = self._make_random_integer()
            latex_answer = f"\\square = {square_value_latex}"
            a, a_latex = self._make_random_integer()
            b, b_latex = self._make_random_integer()
            c = (square_value + a) * b
            c_latex = sy.latex(c)
            if random() > 0.5:  # (□+a)×b=c
                latex_problem = f"(\\square + {a_latex}) \\times {b_latex} = {c_latex}"
            else:  # (a+□)×b=c
                latex_problem = f"({a_latex} + \\square) \\times {b_latex} = {c_latex}"
        elif sy.Rational(6, 13) <= problem_type_checker < sy.Rational(7, 13):  # (□-a)×b=c
            a, a_latex = self._make_random_integer()
            square_value = a + randint(1, 10)
            square_value_latex = sy.latex(square_value)
            latex_answer = f"\\square = {square_value_latex}"
            b, b_latex = self._make_random_integer()
            c = (square_value - a) * b
            c_latex = sy.latex(c)
            latex_problem = f"(\\square - {a_latex}) \\times {b_latex} = {c_latex}"
        elif sy.Rational(7, 13) <= problem_type_checker < sy.Rational(8, 13):  # (□-a)÷b=c
            a, a_latex = self._make_random_integer()
            square_value = a + randint(1, 10)
            square_value_latex = sy.latex(square_value)
            latex_answer = f"\\square = {square_value_latex}"
            b = 1
            for base, index in sy.factorint(square_value - a).items():
                if random() > 0.3:
                    b *= (base ** randint(1, index))
            b_latex = sy.latex(b)
            c = sy.Rational(square_value - a, b)
            c_latex = sy.latex(c)
            latex_problem = f"(\\square - {a_latex}) \\div {b_latex} = {c_latex}"
        elif sy.Rational(8, 13) <= problem_type_checker < sy.Rational(9, 13):  # (a-□)×b=c
            square_value, square_value_latex = self._make_random_integer()
            latex_answer = f"\\square = {square_value_latex}"
            a = square_value + randint(1, 10)
            a_latex = sy.latex(a)
            b, b_latex = self._make_random_integer()
            c = (a - square_value) * b
            c_latex = sy.latex(c)
            latex_problem = f"({a_latex} - \\square) \\times {b_latex} = {c_latex}"
        elif sy.Rational(9, 13) <= problem_type_checker < sy.Rational(10, 13):  # (a-□)÷b=c
            square_value, square_value_latex = self._make_random_integer()
            latex_answer = f"\\square = {square_value_latex}"
            a = square_value + randint(1, 10)
            a_latex = sy.latex(a)
            b = 1
            for base, index in sy.factorint(a - square_value).items():
                if random() > 0.3:
                    b *= (base ** randint(1, index))
            b_latex = sy.latex(b)
            c = sy.Rational(a - square_value, b)
            c_latex = sy.latex(c)
            latex_problem = f"({a_latex} - \\square) \\div {b_latex} = {c_latex}"
        elif sy.Rational(10, 13) <= problem_type_checker < sy.Rational(11, 13):  # (a+b)×□=c, □×(a+b)=c
            a, a_latex = self._make_random_integer()
            b, b_latex = self._make_random_integer()
            square_value, square_value_latex = self._make_random_integer()
            latex_answer = f"\\square = {square_value_latex}"
            c = (a + b) * square_value
            c_latex = sy.latex(c)
            if random() > 0.5:  # (a+b)×□=c
                latex_problem = f"({a_latex} + {b_latex}) \\times \\square = {c_latex}"
            else:  # □×(a+b)=c
                latex_problem = f"\\square \\times ({a_latex} + {b_latex}) = {c_latex}"
        elif sy.Rational(11, 13) <= problem_type_checker < sy.Rational(12, 13):  # (a+b)÷□=c
            a, a_latex = self._make_random_integer()
            b, b_latex = self._make_random_integer()
            square_value = 1
            for base, index in sy.factorint(a + b).items():
                if random() > 0.3:
                    square_value *= (base ** randint(1, index))
            square_value_latex =sy.latex(square_value)
            latex_answer = f"\\square = {square_value_latex}"
            c = sy.Rational(a + b, square_value)
            c_latex = sy.latex(c)
            latex_problem = f"({a_latex} + {b_latex}) \\div \\square = {c_latex}"
        else:  # □÷(a+b)=c
            a, a_latex = self._make_random_integer()
            b, b_latex = self._make_random_integer()
            c, c_latex = self._make_random_integer()
            square_value = (a + b) * c
            square_value_latex = sy.latex(square_value)
            latex_answer = f"\\square = {square_value_latex}"
            latex_problem = f"\\square \\div ({a_latex} + {b_latex}) = {c_latex}"
        return latex_answer, latex_problem
    
    def _make_random_integer(self, max_num=10, min_num=1):
        """ランダムな自然数とそのlatexを生成する

        Args:
            max_num (int, optional): 生成される数の最大値 Defaults to 10.
            min_num (int, optional): 生成される数の最小値 Defaults to 1.
        
        Returns:
            integer (sy.Integer): 計算に用いられる自然数
            integer_latex (str): 表示に用いられるlatex形式の自然数
        """
        integer = sy.Integer(randint(min_num, max_num))
        integer_latex = sy.latex(integer)
        
        return integer, integer_latex
        
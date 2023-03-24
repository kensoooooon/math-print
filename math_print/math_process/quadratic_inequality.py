from random import choice, randint, random


import sympy as sy


class QuadraticInequality:
    """2次不等式の問題と解答を出力
    
    Attributes:
        _used_quadratic_function (list): 登場する2次方程式のタイプを格納
        latex_answer (str): latex形式で記述された解答
        latex_problem (str): latex形式で記述された問題
    """
    def __init__(self, **settings):
        """初期設定
        
        Args:
            settings (dict): 問題の各種設定
        """
        sy.init_printing(order='grevlex')
        used_quadratic_equation = settings["used_quadratic_equation"]
        self._used_answer_in_quadratic_equation = settings["used_answer_in_quadratic_equation"]
        self.latex_answer, self.latex_problem = self._make_problem(used_quadratic_equation)
    
    def _make_problem(self, used_quadratic_functions):
        """問題と解答の出力を制御するコントローラ
        
        Args:
            used_quadratic_functions (list): 使用する2次関数の候補を格納
        
        Returns:
            latex_answer (str): latex形式で記述された解答
            latex_problem (str): latex形式で記述された問題
        """
        selected_quadratic_function = choice(used_quadratic_functions)
        if selected_quadratic_function == "two_different_answer":
            latex_answer, latex_problem = self._make_two_different_answer_problem()
        elif selected_quadratic_function == "same_answer":
            latex_answer, latex_problem = self._make_same_answer_problem()
        elif selected_quadratic_function == "no_answer":
            latex_answer, latex_problem = self._make_no_answer_problem()
        else:
            raise ValueError(f"'selected_quadratic_function' is {selected_quadratic_function}. This isn't expected.")
        return latex_answer, latex_problem
    
    def _make_two_different_answer_problem(self):
        """異なる2つの解を持つ2次方程式を使った2次不等式の問題を作成
        
        Returns:
            latex_answer (str): latex形式で記述された解答
            latex_problem (str): latex形式で記述された問題
        
        Developings:
            f(x) = k(x-a)(x-b) (a < b)
            -> (k > 0) and (f(x) > 0): x < a, b < x
            -> (k > 0) and (f(x) < 0): a < x < b
            -> (k < 0) and (f(x) > 0): a < x < b
            -> (k < 0) and (f(x) < 0): x < a, b < x
            
            plus equal type?
        """
        x = sy.Symbol("x", real=True)
        answer1 = self._make_random_number(min_num=1, max_num=3, integer_or_frac="integer")
        answer2 = answer1 + self._make_random_number(integer_or_frac="integer")
        if answer1 > answer2:
            bigger_answer = answer1
            smaller_answer = answer2
        elif answer1 < answer2:
            bigger_answer = answer2
            smaller_answer = answer1
        inequality_sign_checker = random()
        # (k > 0) and (f(x) > 0): x < a, b < x
        if inequality_sign_checker < 0.25:
            quadratic_coefficient = self._make_random_number(min_num=1, max_num=3, positive_or_negative="positive")
            quadratic_function = sy.expand(quadratic_coefficient * (x - smaller_answer) * (x - bigger_answer))
            # containing equal
            if random() > 0.5:
                latex_answer = f"\( x \\leqq {sy.latex(smaller_answer)}, {sy.latex(bigger_answer)} \\leqq x \)"
                latex_problem = f"\( {sy.latex(quadratic_function)} \\geqq 0 \)"
            # not containing equal
            else:
                latex_answer = f"\( x < {sy.latex(smaller_answer)}, {sy.latex(bigger_answer)} < x \)"
                latex_problem = f"\( {sy.latex(quadratic_function)} > 0 \)"
        # (k > 0) and (f(x) < 0): a < x < b
        elif 0.25 <= inequality_sign_checker < 0.5:
            quadratic_coefficient = self._make_random_number(min_num=1, max_num=3, positive_or_negative="positive")
            quadratic_function = sy.expand(quadratic_coefficient * (x - smaller_answer) * (x - bigger_answer))
            # containing equal
            if random() > 0.5:
                latex_answer = f"\( {sy.latex(smaller_answer)} \\leqq x \\leqq {sy.latex(bigger_answer)} \)"
                latex_problem = f"\( {sy.latex(quadratic_function)} \\leqq 0 \)"
            # not containing equal
            else:
                latex_answer = f"\( {sy.latex(smaller_answer)} < x < {sy.latex(bigger_answer)} \)"
                latex_problem = f"\( {sy.latex(quadratic_function)} < 0 \)"
        # (k < 0) and (f(x) > 0): a < x < b
        elif 0.5 <= inequality_sign_checker < 0.75:
            quadratic_coefficient = self._make_random_number(min_num=1, max_num=3, positive_or_negative="negative")
            quadratic_function = sy.expand(quadratic_coefficient * (x - smaller_answer) * (x - bigger_answer))
            # containing equal
            if random() > 0.5:
                latex_answer = f"\( {sy.latex(smaller_answer)} \\leqq x \\leqq {sy.latex(bigger_answer)} \)"
                latex_problem = f"\( {sy.latex(quadratic_function)} \\geqq 0 \)"
            # not containing equal
            else:
                latex_answer = f"\( {sy.latex(smaller_answer)} < x < {sy.latex(bigger_answer)} \)"
                latex_problem = f"\( {sy.latex(quadratic_function)} > 0 \)"
        #  (k < 0) and (f(x) < 0): x < a, b < x
        else:
            quadratic_coefficient = self._make_random_number(min_num=1, max_num=3, positive_or_negative="negative")
            quadratic_function = sy.expand(quadratic_coefficient * (x - smaller_answer) * (x - bigger_answer))
            if random() > 0.5:
                latex_answer = f"\( x \\leqq {sy.latex(smaller_answer)}, {sy.latex(bigger_answer)} \\leqq x \)"
                latex_problem = f"\( {sy.latex(quadratic_function)} \\leqq 0 \)"
            # not containing equal
            else:
                latex_answer = f"\( x < {sy.latex(smaller_answer)}, {sy.latex(bigger_answer)} < x \)"
                latex_problem = f"\( {sy.latex(quadratic_function)} < 0 \)"
        return latex_answer, latex_problem

    def _make_same_answer_problem(self):
        """重解を持つ2次方程式を使った2次不等式の問題を作成
        
        Returns:
            latex_answer (str): latex形式で記述された解答
            latex_problem (str): latex形式で記述された問題
        """
        x = sy.Symbol("x", real=True)
        answer = self._make_random_number(integer_or_frac="integer")
        inequality_sign_checker = random()
        # (k > 0) and (f(x) > 0)
        if inequality_sign_checker < 0.25:
            quadratic_coefficient = self._make_random_number(min_num=1, max_num=3, positive_or_negative="positive")
            quadratic_function = sy.expand(quadratic_coefficient * (x - answer) ** 2)
            # containing equal
            if random() > 0.5:
                latex_answer = f"\( x \)はすべての実数"
                latex_problem = f"\( {sy.latex(quadratic_function)} \\geqq 0 \)"
            # not containing equal
            else:
                latex_answer = f"\( x \)は\( {sy.latex(answer)} \)を除くすべての実数"
                latex_problem = f"\( {sy.latex(quadratic_function)} > 0 \)"
        # (k > 0) and (f(x) < 0)
        elif 0.25 <= inequality_sign_checker < 0.5:
            quadratic_coefficient = self._make_random_number(min_num=1, max_num=3, positive_or_negative="positive")
            quadratic_function = sy.expand(quadratic_coefficient * (x - answer) ** 2)
            # containing equal
            if random() > 0.5:
                latex_answer = f"\( x = {sy.latex(answer)} \)"
                latex_problem = f"\( {sy.latex(quadratic_function)} \\leqq 0 \)"
            # not containing equal
            else:
                latex_answer = f"不等式を満たす\( x \)は存在しない"
                latex_problem = f"\( {sy.latex(quadratic_function)} < 0 \)"
        # (k < 0) and (f(x) > 0)
        elif 0.5 <= inequality_sign_checker < 0.75:
            quadratic_coefficient = self._make_random_number(min_num=1, max_num=3, positive_or_negative="negative")
            quadratic_function = sy.expand(quadratic_coefficient * (x - answer) ** 2)
            # containing equal
            if random() > 0.5:
                latex_answer = f"\( x = {sy.latex(answer)} \)"
                latex_problem = f"\( {sy.latex(quadratic_function)} \\geqq 0 \)"
            # not containing equal
            else:
                latex_answer = f"不等式を満たす\( x \)は存在しない"
                latex_problem = f"\( {sy.latex(quadratic_function)} > 0 \)"
        #  (k < 0) and (f(x) < 0): x < a, b < x
        else:
            quadratic_coefficient = self._make_random_number(min_num=1, max_num=3, positive_or_negative="negative")
            quadratic_function = sy.expand(quadratic_coefficient * (x - answer) ** 2)
            if random() > 0.5:
                latex_answer = f"\( x \)はすべての実数"
                latex_problem = f"\( {sy.latex(quadratic_function)} \\leqq 0 \)"
            # not containing equal
            else:
                latex_answer = f"\( x \)は\( {sy.latex(answer)} \)を除くすべての実数"
                latex_problem = f"\( {sy.latex(quadratic_function)} < 0 \)"    
        return latex_answer, latex_problem

    def _make_no_answer_problem(self):
        """実数解を持たない2次方程式を使った2次不等式の問題を作成
        
        Returns:
            latex_answer (str): latex形式で記述された解答
            latex_problem (str): latex形式で記述された問題
        """
        x = sy.Symbol("x", real=True)
        x_axis = self._make_random_number(integer_or_frac="integer")
        inequality_sign_checker = random()
        # (k > 0) and (f(x) > 0): all real number
        if inequality_sign_checker < 0.25:
            quadratic_coefficient = self._make_random_number(min_num=1, max_num=3, positive_or_negative="positive")
            y_axis = self._make_random_number(positive_or_negative="positive", min_num=1, max_num=3)
            quadratic_function = sy.expand(quadratic_coefficient * (x - x_axis) ** 2 + y_axis)
            # containing equal
            if random() > 0.5:
                latex_answer = f"\( x \)はすべての実数"
                latex_problem = f"\( {sy.latex(quadratic_function)} \\geqq 0 \)"
            # not containing equal
            else:
                latex_answer = f"\( x \)はすべての実数"
                latex_problem = f"\( {sy.latex(quadratic_function)} > 0 \)"
        # (k > 0) and (f(x) < 0): x doesn't exist.
        elif 0.25 <= inequality_sign_checker < 0.5:
            quadratic_coefficient = self._make_random_number(min_num=1, max_num=3, positive_or_negative="positive")
            y_axis = self._make_random_number(positive_or_negative="positive", min_num=1, max_num=3)
            quadratic_function = sy.expand(quadratic_coefficient * (x - x_axis) ** 2 + y_axis)
            # containing equal
            if random() > 0.5:
                latex_answer = f"不等式を満たす\( x \)は存在しない"
                latex_problem = f"\( {sy.latex(quadratic_function)} \\leqq 0 \)"
            # not containing equal
            else:
                latex_answer = f"不等式を満たす\( x \)は存在しない"
                latex_problem = f"\( {sy.latex(quadratic_function)} < 0 \)"
        # (k < 0) and (f(x) > 0)
        elif 0.5 <= inequality_sign_checker < 0.75:
            quadratic_coefficient = self._make_random_number(min_num=1, max_num=3, positive_or_negative="negative")
            y_axis = self._make_random_number(positive_or_negative="negative", min_num=1, max_num=3)
            quadratic_function = sy.expand(quadratic_coefficient * (x - x_axis) ** 2 + y_axis)
            # containing equal
            if random() > 0.5:
                latex_answer = f"不等式を満たす\( x \)は存在しない"
                latex_problem = f"\( {sy.latex(quadratic_function)} \\geqq 0 \)"
            # not containing equal
            else:
                latex_answer = f"不等式を満たす\( x \)は存在しない"
                latex_problem = f"\( {sy.latex(quadratic_function)} > 0 \)"
        #  (k < 0) and (f(x) < 0): x < a, b < x
        else:
            quadratic_coefficient = self._make_random_number(min_num=1, max_num=3, positive_or_negative="negative")
            y_axis = self._make_random_number(positive_or_negative="negative", min_num=1, max_num=3)
            quadratic_function = sy.expand(quadratic_coefficient * (x - x_axis) ** 2 + y_axis)
            if random() > 0.5:
                latex_answer = f"\( x \)はすべての実数"
                latex_problem = f"\( {sy.latex(quadratic_function)} \\leqq 0 \)"
            # not containing equal
            else:
                latex_answer = f"\( x \)はすべての実数"
                latex_problem = f"\( {sy.latex(quadratic_function)} < 0 \)"    
        return latex_answer, latex_problem
    
    def _make_random_number(self, min_num=1, max_num=6, integer_or_frac=None, positive_or_negative=None):
        """条件を満たす数を出力
        
        Args:
            min_num (int, optional): 出力される数の絶対値の最小値
            max_num (int, optional): 出力される数の絶対値の最大値
            integer_or_frac (Union[str, None], optional): 整数か分数かの指定
            positive_or_negative (Union[str, None], optional): 正負の指定
        
        Return:
            number (Union[sy.Integer, sy.Rational]): 整数または分数
        """

        def make_random_integer(min_num, max_num, positive_or_negative):
            """条件を満たす整数を出力

            Args:
                min_num (int): 出力される数の絶対値の最小値
                max_num (int): 出力される数の絶対値の最大値
                positive_or_negative (Union[str, None]): 正負の指定
            
            Return:
                integer_num (sy.Integer): 条件を満たす整数
            
            Raise:
                ValueError: 想定されていない数の指定が来た時に挙上
            """
            num = randint(min_num, max_num)
            if positive_or_negative is None:
                if random() > 0.5:
                    num *= -1
            elif positive_or_negative == "positive":
                pass
            elif positive_or_negative == "negative":
                num *= -1
            else:
                raise ValueError(f"'positive_or_negative' is {positive_or_negative}")
            integer_num = sy.Integer(num)
            return integer_num
        
        def make_random_frac(min_num, max_num, positive_or_negative):
            """条件を満たす分数を出力
            
            Args:
                min_num(int): 分母分子にあてはめられる数の最小値
                max_num(int): 分母分子にあてはめられる数の最大値
                positive_or_negative (Union[str, None]): 正負の指定
    
            Return:
                frac (sy.Rational): 分数
            """
            while True:
                denominator = randint(2, max_num)
                numerator = randint(min_num, max_num)
                frac = sy.Rational(numerator, denominator)
                if frac.is_noninteger:
                    break
            if positive_or_negative is None:
                if random() > 0.5:
                    frac *= -1
            elif positive_or_negative == "positive":
                pass
            elif positive_or_negative == "negative":
                frac *= -1
            else:
                raise ValueError(f"'positive_or_negative' is {positive_or_negative}")
            return frac
        if integer_or_frac is None:
            integer_or_frac = choice(self._used_answer_in_quadratic_equation)
        if integer_or_frac == "integer":
            number = make_random_integer(min_num, max_num, positive_or_negative)
        elif integer_or_frac == "frac":
            number = make_random_frac(min_num, max_num, positive_or_negative)
        else:
            raise ValueError(f"'integer_of_frac' is {integer_or_frac}. This isn't expected value.")
        return number

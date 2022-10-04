from random import choice, choices, randint, random, shuffle


import sympy as sy


class SquareRootProblem:
    """平方根に関係がある問題と解答を出力
    
    Attributes:
        _problem_types (list): 出題のタイプを格納
        latex_answer (str): latex形式で記述された解答
        latex_problem (str): latex形式で記述された問題
    """
    def __init__(self, **settings):
        """初期処理
        
        Args:
            settings (dict): 問題の設定を格納
        """
        self._problem_types = settings["problem_types"]
        self.latex_answer, self.latex_problem = self._make_problem()
    
    def _make_problem(self):
        """選択された出題のタイプをもとに問題と解答を出力する

        Returns:
            latex_answer (str): latex形式で記述された解答
            latex_problem (str): latex形式で記述された問題
        """
        selected_problem_type = choice(self._problem_types)
        if selected_problem_type == "write_square_root_not_using_radical_sign_only_with_integer":
            latex_answer, latex_problem = self._make_write_square_root_not_using_radical_sign_problem(number_mode="integer")
        elif selected_problem_type == "write_square_root_not_using_radical_sign":
            latex_answer, latex_problem = self._make_write_square_root_not_using_radical_sign_problem()
        elif selected_problem_type == "write_square_root_using_radical_sign_only_with_integer":
            latex_answer, latex_problem = self._make_write_square_root_using_radical_sign_problem(number_mode="integer")
        elif selected_problem_type == "write_square_root_using_radical_sign":
            latex_answer, latex_problem = self._make_write_square_root_using_radical_sign_problem()
        elif selected_problem_type == "put_coefficient_into_radical_sign":
            latex_answer, latex_problem = self._make_put_coefficient_into_radical_sign_problem()
        elif selected_problem_type == "take_out_coefficient_from_radical_sign_inside":
            latex_answer, latex_problem = self._make_take_out_coefficient_from_radical_sign_inside_problem()
        elif selected_problem_type == "rationalize":
            latex_answer, latex_problem = self._make_rationalize_problem()
        else:
            raise ValueError(f"selected_problem_type is '{selected_problem_type}'. This may be wrong.")
        
        return latex_answer, latex_problem

    def _make_write_square_root_not_using_radical_sign_problem(self, number_mode=None):
        """根号を使わずに平方根をもとめる問題と解答を出力

        Args:
            number_mode (Union[str, NoneType], optional): 根号の中に出てくる数の種類の指定。デフォルトはNone。

        Returns:
            latex_answer (str): latex形式で記述された解答
            latex_problem (str): latex形式で記述された問題
        """
        if number_mode == "integer":
            number_type = "integer"
        else:
            number_type = choice(["integer", "frac", "decimal"])
        if number_type == "integer":
            if random() > 0.5:
                base = self._make_random_integer(nearer_distance_from_zero=2, farther_distance_from_zero=15)
            else:
                multiplied_number = self._make_random_integer(nearer_distance_from_zero=2, farther_distance_from_zero=5)
                base = 10 * multiplied_number
        elif number_type == "frac":
            numerator = self._make_random_integer(farther_distance_from_zero=10)
            denominator = self._make_random_integer(nearer_distance_from_zero=2, farther_distance_from_zero=10)
            base = sy.Rational(numerator, denominator)
        elif number_type == "decimal":
            multiplied_number = self._make_random_integer(farther_distance_from_zero=9)
            base = 0.1 * multiplied_number
        latex_answer = f"\\( \\pm {sy.latex(base)} \\)"
        problem_number = sy.Pow(base, 2)
        latex_problem = f"根号を使わずに、\\( {sy.latex(problem_number)} \\)の平方根を書きなさい。"        
        return latex_answer, latex_problem
    
    def _make_write_square_root_using_radical_sign_problem(self, number_mode=None):
        """根号を使って平方根をもとめる問題と解答を出力
        
        Args:
            number_mode (Union[str, NoneType], optional): 根号の中に出てくる数の種類の指定。デフォルトはNone。

        Returns:
            latex_answer (str): latex形式で記述された解答
            latex_problem (str): latex形式で記述された問題
        """
        prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19]
        shuffle(prime_numbers)
        if number_mode == "integer":
            number_type = "integer"
        else:
            number_type = choice(["integer", "decimal"])
        if number_type == "integer":
            base = prime_numbers.pop()
        elif number_type == "decimal":
            base = prime_numbers.pop() * 0.1
        latex_answer = f"\\( \\pm \\sqrt{{{sy.latex(base)}}} \\)"
        latex_problem = f"根号を使って、\\( {sy.latex(base)} \\)の平方根を書きなさい。"
        return latex_answer, latex_problem

    def _make_put_coefficient_into_radical_sign_problem(self):
        """係数を根号の中に入れる問題と解答を出力
        
        Returns:
            latex_answer (str): latex形式で記述された解答
            latex_problem (str): latex形式で記述された問題
        """
        prime_numbers = [2, 3, 5, 7, 11, 13]
        coefficient, number_in_radical_sign = choices(prime_numbers, k=2)
        latex_problem = f"\\( {sy.latex(coefficient)} \\sqrt{{{sy.latex(number_in_radical_sign)}}} \\)を、"
        latex_problem += f"\\( \\sqrt{{a}} \\)の形で表しなさい。"
        number_in_radical_sign_after_putting_into = number_in_radical_sign * (coefficient ** 2)
        latex_answer = f"\\( \\sqrt{{{number_in_radical_sign_after_putting_into}}} \\)" 
        return latex_answer, latex_problem
    
    def _make_take_out_coefficient_from_radical_sign_inside_problem(self):
        """根号の中から係数を取り出す問題と解答を出力
        
        Returns:
            latex_answer (str): latex形式で記述された解答
            latex_problem (str): latex形式で記述された問題
        """
        prime_numbers = [2, 3, 5, 7, 11, 13]
        base1, base2 = choices(prime_numbers, k=2)
        value_in_radical_sign = sy.Pow(base1, 1) * sy.Pow(base2, 2)
        latex_problem = f"\\( \\sqrt{{{sy.latex(value_in_radical_sign)}}} \\)を\\( a \\sqrt{{b}} \\)の形で表しなさい。"
        root_with_coefficient = sy.sqrt(value_in_radical_sign)
        latex_answer = f"\\( {sy.latex(root_with_coefficient)} \\)"
        return latex_answer, latex_problem
    
    def _make_rationalize_problem(self):
        """有理化を行う問題を出力
        
        Returns:
            latex_answer (str): latex形式の解答
            latex_problem (str): latex形式の問題
        """
        prime_numbers = [2, 3, 5, 7, 11, 13, 17]
        shuffle(prime_numbers)
        denominator = sy.sqrt(choice(prime_numbers))
        if random() > 0.5:
            numerator = self._make_random_integer(nearer_distance_from_zero=2, farther_distance_from_zero=20)
        else:
            numerator = sy.sqrt(choice(prime_numbers))
        square_root_value = numerator / denominator
        latex_answer = f"\\( {sy.latex(square_root_value)} \\)"
        latex_problem = f"\\( \\frac{{{sy.latex(numerator)}}}{{{sy.latex(denominator)}}} \\)を有理化しなさい。"
        return latex_answer, latex_problem

    def _make_random_integer(self, nearer_distance_from_zero=1, farther_distance_from_zero=10, positive_or_negative="positive"):
        """原点からの距離がnearer_distance_from_zero以上farther_distance_from_zero以下の範囲の整数を出力

        Args:
            nearer_distance_from_zero (int, optional): 原点により近いポイントまでの距離。デフォルトは10
            farther_distance_from_zero (int, optional): 原点からより遠いポイントまでの距離。デフォルトは10
            positive_or_negative (Union[str, NoneType], optional): 正負の指定。デフォルトはpositive

        Raises:
            ValueError: nearer_distance_from_zeroとfarther_distance_from_zeroの大小関係が入れ替わっていたとき。
                あるいは0より小さかったとき。あるいは整数ではなかったときに挙上
            TypeError: positive_or_negativeがpositive, negative, Noneのいずれでもなかったときに挙上

        Returns:
            integer (sy.Integer): 計算に用いる整数
        """
        if nearer_distance_from_zero >= farther_distance_from_zero:
            raise ValueError(
                f"'nearer_distance_from_zero' is {nearer_distance_from_zero}."\
                f"'farther_distance_from_zero' is {farther_distance_from_zero}."\
                "farther_distance_from_zero must be more than nearer_distance_from_zero."\
                )
        if (nearer_distance_from_zero < 0) or not(isinstance(nearer_distance_from_zero, int)):
            raise ValueError(f"'nearer_distance_from_zero' is {nearer_distance_from_zero}. It must be integer and zero or more.")
        if (farther_distance_from_zero < 0) or not(isinstance(farther_distance_from_zero, int)):
            raise ValueError(f"'farther_distance_from_zero' is {farther_distance_from_zero}. It must be integer and zero or more.")
        
        if positive_or_negative == "positive":
            integer = sy.Integer(randint(nearer_distance_from_zero, farther_distance_from_zero))
        elif positive_or_negative == "negative":
            integer = sy.Integer(randint(-farther_distance_from_zero, -nearer_distance_from_zero))
        elif positive_or_negative is None:
            if random() > 0.5:
                integer = sy.Integer(randint(nearer_distance_from_zero, farther_distance_from_zero))
            else:
                integer = sy.Integer(randint(-farther_distance_from_zero, -nearer_distance_from_zero))
        else:
            raise TypeError(f"'positive_or_negative' is {positive_or_negative}. It must be 'positive', 'negative or None.")

        return integer

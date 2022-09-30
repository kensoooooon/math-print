from random import choice, randint, random, shuffle


import sympy as sy


class SquareRootProblem:
    
    def __init__(self, **settings):
        self._problem_types = settings["problem_types"]
        self.latex_answer, self.latex_problem = self._make_problem()
    
    def _make_problem(self):
        selected_problem_type = choice(self._problem_types)
        if selected_problem_type == "write_square_root":
            latex_answer, latex_problem = self._make_write_square_root_problem()
        elif selected_problem_type == "write_square_root_using_symbol":
            latex_answer, latex_problem = self._make_write_square_root_using_symbol_problem()
        
        return latex_answer, latex_problem

    def _make_write_square_root_problem(self):
        number_type = choice(["integer", "frac", "decimal"])
        if number_type == "integer":
            if random() > 0.5:
                base = self._make_random_integer(farther_distance_from_zero=10)
            else:
                multiplied_number = self._make_random_integer(farther_distance_from_zero=5)
                base = 10 * multiplied_number
        elif number_type == "frac":
            numerator = self._make_random_integer(farther_distance_from_zero=10)
            denominator = self._make_random_integer(farther_distance_from_zero=10)
            base = sy.Rational(numerator, denominator)
        elif number_type == "decimal":
            multiplied_number = self._make_random_integer(farther_distance_from_zero=9)
            base = 0.1 * multiplied_number
        latex_answer = f"\\( \\pm {sy.latex(base)} \\)"
        problem_number = sy.Pow(base, 2)
        latex_problem = f"\\( {sy.latex(problem_number)} \\)の平方根を求めなさい。"        
        return latex_answer, latex_problem
    
    def _make_write_square_root_using_symbol_problem(self):
        prime_numbers = [2, 3, 5, 7, 11, 13]
        shuffle(prime_numbers)
        number_type = choice(["integer", "frac"])
        if number_type == "integer":
            base = prime_numbers.pop()
        elif number_type == "frac":
            numerator = prime_numbers.pop()
            denominator = prime_numbers.pop()
            base = sy.Rational(numerator, denominator)
        square_root_number = sy.sqrt(base)
        latex_answer = f"\\( \\pm {sy.latex(square_root_number)}\\)"
        latex_problem = f"\\( {sy.latex(base)} \\)の平方根を求めなさい。"
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

"""
9/9
平方根の和・差と積・商の計算において、指定の項数で計算できるように変更
    与えられるのは、[2, 3, 4]のような数字入のリスト
"""
from random import choice, randint, random, shuffle


import sympy as sy


class SquareRootCalculateProblem:
    """平方根の計算問題と解答を出力
    
    Attributes:
        _calculation_types (list): 問題に使用される可能性がある計算の種類を格納
        latex_answer (str): latex形式で記述された解答
        latex_problem (str): latex形式で記述された問題
    """
    def __init__(self, **settings):
        """初期処理
        
        Args:
            settings (dict): 問題の設定を格納
        """
        self._calculation_types = settings["calculation_types"]
        self._numbers_of_terms = settings["numbers_of_terms"]
        self.latex_answer, self.latex_problem = self._make_problem()
    
    def _make_problem(self):
        """計算の候補をもとに問題と回答を出力する

        Raises:
            ValueError: 存在していない計算の種類が選択されたときに挙上

        Returns:
            latex_answer (str): latex形式で記述された解答
            latex_problem (str): latex形式で記述された問題
        """
        selected_calculation_type = choice(self._calculation_types)
        if selected_calculation_type == "addition_and_subtraction_only":
            latex_answer, latex_problem = self._make_addition_and_subtraction_only_problem()
        elif selected_calculation_type == "multiplication_and_division_only":
            latex_answer, latex_problem = self._make_multiplication_and_division_only_problem()
        elif selected_calculation_type == "using_expand_formula":
            latex_answer, latex_problem = self._make_using_expand_formula_problem()
        else:
            raise ValueError(f"'selected_calculation_type is {selected_calculation_type}. This calculation type doesn't exist.")
        return latex_answer, latex_problem
    
    def _make_addition_and_subtraction_only_problem(self):
        """和と差のみを用いた計算の問題と解答を出力

        Returns:
            latex_answer (str): latex形式で記述された解答
            latex_problem (str): latex形式で記述された問題
        """
        
        def _latex_formula_maker(coeff_and_base):
            """与えられた係数と平方根の底から、平方根の表示がランダムで切り替わる和と差の計算式と計算結果を出力

            Args:
                coeff_and_base (list): 係数と平方根の底のタプルを格納

            Returns:
                answer_value (sy.Add): 計算結果
                latex_formula (str): latex形式の計算式
            """
            answer_value = 0
            latex_formula = ""
            for coeff, base in coeff_and_base:
                answer_value += coeff * sy.sqrt(base)
                if random() > 0.5:
                    sqrt_latex = sy.latex(sy.sqrt((coeff ** 2) * base))
                else:
                    sqrt_latex = f"\\sqrt{{{(coeff ** 2) * base}}}"
                if not(latex_formula):
                    if coeff == 0:
                        continue
                    elif coeff > 0:
                        latex_formula += f"{sqrt_latex}"
                    else:
                        latex_formula += f"- {sqrt_latex}"
                else:
                    if coeff == 0:
                        continue
                    elif coeff > 0:
                        latex_formula += f"+ {sqrt_latex} "
                    else:
                        latex_formula += f"- {sqrt_latex} "
            return answer_value, latex_formula
        
        prime_numbers = [2, 3, 5, 7, 11]
        shuffle(prime_numbers)
        # number_of_term = randint(2, 4)
        number_of_terms = choice(self._numbers_of_terms)
        # two common bases
        coeff_and_base = []
        if number_of_terms == 2:
            common_base = prime_numbers.pop()
            coefficient1 = self._make_random_integer(farther_distance_from_zero=5)
            coeff_and_base.append((coefficient1, common_base))
            coefficient2 = self._make_random_integer(farther_distance_from_zero=5)
            coeff_and_base.append((coefficient2, common_base))
        # two common bases and one uncommon base 
        elif number_of_terms == 3:
            common_base = prime_numbers.pop()
            coefficient1 = self._make_random_integer(farther_distance_from_zero=5)
            coeff_and_base.append((coefficient1, common_base))
            coefficient2 = self._make_random_integer(farther_distance_from_zero=5)
            coeff_and_base.append((coefficient2, common_base))
            uncommon_base = prime_numbers.pop()
            coefficient3 = self._make_random_integer(farther_distance_from_zero=5)
            coeff_and_base.append((coefficient3, uncommon_base))
        # two common bases and two other common bases
        elif number_of_terms == 4:
            common_base1 = prime_numbers.pop()
            coefficient1 = self._make_random_integer(farther_distance_from_zero=5)
            coeff_and_base.append((coefficient1, common_base1))
            coefficient2 = self._make_random_integer(farther_distance_from_zero=5)
            coeff_and_base.append((coefficient2, common_base1))
            common_base2 = prime_numbers.pop()
            coefficient3 = self._make_random_integer(farther_distance_from_zero=5)
            coeff_and_base.append((coefficient3, common_base2))
            coefficient4 = self._make_random_integer(farther_distance_from_zero=5)
            coeff_and_base.append((coefficient4, common_base2))
        shuffle(coeff_and_base)
        answer, latex_problem = _latex_formula_maker(coeff_and_base)
        latex_answer = f"= {sy.latex(answer)}"
        return latex_answer, latex_problem
    
    def _make_multiplication_and_division_only_problem(self):
        """積と商のみを用いた計算の問題と解答を出力

        Returns:
            latex_answer (str): latex形式で記述された解答
            latex_problem (str): latex形式で記述された問題
        """
        
        def _latex_formula_maker(coeff_and_base_and_calculation_types):
            """与えられた係数の底から、平方根の表示がランダムで切り替わる積と商の計算式と結果を出力

            Args:
                coeff_and_base_and_calculation_types (list): 係数と平方根の底と計算方法のタプルを収納
                
            Returns:
                answer_value (sy.Mul): 計算結果
                latex_formula (str): latex形式の計算式
            """
            answer_value = 1
            latex_formula = ""
            for base, coeff, calculation_type in coeff_and_base_and_calculation_types:
                if calculation_type == "multiplication":
                    answer_value *= coeff * sy.sqrt(base)
                elif calculation_type == "division":
                    answer_value /= coeff * sy.sqrt(base)
                if random() > 0.5:
                    sqrt_latex = sy.latex(sy.sqrt((coeff ** 2) * base))
                else:
                    sqrt_latex = f"\\sqrt{{{(coeff ** 2) * base}}}"
                if not(latex_formula):
                    if coeff == 0:
                        continue
                    elif coeff > 0:
                        if calculation_type == "multiplication":
                            latex_formula += f"{sqrt_latex}"
                        elif calculation_type == "division":
                            latex_formula += f"\\frac{{{1}}}{{{sqrt_latex}}}"
                    else:
                        if calculation_type == "multiplication":
                            latex_formula += f"- {sqrt_latex}"
                        elif calculation_type == "division":
                            latex_formula += f"- \\frac{{{1}}}{{{sqrt_latex}}}"
                else:
                    if coeff == 0:
                        continue
                    elif coeff > 0:
                        if calculation_type == "multiplication":
                            latex_formula += f"\\times {sqrt_latex}"
                        elif calculation_type == "division":
                            latex_formula += f"\\div {sqrt_latex}"
                    else:
                        if calculation_type == "multiplication":
                            latex_formula += f"\\times \\left( - {sqrt_latex} \\right)"
                        elif calculation_type == "division":
                            latex_formula += f"\\div \\left( - {sqrt_latex} \\right)"
            return answer_value, latex_formula
        
        prime_numbers = [2, 3, 5, 7, 11]
        shuffle(prime_numbers)
        # number_of_term = randint(2, 4)
        number_of_terms = choice(self._numbers_of_terms)
        # multiplication to division of common base
        coeff_and_base_and_calculation_types = []
        if number_of_terms == 2:
            common_base = prime_numbers.pop()
            coeff1 = self._make_random_integer(farther_distance_from_zero=5)
            calculation_type1 = "multiplication"
            coeff_and_base_and_calculation_types.append((common_base, coeff1, calculation_type1))
            coeff2 = self._make_random_integer(farther_distance_from_zero=5)
            calculation_type2 = "division"
            coeff_and_base_and_calculation_types.append((common_base, coeff2, calculation_type2))
        # multiplication to division of common base and multiplication or division of uncommon base
        elif number_of_terms == 3:
            common_base = prime_numbers.pop()
            coeff1 = self._make_random_integer(farther_distance_from_zero=4)
            calculation_type1 = "multiplication"
            coeff_and_base_and_calculation_types.append((common_base, coeff1, calculation_type1))
            coeff2 = self._make_random_integer(farther_distance_from_zero=4)
            calculation_type2 = "division"
            coeff_and_base_and_calculation_types.append((common_base, coeff2, calculation_type2))
            uncommon_base = prime_numbers.pop()
            coeff3 = self._make_random_integer(farther_distance_from_zero=4)
            calculation_type3 = choice(["multiplication", "division"])
            coeff_and_base_and_calculation_types.append((uncommon_base, coeff3, calculation_type3))
        # two by two common bases for multiplication to division
        elif number_of_terms == 4:
            common_base1 = prime_numbers.pop()
            coeff1 = self._make_random_integer(farther_distance_from_zero=3)
            calculation_type1 = "multiplication"
            coeff_and_base_and_calculation_types.append((common_base1, coeff1, calculation_type1))
            coeff2 = self._make_random_integer(farther_distance_from_zero=3)
            calculation_type2 = "division"
            coeff_and_base_and_calculation_types.append((common_base1, coeff2, calculation_type2))
            common_base2 = prime_numbers.pop()
            coeff3 = self._make_random_integer(farther_distance_from_zero=3)
            calculation_type3 = "multiplication"
            coeff_and_base_and_calculation_types.append((common_base2, coeff3, calculation_type3))
            coeff4 = self._make_random_integer(farther_distance_from_zero=3)
            calculation_type4 = "multiplication"
            coeff_and_base_and_calculation_types.append((common_base2, coeff4, calculation_type4))
        shuffle(coeff_and_base_and_calculation_types)
        answer, latex_problem = _latex_formula_maker(coeff_and_base_and_calculation_types)
        latex_answer = f"= {sy.latex(answer)}"
        return latex_answer, latex_problem
    
    def _make_using_expand_formula_problem(self):
        """展開公式を用いる平方根の計算問題と解答を出力

        Returns:
            latex_answer (str): latex形式で記述された解答
            latex_problem (str): latex形式で記述された問題
        """
        prime_numbers = [2, 3, 5, 7, 11]
        shuffle(prime_numbers)
        selected_formula = choice(
            ["a(b+c)=ab+ac", "(a+b)c=ac+bc",
            "(a+b)(c+d)=ac+ad+bc+bd", "(a+b)^2=a^2+2ab+b^2",
            "(a-b)^2=a^2-2ab+b^2", "(a+b)(a-b)=a^2-b^2",]
        )
        latex_problem = ""
        if selected_formula == "a(b+c)=ab+ac":
            a_coeff = self._make_random_integer(farther_distance_from_zero=6)
            a_inner_value = self._make_random_integer(positive_or_negative="positive")
            a = a_coeff * sy.sqrt(a_inner_value)
            latex_problem += f"{sy.latex(a)} \\times \\left( "
            b_inner_value = prime_numbers.pop()
            c_inner_value = self._make_random_integer(positive_or_negative="positive")
            if random() > 0.5:
                b_inner_value, c_inner_value = c_inner_value, b_inner_value
            b_coeff = self._make_random_integer(farther_distance_from_zero=6)
            b = b_coeff * sy.sqrt(b_inner_value)
            latex_problem += f"{sy.latex(b)}"
            c_coeff = self._make_random_integer(farther_distance_from_zero=6)
            c = c_coeff * sy.sqrt(c_inner_value)
            if c > 0:
                latex_problem += f"+ {sy.latex(c)} \\right)"
            else:
                latex_problem += f"{sy.latex(c)} \\right)"
            answer = sy.expand(a * (b + c))
        elif selected_formula == "(a+b)c=ac+bc":
            a_inner_value = prime_numbers.pop()
            b_inner_value = self._make_random_integer(positive_or_negative="positive")
            if random() > 0.5:
                a_inner_value, b_inner_value = b_inner_value, a_inner_value
            a_coeff = self._make_random_integer(farther_distance_from_zero=6)
            a = a_coeff * sy.sqrt(a_inner_value)
            latex_problem += f"\\left( {sy.latex(a)} "
            b_coeff = self._make_random_integer(farther_distance_from_zero=6)
            b = b_coeff * sy.sqrt(b_inner_value)
            if b > 0:
                latex_problem += f" + {sy.latex(b)} \\right) \\times "
            else:
                latex_problem += f"{sy.latex(b)} \\right) \\times "
            c_coeff = self._make_random_integer(farther_distance_from_zero=6)
            c_inner_value = self._make_random_integer(positive_or_negative="positive")
            c = c_coeff * sy.sqrt(c_inner_value)
            if c > 0:
                latex_problem += f"{sy.latex(c)}"
            else:
                latex_problem += f"\\left( {sy.latex(c)} \\right)"
            answer = sy.expand((a + b) * c)
        elif selected_formula == "(a+b)(c+d)=ac+ad+bc+bd":
            a_inner_value = prime_numbers.pop()
            b_inner_value = self._make_random_integer(positive_or_negative="positive")
            if random() > 0.5:
                a_inner_value, b_inner_value = b_inner_value, a_inner_value
            a_coeff = self._make_random_integer(farther_distance_from_zero=6)
            a = a_coeff * sy.sqrt(a_inner_value)
            latex_problem += f"\\left( {sy.latex(a)} "
            b_coeff = self._make_random_integer(nearer_distance_from_zero=2, farther_distance_from_zero=6)
            b = b_coeff * sy.sqrt(b_inner_value)
            if b > 0:
                latex_problem += f" + {sy.latex(b)} \\right) "
            else:
                latex_problem += f"{sy.latex(b)} \\right) "
            c_inner_value = prime_numbers.pop()
            d_inner_value = self._make_random_integer(positive_or_negative="positive")
            if random() > 0.5:
                c_inner_value, d_inner_value = d_inner_value, c_inner_value
            c_coeff = self._make_random_integer(farther_distance_from_zero=6)
            c = c_coeff * sy.sqrt(c_inner_value)
            latex_problem += f"\\left( {sy.latex(c)} "
            d_coeff = self._make_random_integer(farther_distance_from_zero=6)
            d = d_coeff * sy.sqrt(d_inner_value)
            if d > 0:
                latex_problem += f"+ {sy.latex(d)} \\right)"
            else:
                latex_problem += f"{sy.latex(d)} \\right)"
            answer = sy.expand((a + b) * (c + d))
        elif selected_formula == "(a+b)^2=a^2+2ab+b^2":
            a_inner_value = prime_numbers.pop()
            b_inner_value = self._make_random_integer(positive_or_negative="positive")
            if random() > 0.5:
                a_inner_value, b_inner_value = b_inner_value, a_inner_value
            a_coeff = self._make_random_integer(farther_distance_from_zero=3, positive_or_negative="positive")
            a = a_coeff * sy.sqrt(a_inner_value)
            latex_problem += f"\\left( {sy.latex(a)} "
            b_coeff = self._make_random_integer(farther_distance_from_zero=3, positive_or_negative="positive")
            b = b_coeff * sy.sqrt(b_inner_value)
            latex_problem += f" + {sy.latex(b)} \\right)^2 "
            answer = sy.expand((a + b) ** 2)
        elif selected_formula == "(a-b)^2=a^2-2ab+b^2":
            a_inner_value = prime_numbers.pop()
            b_inner_value = self._make_random_integer(positive_or_negative="positive")
            if random() > 0.5:
                a_inner_value, b_inner_value = b_inner_value, a_inner_value
            a_coeff = self._make_random_integer(farther_distance_from_zero=3, positive_or_negative="positive")
            a = a_coeff * sy.sqrt(a_inner_value)
            latex_problem += f"\\left( {sy.latex(a)} "
            b_coeff = self._make_random_integer(farther_distance_from_zero=3, positive_or_negative="positive")
            b = b_coeff * sy.sqrt(b_inner_value)
            latex_problem += f" - {sy.latex(b)} \\right)^2 "
            answer = sy.expand((a - b) ** 2)
        elif selected_formula == "(a+b)(a-b)=a^2-b^2":
            a_inner_value = prime_numbers.pop()
            b_inner_value = self._make_random_integer(positive_or_negative="positive")
            if random() > 0.5:
                a_inner_value, b_inner_value = b_inner_value, a_inner_value
            a_coeff = self._make_random_integer(farther_distance_from_zero=3, positive_or_negative="positive")
            a = a_coeff * sy.sqrt(a_inner_value)
            a_latex = sy.latex(a)
            b_coeff = self._make_random_integer(farther_distance_from_zero=3, positive_or_negative="positive")
            b = b_coeff * sy.sqrt(b_inner_value)
            b_latex = sy.latex(b)
            if random() > 0.5:
                latex_problem = f"\\left( {a_latex} + {b_latex} \\right)\\left( {a_latex} - {b_latex} \\right)"
            else:
                latex_problem = f"\\left( {a_latex} - {b_latex} \\right)\\left( {a_latex} + {b_latex} \\right)"
            answer = sy.expand((a + b) * (a - b))
        latex_answer = f"= {sy.latex(answer)}"
        return latex_answer, latex_problem

    def _make_random_integer(self, nearer_distance_from_zero=1, farther_distance_from_zero=10, positive_or_negative=None):
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

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
        elif selected_calculation_type == "all_types_calculation":
            latex_answer, latex_problem = self._make_all_types_calculation_problem()
        else:
            raise ValueError(f"'selected_calculation_type is {selected_calculation_type}. This calculation type doesn't exist.")
        return latex_answer, latex_problem
    
    def _make_addition_and_subtraction_only_problem(self):
        """和と差のみを用いた計算の問題と解答を出力

        Returns:
            latex_answer (str): latex形式で記述された解答
            latex_problem (str): latex形式で記述された問題
        
        Developing:
            2~4項で計算のタイプが変わる
            2項: 同じ底で足し引き
            3項: 同じ底×2+異なる底×1で計算できるものとできないものの区別
            4項: 同じ底×2+同じ底'×2
            5項: 同じ底×2+同じ底'×2+異なる底
        """
        prime_numbers = [2, 3, 5, 7, 11, 13]
        shuffle(prime_numbers)
        number_of_term = randint(2, 5)
        # two common bases
        coeff_and_base = []
        if number_of_term == 2:
            common_base = prime_numbers.pop()
            coefficient1 = self._make_random_integer(farther_distance_from_zero=3)
            coeff_and_base.append((coefficient1, common_base))
            coefficient2 = self._make_random_integer(farther_distance_from_zero=3)
            coeff_and_base.append((coefficient2, common_base))
        # two common bases and one uncommon base 
        elif number_of_term == 3:
            common_base = prime_numbers.pop()
            coefficient1 = self._make_random_integer(farther_distance_from_zero=3)
            coeff_and_base.append((coefficient1, common_base))
            coefficient2 = self._make_random_integer(farther_distance_from_zero=3)
            coeff_and_base.append((coefficient2, common_base))
            uncommon_base = prime_numbers.pop()
            coefficient3 = self._make_random_integer(farther_distance_from_zero=3)
            coeff_and_base.append((coefficient3, uncommon_base))
        # two common bases and two other common bases
        elif number_of_term == 4:
            common_base1 = prime_numbers.pop()
            coefficient1 = self._make_random_integer(farther_distance_from_zero=3)
            coeff_and_base.append((coefficient1, common_base1))
            coefficient2 = self._make_random_integer(farther_distance_from_zero=3)
            coeff_and_base.append((coefficient2, common_base1))
            common_base2 = prime_numbers.pop()
            coefficient3 = self._make_random_integer(farther_distance_from_zero=3)
            coeff_and_base.append((coefficient3, common_base2))
            coefficient4 = self._make_random_integer(farther_distance_from_zero=3)
            coeff_and_base.append((coefficient4, common_base2))
        # two common bases and two other common bases and one uncommon base
        elif number_of_term == 5:
            common_base1 = prime_numbers.pop()
            coefficient1 = self._make_random_integer(farther_distance_from_zero=3)
            coeff_and_base.append((coefficient1, common_base1))
            coefficient2 = self._make_random_integer(farther_distance_from_zero=3)
            coeff_and_base.append((coefficient2, common_base1))
            common_base2 = prime_numbers.pop()
            coefficient3 = self._make_random_integer(farther_distance_from_zero=3)
            coeff_and_base.append((coefficient3, common_base2))
            coefficient4 = self._make_random_integer(farther_distance_from_zero=3)
            coeff_and_base.append((coefficient4, common_base2))
            uncommon_base = prime_numbers.pop()
            coefficient5 = self._make_random_integer(farther_distance_from_zero=3)
            coeff_and_base.append((coefficient5, uncommon_base))
        shuffle(coeff_and_base)
        answer, latex_problem = self._latex_formula_maker(coeff_and_base)
        latex_answer = sy.latex(answer)
        return latex_answer, latex_problem
    
    def _make_multiplication_and_division_only_problem(self):
        latex_answer = "dummmymmyanswererwewr"
        latex_problem = "dummdududmmmyyyprorororproblem"
        return latex_answer, latex_problem
    
    def _make_all_types_calculation_problem(self):
        latex_answer = "dummmymmyanswererwewr"
        latex_problem = "dummdududmmmyyyprorororproblem"
        return latex_answer, latex_problem
    
    def _latex_formula_maker(self, coeff_and_base):
        """与えられた係数と平方根の底から、平方根の表示がランダムで切り替わる和と差の計算式と計算結果を出力

        Args:
            coeff_and_base (list): 係数と平方根の底のタプルを格納

        Returns:
            answer_value (sy.Add): 計算結果
            latex_formula (str): latex形式の計算式
        
        Developing:
            2√3, 2√3みたいなケースが不味そう。(上書き？だったはず？)
            ->list of tupleのがよき？
        """
        answer_value = 0
        latex_formula = ""
        for coeff, base in coeff_and_base:
            print(f"coeff: {coeff}, base: {base}")
            answer_value += coeff * sy.sqrt(base)
            if random() > 0.5:
                sqrt_latex = sy.latex(sy.sqrt((coeff ** 2) * base))
            else:
                sqrt_latex = f"\\sqrt{{{(coeff ** 2) * base}}}"
            if not(latex_formula):
                if coeff == 0:
                    continue
                else:
                    latex_formula += f"{sqrt_latex}"
            else:
                if coeff == 0:
                    continue
                elif coeff > 0:
                    latex_formula += f"+ {sqrt_latex} "
                else:
                    latex_formula += f"- {sqrt_latex} "
        return answer_value, latex_formula

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

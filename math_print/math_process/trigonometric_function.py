from random import choice, randint, random

import sympy as sy


class TrigonometricFunctionProblem:
    """三角関数の値と角度に関連する問題を出力
    
    Attributes:
        _problem_types (list): 問題の候補を格納
        _used_trigonometric_functions (list): 値と角度の相互変換に使用される三角関数
        _radian_range (str): 値と角度の相互変換に使用される角度の範囲
        latex_answer (str): latex形式で記述された解答
        latex_problem (str): latex形式で記述された問題
    """
    def __init__(self, **settings):
        """初期処理
        
        settings (dict): 問題設定を格納
        """
        self._problem_types = settings["problem_types"]
        self._radian_range = settings["radian_range"]
        self._used_trigonometric_functions = settings["used_trigonometric_functions"]
        self._sin_values, self._cos_values, self._tan_values = self._trigonometric_functions_latex_maker()
        self.latex_answer, self.latex_problem = self._make_problem()
    
    def _make_problem(self):
        """問題作成のコントローラー

        Returns:
            latex_answer (str): latex形式で記述された解答
            latex_problem (str): latex形式で記述された問題
        
        Raises:
            ValueError: 問題のタイプが存在しない時に挙上
        """
        selected_problem_type = choice(self._problem_types)
        selected_trigonometric_function = choice(self._used_trigonometric_functions)
        if selected_problem_type == "value_to_radian":
            latex_answer, latex_problem = self._make_value_to_radian_problem(selected_trigonometric_function)
        elif selected_problem_type == "radian_to_value":
            latex_answer, latex_problem = self._make_radian_to_value_problem(selected_trigonometric_function)
        elif selected_problem_type == "mutual_relationships":
            latex_answer, latex_problem = self._make_mutual_relationships_problem()
        else:
            raise ValueError(f"'selected_problem_type' is {selected_problem_type}. This may be wrong.")
        return latex_answer, latex_problem
    
    def _make_value_to_radian_problem(self, trigonometric_function):
        """値から角度を求める問題と解答の出力
        
        Args:
            trigonometric_function (str): 問題に使用される三角関数の出力
        
        Returns:
            latex_answer (str): latex形式で記述された解答
            latex_problem (str): latex形式で記述された問題
        
        Raises:
            ValueError: _radian_rangeに想定されていないものが使用された時に挙上
        """
        if self._radian_range == "up_to_pi_over_2":
            list_6 = [sy.Rational(i, 6) * sy.pi for i in range(4)]
            list_4 = [sy.Rational(i, 4) * sy.pi for i in range(3)]
        elif self._radian_range == "up_to_pi":
            list_6 = [sy.Rational(i, 6) * sy.pi for i in range(7)]
            list_4 = [sy.Rational(i, 4) * sy.pi for i in range(5)]
        elif self._radian_range == "up_to_2pi":
            list_6 = [sy.Rational(i, 6) * sy.pi for i in range(12)]
            list_4 = [sy.Rational(i, 4) * sy.pi for i in range(8)]
        else:
            raise ValueError(f"'_radian_range' is {self._radian_range}. This may be wrong.")
        radian_candidates = list(set(list_6 + list_4))
        if trigonometric_function == "sin":
            selected_radian = choice(radian_candidates)
            if self._radian_range == "up_to_pi_over_2":
                latex_answer = f"\\( \\theta = {sy.latex(selected_radian)} \\)"
                latex_problem = f"\\( \\sin \\theta = {self._sin_values[selected_radian]} \\)を満たす\\( \\theta (0 \\leqq \\theta \\leqq {sy.latex(sy.pi / 2)}) \\)を求めよ。"
            elif self._radian_range == "up_to_pi":
                if selected_radian == sy.pi / 2:
                    latex_answer = f"\\( \\theta = {sy.latex(selected_radian)}\\)"
                else:
                    selected_radian1 = selected_radian
                    selected_radian2 = sy.pi - selected_radian1
                    if selected_radian1 > selected_radian2:
                        selected_radian1, selected_radian2 = selected_radian2, selected_radian1
                    latex_answer = f"\\( \\theta = {sy.latex(selected_radian1)}, {sy.latex(selected_radian2)} \\)"
                latex_problem = f"\\( \\sin \\theta = {self._sin_values[selected_radian]} \\)を満たす\\( \\theta (0 \\leqq \\theta \\leqq {sy.latex(sy.pi)}) \\)を求めよ。"
            elif self._radian_range == "up_to_2pi":
                if (selected_radian == sy.pi / 2) or (selected_radian == 3 * sy.pi / 2):
                    latex_answer = f"\\( \\theta = {sy.latex(selected_radian)} \\)"
                else:
                    if selected_radian <= sy.pi:
                        selected_radian1 = selected_radian
                        selected_radian2 = sy.pi - selected_radian1
                    elif selected_radian > sy.pi:
                        selected_radian1 = selected_radian
                        selected_radian2 = 3 * sy.pi - selected_radian1
                    if selected_radian1 > selected_radian2:
                        selected_radian1, selected_radian2 = selected_radian2, selected_radian1
                    latex_answer = f"\\( \\theta = {sy.latex(selected_radian1)}, {sy.latex(selected_radian2)} \\)"
                latex_problem = f"\\( \\sin \\theta = {self._sin_values[selected_radian]} \\)を満たす\\( \\theta (0 \\leqq \\theta < {sy.latex(2 * sy.pi)}) \\)を求めよ。"           
        elif trigonometric_function == "cos":
            selected_radian = choice(radian_candidates)
            if self._radian_range == "up_to_pi_over_2":
                latex_answer = f"\\( \\theta = {sy.latex(selected_radian)} \\)"
                latex_problem = f"\\( \\cos \\theta = {self._cos_values[selected_radian]} \\)を満たす\\( \\theta (0 \\leqq \\theta \\leqq {sy.latex(sy.pi / 2)}) \\)を求めよ。"
            elif self._radian_range == "up_to_pi":
                latex_answer = f"\\( \\theta = {sy.latex(selected_radian)} \\)"
                latex_problem = f"\\( \\cos \\theta = {self._cos_values[selected_radian]} \\)を満たす\\( \\theta (0 \\leqq \\theta \\leqq {sy.latex(sy.pi)}) \\)を求めよ。"
            elif self._radian_range == "up_to_2pi":
                if (selected_radian == 0) or (selected_radian == sy.pi):
                    latex_answer = f"\\( \\theta = {sy.latex(selected_radian)} \\)"
                else:
                    selected_radian1 = selected_radian
                    selected_radian2 = 2 * sy.pi - selected_radian1
                    if selected_radian1 > selected_radian2:
                        selected_radian1, selected_radian2 = selected_radian2, selected_radian1
                    latex_answer = f"\\( \\theta = {sy.latex(selected_radian1)}, {sy.latex(selected_radian2)} \\)"
                latex_problem = f"\\( \\cos \\theta = {self._cos_values[selected_radian]} \\)を満たす\\( \\theta (0 \\leqq \\theta < {sy.latex(2 * sy.pi)}) \\)を求めよ。"       
        elif trigonometric_function == "tan":
            radian_candidates.remove(sy.pi / 2)
            if self._radian_range == "up_to_2pi":
                radian_candidates.remove(3 * sy.pi / 2)
            selected_radian = choice(radian_candidates)
            if self._radian_range == "up_to_pi_over_2":
                latex_answer = f"\\( \\theta = {sy.latex(selected_radian)} \\)"
                latex_problem = f"\\( \\tan \\theta = {self._tan_values[selected_radian]} \\)を満たす\\( \\theta (0 \\leqq \\theta < {sy.latex(sy.pi / 2)}) \\)を求めよ。"
            elif self._radian_range == "up_to_pi":
                if (selected_radian == 0) or (selected_radian == sy.pi):
                    selected_radian1 = selected_radian
                    selected_radian2 = sy.pi - selected_radian1
                    if selected_radian1 > selected_radian2:
                        selected_radian1, selected_radian2 = selected_radian2, selected_radian1
                    latex_answer = f"\\( \\theta = {sy.latex(selected_radian1)}, {sy.latex(selected_radian2)} \\)"
                else:
                    latex_answer = f"\\( \\theta = {sy.latex(selected_radian)} \\)"
                latex_problem = f"\\( \\tan \\theta = {self._tan_values[selected_radian]} \\)を満たす\\( \\theta (0 \\leqq \\theta \\leqq {sy.latex(sy.pi)}, \\theta \\neq {sy.latex(sy.pi / 2)}) \\)を求めよ。"
            elif self._radian_range == "up_to_2pi":
                if selected_radian < sy.pi:
                    selected_radian1 = selected_radian
                    selected_radian2 = selected_radian1 + sy.pi
                else:
                    selected_radian2 = selected_radian
                    selected_radian1 = selected_radian2 - sy.pi
                latex_answer = f"\\( \\theta = {sy.latex(selected_radian1)}, {sy.latex(selected_radian2)} \\)"
                latex_problem = f"\\( \\tan \\theta = {self._tan_values[selected_radian]} \\)を満たす\\( \\theta (0 \\leqq \\theta < {sy.latex(2 * sy.pi)}, \\theta \\neq {sy.latex(sy.pi / 2)}, {sy.latex(3 * sy.pi / 2)})\\)を求めよ。"
        return latex_answer, latex_problem
    
    def _make_radian_to_value_problem(self, trigonometric_function):
        """角度から値を求める問題の出力
        
        Args:
            trigonometric_function (str): 問題に使用される三角関数
            
        Returns:
            latex_answer (str): latex形式で記述された解答
            latex_problem (str): latex形式で記述された問題
        
        Raises:
            ValueError: 想定されていない角度の範囲が入力されたときに挙上
        """
        if self._radian_range == "up_to_pi_over_2":
            list_6 = [sy.Rational(i, 6) * sy.pi for i in range(4)]
            list_4 = [sy.Rational(i, 4) * sy.pi for i in range(3)]
        elif self._radian_range == "up_to_pi":
            list_6 = [sy.Rational(i, 6) * sy.pi for i in range(7)]
            list_4 = [sy.Rational(i, 4) * sy.pi for i in range(5)]
        elif self._radian_range == "up_to_2pi":
            list_6 = [sy.Rational(i, 6) * sy.pi for i in range(12)]
            list_4 = [sy.Rational(i, 4) * sy.pi for i in range(8)]
        else:
            raise ValueError(f"'_radian_range' is {self._radian_range}. This may be wrong.")
        radian_candidates = list(set(list_6 + list_4))
        if trigonometric_function == "sin":
            selected_radian = choice(radian_candidates)
            latex_problem = f"\\( \\sin {sy.latex(selected_radian)} \\)の値を求めよ。"
            sin_value = self._sin_values[selected_radian]
            latex_answer = f"\\( = {sin_value} \\)"
        elif trigonometric_function == "cos":
            selected_radian = choice(radian_candidates)
            latex_problem = f"\\( \\cos {sy.latex(selected_radian)} \\)の値を求めよ。"
            cos_value = self._cos_values[selected_radian]
            latex_answer = f"\\( = {cos_value} \\)"
        elif trigonometric_function == "tan":
            radian_candidates.remove(sy.pi / 2)
            if self._radian_range == "up_to_2pi":
                radian_candidates.remove(3 * sy.pi / 2)
            selected_radian = choice(radian_candidates)
            latex_problem = f"\\( \\tan {sy.latex(selected_radian)} \\)の値を求めよ。"
            tan_value = self._tan_values[selected_radian]
            latex_answer = f"\\( = {tan_value} \\)"
        return latex_answer, latex_problem
    
    def _make_mutual_relationships_problem(self):
        """三角関数の相互関係を求める問題を出力
        
        Returns:
            latex_answer (str): latex形式で記述された解答
            latex_problem (str): latex形式で記述された問題
        
        Developing:
            step by pi / 2
                0 <= theta <= pi / 2
                pi / 2 <= theta <= pi
                pi <= theta <= 3 * pi / 2
                3 * pi / 2 <= theta < 2 * pi
            step by pi
                0 <= theta <= pi
                pi / 2 <= theta = 3 * pi / 2
                pi <= theta < 2 * pi
            step by 3 * pi / 2
                0 <= theta <= 3 * pi /2
                pi / 2 <= theta < 2 * pi
            step by 2 * pi
                0 <= theta < 2 * pi
            divide?
        """
        def latex_answer_and_problem_maker(start_trigonometric_function, radian_range):
            """与えられた三角関数と角度の範囲から、解答と問題を出力

            Args:
                trigonometric_function (str): 解答の起点となる三角関数
                radian_range (str): 角度の範囲

            Returns:
                latex_answer (str): latex形式で記述された解答
                latex_problem (str): latex形式で記述された問題
            
            Developing:
                step by pi / 2
                    0 <= theta <= pi / 2
                    pi / 2 <= theta <= pi
                    pi <= theta <= 3 * pi / 2
                    3 * pi / 2 <= theta < 2 * pi
                step by pi
                    0 <= theta <= pi
                    pi / 2 <= theta = 3 * pi / 2
                    pi <= theta < 2 * pi
                step by 3 * pi / 2
                    0 <= theta <= 3 * pi /2
                    pi / 2 <= theta < 2 * pi
                step by 2 * pi
                    0 <= theta < 2 * pi
            """
            if start_trigonometric_function == "sin":
                # step by pi over 2
                # 0 <= sin <= 1, 0 <= cos <= 1, 0 <= tan <= 1
                if radian_range == "from_zero_up_to_pi_over_2":
                    sin_value_denominator = randint(2, 10)
                    sin_value_numerator = randint(1, sin_value_denominator - 1)
                    sin_value = sy.Rational(sin_value_numerator, sin_value_denominator)
                    latex_problem = f"\\( \\sin \\theta = {sy.latex(sin_value)} \\)のとき、"\
                        f"\\( \\cos \\theta \\)と\\( \\tan \\theta \\)の値を求めよ。\\( (0 \\leqq \\theta \\leqq {sy.latex(sy.pi / 2)}) \\)"
                    cos_square_value = 1 - sin_value ** 2
                    cos_value = sy.sqrt(cos_square_value)
                    tan_value = sin_value / cos_value
                    latex_answer = f"\\( \\sin^2 \\theta + \\cos^2 \\theta = 1\\)より、\n"\
                        "\\( \\cos^2 \\theta = 1 - \\sin^2 \\theta \\)"\
                        f"\\( = 1 - ({sy.latex(sin_value)})^2 = {sy.latex(cos_square_value)}\\) \n"\
                        f"今、\\( \\theta \\)の定義域は\\( 0 \\leqq \\theta \\leqq {sy.latex(sy.pi / 2)} \\)であるため、"\
                        "\\( 0 \\leqq \\cos \\theta \\leqq 1 \\)が常に成り立つ。\n"\
                        f"よって、\\( \\cos \\theta = {sy.latex(cos_value)} \\)\n"\
                        "また、\\( \\tan \\theta = \\frac{\\sin \\theta}{\\cos \\theta}\\)より、\n"\
                        f"\\( \\tan \\theta = \\frac{{{sy.latex(sin_value)}}}{{{sy.latex(cos_value)}}} = {sy.latex(tan_value)} \\)"
                # 0 <= sin <= 1, -1 <= cos <= 0, -oo <= tan <= 0
                elif radian_range == "from_pi_over_2_up_to_pi":
                    sin_value_denominator = randint(2, 10)
                    sin_value_numerator = randint(1, sin_value_denominator - 1)
                    sin_value = sy.Rational(sin_value_numerator, sin_value_denominator)
                    latex_problem = f"\\( \\sin \\theta = {sy.latex(sin_value)} \\)のとき、"\
                        f"\\( \\cos \\theta \\)と\\( \\tan \\theta \\)の値を求めよ。\\( ({sy.latex(sy.pi / 2)} \\leqq \\theta \\leqq {sy.latex(sy.pi)}) \\)"
                    cos_square_value = 1 - sin_value ** 2
                    cos_value = -sy.sqrt(cos_square_value)
                    tan_value = sin_value / cos_value
                    latex_answer = f"\\( \\sin^2 \\theta + \\cos^2 \\theta = 1\\)より、\n"\
                        "\\( \\cos^2 \\theta = 1 - \\sin^2 \\theta \\)"\
                        f"\\( = 1 - ({sy.latex(sin_value)})^2 = {sy.latex(cos_square_value)}\\) \n"\
                        f"今、\\( \\theta \\)の定義域は\\( {sy.latex(sy.pi / 2)} \\leqq \\theta \\leqq {sy.latex(sy.pi)} \\)であるため、"\
                        "\\( -1 \\leqq \\cos \\theta \\leqq 0 \\)が常に成り立つ。\n"\
                        f"よって、\\( \\cos \\theta = {sy.latex(cos_value)} \\)\n"\
                        "また、\\( \\tan \\theta = \\frac{\\sin \\theta}{\\cos \\theta}\\)より、\n"\
                        f"\\( \\tan \\theta = \\frac{{{sy.latex(sin_value)}}}{{{sy.latex(cos_value)}}} = {sy.latex(tan_value)} \\)"
                # -1 <= sin <= 0, -1 <= cos <= 0, 0 <= tan < oo
                elif radian_range == "from_pi_up_to_3pi_over_2":
                    sin_value_denominator = randint(2, 10)
                    sin_value_numerator = randint(1, sin_value_denominator - 1)
                    sin_value = -sy.Rational(sin_value_numerator, sin_value_denominator)
                    latex_problem = f"\\( \\sin \\theta = {sy.latex(sin_value)} \\)のとき、"\
                        f"\\( \\cos \\theta \\)と\\( \\tan \\theta \\)の値を求めよ。\\( ({sy.latex(sy.pi)} \\leqq \\theta \\leqq {sy.latex(3 * sy.pi / 2)}) \\)"
                    cos_square_value = 1 - sin_value ** 2
                    cos_value = -sy.sqrt(cos_square_value)
                    tan_value = sin_value / cos_value
                    latex_answer = f"\\( \\sin^2 \\theta + \\cos^2 \\theta = 1\\)より、\n"\
                        "\\( \\cos^2 \\theta = 1 - \\sin^2 \\theta \\)"\
                        f"\\( = 1 - ({sy.latex(sin_value)})^2 = {sy.latex(cos_square_value)}\\) \n"\
                        f"今、\\( \\theta \\)の定義域は\\( {sy.latex(sy.pi)} \\leqq \\theta \\leqq {sy.latex(3 * sy.pi / 2)} \\)であるため、"\
                        "\\( -1 \\leqq \\cos \\theta \\leqq 0 \\)が常に成り立つ。\n"\
                        f"よって、\\( \\cos \\theta = {sy.latex(cos_value)} \\)\n"\
                        "また、\\( \\tan \\theta = \\frac{\\sin \\theta}{\\cos \\theta}\\)より、\n"\
                        f"\\( \\tan \\theta = \\frac{{{sy.latex(sin_value)}}}{{{sy.latex(cos_value)}}} = {sy.latex(tan_value)} \\)"
                # -1 <= sin <= 0, 0 <= cos <= 1, -oo < tan < 0
                elif radian_range == "from_3pi_over_2_up_to_2pi":
                    sin_value_denominator = randint(2, 10)
                    sin_value_numerator = randint(1, sin_value_denominator - 1)
                    sin_value = -sy.Rational(sin_value_numerator, sin_value_denominator)
                    latex_problem = f"\\( \\sin \\theta = {sy.latex(sin_value)} \\)のとき、"\
                        f"\\( \\cos \\theta \\)と\\( \\tan \\theta \\)の値を求めよ。\\( ({sy.latex(3 * sy.pi / 2)} \\leqq \\theta < {sy.latex(2 * sy.pi)}) \\)"
                    cos_square_value = 1 - sin_value ** 2
                    cos_value = sy.sqrt(cos_square_value)
                    tan_value = sin_value / cos_value
                    latex_answer = f"\\( \\sin^2 \\theta + \\cos^2 \\theta = 1\\)より、\n"\
                        "\\( \\cos^2 \\theta = 1 - \\sin^2 \\theta \\)"\
                        f"\\( = 1 - ({sy.latex(sin_value)})^2 = {sy.latex(cos_square_value)}\\) \n"\
                        f"今、\\( \\theta \\)の定義域は\\( {sy.latex(3 * sy.pi / 2)} \\leqq \\theta < {sy.latex(2 * sy.pi)} \\)であるため、"\
                        "\\( 0 \\leqq \\cos \\theta \\leqq 1 \\)が常に成り立つ。\n"\
                        f"よって、\\( \\cos \\theta = {sy.latex(cos_value)} \\)\n"\
                        "また、\\( \\tan \\theta = \\frac{\\sin \\theta}{\\cos \\theta}\\)より、\n"\
                        f"\\( \\tan \\theta = \\frac{{{sy.latex(sin_value)}}}{{{sy.latex(cos_value)}}} = {sy.latex(tan_value)} \\)"  
                # step by over pi
                # 0 <= sin <= 1, -1 <= cos <= 1, -oo < tan < oo
                elif radian_range == "from_zero_up_to_pi":
                    sin_value_denominator = randint(2, 10)
                    sin_value_numerator = randint(1, sin_value_denominator - 1)
                    sin_value = sy.Rational(sin_value_numerator, sin_value_denominator)
                    latex_problem = f"\\( \\sin \\theta = {sy.latex(sin_value)} \\)のとき、"\
                        f"\\( \\cos \\theta \\)と\\( \\tan \\theta \\)の値を求めよ。\\( (0 \\leqq \\theta \\leqq {sy.latex(sy.pi)}) \\)"
                    cos_square_value = 1 - sin_value ** 2
                    cos_value1 = sy.sqrt(cos_square_value)
                    cos_value2 = -sy.sqrt(cos_square_value)
                    tan_value1 = sin_value / cos_value1
                    tan_value2 = sin_value / cos_value2
                    latex_answer = f"\\( \\sin^2 \\theta + \\cos^2 \\theta = 1\\)より、\n"\
                        "\\( \\cos^2 \\theta = 1 - \\sin^2 \\theta \\)"\
                        f"\\( = 1 - ({sy.latex(sin_value)})^2 = {sy.latex(cos_square_value)}\\) \n"\
                        f"今、\\( \\theta \\) の定義域は\\( 0 \\leqq \\theta \\leqq {sy.latex(sy.pi)} \\)であるため、"\
                        "\\( \\cos \\theta \\)には正の場合と負の場合の両方が存在する。\n"\
                        f"よって、\\( \\cos \\theta = \\pm {sy.latex(cos_value1)} \\)\n"\
                        "また、\\( \\tan \\theta = \\frac{\\sin \\theta}{\\cos \\theta}\\)より、\n"\
                        f"\\( \\tan \\theta = \\frac{{{sy.latex(sin_value)}}}{{\\pm{sy.latex(cos_value1)}}} = \\pm {sy.latex(tan_value1)} \\)"
                # -1 <= sin <= 1, -1 <= cos <= 0, -oo < tan < oo
                elif radian_range == "from_pi_over_2_up_to_3pi_over_2":
                    sin_value_denominator = randint(2, 10)
                    sin_value_numerator = randint(1, sin_value_denominator - 1)
                    sin_value = sy.Rational(sin_value_numerator, sin_value_denominator)
                    if random() > 0.5:
                        sin_value *= -1
                    latex_problem = f"\\( \\sin \\theta = {sy.latex(sin_value)} \\)のとき、"\
                        f"\\( \\cos \\theta \\)と\\( \\tan \\theta \\)の値を求めよ。\\( {sy.latex(sy.pi / 2)} \\leqq \\theta \\leqq {sy.latex(3 * sy.pi / 2)}) \\)"
                    cos_square_value = 1 - sin_value ** 2
                    cos_value = -sy.sqrt(cos_square_value)
                    tan_value = sin_value / cos_value
                    latex_answer = f"\\( \\sin^2 \\theta + \\cos^2 \\theta = 1\\)より、\n"\
                        "\\( \\cos^2 \\theta = 1 - \\sin^2 \\theta \\)"\
                        f"\\( = 1 - ({sy.latex(sin_value)})^2 = {sy.latex(cos_square_value)}\\) \n"\
                        f"今、\\( \\theta \\) の定義域は\\( {sy.latex(sy.pi / 2)} \\leqq \\theta \\leqq {sy.latex(3 * sy.pi / 2)} \\)であるため、"\
                        "\\( -1 \\leqq \\cos \\theta \\leqq 0 \\)が常に成り立つ。\n"\
                        f"よって、\\( \\cos \\theta = {sy.latex(cos_value)} \\)\n"\
                        "また、\\( \\tan \\theta = \\frac{\\sin \\theta}{\\cos \\theta}\\)より、\n"\
                        f"\\( \\tan \\theta = \\frac{{{sy.latex(sin_value)}}}{{{sy.latex(cos_value)}}} = {sy.latex(tan_value)} \\)"
                # -1 <= sin <= 0, -1 <= cos < 1, -oo < tan < oo
                elif radian_range == "from_pi_up_to_2pi":
                    sin_value_denominator = randint(2, 10)
                    sin_value_numerator = randint(1, sin_value_denominator - 1)
                    sin_value = -sy.Rational(sin_value_numerator, sin_value_denominator)
                    latex_problem = f"\\( \\sin \\theta = {sy.latex(sin_value)} \\)のとき、"\
                        f"\\( \\cos \\theta \\)と\\( \\tan \\theta \\)の値を求めよ。\\( {sy.latex(sy.pi)} \\leqq \\theta < {sy.latex(2 * sy.pi)}) \\)"
                    cos_square_value = 1 - sin_value ** 2
                    cos_value1 = sy.sqrt(cos_square_value)
                    cos_value2 = -sy.sqrt(cos_square_value)
                    tan_value1 = sin_value / cos_value1
                    tan_value2 = sin_value / cos_value2
                    latex_answer = f"\\( \\sin^2 \\theta + \\cos^2 \\theta = 1\\)より、\n"\
                        "\\( \\cos^2 \\theta = 1 - \\sin^2 \\theta \\)"\
                        f"\\( = 1 - ({sy.latex(sin_value)})^2 = {sy.latex(cos_square_value)}\\) \n"\
                        f"今、\\( \\theta \\) の定義域は\\( {sy.latex(sy.pi)} \\leqq \\theta < {sy.latex(2 * sy.pi)} \\)であるため、"\
                        "\\( \\cos \\theta \\)には正の場合と負の場合の両方が存在する。\n"\
                        f"よって、\\( \\cos \\theta = \\pm {sy.latex(cos_value1)} \\)\n"\
                        "また、\\( \\tan \\theta = \\frac{\\sin \\theta}{\\cos \\theta}\\)より、\n"\
                        f"\\( \\tan \\theta = \\frac{{{sy.latex(sin_value)}}}{{\\pm {sy.latex(cos_value1)}}} = \\pm {sy.latex(tan_value2)} \\)"
                # step by 3 * pi /2
                # -1 <= sin <= 1, -1 <= cos <= 1, -oo < tan < oo
                elif radian_range == "from_zero_up_to_3pi_over_2":
                    sin_value_denominator = randint(2, 10)
                    sin_value_numerator = randint(1, sin_value_denominator - 1)
                    sin_value = sy.Rational(sin_value_numerator, sin_value_denominator)
                    if random() > 0.5:
                        sin_value *= -1
                    latex_problem = f"\\( \\sin \\theta = {sy.latex(sin_value)} \\)のとき、"\
                        f"\\( \\cos \\theta \\)と\\( \\tan \\theta \\)の値を求めよ。\\( 0 \\leqq \\theta \\leqq {sy.latex(3 * sy.pi / 2)}) \\)"
                    # 0 <= sin <= 1, -1 <= cos <= 1, -oo < tan < oo(same as 0 <= theta <= pi)
                    if sin_value > 0:
                        cos_square_value = 1 - sin_value ** 2
                        cos_value1 = sy.sqrt(cos_square_value)
                        cos_value2 = -sy.sqrt(cos_square_value)
                        tan_value1 = sin_value / cos_value1
                        tan_value2 = sin_value / cos_value2
                        latex_answer = f"\\( \\sin^2 \\theta + \\cos^2 \\theta = 1\\)より、\n"\
                            "\\( \\cos^2 \\theta = 1 - \\sin^2 \\theta \\)"\
                            f"\\( = 1 - ({sy.latex(sin_value)})^2 = {sy.latex(cos_square_value)}\\) \n"\
                            f"今、\\( \\theta \\) の定義域は\\( 0 \\leqq \\theta \\leqq {sy.latex(3 * sy.pi / 2)} \\)である。"\
                            f"この範囲で\\( \\sin \\theta > 0 \\)となるのは、\\( 0 < \\theta < {sy.latex(sy.pi)} \\)である。\n"\
                            "そのため、\\( \\cos \\theta \\)には正の場合と負の場合の両方が存在する。\n"\
                            f"よって、\\( \\cos \\theta = \\pm {sy.latex(cos_value1)} \\)\n"\
                            "また、\\( \\tan \\theta = \\frac{\\sin \\theta}{\\cos \\theta}\\)より、\n"\
                            f"\\( \\tan \\theta = \\frac{{{sy.latex(sin_value)}}}{{\\pm {sy.latex(cos_value1)}}} = \\pm {sy.latex(tan_value1)}\\)"
                    # -1 <= sin <= 0, -1 <= cos <= 0, tan >= 0 (same as pi <= theta <= 3 pi / 2)
                    else:
                        cos_square_value = 1 - sin_value ** 2
                        cos_value = -sy.sqrt(cos_square_value)
                        tan_value = sin_value / cos_value
                        latex_answer = f"\\( \\sin^2 \\theta + \\cos^2 \\theta = 1\\)より、\n"\
                            "\\( \\cos^2 \\theta = 1 - \\sin^2 \\theta \\)"\
                            f"\\( = 1 - ({sy.latex(sin_value)})^2 = {sy.latex(cos_square_value)}\\) \n"\
                            f"今、\\( \\theta \\) の定義域は\\( 0 \\leqq \\theta \\leqq {sy.latex(3 * sy.pi / 2)} \\)である。"\
                            f"この範囲で\\( \\sin \\theta < 0 \\)となるのは、\\( {sy.latex(sy.pi)} < \\theta \\leqq {sy.latex(3 * sy.pi / 2)} \\)である。\n"\
                            "そのため、\\( -1 < \\cos \\theta \\leqq 0 \\)が常に成り立つ。\n"\
                            f"よって、\\( \\cos \\theta = {sy.latex(cos_value)} \\)\n"\
                            "また、\\( \\tan \\theta = \\frac{\\sin \\theta}{\\cos \\theta}\\)より、\n"\
                            f"\\( \\tan \\theta = \\frac{{{sy.latex(sin_value)}}}{{{sy.latex(cos_value)}}} = {sy.latex(tan_value)} \\)"
                # -1 <= sin <= 1, -1 <= cos < 1, -oo < tan < oo
                elif radian_range == "from_pi_over_2_up_to_2pi":
                    sin_value_denominator = randint(2, 10)
                    sin_value_numerator = randint(1, sin_value_denominator - 1)
                    sin_value = sy.Rational(sin_value_numerator, sin_value_denominator)
                    if random() > 0.5:
                        sin_value *= -1
                    latex_problem = f"\\( \\sin \\theta = {sy.latex(sin_value)} \\)のとき、"\
                        f"\\( \\cos \\theta \\)と\\( \\tan \\theta \\)の値を求めよ。\\( {sy.latex(sy.pi / 2)} \\leqq \\theta < {sy.latex(2 * sy.pi)}) \\)"
                    # 0 <= sin <= 1, -1 <= cos <= 0, tan < 0 (same as pi / 2 <= theta <= pi)
                    if sin_value > 0:
                        cos_square_value = 1 - sin_value ** 2
                        cos_value1 = sy.sqrt(cos_square_value)
                        cos_value2 = -sy.sqrt(cos_square_value)
                        tan_value1 = sin_value / cos_value1
                        tan_value2 = sin_value / cos_value2
                        latex_answer = f"\\( \\sin^2 \\theta + \\cos^2 \\theta = 1\\)より、\n"\
                            "\\( \\cos^2 \\theta = 1 - \\sin^2 \\theta \\)"\
                            f"\\( = 1 - ({sy.latex(sin_value)})^2 = {sy.latex(cos_square_value)}\\) \n"\
                            f"今、\\( \\theta \\) の定義域は\\( 0 \\leqq \\theta \\leqq {sy.latex(3 * sy.pi / 2)} \\)である。"\
                            f"この範囲で\\( \\sin \\theta > 0 \\)となるのは、\\( 0 < \\theta < {sy.latex(sy.pi)} \\)である。\n"\
                            "そのため、\\( \\cos \\theta \\)には正の場合と負の場合の両方が存在する。\n"\
                            f"よって、\\( \\cos \\theta = \\pm {sy.latex(cos_value1)} \\)\n"\
                            "また、\\( \\tan \\theta = \\frac{\\sin \\theta}{\\cos \\theta}\\)より、\n"\
                            f"\\( \\tan \\theta = \\frac{{{sy.latex(sin_value)}}}{{\\pm {sy.latex(cos_value1)}}} = \\pm {sy.latex(tan_value1)} \\)"
                    # -1 <= sin <= 0, -1 <= cos <1 , tan >= 0 (same as pi <= theta < 2 * pi)
                    else:
                        cos_square_value = 1 - sin_value ** 2
                        cos_value1 = sy.sqrt(cos_square_value)
                        cos_value2 = -sy.sqrt(cos_square_value)
                        tan_value1 = sin_value / cos_value1
                        tan_value2 = sin_value / cos_value2
                        latex_answer = f"\\( \\sin^2 \\theta + \\cos^2 \\theta = 1\\)より、\n"\
                            "\\( \\cos^2 \\theta = 1 - \\sin^2 \\theta \\)"\
                            f"\\( = 1 - ({sy.latex(sin_value)})^2 = {sy.latex(cos_square_value)}\\) \n"\
                            f"今、\\( \\theta \\) の定義域は\\( 0 \\leqq \\theta \\leqq {sy.latex(3 * sy.pi / 2)} \\)である。"\
                            f"この範囲で\\( \\sin \\theta < 0 \\)となるのは、\\( {sy.latex(sy.pi)} < \\theta < {sy.latex(2 * sy.pi)} \\)である。\n"\
                            "そのため、\\( \\cos \\theta \\)には正の場合と負の場合の両方が存在する。\n"\
                            f"よって、\\( \\cos \\theta = \\pm {sy.latex(cos_value1)} \\)\n"\
                            "また、\\( \\tan \\theta = \\frac{\\sin \\theta}{\\cos \\theta}\\)より、\n"\
                            f"\\( \\tan \\theta = \\frac{{{sy.latex(sin_value)}}}{{\\pm {sy.latex(cos_value1)}}} = \\pm {sy.latex(tan_value2)} \\)"
                # step by 2 pi
                # -1 <= sin <= 0, -1 <= cos <= 1, -oo < tan < oo
                elif radian_range == "from_zero_up_to_2pi":
                    sin_value_denominator = randint(2, 10)
                    sin_value_numerator = randint(1, sin_value_denominator - 1)
                    sin_value = sy.Rational(sin_value_numerator, sin_value_denominator)
                    if random() > 0.5:
                        sin_value *= -1
                    latex_problem = f"\\( \\sin \\theta = {sy.latex(sin_value)} \\)のとき、"\
                        f"\\( \\cos \\theta \\)と\\( \\tan \\theta \\)の値を求めよ。\\( 0 \\leqq \\theta < {sy.latex(2 * sy.pi)}) \\)"
                    # 0 <= sin <= 1, -1 <= cos <= 1, -oo < tan < oo
                    if sin_value > 0:
                        cos_square_value = 1 - sin_value ** 2
                        cos_value1 = sy.sqrt(cos_square_value)
                        cos_value2 = -sy.sqrt(cos_square_value)
                        tan_value1 = sin_value / cos_value1
                        tan_value2 = sin_value / cos_value2
                        latex_answer = f"\\( \\sin^2 \\theta + \\cos^2 \\theta = 1\\)より、\n"\
                            "\\( \\cos^2 \\theta = 1 - \\sin^2 \\theta \\)"\
                            f"\\( = 1 - ({sy.latex(sin_value)})^2 = {sy.latex(cos_square_value)}\\) \n"\
                            f"今、\\( \\theta \\) の定義域は\\( 0 \\leqq \\theta < {sy.latex(2 * sy.pi)} \\)である。"\
                            f"この範囲で\\( \\sin \\theta > 0 \\)となるのは、\\( 0 < \\theta < {sy.latex(sy.pi)} \\)である。\n"\
                            "そのため、\\( \\cos \\theta \\)には正の場合と負の場合の両方が存在する。\n"\
                            f"よって、\\( \\cos \\theta = \\pm {sy.latex(cos_value1)} \\)\n"\
                            "また、\\( \\tan \\theta = \\frac{\\sin \\theta}{\\cos \\theta}\\)より、\n"\
                            f"\\( \\tan \\theta = \\frac{{{sy.latex(sin_value)}}}{{\\pm {sy.latex(cos_value1)}}} = \\pm {sy.latex(tan_value1)} \\)"
                    # -1 <= sin <= 0, -1 <= cos <= 1, -oo < tan < oo
                    else:
                        cos_square_value = 1 - sin_value ** 2
                        cos_value1 = sy.sqrt(cos_square_value)
                        cos_value2 = -sy.sqrt(cos_square_value)
                        tan_value1 = sin_value / cos_value1
                        tan_value2 = sin_value / cos_value2
                        latex_answer = f"\\( \\sin^2 \\theta + \\cos^2 \\theta = 1\\)より、\n"\
                            "\\( \\cos^2 \\theta = 1 - \\sin^2 \\theta \\)"\
                            f"\\( = 1 - ({sy.latex(sin_value)})^2 = {sy.latex(cos_square_value)}\\) \n"\
                            f"今、\\( \\theta \\) の定義域は\\( 0 \\leqq \\theta < {sy.latex(2 * sy.pi)} \\)である。"\
                            f"この範囲で\\( \\sin \\theta < 0 \\)となるのは、\\( {sy.latex(sy.pi)} < \\theta < {sy.latex(2 * sy.pi)} \\)である。\n"\
                            "そのため、\\( \\cos \\theta \\)には正の場合と負の場合の両方が存在する。\n"\
                            f"よって、\\( \\cos \\theta = \\pm {sy.latex(cos_value1)} \\)\n"\
                            "また、\\( \\tan \\theta = \\frac{\\sin \\theta}{\\cos \\theta}\\)より、\n"\
                            f"\\( \\tan \\theta = \\frac{{{sy.latex(sin_value)}}}{{\\pm {sy.latex(cos_value1)}}} = \\pm {sy.latex(tan_value2)} \\)"
            elif start_trigonometric_function == "cos":
                # step by pi over 2
                # 0 <= sin <= 1, 0 <= cos <= 1, 0 <= tan <= 1
                if radian_range == "from_zero_up_to_pi_over_2":
                    cos_value_denominator = randint(2, 10)
                    cos_value_numerator = randint(1, cos_value_denominator - 1)
                    cos_value = sy.Rational(cos_value_numerator, cos_value_denominator)
                    latex_problem = f"\\( \\cos \\theta = {sy.latex(cos_value)} \\)のとき、"\
                        f"\\( \\sin \\theta \\)と\\( \\tan \\theta \\)の値を求めよ。\\( (0 \\leqq \\theta \\leqq {sy.latex(sy.pi / 2)}) \\)"
                    sin_square_value = 1 - cos_value ** 2
                    sin_value = sy.sqrt(sin_square_value)
                    tan_value = sin_value / cos_value
                    latex_answer = f"\\( \\sin^2 \\theta + \\cos^2 \\theta = 1\\)より、\n"\
                        "\\( \\sin^2 \\theta = 1 - \\cos^2 \\theta \\)"\
                        f"\\( = 1 - ({sy.latex(cos_value)})^2 = {sy.latex(sin_square_value)}\\) \n"\
                        f"今、\\( \\theta \\)の定義域は\\( 0 \\leqq \\theta \\leqq {sy.latex(sy.pi / 2)} \\)であるため、"\
                        "\\( 0 \\leqq \\sin \\theta \\leqq 1 \\)が常に成り立つ。\n"\
                        f"よって、\\( \\sin \\theta = {sy.latex(sin_value)} \\)\n"\
                        "また、\\( \\tan \\theta = \\frac{\\sin \\theta}{\\cos \\theta}\\)より、\n"\
                        f"\\( \\tan \\theta = \\frac{{{sy.latex(sin_value)}}}{{{sy.latex(cos_value)}}} = {sy.latex(tan_value)} \\)"
                # 0 <= sin <= 1, -1 <= cos <= 0, -oo <= tan <= 0
                elif radian_range == "from_pi_over_2_up_to_pi":
                    cos_value_denominator = randint(2, 10)
                    cos_value_numerator = randint(1, cos_value_denominator - 1)
                    cos_value = -sy.Rational(cos_value_numerator, cos_value_denominator)
                    latex_problem = f"\\( \\cos \\theta = {sy.latex(cos_value)} \\)のとき、"\
                        f"\\( \\sin \\theta \\)と\\( \\tan \\theta \\)の値を求めよ。\\( ({sy.latex(sy.pi / 2)} \\leqq \\theta \\leqq {sy.latex(sy.pi)}) \\)"
                    sin_square_value = 1 - cos_value ** 2
                    sin_value = sy.sqrt(sin_square_value)
                    tan_value = sin_value / cos_value
                    latex_answer = f"\\( \\sin^2 \\theta + \\cos^2 \\theta = 1\\)より、\n"\
                        "\\( \\sin^2 \\theta = 1 - \\cos^2 \\theta \\)"\
                        f"\\( = 1 - ({sy.latex(cos_value)})^2 = {sy.latex(sin_square_value)}\\) \n"\
                        f"今、\\( \\theta \\)の定義域は\\( {sy.latex(sy.pi / 2)} \\leqq \\theta \\leqq {sy.latex(sy.pi)} \\)であるため、"\
                        "\\( 0 \\leqq \\sin \\theta \\leqq 1 \\)が常に成り立つ。\n"\
                        f"よって、\\( \\sin \\theta = {sy.latex(sin_value)} \\)\n"\
                        "また、\\( \\tan \\theta = \\frac{\\sin \\theta}{\\cos \\theta}\\)より、\n"\
                        f"\\( \\tan \\theta = \\frac{{{sy.latex(sin_value)}}}{{{sy.latex(cos_value)}}} = {sy.latex(tan_value)} \\)"
                # -1 <= sin <= 0, -1 <= cos <= 0, 0 <= tan < oo
                elif radian_range == "from_pi_up_to_3pi_over_2":
                    cos_value_denominator = randint(2, 10)
                    cos_value_numerator = randint(1, cos_value_denominator - 1)
                    cos_value = -sy.Rational(cos_value_numerator, cos_value_denominator)
                    latex_problem = f"\\( \\cos \\theta = {sy.latex(cos_value)} \\)のとき、"\
                        f"\\( \\sin \\theta \\)と\\( \\tan \\theta \\)の値を求めよ。\\( ({sy.latex(sy.pi)} \\leqq \\theta \\leqq {sy.latex(3 * sy.pi / 2)}) \\)"
                    sin_square_value = 1 - cos_value ** 2
                    sin_value = -sy.sqrt(sin_square_value)
                    tan_value = sin_value / cos_value
                    latex_answer = f"\\( \\sin^2 \\theta + \\cos^2 \\theta = 1\\)より、\n"\
                        "\\( \\sin^2 \\theta = 1 - \\cos^2 \\theta \\)"\
                        f"\\( = 1 - ({sy.latex(cos_value)})^2 = {sy.latex(sin_square_value)}\\) \n"\
                        f"今、\\( \\theta \\)の定義域は\\( {sy.latex(sy.pi)} \\leqq \\theta \\leqq {sy.latex(3 * sy.pi / 2)} \\)であるため、"\
                        "\\( -1 \\leqq \\sin \\theta \\leqq 0 \\)が常に成り立つ。\n"\
                        f"よって、\\( \\sin \\theta = {sy.latex(sin_value)} \\)\n"\
                        "また、\\( \\tan \\theta = \\frac{\\sin \\theta}{\\cos \\theta}\\)より、\n"\
                        f"\\( \\tan \\theta = \\frac{{{sy.latex(sin_value)}}}{{{sy.latex(cos_value)}}} = {sy.latex(tan_value)} \\)"
                # -1 <= sin <= 0, 0 <= cos <= 1, -oo < tan < 0
                elif radian_range == "from_3pi_over_2_up_to_2pi":
                    cos_value_denominator = randint(2, 10)
                    cos_value_numerator = randint(1, cos_value_denominator - 1)
                    cos_value = sy.Rational(cos_value_numerator, cos_value_denominator)
                    latex_problem = f"\\( \\cos \\theta = {sy.latex(cos_value)} \\)のとき、"\
                        f"\\( \\sin \\theta \\)と\\( \\tan \\theta \\)の値を求めよ。\\( ({sy.latex(3 * sy.pi / 2)} \\leqq \\theta < {sy.latex(2 * sy.pi)}) \\)"
                    sin_square_value = 1 - cos_value ** 2
                    sin_value = -sy.sqrt(sin_square_value)
                    tan_value = sin_value / cos_value
                    latex_answer = f"\\( \\sin^2 \\theta + \\cos^2 \\theta = 1\\)より、\n"\
                        "\\( \\sin^2 \\theta = 1 - \\cos^2 \\theta \\)"\
                        f"\\( = 1 - ({sy.latex(cos_value)})^2 = {sy.latex(sin_square_value)}\\) \n"\
                        f"今、\\( \\theta \\)の定義域は\\( {sy.latex(3 * sy.pi / 2)} \\leqq \\theta < {sy.latex(2 * sy.pi)} \\)であるため、"\
                        "\\( -1 \\leqq \\sin \\theta \\leqq 0 \\)が常に成り立つ。\n"\
                        f"よって、\\( \\sin \\theta = {sy.latex(sin_value)} \\)\n"\
                        "また、\\( \\tan \\theta = \\frac{\\sin \\theta}{\\cos \\theta}\\)より、\n"\
                        f"\\( \\tan \\theta = \\frac{{{sy.latex(sin_value)}}}{{{sy.latex(cos_value)}}} = {sy.latex(tan_value)} \\)"  
                # step by over pi
                # 0 <= sin <= 1, -1 <= cos <= 1, -oo < tan < oo
                elif radian_range == "from_zero_up_to_pi":
                    cos_value_denominator = randint(2, 10)
                    cos_value_numerator = randint(1, cos_value_denominator - 1)
                    cos_value = sy.Rational(cos_value_numerator, cos_value_denominator)
                    if random() > 0.5:
                        cos_value *= -1
                    latex_problem = f"\\( \\cos \\theta = {sy.latex(cos_value)} \\)のとき、"\
                        f"\\( \\sin \\theta \\)と\\( \\tan \\theta \\)の値を求めよ。\\( (0 \\leqq \\theta \\leqq {sy.latex(sy.pi)}) \\)"
                    sin_square_value = 1 - cos_value ** 2
                    sin_value = sy.sqrt(sin_square_value)
                    tan_value = sin_value / cos_value
                    latex_answer = f"\\( \\sin^2 \\theta + \\cos^2 \\theta = 1\\)より、\n"\
                        "\\( \\sin^2 \\theta = 1 - \\cos^2 \\theta \\)"\
                        f"\\( = 1 - ({sy.latex(cos_value)})^2 = {sy.latex(sin_square_value)}\\) \n"\
                        f"今、\\( \\theta \\) の定義域は\\( 0 \\leqq \\theta \\leqq {sy.latex(sy.pi)} \\)であるため、"\
                        "\\( 0 \\leqq \\sin \\theta \\leqq 1 \\)が常に成り立つ。\n"\
                        f"よって、\\( \\sin \\theta = {sy.latex(sin_value)} \\)\n"\
                        "また、\\( \\tan \\theta = \\frac{\\sin \\theta}{\\cos \\theta}\\)より、\n"\
                        f"\\( \\tan \\theta = \\frac{{{sy.latex(sin_value)}}}{{{sy.latex(cos_value)}}} = {sy.latex(tan_value)} \\)"
                # -1 <= sin <= 1, -1 <= cos <= 0, -oo < tan < oo
                elif radian_range == "from_pi_over_2_up_to_3pi_over_2":
                    cos_value_denominator = randint(2, 10)
                    cos_value_numerator = randint(1, cos_value_denominator - 1)
                    cos_value = -sy.Rational(cos_value_numerator, cos_value_denominator)
                    latex_problem = f"\\( \\cos \\theta = {sy.latex(cos_value)} \\)のとき、"\
                        f"\\( \\sin \\theta \\)と\\( \\tan \\theta \\)の値を求めよ。\\( {sy.latex(sy.pi / 2)} \\leqq \\theta \\leqq {sy.latex(3 * sy.pi / 2)}) \\)"
                    sin_square_value = 1 - cos_value ** 2
                    sin_value1 = sy.sqrt(sin_square_value)
                    sin_value2 = -sy.sqrt(sin_square_value)
                    tan_value1 = sin_value1 / cos_value
                    tan_value2 = sin_value2 / cos_value
                    latex_answer = f"\\( \\sin^2 \\theta + \\cos^2 \\theta = 1\\)より、\n"\
                        "\\( \\sin^2 \\theta = 1 - \\cos^2 \\theta \\)"\
                        f"\\( = 1 - ({sy.latex(cos_value)})^2 = {sy.latex(sin_square_value)}\\) \n"\
                        f"今、\\( \\theta \\) の定義域は\\( {sy.latex(sy.pi / 2)} \\leqq \\theta \\leqq {sy.latex(3 * sy.pi / 2)} \\)であるため、"\
                        "\\( \\sin \\theta \\)には正の場合と負の場合の両方が存在する。\n"\
                        f"よって、\\( \\sin \\theta = \\pm {sy.latex(sin_value1)} \\)\n"\
                        "また、\\( \\tan \\theta = \\frac{\\sin \\theta}{\\cos \\theta}\\)より、\n"\
                        f"\\( \\tan \\theta = \\frac{{\\pm {sy.latex(sin_value1)}}}{{{sy.latex(cos_value)}}} = \\pm {sy.latex(tan_value2)} \\)"
                # -1 <= sin <= 0, -1 <= cos < 1, -oo < tan < oo
                elif radian_range == "from_pi_up_to_2pi":
                    cos_value_denominator = randint(2, 10)
                    cos_value_numerator = randint(1, cos_value_denominator - 1)
                    cos_value = sy.Rational(cos_value_numerator, cos_value_denominator)
                    if random() > 0.5:
                        cos_value *= -1
                    latex_problem = f"\\( \\cos \\theta = {sy.latex(cos_value)} \\)のとき、"\
                        f"\\( \\sin \\theta \\)と\\( \\tan \\theta \\)の値を求めよ。\\( {sy.latex(sy.pi)} \\leqq \\theta < {sy.latex(2 * sy.pi)}) \\)"
                    sin_square_value = 1 - cos_value ** 2
                    sin_value = -sy.sqrt(sin_square_value)
                    tan_value = sin_value / cos_value
                    latex_answer = f"\\( \\sin^2 \\theta + \\cos^2 \\theta = 1\\)より、\n"\
                        "\\( \\sin^2 \\theta = 1 - \\cos^2 \\theta \\)"\
                        f"\\( = 1 - ({sy.latex(cos_value)})^2 = {sy.latex(sin_square_value)}\\) \n"\
                        f"今、\\( \\theta \\) の定義域は\\( {sy.latex(sy.pi)} \\leqq \\theta < {sy.latex(2 * sy.pi)} \\)であるため、"\
                        "\\( -1 \\leqq \\sin \\theta \\leqq 0 \\)が常に成り立つ。\n"\
                        f"よって、\\( \\sin \\theta = {sy.latex(sin_value)} \\)\n"\
                        "また、\\( \\tan \\theta = \\frac{\\sin \\theta}{\\cos \\theta}\\)より、\n"\
                        f"\\( \\tan \\theta = \\frac{{{sy.latex(sin_value)}}}{{{sy.latex(cos_value)}}} = {sy.latex(tan_value)} \\)"
                # step by 3 * pi /2
                # -1 <= sin <= 1, -1 <= cos <= 1, -oo < tan < oo
                elif radian_range == "from_zero_up_to_3pi_over_2":
                    cos_value_denominator = randint(2, 10)
                    cos_value_numerator = randint(1, cos_value_denominator - 1)
                    cos_value = sy.Rational(cos_value_numerator, cos_value_denominator)
                    if random() > 0.5:
                        cos_value *= -1
                    latex_problem = f"\\( \\cos \\theta = {sy.latex(cos_value)} \\)のとき、"\
                        f"\\( \\sin \\theta \\)と\\( \\tan \\theta \\)の値を求めよ。\\( 0 \\leqq \\theta \\leqq {sy.latex(3 * sy.pi / 2)}) \\)"
                    # 0 <= sin <= 1, 0 <= cos <= 1, 0 < tan (same as 0 <= theta <= pi / 2)
                    if cos_value > 0:
                        sin_square_value = 1 - cos_value ** 2
                        sin_value = sy.sqrt(sin_square_value)
                        tan_value = sin_value / cos_value
                        latex_answer = f"\\( \\sin^2 \\theta + \\cos^2 \\theta = 1\\)より、\n"\
                            "\\( \\sin^2 \\theta = 1 - \\cos^2 \\theta \\)"\
                            f"\\( = 1 - ({sy.latex(cos_value)})^2 = {sy.latex(sin_square_value)}\\) \n"\
                            f"今、\\( \\theta \\) の定義域は\\( 0 \\leqq \\theta \\leqq {sy.latex(3 * sy.pi / 2)} \\)である。"\
                            f"この範囲で\\( \\cos \\theta > 0 \\)となるのは、\\( 0 < \\theta < {sy.latex(sy.pi / 2)} \\)である。\n"\
                            "そのため、\\( 0 \\leqq \\sin \\theta \\leqq 1 \\)が常に成り立つ。\n"\
                            f"よって、\\( \\sin \\theta = {sy.latex(sin_value)} \\)\n"\
                            "また、\\( \\tan \\theta = \\frac{\\sin \\theta}{\\cos \\theta}\\)より、\n"\
                            f"\\( \\tan \\theta = \\frac{{{sy.latex(sin_value)}}}{{{sy.latex(cos_value)}}} = {sy.latex(tan_value)} \\)"
                    # -1 <= sin <= 1, -1 <= cos <= 0, tan >= 0 (same as pi / 2 <= theta <= 3 pi / 2)
                    else:
                        sin_square_value = 1 - cos_value ** 2
                        sin_value1 = sy.sqrt(sin_square_value)
                        sin_value2 = -sy.sqrt(sin_square_value)
                        tan_value1 = sin_value1 / cos_value
                        tan_value2 = sin_value2 / cos_value
                        latex_answer = f"\\( \\sin^2 \\theta + \\cos^2 \\theta = 1\\)より、\n"\
                            "\\( \\sin^2 \\theta = 1 - \\cos^2 \\theta \\)"\
                            f"\\( = 1 - ({sy.latex(cos_value)})^2 = {sy.latex(sin_square_value)}\\) \n"\
                            f"今、\\( \\theta \\) の定義域は\\( 0 \\leqq \\theta \\leqq {sy.latex(3 * sy.pi / 2)} \\)である。"\
                            f"この範囲で\\( \\cos \\theta < 0 \\)となるのは、\\( {sy.latex(sy.pi / 2)} < \\theta < {sy.latex(3 * sy.pi / 2)} \\)であるため、"\
                            "\\( \\sin \\theta \\)には正の場合と負の場合の両方が存在する。\n"\
                            f"よって、\\( \\sin \\theta = \\pm {sy.latex(sin_value1)} \\)\n"\
                            "また、\\( \\tan \\theta = \\frac{\\sin \\theta}{\\cos \\theta}\\)より、\n"\
                            f"\\( \\tan \\theta = \\frac{{\\pm {sy.latex(sin_value1)}}}{{{sy.latex(cos_value)}}} = \\pm {sy.latex(tan_value2)} \\)"
                # -1 <= sin <= 1, -1 <= cos < 1, -oo < tan < oo
                elif radian_range == "from_pi_over_2_up_to_2pi":
                    cos_value_denominator = randint(2, 10)
                    cos_value_numerator = randint(1, cos_value_denominator - 1)
                    cos_value = sy.Rational(cos_value_numerator, cos_value_denominator)
                    if random() > 0.5:
                        cos_value *= -1
                    latex_problem = f"\\( \\cos \\theta = {sy.latex(cos_value)} \\)のとき、"\
                        f"\\( \\sin \\theta \\)と\\( \\tan \\theta \\)の値を求めよ。\\( {sy.latex(sy.pi / 2)} \\leqq \\theta < {sy.latex(2 * sy.pi)}) \\)"
                    # -1 <= sin < 0, 0 <= cos < 1, tan < 0 (same as 3pi / 2 <= theta < 2pi)
                    if cos_value > 0:
                        sin_square_value = 1 - cos_value ** 2
                        sin_value = -sy.sqrt(sin_square_value)
                        tan_value = sin_value / cos_value
                        latex_answer = f"\\( \\sin^2 \\theta + \\cos^2 \\theta = 1\\)より、\n"\
                            "\\( \\sin^2 \\theta = 1 - \\cos^2 \\theta \\)"\
                            f"\\( = 1 - ({sy.latex(cos_value)})^2 = {sy.latex(sin_square_value)}\\) \n"\
                            f"今、\\( \\theta \\) の定義域は\\( 0 \\leqq \\theta \\leqq {sy.latex(3 * sy.pi / 2)} \\)である。"\
                            f"この範囲で\\( \\cos \\theta > 0 \\)となるのは、\\( {sy.latex(3 * sy.pi / 2)} \leqq \\theta < {sy.latex(2 * sy.pi)} \\)である。\n"\
                            "そのため、\\( \\sin \\theta < 0 \\)が常に成り立つ。\n"\
                            f"よって、\\( \\sin \\theta = {sy.latex(sin_value)} \\)\n"\
                            "また、\\( \\tan \\theta = \\frac{\\sin \\theta}{\\cos \\theta}\\)より、\n"\
                            f"\\( \\tan \\theta = \\frac{{{sy.latex(sin_value)}}}{{{sy.latex(cos_value)}}} = {sy.latex(tan_value)} \\)"
                    # -1 <= sin <= 1, -1 <= cos <= 0, -oo < tan < oo (same as pi / 2 <= theta < 3pi/2)
                    else:
                        sin_square_value = 1 - cos_value ** 2
                        sin_value1 = sy.sqrt(sin_square_value)
                        sin_value2 = -sy.sqrt(sin_square_value)
                        tan_value1 = sin_value1 / cos_value
                        tan_value2 = sin_value2 / cos_value
                        latex_answer = f"\\( \\sin^2 \\theta + \\cos^2 \\theta = 1\\)より、\n"\
                            "\\( \\sin^2 \\theta = 1 - \\cos^2 \\theta \\)"\
                            f"\\( = 1 - ({sy.latex(cos_value)})^2 = {sy.latex(sin_square_value)}\\) \n"\
                            f"今、\\( \\theta \\) の定義域は\\( 0 \\leqq \\theta \\leqq {sy.latex(3 * sy.pi / 2)} \\)である。"\
                            f"この範囲で\\( \\cos \\theta < 0 \\)となるのは、\\( {sy.latex(sy.pi / 2)} < \\theta < {sy.latex(3 * sy.pi / 2)} \\)である。\n"\
                            "そのため、\\( \\sin \\theta \\)には正の場合と負の場合の両方が存在する。\n"\
                            f"よって、\\( \\sin \\theta = \\pm {sy.latex(sin_value1)} \\)\n"\
                            "また、\\( \\tan \\theta = \\frac{\\sin \\theta}{\\cos \\theta}\\)より、\n"\
                            f"\\( \\tan \\theta = \\frac{{\\pm {sy.latex(sin_value1)}}}{{{sy.latex(cos_value)}}} = \\pm {sy.latex(tan_value2)} \\)"
                # step by 2 pi
                # -1 <= sin <= 1, -1 <= cos <= 1, -oo < tan < oo
                elif radian_range == "from_zero_up_to_2pi":
                    cos_value_denominator = randint(2, 10)
                    cos_value_numerator = randint(1, cos_value_denominator - 1)
                    cos_value = sy.Rational(cos_value_numerator, cos_value_denominator)
                    if random() > 0.5:
                        cos_value *= -1
                    latex_problem = f"\\( \\cos \\theta = {sy.latex(cos_value)} \\)のとき、"\
                        f"\\( \\sin \\theta \\)と\\( \\tan \\theta \\)の値を求めよ。\\( 0 \\leqq \\theta < {sy.latex(2 * sy.pi)}) \\)"
                    # -1 <= sin <= 1, 0 < cos <= 1, -oo < tan < oo (same as 0 < theta < pi / 2, 3pi / 2 < theta < 2pi)
                    if cos_value > 0:
                        sin_square_value = 1 - cos_value ** 2
                        sin_value1 = sy.sqrt(sin_square_value)
                        sin_value2 = -sy.sqrt(sin_square_value)
                        tan_value1 = sin_value1 / cos_value
                        tan_value2 = sin_value2 / cos_value
                        latex_answer = f"\\( \\sin^2 \\theta + \\cos^2 \\theta = 1\\)より、\n"\
                            "\\( \\sin^2 \\theta = 1 - \\cos^2 \\theta \\)"\
                            f"\\( = 1 - ({sy.latex(cos_value)})^2 = {sy.latex(sin_square_value)}\\) \n"\
                            f"今、\\( \\theta \\) の定義域は\\( 0 \\leqq \\theta < {sy.latex(2 * sy.pi)} \\)である。"\
                            f"この範囲で\\( \\cos \\theta > 0 \\)となるのは、\\( 0 < \\theta < {sy.latex(sy.pi / 2)}, {sy.latex(3 * sy.pi / 2)} < \\theta < {sy.latex(2 * sy.pi)} \\)である。\n"\
                            "そのため、\\( \\sin \\theta \\)には正の場合と負の場合の両方が存在する。\n"\
                            f"よって、\\( \\sin \\theta = \\pm {sy.latex(sin_value1)} \\)\n"\
                            "また、\\( \\tan \\theta = \\frac{\\sin \\theta}{\\cos \\theta}\\)より、\n"\
                            f"\\( \\tan \\theta = \\frac{{\\pm {sy.latex(sin_value1)}}}{{{sy.latex(cos_value)}}} = \\pm {sy.latex(tan_value1)} \\)"
                    # -1 <= sin <= 1, -1 <= cos < 0, -oo < tan < oo (same as pi / 2 < theta < 3pi / 2)
                    ####### next #######
                    else:
                        sin_square_value = 1 - cos_value ** 2
                        sin_value1 = sy.sqrt(sin_square_value)
                        sin_value2 = -sy.sqrt(sin_square_value)
                        tan_value1 = sin_value1 / cos_value
                        tan_value2 = sin_value2 / cos_value
                        latex_answer = f"\\( \\sin^2 \\theta + \\cos^2 \\theta = 1\\)より、\n"\
                            "\\( \\sin^2 \\theta = 1 - \\cos^2 \\theta \\)"\
                            f"\\( = 1 - ({sy.latex(cos_value)})^2 = {sy.latex(sin_square_value)}\\) \n"\
                            f"今、\\( \\theta \\) の定義域は\\( 0 \\leqq \\theta < {sy.latex(2 * sy.pi)} \\)である。"\
                            f"この範囲で\\( \\cos \\theta < 0 \\)となるのは、\\( {sy.latex(sy.pi / 2)} < \\theta < {sy.latex(3 * sy.pi / 2)} \\)である。\n"\
                            "そのため、\\( \\sin \\theta \\)には正の場合と負の場合の両方が存在する。\n"\
                            f"よって、\\( \\sin \\theta = \\pm {sy.latex(sin_value1)} \\)\n"\
                            "また、\\( \\tan \\theta = \\frac{\\sin \\theta}{\\cos \\theta}\\)より、\n"\
                            f"\\( \\tan \\theta = \\frac{{{sy.latex(sin_value1)}}}{{{sy.latex(cos_value)}}} = {sy.latex(tan_value1)} \\)\n"\
                            f"\\( \\tan \\theta = \\frac{{{sy.latex(sin_value2)}}}{{{sy.latex(cos_value)}}} = {sy.latex(tan_value2)} \\)\n"\
                            f"すなわち、\\( \\tan \\theta = \\pm {sy.latex(tan_value2)} \\)"
            elif start_trigonometric_function == "tan":
                # step by pi over 2
                # 0 <= sin <= 1, 0 <= cos <= 1, 0 <= tan 
                if radian_range == "from_zero_up_to_pi_over_2":
                    tan_value_denominator = randint(1, 6)
                    tan_value_numerator = randint(1, 3 * tan_value_denominator)
                    tan_value = sy.Rational(tan_value_numerator, tan_value_denominator)
                    latex_problem = f"\\( \\tan \\theta = {sy.latex(tan_value)} \\)のとき、"\
                        f"\\( \\sin \\theta \\)と\\( \\cos \\theta \\)の値を求めよ。\\( (0 \\leqq \\theta \\leqq {sy.latex(sy.pi / 2)}) \\)"
                    cos_square_value = 1 / (1 + tan_value ** 2)
                    cos_value = sy.sqrt(cos_square_value)
                    sin_value = tan_value * cos_value
                    latex_answer = "\\( 1 + \\tan^2 \\theta = \\frac{1}{\\cos^2 \\theta}\\)より、\n"\
                        "\\( \\cos^2 \\theta = \\frac{1}{1 + \\tan^2 \\theta} \\)"\
                        f"\\( = \\frac{{1}}{{1 + ({sy.latex(tan_value)})^2}} = {sy.latex(cos_square_value)}\\) \n"\
                        f"今、\\( \\theta \\)の定義域は\\( 0 \\leqq \\theta \\leqq {sy.latex(sy.pi / 2)} \\)であるため、"\
                        "\\( 0 \\leqq \\cos \\theta \\leqq 1 \\)が常に成り立つ。\n"\
                        f"よって、\\( \\cos \\theta = {sy.latex(cos_value)} \\)\n"\
                        "また、\\( \\tan \\theta = \\frac{\\sin \\theta}{\\cos \\theta} \\)より、\n"\
                        f"\\( \\sin \\theta = \\tan \\theta \\cos \\theta = {sy.latex(tan_value)} \\cdot {sy.latex(cos_value)}  = {sy.latex(sin_value)} \\)"
                # 0 <= sin <= 1, -1 <= cos <= 0, -oo <= tan <= 0
                elif radian_range == "from_pi_over_2_up_to_pi":
                    tan_value_denominator = randint(1, 6)
                    tan_value_numerator = randint(1, 3 * tan_value_denominator)
                    tan_value = -sy.Rational(tan_value_numerator, tan_value_denominator)
                    latex_problem = f"\\( \\tan \\theta = {sy.latex(tan_value)} \\)のとき、"\
                        f"\\( \\sin \\theta \\)と\\( \\cos \\theta \\)の値を求めよ。\\( ({sy.latex(sy.pi / 2)} \\leqq \\theta \\leqq {sy.latex(sy.pi)}) \\)"
                    cos_square_value = 1 / (1 + tan_value ** 2)
                    cos_value = -sy.sqrt(cos_square_value)
                    sin_value = tan_value * cos_value
                    latex_answer = "\\( 1 + \\tan^2 \\theta = \\frac{1}{\\cos^2 \\theta}\\)より、\n"\
                        "\\( \\cos^2 \\theta = \\frac{1}{1 + \\tan^2 \\theta} \\)"\
                        f"\\( = \\frac{{1}}{{1 + ({sy.latex(tan_value)})^2}} = {sy.latex(cos_square_value)}\\) \n"\
                        f"今、\\( \\theta \\)の定義域は\\( {sy.latex(sy.pi / 2)} \\leqq \\theta \\leqq {sy.latex(sy.pi)} \\)であるため、"\
                        "\\( -1 \\leqq \\cos \\theta \\leqq 0 \\)が常に成り立つ。\n"\
                        f"よって、\\( \\cos \\theta = {sy.latex(cos_value)} \\)\n"\
                        "また、\\( \\tan \\theta = \\frac{\\sin \\theta}{\\cos \\theta}\\)より、\n"\
                        f"\\( \\sin \\theta = \\tan \\theta \\cos \\theta = {sy.latex(tan_value)} \\cdot {sy.latex(cos_value)}  = {sy.latex(sin_value)} \\)"
                # -1 <= sin <= 0, -1 <= cos <= 0, 0 <= tan < oo
                elif radian_range == "from_pi_up_to_3pi_over_2":
                    tan_value_denominator = randint(1, 6)
                    tan_value_numerator = randint(1, 3 * tan_value_denominator)
                    tan_value = sy.Rational(tan_value_numerator, tan_value_denominator)
                    latex_problem = f"\\( \\tan \\theta = {sy.latex(tan_value)} \\)のとき、"\
                        f"\\( \\sin \\theta \\)と\\( \\cos \\theta \\)の値を求めよ。\\( ({sy.latex(sy.pi)} \\leqq \\theta \\leqq {sy.latex(3 * sy.pi / 2)}) \\)"
                    cos_square_value = 1 / (1 + tan_value ** 2)
                    cos_value = -sy.sqrt(cos_square_value)
                    sin_value = tan_value * cos_value
                    latex_answer = "\\( 1 + \\tan^2 \\theta = \\frac{1}{\\cos^2 \\theta}\\)より、\n"\
                        "\\( \\cos^2 \\theta = \\frac{1}{1 + \\tan^2 \\theta} \\)"\
                        f"\\( = \\frac{{1}}{{1 + ({sy.latex(tan_value)})^2}} = {sy.latex(cos_square_value)}\\) \n"\
                        f"今、\\( \\theta \\)の定義域は\\( {sy.latex(sy.pi)} \\leqq \\theta \\leqq {sy.latex(3 * sy.pi / 2)} \\)であるため、"\
                        "\\( -1 \\leqq \\cos \\theta \\leqq 0 \\)が常に成り立つ。\n"\
                        f"よって、\\( \\cos \\theta = {sy.latex(cos_value)} \\)\n"\
                        "また、\\( \\tan \\theta = \\frac{\\sin \\theta}{\\cos \\theta}\\)より、\n"\
                        f"\\( \\sin \\theta = \\tan \\theta \\cos \\theta = {sy.latex(tan_value)} \\cdot {sy.latex(cos_value)}  = {sy.latex(sin_value)} \\)"
                # -1 <= sin <= 0, 0 <= cos <= 1, tan < 0
                elif radian_range == "from_3pi_over_2_up_to_2pi":
                    tan_value_denominator = randint(1, 6)
                    tan_value_numerator = randint(1, 3 * tan_value_denominator)
                    tan_value = -sy.Rational(tan_value_numerator, tan_value_denominator)
                    latex_problem = f"\\( \\tan \\theta = {sy.latex(tan_value)} \\)のとき、"\
                        f"\\( \\sin \\theta \\)と\\( \\cos \\theta \\)の値を求めよ。\\( ({sy.latex(3 * sy.pi / 2)} \\leqq \\theta < {sy.latex(2 * sy.pi)}) \\)"
                    cos_square_value = 1 / (1 + tan_value ** 2)
                    cos_value = sy.sqrt(cos_square_value)
                    sin_value = tan_value * cos_value
                    latex_answer = "\\( 1 + \\tan^2 \\theta = \\frac{1}{\\cos^2 \\theta}\\)より、\n"\
                        "\\( \\cos^2 \\theta = \\frac{1}{1 + \\tan^2 \\theta} \\)"\
                        f"\\( = \\frac{{1}}{{1 + ({sy.latex(tan_value)})^2}} = {sy.latex(cos_square_value)}\\) \n"\
                        f"今、\\( \\theta \\)の定義域は\\( {sy.latex(3 * sy.pi / 2)} \\leqq \\theta < {sy.latex(2 * sy.pi)} \\)であるため、"\
                        "\\( 0 \\leqq \\cos \\theta < 1 \\)が常に成り立つ。\n"\
                        f"よって、\\( \\cos \\theta = {sy.latex(cos_value)} \\)\n"\
                        "また、\\( \\tan \\theta = \\frac{\\sin \\theta}{\\cos \\theta}\\)より、\n"\
                        f"\\( \\sin \\theta = \\tan \\theta \\cos \\theta = {sy.latex(tan_value)} \\cdot {sy.latex(cos_value)}  = {sy.latex(sin_value)} \\)"
                # step by over pi
                # 0 <= sin <= 1, -1 <= cos <= 1, -oo < tan < oo
                elif radian_range == "from_zero_up_to_pi":
                    tan_value_denominator = randint(1, 6)
                    tan_value_numerator = randint(1, 3 * tan_value_denominator)
                    tan_value = sy.Rational(tan_value_numerator, tan_value_denominator)
                    if random() > 0.5:
                        tan_value *= -1
                    latex_problem = f"\\( \\tan \\theta = {sy.latex(tan_value)} \\)のとき、"\
                        f"\\( \\sin \\theta \\)と\\( \\cos \\theta \\)の値を求めよ。\\( ({sy.latex(0)} \\leqq \\theta < {sy.latex(sy.pi)}) \\)"
                    cos_square_value = 1 / (1 + tan_value ** 2)
                    # 0 <= sin <= 1, 0 <= cos <= 1, tan > 0 (same as 0 <= theta <= pi / 2)
                    if tan_value > 0:
                        cos_value = sy.sqrt(cos_square_value)
                        sin_value = tan_value * cos_value
                        latex_answer = "\\( 1 + \\tan^2 \\theta = \\frac{1}{\\cos^2 \\theta}\\)より、\n"\
                            "\\( \\cos^2 \\theta = \\frac{1}{1 + \\tan^2 \\theta} \\)"\
                            f"\\( = \\frac{{1}}{{1 + ({sy.latex(tan_value)})^2}} = {sy.latex(cos_square_value)}\\) \n"\
                            f"今、\\( \\theta \\) の定義域は\\( {sy.latex(0)} \\leqq \\theta \\leqq {sy.latex(sy.pi)} \\)である。"\
                            f"この範囲で\\( \\tan \\theta > 0 \\)となるのは、\\( 0 < \\theta < {sy.latex(sy.pi / 2)} \\)である。\n"\
                            "そのため、\\( 0 < \\cos \\theta \\leqq 1 \\)が常に成り立つ。\n"\
                            f"よって、\\( \\cos \\theta = {sy.latex(cos_value)} \\)\n"\
                            "また、\\( \\tan \\theta = \\frac{\\sin \\theta}{\\cos \\theta}\\)より、\n"\
                            f"\\( \\sin \\theta = \\tan \\theta \\cos \\theta = {sy.latex(tan_value)} \\cdot {sy.latex(cos_value)}  = {sy.latex(sin_value)} \\)"
                    # 0 <= sin <= 1, -1 <= cos <= 0, tan < 0 (same as pi / 2 <= theta <= pi)
                    else:
                        cos_value = -sy.sqrt(cos_square_value)
                        sin_value = tan_value * cos_value
                        latex_answer = "\\( 1 + \\tan^2 \\theta = \\frac{1}{\\cos^2 \\theta}\\)より、\n"\
                            "\\( \\cos^2 \\theta = \\frac{1}{1 + \\tan^2 \\theta} \\)"\
                            f"\\( = \\frac{{1}}{{1 + ({sy.latex(tan_value)})^2}} = {sy.latex(cos_square_value)}\\) \n"\
                            f"今、\\( \\theta \\) の定義域は\\( {sy.latex(0)} \\leqq \\theta \\leqq {sy.latex(sy.pi)} \\)である。"\
                            f"この範囲で\\( \\tan \\theta < 0 \\)となるのは、\\( {sy.latex(sy.pi / 2)} < \\theta < {sy.latex(sy.pi)} \\)である。\n"\
                            "そのため、\\( -1 \\leqq \\cos \\theta < 0 \\)が常に成り立つ。\n"\
                            f"よって、\\( \\cos \\theta = {sy.latex(cos_value)} \\)\n"\
                            "また、\\( \\tan \\theta = \\frac{\\sin \\theta}{\\cos \\theta}\\)より、\n"\
                            f"\\( \\sin \\theta = \\tan \\theta \\cos \\theta = {sy.latex(tan_value)} \\cdot {sy.latex(cos_value)}  = {sy.latex(sin_value)} \\)"
                # -1 <= sin <= 1, -1 <= cos <= 0, -oo < tan < oo
                elif radian_range == "from_pi_over_2_up_to_3pi_over_2":
                    tan_value_denominator = randint(1, 6)
                    tan_value_numerator = randint(1, 3 * tan_value_denominator)
                    tan_value = sy.Rational(tan_value_numerator, tan_value_denominator)
                    if random() > 0.5:
                        tan_value *= -1
                    latex_problem = f"\\( \\tan \\theta = {sy.latex(tan_value)} \\)のとき、"\
                        f"\\( \\sin \\theta \\)と\\( \\cos \\theta \\)の値を求めよ。\\( ({sy.latex(sy.pi / 2)} \\leqq \\theta < {sy.latex(3 * sy.pi / 2)}) \\)"
                    cos_square_value = 1 / (1 + tan_value ** 2)
                    cos_value = sy.sqrt(cos_square_value)
                    sin_value = tan_value * cos_value
                    latex_answer = "\\( 1 + \\tan^2 \\theta = \\frac{1}{\\cos^2 \\theta}\\)より、\n"\
                        "\\( \\cos^2 \\theta = \\frac{1}{1 + \\tan^2 \\theta} \\)"\
                        f"\\( = \\frac{{1}}{{1 + ({sy.latex(tan_value)})^2}} = {sy.latex(cos_square_value)}\\) \n"\
                        f"今、\\( \\theta \\) の定義域は\\( {sy.latex(sy.pi / 2)} \\leqq \\theta \\leqq {sy.latex(3 * sy.pi / 2)} \\)であるため、"\
                        "\\( -1 \\leqq \\cos \\theta \\leqq 0 \\)が常に成り立つ。\n"\
                        f"よって、\\( \\cos \\theta = {sy.latex(cos_value)} \\)\n"\
                        "また、\\( \\tan \\theta = \\frac{\\sin \\theta}{\\cos \\theta}\\)より、\n"\
                        f"\\( \\sin \\theta = \\tan \\theta \\cos \\theta = {sy.latex(tan_value)} \\cdot {sy.latex(cos_value)}  = {sy.latex(sin_value)} \\)"
                # -1 <= sin <= 0, -1 <= cos < 1, -oo < tan < oo
                elif radian_range == "from_pi_up_to_2pi":
                    tan_value_denominator = randint(1, 6)
                    tan_value_numerator = randint(1, 3 * tan_value_denominator)
                    tan_value = sy.Rational(tan_value_numerator, tan_value_denominator)
                    if random() > 0.5:
                        tan_value *= -1
                    latex_problem = f"\\( \\tan \\theta = {sy.latex(tan_value)} \\)のとき、"\
                        f"\\( \\sin \\theta \\)と\\( \\cos \\theta \\)の値を求めよ。\\( ({sy.latex(sy.pi)} \\leqq \\theta < {sy.latex(2 * sy.pi)}) \\)"
                    cos_square_value = 1 / (1 + tan_value ** 2)
                    # -1 <= sin <= 0, -1 <= cos <= 0, tan > 0 (same as pi <= theta < 3pi / 2)
                    if tan_value > 0:
                        cos_value = -sy.sqrt(cos_square_value)
                        sin_value = tan_value * cos_value
                        latex_answer = "\\( 1 + \\tan^2 \\theta = \\frac{1}{\\cos^2 \\theta}\\)より、\n"\
                            "\\( \\cos^2 \\theta = \\frac{1}{1 + \\tan^2 \\theta} \\)"\
                            f"\\( = \\frac{{1}}{{1 + ({sy.latex(tan_value)})^2}} = {sy.latex(cos_square_value)}\\) \n"\
                            f"今、\\( \\theta \\) の定義域は\\( {sy.latex(sy.pi)} \\leqq \\theta < {sy.latex(2 * sy.pi)} \\)である。"\
                            f"この範囲で\\( \\tan \\theta > 0 \\)となるのは、\\( {sy.latex(sy.pi)} < \\theta < {sy.latex(3 * sy.pi / 2)} \\)である。\n"\
                            "そのため、\\( -1 < \\cos < 0 \\)が常に成り立つ。\n"\
                            f"よって、\\( \\cos \\theta = {sy.latex(cos_value)} \\)\n"\
                            "また、\\( \\tan \\theta = \\frac{\\sin \\theta}{\\cos \\theta}\\)より、\n"\
                            f"\\( \\sin \\theta = \\tan \\theta \\cos \\theta = {sy.latex(tan_value)} \\cdot {sy.latex(cos_value)}  = {sy.latex(sin_value)} \\)"
                    # 0 <= sin <= 1, -1 <= cos <= 0, tan < 0 (same as 3pi / 2 <= theta < 2pi)
                    else:
                        cos_value = sy.sqrt(cos_square_value)
                        sin_value = tan_value * cos_value
                        latex_answer = "\\( 1 + \\tan^2 \\theta = \\frac{1}{\\cos^2 \\theta}\\)より、\n"\
                            "\\( \\cos^2 \\theta = \\frac{1}{1 + \\tan^2 \\theta} \\)"\
                            f"\\( = \\frac{{1}}{{1 + ({sy.latex(tan_value)})^2}} = {sy.latex(cos_square_value)}\\) \n"\
                            f"今、\\( \\theta \\) の定義域は\\( {sy.latex(sy.pi)} \\leqq \\theta < {sy.latex(2 * sy.pi)} \\)である。"\
                            f"この範囲で\\( \\tan \\theta < 0 \\)となるのは、\\( {sy.latex(3 * sy.pi / 3)} < \\theta < {sy.latex(2 * sy.pi)} \\)である。\n"\
                            "そのため、\\( 0 < \\cos \\theta < 1 \\)が常に成り立つ。\n"\
                            f"よって、\\( \\cos \\theta = {sy.latex(cos_value)} \\)\n"\
                            "また、\\( \\tan \\theta = \\frac{\\sin \\theta}{\\cos \\theta}\\)より、\n"\
                            f"\\( \\sin \\theta = \\tan \\theta \\cos \\theta = {sy.latex(tan_value)} \\cdot {sy.latex(cos_value)}  = {sy.latex(sin_value)} \\)"
                # step by 3 * pi /2
                # -1 <= sin <= 1, -1 <= cos <= 1, -oo < tan < oo
                elif radian_range == "from_zero_up_to_3pi_over_2":
                    tan_value_denominator = randint(1, 6)
                    tan_value_numerator = randint(1, 3 * tan_value_denominator)
                    tan_value = sy.Rational(tan_value_numerator, tan_value_denominator)
                    if random() > 0.5:
                        tan_value *= -1
                    latex_problem = f"\\( \\tan \\theta = {sy.latex(tan_value)} \\)のとき、"\
                        f"\\( \\sin \\theta \\)と\\( \\cos \\theta \\)の値を求めよ。\\( (0 \\leqq \\theta \\leqq {sy.latex(3 * sy.pi / 2)}) \\)"
                    cos_square_value = 1 / (1 + tan_value ** 2)
                    # -1 <= sin <= 0, -1 <= cos <= 1, 0 < tan (same as 0 <= theta <= pi / 2, pi <= theta < 3pi / 2)
                    if tan_value > 0:
                        cos_value1 = sy.sqrt(cos_square_value)
                        cos_value2 = -sy.sqrt(cos_square_value)
                        sin_value1 = tan_value * cos_value1
                        sin_value2 = tan_value * cos_value2
                        latex_answer = "\\( 1 + \\tan^2 \\theta = \\frac{1}{\\cos^2 \\theta}\\)より、\n"\
                            "\\( \\cos^2 \\theta = \\frac{1}{1 + \\tan^2 \\theta} \\)"\
                            f"\\( = \\frac{{1}}{{1 + ({sy.latex(tan_value)})^2}} = {sy.latex(cos_square_value)}\\) \n"\
                            f"今、\\( \\theta \\) の定義域は\\( {sy.latex(0)} \\leqq \\theta < {sy.latex(3 * sy.pi / 2)} \\)である。"\
                            f"この範囲で\\( \\tan \\theta < 0 \\)となるのは、\\( {sy.latex(0)} < \\theta < {sy.latex(sy.pi / 2)}, {sy.latex(sy.pi)} < \\theta < {sy.latex(3 * sy.pi / 2)} \\)である。\n"\
                            "そのため、\\( \\cos \\theta \\)には正の場合と負の場合の両方が存在する。\n"\
                            f"よって、\\( \\cos \\theta = \\pm {sy.latex(cos_value1)} \\)\n"\
                            "また、\\( \\tan \\theta = \\frac{\\sin \\theta}{\\cos \\theta}\\)より、\n"\
                            f"\\( \\sin \\theta = \\tan \\theta \\cos \\theta = {sy.latex(tan_value)} \\cdot {sy.latex(cos_value1)}  = {sy.latex(sin_value1)} \\)\n"\
                            f"\\( \\sin \\theta = \\tan \\theta \\cos \\theta = {sy.latex(tan_value)} \\cdot {sy.latex(cos_value2)}  = {sy.latex(sin_value2)} \\)\n"\
                            f"すなわち、\\( \\sin \\theta = \\pm {sy.latex(sin_value1)} \\)"
                    # -1 <= sin <= 0, -1 <= cos <= 1, 0 < tan (same as 0 <= theta <= pi / 2, pi <= theta < 3pi / 2)
                    else:
                        cos_value = -sy.sqrt(cos_square_value)
                        sin_value = tan_value * cos_value
                        latex_answer = "\\( 1 + \\tan^2 \\theta = \\frac{1}{\\cos^2 \\theta}\\)より、\n"\
                            "\\( \\cos^2 \\theta = \\frac{1}{1 + \\tan^2 \\theta} \\)"\
                            f"\\( = \\frac{{1}}{{1 + ({sy.latex(tan_value)})^2}} = {sy.latex(cos_square_value)}\\) \n"\
                            f"今、\\( \\theta \\) の定義域は\\( {sy.latex(0)} \\leqq \\theta < {sy.latex(3 * sy.pi / 2)} \\)である。"\
                            f"この範囲で\\( \\tan \\theta < 0 \\)となるのは、\\( {sy.latex(sy.pi / 2)} < \\theta < {sy.latex(sy.pi)} \\)である。\n"\
                            "そのため、\\( \\cos \\theta < 0 \\)が常に成り立つ。\n"\
                            f"よって、\\( \\cos \\theta = {sy.latex(cos_value)} \\)\n"\
                            "また、\\( \\tan \\theta = \\frac{\\sin \\theta}{\\cos \\theta}\\)より、\n"\
                            f"\\( \\sin \\theta = \\tan \\theta \\cos \\theta = {sy.latex(tan_value)} \\cdot {sy.latex(cos_value)}  = {sy.latex(sin_value)} \\)\n"
                # -1 <= sin <= 1, -1 <= cos < 1, -oo < tan < oo
                elif radian_range == "from_pi_over_2_up_to_2pi":
                    tan_value_denominator = randint(1, 6)
                    tan_value_numerator = randint(1, 3 * tan_value_denominator)
                    tan_value = sy.Rational(tan_value_numerator, tan_value_denominator)
                    if random() > 0.5:
                        tan_value *= -1
                    latex_problem = f"\\( \\tan \\theta = {sy.latex(tan_value)} \\)のとき、"\
                        f"\\( \\sin \\theta \\)と\\( \\cos \\theta \\)の値を求めよ。\\( ({sy.latex(sy.pi / 2)} \\leqq \\theta < {sy.latex(2 * sy.pi)}) \\)"
                    cos_square_value = 1 / (1 + tan_value ** 2)
                    # -1 < sin < 0, -1 < cos < 0, 0 < tan (same as pi <= theta <= 3pi / 2)
                    if tan_value > 0:
                        cos_value = -sy.sqrt(cos_square_value)
                        sin_value = tan_value * cos_value
                        latex_answer = "\\( 1 + \\tan^2 \\theta = \\frac{1}{\\cos^2 \\theta}\\)より、\n"\
                            "\\( \\cos^2 \\theta = \\frac{1}{1 + \\tan^2 \\theta} \\)"\
                            f"\\( = \\frac{{1}}{{1 + ({sy.latex(tan_value)})^2}} = {sy.latex(cos_square_value)}\\) \n"\
                            f"今、\\( \\theta \\) の定義域は\\( {sy.latex(sy.pi / 2)} \\leqq \\theta < {sy.latex(2 * sy.pi)} \\)である。"\
                            f"この範囲で\\( \\tan \\theta > 0 \\)となるのは、\\( {sy.latex(sy.pi)} < \\theta < {sy.latex(3 * sy.pi / 2)} \\)である。\n"\
                            "そのため、\\( \\cos \\theta < 0 \\)が常に成り立つ。\n"\
                            f"よって、\\( \\cos \\theta = {sy.latex(cos_value)} \\)\n"\
                            "また、\\( \\tan \\theta = \\frac{\\sin \\theta}{\\cos \\theta}\\)より、\n"\
                            f"\\( \\sin \\theta = \\tan \\theta \\cos \\theta = {sy.latex(tan_value)} \\cdot {sy.latex(cos_value)}  = {sy.latex(sin_value)} \\)\n"
                    # -1 <= sin <= 1, -1 <= cos <= 1, 0 < tan (same as pi / 2 <= theta <= pi, 3pi / 2 <= theta < 2pi)
                    else:
                        cos_value1 = sy.sqrt(cos_square_value)
                        cos_value2 = -sy.sqrt(cos_square_value)
                        sin_value1 = tan_value * cos_value1
                        sin_value2 = tan_value * cos_value2
                        latex_answer = "\\( 1 + \\tan^2 \\theta = \\frac{1}{\\cos^2 \\theta}\\)より、\n"\
                            "\\( \\cos^2 \\theta = \\frac{1}{1 + \\tan^2 \\theta} \\)"\
                            f"\\( = \\frac{{1}}{{1 + ({sy.latex(tan_value)})^2}} = {sy.latex(cos_square_value)}\\) \n"\
                            f"今、\\( \\theta \\) の定義域は\\( {sy.latex(sy.pi / 2)} \\leqq \\theta < {sy.latex(2 * sy.pi)} \\)である。"\
                            f"この範囲で\\( \\tan \\theta < 0 \\)となるのは、\\( {sy.latex(sy.pi / 2)} < \\theta < {sy.latex(sy.pi)}, {sy.latex(3 * sy.pi / 2)} \\theta < {sy.latex(2 * sy.pi)} \\)である。\n"\
                            "そのため、\\( \\cos \\theta \\)には正の場合と負の場合の両方が存在する。\n"\
                            f"よって、\\( \\cos \\theta = \\pm {sy.latex(cos_value1)} \\)\n"\
                            "また、\\( \\tan \\theta = \\frac{\\sin \\theta}{\\cos \\theta}\\)より、\n"\
                            f"\\( \\sin \\theta = \\tan \\theta \\cos \\theta = {sy.latex(tan_value)} \\cdot {sy.latex(cos_value1)}  = {sy.latex(sin_value1)} \\)\n"\
                            f"\\( \\sin \\theta = \\tan \\theta \\cos \\theta = {sy.latex(tan_value)} \\cdot {sy.latex(cos_value2)}  = {sy.latex(sin_value2)} \\)\n"\
                            f"すなわち、\\( \\sin \\theta = \\pm {sy.latex(sin_value1)} \\)"           
                # step by 2 pi
                # -1 <= sin <= 1, -1 <= cos <= 1, -oo < tan < oo
                elif radian_range == "from_zero_up_to_2pi":
                    tan_value_denominator = randint(1, 6)
                    tan_value_numerator = randint(1, 3 * tan_value_denominator)
                    tan_value = sy.Rational(tan_value_numerator, tan_value_denominator)
                    if random() > 0.5:
                        tan_value *= -1
                    latex_problem = f"\\( \\tan \\theta = {sy.latex(tan_value)} \\)のとき、"\
                        f"\\( \\sin \\theta \\)と\\( \\cos \\theta \\)の値を求めよ。\\( ({sy.latex(0)} \\leqq \\theta < {sy.latex(2 * sy.pi)}) \\)"
                    cos_square_value = 1 / (1 + tan_value ** 2)
                    # -1 < sin < 0, -1 < cos < 0, 0 < tan (same as 0 <= theta < pi / 2,  3pi / 2 <= theta < 2pi)
                    if tan_value > 0:
                        cos_value1 = sy.sqrt(cos_square_value)
                        cos_value2 = -sy.sqrt(cos_square_value)
                        sin_value1 = tan_value * cos_value1
                        sin_value2 = tan_value * cos_value2
                        latex_answer = "\\( 1 + \\tan^2 \\theta = \\frac{1}{\\cos^2 \\theta}\\)より、\n"\
                            "\\( \\cos^2 \\theta = \\frac{1}{1 + \\tan^2 \\theta} \\)"\
                            f"\\( = \\frac{{1}}{{1 + ({sy.latex(tan_value)})^2}} = {sy.latex(cos_square_value)}\\) \n"\
                            f"今、\\( \\theta \\) の定義域は\\( {sy.latex(0)} \\leqq \\theta < {sy.latex(2 * sy.pi)} \\)である。"\
                            f"この範囲で\\( \\tan \\theta > 0 \\)となるのは、\\( {sy.latex(0)} < \\theta < {sy.latex(sy.pi / 2)}, {sy.latex(sy.pi)} < \\theta < {sy.latex(3 * sy.pi / 2)} \\)である。\n"\
                            "そのため、\\( \\cos \\theta \\)には正の場合と負の場合の両方が存在する。\n"\
                            f"よって、\\( \\cos \\theta = \\pm {sy.latex(cos_value1)} \\)\n"\
                            "また、\\( \\tan \\theta = \\frac{\\sin \\theta}{\\cos \\theta}\\)より、\n"\
                            f"\\( \\sin \\theta = \\tan \\theta \\cos \\theta = {sy.latex(tan_value)} \\cdot {sy.latex(cos_value1)}  = {sy.latex(sin_value1)} \\)\n"\
                            f"\\( \\sin \\theta = \\tan \\theta \\cos \\theta = {sy.latex(tan_value)} \\cdot {sy.latex(cos_value2)}  = {sy.latex(sin_value2)} \\)\n"\
                            f"すなわち、\\( \\sin \\theta = \\pm {sy.latex(sin_value1)} \\)"           
                    # -1 <= sin <= 1, -1 <= cos <= 1, tan < 0 (same as pi / 2 <= theta <= pi, 3pi / 2 <= theta < 2pi)
                    else:
                        cos_value1 = sy.sqrt(cos_square_value)
                        cos_value2 = -sy.sqrt(cos_square_value)
                        sin_value1 = tan_value * cos_value1
                        sin_value2 = tan_value * cos_value2
                        latex_answer = "\\( 1 + \\tan^2 \\theta = \\frac{1}{\\cos^2 \\theta}\\)より、\n"\
                            "\\( \\cos^2 \\theta = \\frac{1}{1 + \\tan^2 \\theta} \\)"\
                            f"\\( = \\frac{{1}}{{1 + ({sy.latex(tan_value)})^2}} = {sy.latex(cos_square_value)}\\) \n"\
                            f"今、\\( \\theta \\) の定義域は\\( {sy.latex(0)} \\leqq \\theta < {sy.latex(2 * sy.pi)} \\)である。"\
                            f"この範囲で\\( \\tan \\theta < 0 \\)となるのは、\\( {sy.latex(sy.pi / 2)} < \\theta < {sy.latex(sy.pi)}, {sy.latex(3 * sy.pi / 2)} < \\theta < {sy.latex(2 * sy.pi)} \\)である。\n"\
                            "そのため、\\( \\cos \\theta \\)には正の場合と負の場合の両方が存在する。\n"\
                            f"よって、\\( \\cos \\theta = \\pm {sy.latex(cos_value1)} \\)\n"\
                            "また、\\( \\tan \\theta = \\frac{\\sin \\theta}{\\cos \\theta}\\)より、\n"\
                            f"\\( \\sin \\theta = \\tan \\theta \\cos \\theta = {sy.latex(tan_value)} \\cdot {sy.latex(cos_value1)}  = {sy.latex(sin_value1)} \\)\n"\
                            f"\\( \\sin \\theta = \\tan \\theta \\cos \\theta = {sy.latex(tan_value)} \\cdot {sy.latex(cos_value2)}  = {sy.latex(sin_value2)} \\)\n"\
                            f"すなわち、\\( \\sin \\theta = \\pm {sy.latex(sin_value2)} \\)"                    
            return latex_answer, latex_problem
        
        selected_trigonometric_function = choice(self._used_trigonometric_functions)
        if self._radian_range == "up_to_pi_over_2":
            selected_radian_range = "from_zero_up_to_pi_over_2"
        elif self._radian_range == "up_to_pi":
            selected_radian_range = choice(
                [
                    "from_zero_up_to_pi_over_2",
                    "from_pi_over_2_up_to_pi", "from_zero_up_to_pi"
                ]
            )
        elif self._radian_range == "up_to_2pi":
            selected_radian_range = choice(
                [
                    "from_zero_up_to_pi_over_2", 
                    "from_pi_over_2_up_to_pi", "from_zero_up_to_pi",
                    "from_pi_up_to_3pi_over_2", "from_3pi_over_2_up_to_2pi",
                    "from_pi_over_2_up_to_3pi_over_2", "from_pi_up_to_2pi",
                    "from_zero_up_to_3pi_over_2", "from_pi_over_2_up_to_2pi",
                    "from_zero_up_to_2pi"
                ]
            )
        latex_answer, latex_problem = latex_answer_and_problem_maker(selected_trigonometric_function, selected_radian_range)
        return latex_answer, latex_problem
    
    def _trigonometric_functions_latex_maker(self):
        """有理化を施さない三角関数の値を、latex形式で格納した辞書を出力
        
        Returns:
            sin_values (dict): sinの値を格納
            cos_values (dict): cosの値を格納
            tan_values (dict): tanの値を格納
        """
        sin_values = {
            0: "0",
            sy.pi / 6: "\\frac{1}{2}",
            sy.pi / 4: "\\frac{1}{\\sqrt{2}}",
            sy.pi / 3: "\\frac{\\sqrt{3}}{2}",
            sy.pi / 2: "1",
            2 * sy.pi / 3: "\\frac{\\sqrt{3}}{2}",
            3 * sy.pi / 4: "\\frac{1}{\\sqrt{2}}",
            5 * sy.pi / 6: "\\frac{1}{2}",
            sy.pi: "0",
            7 * sy.pi / 6: "-\\frac{1}{2}",
            5 * sy.pi / 4: "-\\frac{1}{\\sqrt{2}}",
            4 * sy.pi / 3: "-\\frac{\\sqrt{3}}{2}",
            3 * sy.pi / 2: "-1",
            5 * sy.pi / 3: "-\\frac{\\sqrt{3}}{2}",
            7 * sy.pi / 4: "-\\frac{1}{\\sqrt{2}}",
            11 * sy.pi / 6: "-\\frac{1}{2}",
        }
        cos_values = {
            0: "1",
            sy.pi / 6: "\\frac{\\sqrt{3}}{2}",
            sy.pi / 4: "\\frac{1}{\\sqrt{2}}",
            sy.pi / 3: "\\frac{1}{2}",
            sy.pi / 2: "0",
            2 * sy.pi / 3: "-\\frac{1}{2}",
            3 * sy.pi / 4: "-\\frac{1}{\\sqrt{2}}",
            5 * sy.pi / 6: "-\\frac{\\sqrt{3}}{2}",
            sy.pi: "-1",
            7 * sy.pi / 6: "-\\frac{\\sqrt{3}}{2}",
            5 * sy.pi / 4: "-\\frac{1}{\\sqrt{2}}",
            4 * sy.pi / 3: "-\\frac{1}{2}",
            3 * sy.pi / 2: "0",
            5 * sy.pi / 3: "\\frac{1}{2}",
            7 * sy.pi / 4: "\\frac{1}{\\sqrt{2}}",
            11 * sy.pi / 6: "\\frac{\\sqrt{3}}{2}",
        }
        tan_values = {
            0: "0",
            sy.pi / 6: "\\frac{1}{\\sqrt{3}}",
            sy.pi / 4: "1",
            sy.pi / 3: "\\sqrt{3}",
            2 * sy.pi / 3: "-\\sqrt{3}",
            3 * sy.pi / 4: "-1",
            5 * sy.pi / 6: "-\\frac{1}{\\sqrt{3}}",
            sy.pi: "0",
            7 * sy.pi / 6: "\\frac{1}{\\sqrt{3}}",
            5 * sy.pi / 4: "1",
            4 * sy.pi / 3: "\\sqrt{3}",
            5 * sy.pi / 3: "-\\sqrt{3}",
            7 * sy.pi / 4: "-1",
            11 * sy.pi / 6: "-\\frac{1}{\\sqrt{3}}",
        }
        return sin_values, cos_values, tan_values
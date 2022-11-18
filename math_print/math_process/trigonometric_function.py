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
            latex_answer = "hogehogetan"
            latex_problem = "fugafugatan"
        return latex_answer, latex_problem
    
    def _make_radian_to_value_problem(self, trigonometric_ratio):
        latex_answer = "fuga"
        latex_problem = "hoge"
        return latex_answer, latex_problem
    
    def _make_mutual_relationships_problem(self):
        latex_answer = "fuga"
        latex_problem = "hoge"
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
from random import choice, randint, random

import sympy as sy


class TrigonometricRatioProblem:
    """三角比の値と角度に関連する問題を出力
    
    Attributes:
        _problem_types (list): 問題の候補を格納
        _used_trigonometric_ratios (list): 値と角度の相互変換に使用される三角比の候補を格納
        _degree_range (str): 値と角度の相互変換に使用される角度の範囲
        _sin_values (dict): 有理化を施さないsinの値を格納
        _cos_values (dict): 有理化を施さないcosの値を格納
        _tan_values (dict): 有理化を施さないtanの値を格納
        latex_answer (str): latex形式で記述された解答
        latex_answer (str): latex形式で記述された問題
    """
    def __init__(self, **settings):
        """初期処理
        
        settings (dict): 問題設定を格納
        """
        sy.init_printing(order='grevlex')
        self._problem_types = settings["problem_types"]
        self._used_trigonometric_ratios = settings["used_trigonometric_ratios"]
        self._degree_range = settings["degree_range"]
        self._sin_values, self._cos_values, self._tan_values = self._trigonometric_ratios_latex_maker()
        self.latex_answer, self.latex_problem = self._make_problem()
    
    def _make_problem(self):
        """問題作成のコントローラー

        Returns:
            latex_answer (str): latex形式で記述された解答
            latex_problem (str): latex形式で記述された問題
        
        Raises:
            ValueError: 問題のタイプが存在しないときに挙上
        """
        selected_problem_type = choice(self._problem_types)
        selected_used_trigonometric_ratio = choice(self._used_trigonometric_ratios)
        if selected_problem_type == "value_to_degree":
            latex_answer, latex_problem = self._make_value_to_degree_problem(selected_used_trigonometric_ratio)
        elif selected_problem_type == "degree_to_value":
            latex_answer, latex_problem = self._make_degree_to_value_problem(selected_used_trigonometric_ratio)
        elif selected_problem_type == "mutual_relationships":
            latex_answer, latex_problem = self._make_mutual_relationships_problem()
        else:
            raise ValueError(f"selected_problem_type is {selected_problem_type}. This must be wrong.")
        return latex_answer, latex_problem
    
    def _make_value_to_degree_problem(self, trigonometric_ratio):
        """値から角度を求める問題と解答の出力
        
        Args:
            trigonometric_ratio (str): 問題に使用される三角比
        
        Returns:
            latex_answer (str): latex形式で記述された解答
            latex_problem (str): latex形式で記述された問題
        """
        if self._degree_range == "up_to_90":
            list_30 = [i * 30 for i in range(4)]
            list_45 = [i * 45 for i in range(3)]
        elif self._degree_range == "up_to_180":
            list_30 = [i * 30 for i in range(7)]
            list_45 = [i * 45 for i in range(5)]
        degree_candidates = list(set(list_30 + list_45))
        if trigonometric_ratio == "sin":
            selected_degree = choice(degree_candidates)
            # selected_radian = selected_degree * sy.pi / 180
            # sin_value = sy.sin(selected_radian)
            if self._degree_range == "up_to_90":
                latex_answer = f"\\( \\theta = {selected_degree}^{{\\circ}} \\)"
                latex_problem = f"\\( \\sin \\theta = {self._sin_values[selected_degree]} \\)を満たす\\( \\theta (0^{{\\circ}} \\leqq \\theta \\leqq 90^{{\\circ}}) \\)を求めよ。"
            elif self._degree_range == "up_to_180":
                if selected_degree == 90:
                    latex_answer = f"\\( \\theta = {selected_degree}^{{\\circ}} \\)"
                else:
                    selected_degree1 = selected_degree
                    selected_degree2 = 180 - selected_degree1
                    if selected_degree1 > selected_degree2:
                        selected_degree1, selected_degree2 = selected_degree2, selected_degree1
                    latex_answer = f"\\( \\theta = {selected_degree1}^{{\\circ}}, {selected_degree2}^{{\\circ}} \\)"
                latex_problem = f"\\( \\sin \\theta = {self._sin_values[selected_degree]} \\)を満たす\\( \\theta (0^{{\\circ}} \\leqq \\theta \\leqq 180^{{\\circ}}) \\)を求めよ。"
        elif trigonometric_ratio == "cos":
            selected_degree = choice(degree_candidates)
            # selected_radian = selected_degree * sy.pi / 180
            # cos_value = sy.cos(selected_radian)
            latex_answer = f"\\( \\theta = {selected_degree}^{{\\circ}} \\)"
            if self._degree_range == "up_to_90":
                latex_problem = f"\\( \\cos \\theta = {self._cos_values[selected_degree]} \\)を満たす\\( \\theta (0^{{\\circ}} \\leqq \\theta \\leqq 90^{{\\circ}}) \\)を求めよ。"
            elif self._degree_range == "up_to_180":
                latex_problem = f"\\( \\cos \\theta = {self._cos_values[selected_degree]} \\)を満たす\\( \\theta (0^{{\\circ}} \\leqq \\theta \\leqq 180^{{\\circ}}) \\)を求めよ。"
        elif trigonometric_ratio == "tan":
            degree_candidates.remove(90)
            selected_degree = choice(degree_candidates)
            # selected_radian = selected_degree * sy.pi / 180
            # tan_value = sy.tan(selected_radian)
            latex_answer = f"\\( \\theta = {selected_degree}^{{\\circ}} \\)"
            if self._degree_range == "up_to_90":
                latex_problem = f"\\( \\tan \\theta = {self._tan_values[selected_degree]} \\)を満たす\\( \\theta (0^{{\\circ}} \\leqq \\theta < 90^{{\\circ}}) \\)を求めよ。"
            elif self._degree_range == "up_to_180":
                latex_problem = f"\\( \\tan \\theta = {self._tan_values[selected_degree]} \\)を満たす\\( \\theta (0^{{\\circ}} \\leqq \\theta < 90^{{\\circ}}, \\quad 90^{{\\circ}} < \\theta \\leqq 180^{{\\circ}}) \\)を求めよ。"
        return latex_answer, latex_problem
    
    def _make_degree_to_value_problem(self, trigonometric_ratio):
        """角度から値を求める問題と解答の出力
        
        Args:
            trigonometric_ratio (str): 問題に使用される三角比

        Returns:
            latex_answer (str): latex形式で記述された解答
            latex_problem (str): latex形式で記述された問題
        """
        if self._degree_range == "up_to_90":
            list_30 = [i * 30 for i in range(4)]
            list_45 = [i * 45 for i in range(3)]
        elif self._degree_range == "up_to_180":
            list_30 = [i * 30 for i in range(7)]
            list_45 = [i * 45 for i in range(5)]
        degree_candidates = list(set(list_30 + list_45))
        if trigonometric_ratio == "tan":
            degree_candidates.remove(90)
        selected_degree = choice(degree_candidates)
        latex_problem = f"\\( \\{trigonometric_ratio} {selected_degree}^{{\\circ}} \\)の値を求めよ。"
        # selected_radian = selected_degree * sy.pi / 180
        if trigonometric_ratio == "sin":
            # sin_value = sy.sin(selected_radian)
            latex_answer = f"\\( = {self._sin_values[selected_degree]} \\)"
        elif trigonometric_ratio == "cos":
            # cos_value = sy.cos(selected_radian)
            latex_answer = f"\\( = {self._cos_values[selected_degree]} \\)"
        elif trigonometric_ratio == "tan":
            # tan_value = sy.tan(selected_radian)
            latex_answer = f"\\( = {self._tan_values[selected_degree]} \\)"  
        return latex_answer, latex_problem

    def _make_mutual_relationships_problem(self):
        """相互変換で三角比を求める問題を出力
        
        Returns:
            latex_answer (str): latex形式で記述された解答
            latex_problem (str): latex形式で記述された問題
        """
        start_trigonometric_ratio = choice(["sin", "cos", "tan"])
        if start_trigonometric_ratio == "sin":
            sin_value_denominator = randint(2, 10)
            sin_value_numerator = randint(1, sin_value_denominator - 1)
            sin_value = sy.Rational(sin_value_numerator, sin_value_denominator)
            latex_problem = f"\\( \\sin \\theta = {sy.latex(sin_value)} \\)のとき、"\
                f"\\( \\cos \\theta \\)と\\( \\tan \\theta \\)の値を求めよ。\\( (0^{{\\circ}} \\leqq \\theta \\leqq 180^{{\\circ}}) \\)"
            cos_square_value = 1 - sin_value ** 2
            cos_value1 = sy.sqrt(1 - sin_value ** 2)
            cos_value2 = -sy.sqrt(1 - sin_value ** 2)
            tan_value1 = sin_value / cos_value1
            tan_value2 = sin_value / cos_value2
            latex_answer = f"\\( \\sin^2 \\theta + \\cos^2 \\theta = 1\\)より、\n"\
                "\\( \\cos^2 \\theta = 1 - \\sin^2 \\theta \\)"\
                f"\\( = 1 - ({sy.latex(sin_value)})^2 = {sy.latex(cos_square_value)}\\) \n"\
                f"今、定義域は\\( (0^{{\\circ}} \\leqq \\theta \\leqq 180^{{\\circ}}) \\)であるため、"\
                "\\( \\cos \\theta \\)には正の場合と負の場合の両方が存在する。\n"\
                f"よって、\\( \\cos \\theta = \\pm {sy.latex(cos_value1)} \\)\n"\
                "また、\\( \\tan \\theta = \\frac{\\sin \\theta}{\\cos \\theta}\\)より、\n"\
                f"\\( \\tan \\theta = \\frac{{{sy.latex(sin_value)}}}{{{sy.latex(cos_value1)}}} = {sy.latex(tan_value1)} \\)\n"\
                f"\\( \\tan \\theta = \\frac{{{sy.latex(sin_value)}}}{{{sy.latex(cos_value2)}}} = {sy.latex(tan_value2)} \\)\n"\
                f"すなわち、\\( \\tan \\theta = \\pm {sy.latex(tan_value1)} \\)"
        elif start_trigonometric_ratio == "cos":
            cos_value_denominator = randint(2, 10)
            cos_value_numerator = randint(1, cos_value_denominator - 1)
            if random() > 0.5:
                cos_value_denominator *= -1
            cos_value = sy.Rational(cos_value_numerator, cos_value_denominator)
            latex_problem = f"\\( \\cos \\theta = {sy.latex(cos_value)} \\)のとき、"\
                f"\\( \\sin \\theta \\)と\\( \\tan \\theta \\)の値を求めよ。\\( (0^{{\\circ}} \\leqq \\theta \\leqq 180^{{\\circ}}) \\)"
            sin_square_value = 1 - cos_value ** 2
            sin_value = sy.sqrt(sin_square_value)
            tan_value = sin_value / cos_value
            latex_answer = f"\\( \\sin^2 \\theta + \\cos^2 \\theta = 1\\)より、\n"\
                "\\( \\sin^2 \\theta = 1 - \\cos^2 \\theta \\)"\
                f"\\( = 1 - ({sy.latex(cos_value)})^2 = {sy.latex(sin_square_value)}\\) "\
                f"よって、\\( \\sin \\theta = {sy.latex(sin_value)} \\)\n"\
                "また、\\( \\tan \\theta = \\frac{\\sin \\theta}{\\cos \\theta}\\)より、\n"\
                f"\\( \\tan \\theta = \\frac{{{sy.latex(sin_value)}}}{{{sy.latex(cos_value)}}} = {sy.latex(tan_value)} \\)\n"
        elif start_trigonometric_ratio == "tan":
            tan_value_denominator = randint(1, 10)
            tan_value_numerator = randint(1, 10)
            if random() > 0.5:
                tan_value_denominator *= -1
            tan_value = sy.Rational(tan_value_numerator, tan_value_denominator)
            latex_problem = f"\\( \\tan \\theta = {sy.latex(tan_value)} \\)のとき、"\
                f"\\( \\sin \\theta \\)と\\( \\cos \\theta \\)の値を求めよ。\\( (0^{{\\circ}} \\leqq \\theta \\leqq 180^{{\\circ}}) \\)"
            cos_square_value = sy.Rational(1, 1 + tan_value ** 2)
            if tan_value > 0:
                cos_value = sy.sqrt(cos_square_value)
            else:
                cos_value = -sy.sqrt(cos_square_value)
            sin_value = tan_value * cos_value
            latex_answer = "\\( 1 + \\tan^2 \\theta = \\frac{1}{\\cos^2 \\theta}\\)より、\n"\
                "\\( \\cos^2 \\theta = \\frac{1}{1 + \\tan^2 \\theta} \\)"\
                f"\\( = \\frac{{1}}{{1 + {sy.latex(tan_value ** 2)}}} = {sy.latex(cos_square_value)}\\)\n"
            if cos_value > 0:
                latex_answer += "ここで、\\( \\tan \\theta  > 0 \\)より、\\( 0^{\\circ} < \\theta < 90^{\\circ} \\)であるため、"\
                    "\\( \\cos \\theta > 0 \\)である。\n"
            else:
                latex_answer += "ここで、\\( \\tan \\theta < 0 \\)より、\\( 90^{\\circ} < \\theta < 180^{\\circ} \\)であるため、"\
                    "\\( \\cos \\theta < 0 \\)である。\n"
            latex_answer += f"よって、\\( \\cos \\theta = {sy.latex(cos_value)} \\)\n"\
                "また、\\( \\tan \\theta = \\frac{\\sin \\theta}{\\cos \\theta} \\)より、\n"\
                "\\( \\sin \\theta = \\tan \\theta \\cos \\theta \\)"\
                f"\\( = ({sy.latex(tan_value)}) \\times ({sy.latex(cos_value)}) \\)"\
                f"\\( = {sy.latex(sin_value)} \\)"
        return latex_answer, latex_problem

    def _trigonometric_ratios_latex_maker(self):
        """有理化を施さない三角比の値を、latex形式で格納した辞書を出力
        
        Returns:
            sin_values (dict): sinの値を格納
            cos_values (dict): cosの値を格納
            tan_values (dict): tanの値を格納
        """
        sin_values = {
            0: "0",
            30: "\\frac{1}{2}",
            45: "\\frac{1}{\\sqrt{2}}",
            60: "\\frac{\\sqrt{3}}{2}",
            90: "1",
            120: "\\frac{\\sqrt{3}}{2}",
            135: "\\frac{1}{\\sqrt{2}}",
            150: "\\frac{1}{2}",
            180: "0"
        }
        cos_values = {
            0: "1",
            30: "\\frac{\\sqrt{3}}{2}",
            45: "\\frac{1}{\\sqrt{2}}",
            60: "\\frac{1}{2}",
            90: "0",
            120: "-\\frac{1}{2}",
            135: "-\\frac{1}{\\sqrt{2}}",
            150: "-\\frac{\\sqrt{3}}{2}",
            180: "-1"
        }
        tan_values = {
            0: "0",
            30: "\\frac{1}{\\sqrt{3}}",
            45: "1",
            60: "\\sqrt{3}",
            120: "-\\sqrt{3}",
            135: "-1",
            150: "-\\frac{1}{\\sqrt{3}}",
            180: "0"
        }
        return sin_values, cos_values, tan_values

from random import choice, randint, random
from typing import NamedTuple


import sympy as sy


class LinearFunctionWithGraphProblem:
    """グラフ付きの1次関数の問題を出力
    
    Attributes:
        graph_to_use (str): グリッドの有無
        latex_answer (str): latex形式の解答
        linear_function (LinearFunction): 1次関数の通る点と式を格納
    """
    def __init__(self, **settings):
        """初期処理
        
        settings (dict): 問題の設定を格納した辞書
        """
        sy.init_printing(order="grevlex")
        self._problem_types = settings["problem_types"]
        self.graph_to_use, self.latex_answer, self.linear_function = self._make_problem()
    
    def _make_problem(self):
        """問題作成と描画のための情報作成のコントローラー

        Returns:
            latex_answer (str): latex形式の解答
            linear_function (LinearFunction): 1次関数の通る点と式を格納
        """
        selected_problem_type = choice(self._problem_types)
        if selected_problem_type == "without_grid_to_linear_function":
            graph_to_use = "without_grid"
        else:
            graph_to_use = "with_grid"
        linear_function = self._decide_linear_function_status()
        latex_answer = f"{linear_function.linear_equation_latex}"
        return graph_to_use, latex_answer, linear_function
    
    def _decide_linear_function_status(self):
        """1次関数のステータスを決定

        Returns:
            linear_function (LinearFunction): 1次関数の式と通る点を格納
        """
        class LinearFunction(NamedTuple):
            """1次関数の通る点と式を格納

            Args:
                x1, y1, x2, y2 (str): 1次関数が通る2点
                linear_function_latex (str): latex形式で記述された1次関数の式
            """
            x1: str
            y1: str
            x2: str
            y2: str
            linear_equation_latex: str

        x = sy.Symbol("x", real=True)
        y = sy.Symbol("y", real=True)
        # x1 = randint(min, max-1)
        # x2 = x1 + randint(1, max - x1)
        x1 = randint(-5, 5 - 1)
        x2 = x1 + randint(1, 5 - x1)
        y1 = randint(-5, 5 - 1)
        y2 = y1 + randint(1, 5 - y1)
        if random() > 0.5:
            y1, y2 = y2, y1
        linear_coefficient = sy.Rational(y2 - y1, x2 - x1)
        right_of_equation = sy.expand(linear_coefficient * x - linear_coefficient * x1 + y1)
        # equation = sy.Eq(y, right_of_equation)
        right_of_equation_latex = sy.latex(right_of_equation)
        linear_equation_latex = f"\( y = {right_of_equation_latex} \)".replace("\\", "\\\\")
        linear_function = LinearFunction(
            x1=str(x1), y1=str(y1),
            x2=str(x2), y2=str(y2),
            linear_equation_latex=linear_equation_latex
        )
        return linear_function
        
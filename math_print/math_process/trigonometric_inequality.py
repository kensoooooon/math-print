from math import cos, isclose, pi, sin, tan
from random import choice

import sympy as sy

from .trigonometric_function import TrigonometricFunctionProblem


class TrigonometricInequalityProblem:
    """三角関数を含む基本的な不等式(sinθ > a など)の問題を出力

    角度はすべて π/12 を単位とする整数(twelfths)で扱い、
    境界点と境界点の間の区間ごとに不等式を満たすかを判定して解を組み立てる。

    Attributes:
        _used_trigonometric_functions (list): 問題に使用される三角関数
        _radian_range (str): θの定義域。"up_to_pi"(0≦θ≦π)または"up_to_2pi"(0≦θ<2π)
        latex_answer (str): latex形式で記述された解答
        latex_problem (str): latex形式で記述された問題
    """
    _INEQUALITY_SIGNS = {
        "<": "<",
        "<=": "\\leqq",
        ">": ">",
        ">=": "\\geqq",
    }

    def __init__(self, **settings):
        """初期処理

        settings (dict): 問題設定を格納
        """
        self._used_trigonometric_functions = settings["used_trigonometric_functions"]
        self._radian_range = settings["radian_range"]
        if self._radian_range == "up_to_pi":
            self._domain_end = 12
            self._is_domain_end_included = True
        elif self._radian_range == "up_to_2pi":
            self._domain_end = 24
            self._is_domain_end_included = False
        else:
            raise ValueError(f"'_radian_range' is {self._radian_range}. This may be wrong.")
        self._sin_values, self._cos_values, self._tan_values = TrigonometricFunctionProblem._trigonometric_functions_latex_maker()
        self.latex_answer, self.latex_problem = self._make_problem()

    def _make_problem(self):
        """問題作成のコントローラー

        解なし、または定義域全体が解となる問題は避けて作り直す。

        Returns:
            latex_answer (str): latex形式で記述された解答
            latex_problem (str): latex形式で記述された問題
        """
        while True:
            trigonometric_function = choice(self._used_trigonometric_functions)
            sign = choice(list(self._INEQUALITY_SIGNS.keys()))
            value_twelfths, value_latex = self._select_value(trigonometric_function)
            components = self._solve(trigonometric_function, sign, value_twelfths)
            if not(components):
                continue
            if components == [((0, True), (self._domain_end, self._is_domain_end_included))]:
                continue
            break
        if self._radian_range == "up_to_pi":
            latex_domain = f"0 \\leqq \\theta \\leqq {sy.latex(sy.pi)}"
        else:
            latex_domain = f"0 \\leqq \\theta < {sy.latex(2 * sy.pi)}"
        latex_problem = f"\\( {latex_domain} \\)のとき、不等式\\( \\{trigonometric_function} \\theta {self._INEQUALITY_SIGNS[sign]} {value_latex} \\)を解け。"
        latex_answer = self._components_to_latex(components)
        return latex_answer, latex_problem

    def _select_value(self, trigonometric_function):
        """不等式の右辺に使う値を選ぶ

        有名角(π/6, π/4の倍数)を1つ選び、その角度での三角関数の値を右辺とする。

        Args:
            trigonometric_function (str): 問題に使用される三角関数

        Returns:
            value_twelfths (int): 右辺の値を与える角度(π/12単位)
            value_latex (str): 右辺の値のlatex表記
        """
        candidates = sorted(set(range(0, self._domain_end + 1, 2)) | set(range(0, self._domain_end + 1, 3)))
        if not(self._is_domain_end_included):
            candidates.remove(self._domain_end)
        # tanの定義されない角度と、sin, cosの値が±1になる角度(基本問題として不自然な解になる)は除く
        if trigonometric_function in ("sin", "tan"):
            candidates = [twelfths for twelfths in candidates if twelfths % 12 != 6]
        if trigonometric_function == "cos":
            candidates = [twelfths for twelfths in candidates if twelfths % 12 != 0]
        value_twelfths = choice(candidates)
        values = {"sin": self._sin_values, "cos": self._cos_values, "tan": self._tan_values}[trigonometric_function]
        # 値のテーブルは0≦θ<2πで定義されているので、2πは0として参照する
        value_latex = values[sy.Rational(value_twelfths % 24, 12) * sy.pi]
        return value_twelfths, value_latex

    def _solve(self, trigonometric_function, sign, value_twelfths):
        """不等式の解を、定義域内の連続した範囲のリストとして求める

        境界点(f(θ)=a となる点、tanの定義されない点、定義域の端)と、
        境界点に挟まれた開区間を順に並べ、条件を満たすものをつなげて範囲にする。

        Args:
            trigonometric_function (str): 問題に使用される三角関数
            sign (str): 不等号("<", "<=", ">", ">=")
            value_twelfths (int): 右辺の値を与える角度(π/12単位)

        Returns:
            components (list): ((始点, 始点を含むか), (終点, 終点を含むか))のリスト。角度はπ/12単位
        """
        function = {"sin": sin, "cos": cos, "tan": tan}[trigonometric_function]
        value = function(value_twelfths * pi / 12)

        def is_defined(twelfths):
            return not(trigonometric_function == "tan" and (twelfths % 12) == 6)

        def is_satisfied(twelfths):
            if not(is_defined(twelfths)):
                return False
            difference = function(twelfths * pi / 12) - value
            if isclose(difference, 0, abs_tol=1e-9):
                return sign in ("<=", ">=")
            if sign in ("<", "<="):
                return difference < 0
            return difference > 0

        boundaries = [
            twelfths for twelfths in range(self._domain_end + 1)
            if (twelfths in (0, self._domain_end)) or not(is_defined(twelfths))
            or isclose(function(twelfths * pi / 12), value, abs_tol=1e-9)
        ]
        # (左端, 右端, 満たすか) の並び。点は左端=右端、開区間は左端<右端
        items = []
        for index, boundary in enumerate(boundaries):
            is_point_in_domain = (boundary != self._domain_end) or self._is_domain_end_included
            items.append((boundary, boundary, is_point_in_domain and is_satisfied(boundary)))
            if index + 1 < len(boundaries):
                next_boundary = boundaries[index + 1]
                items.append((boundary, next_boundary, is_satisfied((boundary + next_boundary) / 2)))

        components = []
        start_item = None
        previous_item = None
        for item in items + [(None, None, False)]:
            if item[2] and start_item is None:
                start_item = item
            elif not(item[2]) and start_item is not None:
                start = (start_item[0], start_item[0] == start_item[1])
                end = (previous_item[1], previous_item[0] == previous_item[1])
                components.append((start, end))
                start_item = None
            previous_item = item
        return components

    def _components_to_latex(self, components):
        """解の範囲を高校生向けのlatex表記に変換

        Args:
            components (list): ((始点, 始点を含むか), (終点, 終点を含むか))のリスト

        Returns:
            latex_answer (str): latex形式で記述された解答
        """
        latex_components = []
        for (start, is_start_included), (end, is_end_included) in components:
            latex_start = sy.latex(sy.Rational(start, 12) * sy.pi)
            latex_end = sy.latex(sy.Rational(end, 12) * sy.pi)
            if start == end:
                latex_components.append(f"\\theta = {latex_start}")
            else:
                start_sign = "\\leqq" if is_start_included else "<"
                end_sign = "\\leqq" if is_end_included else "<"
                latex_components.append(f"{latex_start} {start_sign} \\theta {end_sign} {latex_end}")
        latex_answer = f"\\( {', '.join(latex_components)} \\)"
        return latex_answer

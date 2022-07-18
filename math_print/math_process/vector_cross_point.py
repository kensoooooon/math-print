from random import choice, randint

import sympy as sy


class VectorCrossPoint:
    """交点の位置ベクトルを求める問題
    
    Attributes:
        _problem_type_list (list): 選択された問題タイプが格納されたリスト
        latex_answer (str): latex形式で記述された解答
        latex_problem (str): latex形式で記述された問題
    """
    def __init__(self, **settings):
        """
        Args:
            settings (dict): 問題の設定
        """
        self._problem_type_list = settings["problem_type_list"]
        self.latex_answer, self.latex_problem = self._make_problem()
    
    def _make_problem(self):
        """問題作成のコントローラー

        Returns:
            latex_answer (str): latex形式で記述された解答
            latex_problem (str): latex形式で記述された問題
        """
        selected_problem_type = choice(self._problem_type_list)
        if selected_problem_type == "cross_point_of_two_line":
            latex_answer, latex_problem = self._make_two_line_problem()
        elif selected_problem_type == "cross_point_of_plane_and_line":
            latex_answer, latex_problem = self._make_plane_and_line_problem()
    
        return latex_answer, latex_problem
    
    def _make_two_line_problem(self):
        """2直線の交点の位置ベクトルを求める問題の作成
        
        Returns:
            latex_answer (str): latex形式で記述された解答
            latex_problem (str): latex形式で記述された問題
        Note:
            三角形の2辺の内分点を通る直線の交点を求める問題を出力する
        Caution:
            latexを利用する際には、\\(\\)で囲むこと
        """
        left_internal_ratio1, left_internal_ratio2 = self._internal_ratio_maker()
        right_internal_ratio1, right_internal_ratio2 = self._internal_ratio_maker()
        
        # for abbreviation
        l1, l2 = left_internal_ratio1, left_internal_ratio2
        l_coeff_latex = sy.latex(sy.Rational(l1, l1 + l2))
        r1, r2 = right_internal_ratio1, right_internal_ratio2
        r_coeff_latex = sy.latex(sy.Rational(r1, r1 + r2))
        s = sy.Rational(l2 * r1, l1 * r2 + l2 * r1 + l2 * r2)
        s_latex = sy.latex(s)
        t = sy.Rational(l1 * r2, l1 * r2 + l2 * r1 + l2 * r2)
        t_latex = sy.latex(t)
        a_coeff = sy.Rational(l1 * r2, l1 * r2 + l2 * r1 + l2 * r2)
        a_coeff_latex = sy.latex(a_coeff)
        b_coeff = sy.Rational(l2 * r1, l1 * r2 + l2 * r1 + l2 * r2)
        b_coeff_latex = sy.latex(b_coeff)
        
        latex_problem = "\\( \\triangle{{OAB}}\\)において、"\
            f"辺\\( OA \\)を\\( {sy.latex(l1)}:{sy.latex(l2)} \\)に内分する点を\\( M \\)、\n"\
            f"辺\\( OB \\)を\\( {sy.latex(r1)}:{sy.latex(r2)} \\)に内分する点を\\( N \\)、\n"\
            f"線分\\( AN \\)と\\( MB \\)の交点を\\( P \\)、直線\\( OP \\)と辺\\( AB \\)との交点を\\( Q \\)とする。\n"\
            "\\( (1) \\) \\( \\vec{{OP}} \\)を\\( \\vec{{OA}} = \\vec{{a}}, \\vec{{OB}} = \\vec{{b}} \\)を用いて表せ。\n"\
            "\\( (2) \\) \\( \\vec{{OP}} \\)を\\( \\vec{{OA}} = \\vec{{a}}, \\vec{{OB}} = \\vec{{b}} \\)を用いて表せ。"
        
        latex_answer = "\\( MP:PB = s:1-s, AP:PN = 1-t:t \\)とする。"\
            f"点Pは線分\\( MB \\)を\\( s:1-s \\)に内分する点であるため、内分の公式より、\n"\
            "\\( \\vec{{OP}} = (1-s)\\vec{{OM}} + s\\vec{{OB}} \\)"\
            f"\\( = (1-s) ({l_coeff_latex} \\vec{{a}}) + s \\vec{{b}} \\)"\
            f"\\( = ({l_coeff_latex} - {l_coeff_latex}s)\\vec{{a}} + s\\vec{{b}} \\)と表せる。\n"\
            "同様に、点Pは線分\\( AN \\)を\\( 1-t:t \\)に内分する点であるため、\n"\
            "\\( \\vec{{OP}} = t\\vec{{OA}} + (1-t)\\vec{{ON}} \\)"\
            f"\\( = t\\vec{{a}}) + (1-t)({r_coeff_latex} \\vec{{b}}) \\)"\
            f"\\( = t\\vec{{a}} + ({r_coeff_latex} - {r_coeff_latex}t) \\vec{{b}}\\)と表せる。\n"\
            "\\( \\vec{{a}} \\)と\\( \\vec{{b}} \\)は一次独立であるため、\n"\
            f"\\( {l_coeff_latex} - {l_coeff_latex}s = t \\\\ s = {r_coeff_latex} - {r_coeff_latex}t \\)\n"\
            "が成り立つ。これを解くと、\n"\
            f"\\( s = {s_latex} \\\\ t = {t_latex} \\)となり、\n"\
            f"\\( \\vec{{OP}} = {a_coeff_latex} \\vec{{a}} + {b_coeff_latex} \\vec{{b}} \\)"

        return latex_answer, latex_problem
    
    def _make_plane_and_line_problem(self):
        latex_answer = "aaaaaaaaaaa"
        latex_problem = "bbbbbbbbbbbbbbb"
        
        return latex_answer, latex_problem
    
    def _internal_ratio_maker(self):
        """互いに素な内分比を出力する

        Returns:
            internal_ratio1 (int): ひとつめの内分比
            internal_ratio2 (int): ふたつめの内分比
        """
        from math import gcd
        internal_ratio1 = randint(1, 10)
        internal_ratio2 = randint(1, 10)
        divisor = gcd(internal_ratio1, internal_ratio2)
        internal_ratio1 /= divisor
        internal_ratio2 /= divisor
        return int(internal_ratio1), int(internal_ratio2)
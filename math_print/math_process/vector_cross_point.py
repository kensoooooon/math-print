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
        
        k = sy.Rational(1, a_coeff + b_coeff)
        k_latex = sy.latex(k)
        
        latex_problem = "\\( \\triangle{{OAB}}\\)において、"\
            f"辺\\( OA \\)を\\( {sy.latex(l1)}:{sy.latex(l2)} \\)に内分する点を\\( M \\)、"\
            f"辺\\( OB \\)を\\( {sy.latex(r1)}:{sy.latex(r2)} \\)に内分する点を\\( N \\)、\n"\
            f"線分\\( AN \\)と\\( MB \\)の交点を\\( P \\)、直線\\( OP \\)と辺\\( AB \\)との交点を\\( Q \\)とする。\n"\
            "\\( (1) \\) \\( \\overrightarrow{{OP}} \\)を\\( \\overrightarrow{{OA}} = \\overrightarrow{{a}}, \\overrightarrow{{OB}} = \\vec{{b}} \\)を用いて表せ。\n"\
            "\\( (2) \\) \\( \\overrightarrow{{OP}} \\)を\\( \\overrightarrow{{OA}} = \\vec{{a}}, \\overrightarrow{{OB}} = \\vec{{b}} \\)を用いて表せ。"
        
        latex_answer = "(1) \\( MP:PB = s:1-s, AP:PN = 1-t:t \\)とする。"\
            f"点Pは線分\\( MB \\)を\\( s:1-s \\)に内分する点であるため、内分の公式より、\n"\
            "\\( \\overrightarrow{{OP}} = (1-s)\\overrightarrow{{OM}} + s\\overrightarrow{{OB}} \\)"\
            f"\\( = (1-s) ({l_coeff_latex} \\vec{{a}}) + s \\vec{{b}} \\)"\
            f"\\( = ({l_coeff_latex} - {l_coeff_latex}s)\\vec{{a}} + s\\vec{{b}} \\)と表せる。\n"\
            "同様に、点Pは線分\\( AN \\)を\\( 1-t:t \\)に内分する点であるため、\n"\
            "\\( \\overrightarrow{{OP}} = t\\overrightarrow{{OA}} + (1-t)\\overrightarrow{{ON}} \\)"\
            f"\\( = t\\vec{{a}}) + (1-t)({r_coeff_latex} \\vec{{b}}) \\)"\
            f"\\( = t\\vec{{a}} + ({r_coeff_latex} - {r_coeff_latex}t) \\vec{{b}}\\)と表せる。\n"\
            "\\( \\vec{{a}} \\)と\\( \\vec{{b}} \\)は一次独立であるため、\n"\
            f"\\( \\left\\{{ \\begin{{array}}{{l}} {l_coeff_latex} - {l_coeff_latex}s = t \\\\ s = {r_coeff_latex} - {r_coeff_latex}t \\end{{array}} \\right. \\)\n"\
            "が成り立つ。これを解くと、\n"\
            f"\\( s = {s_latex}, t = {t_latex} \\)となり、\n"\
            f"\\( \\overrightarrow{{OP}} = {a_coeff_latex} \\vec{{a}} + {b_coeff_latex} \\vec{{b}} \\)となる。\n"\
            f"(2) 点Qは直線OP上にあるため\\( \\overrightarrow{{OQ}} = k \\overrightarrow{{OP}} = {a_coeff_latex} k \\vec{{a}} + {b_coeff_latex} k \\vec{{b}} \\)とおける。\n"\
            f"ここで、点Qは直線AB上の点でもあるため、\\( {a_coeff_latex} k + {b_coeff_latex} k = 1\\)が成立し、"\
            f"これを解くと、\\( k = {k_latex} \\)となる。\n"\
            f"よって答えは、\\( \\overrightarrow{{OQ}} = {sy.latex(k * a_coeff)} \\vec{{a}} + {sy.latex(k * b_coeff)} \\vec{{b}} \\)である。"

        return latex_answer, latex_problem
    
    def _make_plane_and_line_problem(self):
        left_internal_ratio1, left_internal_ratio2 = self._internal_ratio_maker()
        right_internal_ratio1, right_internal_ratio2 = self._internal_ratio_maker()
        
        # for abbreviation
        # (1)
        l1, l2 = left_internal_ratio1, left_internal_ratio2
        l1_latex = sy.latex(l1)
        l2_latex = sy.latex(l2)
        r1, r2 = right_internal_ratio1, right_internal_ratio2
        r1_latex = sy.latex(r1)
        r2_latex = sy.latex(r2)
        
        r_b_coeff = sy.Rational(r2, r1 + r2)
        r_b_coeff_latex = sy.latex(r_b_coeff)
        r_c_coeff = sy.Rational(r1, r1 + r2)
        r_c_coeff_latex = sy.latex(r_c_coeff)
        
        l_a_coeff = sy.Rational(l2, l1 + l2)
        l_a_coeff_latex = sy.latex(l_a_coeff)
        l_b_coeff = sy.Rational(l1, l1 + l2)
        l_b_coeff_latex = sy.latex(l_b_coeff)
        
        s = sy.Rational((r1 + r2) * l1, l1 * r1 + l1 * r2 + l2 * r2)
        s_latex = sy.latex(s)
        t = sy.Rational((l1 + l2) * r2, l1 * r1 + l1 * r2 + l2 * r2)
        t_latex = sy.latex(t)
        
        a_coeff = sy.Rational(l2 * r2, l1 * r1 + l1 * r2 + l2 * r2)
        a_coeff_latex = sy.latex(a_coeff)
        b_coeff = sy.Rational(l1 * r2, l1 * r1 + l1 * r2 + l2 * r2)
        b_coeff_latex = sy.latex(b_coeff)
        c_coeff = sy.Rational(l1 * r1, l1 * r1 + l1 * r2 + l2 * r2)
        c_coeff_latex = sy.latex(c_coeff)
        
        # (2)
        c1, c2 = self._internal_ratio_maker()
        c1_latex = sy.latex(c1)
        c2_latex = sy.latex(c2)
        on_by_c_coeff = sy.Rational(c1, c1 + c2)
        on_by_c_coeff_latex = sy.latex(on_by_c_coeff)
        c_by_on = sy.Rational(1, on_by_c_coeff)
        c_by_on_latex = sy.latex(c_by_on)
        oq_on_coeff = c_coeff * c_by_on
        oq_on_coeff_latex = sy.latex(oq_on_coeff)
        k = sy.Rational(1, a_coeff + b_coeff + oq_on_coeff)
        k_latex = sy.latex(k)
        oq_a_coeff = a_coeff * k
        oq_a_coeff_latex = sy.latex(oq_a_coeff)
        oq_b_coeff = b_coeff * k
        oq_b_coeff_latex = sy.latex(oq_b_coeff)
        oq_c_coeff = c_coeff * k
        oq_c_coeff_latex = sy.latex(oq_c_coeff)
        
        latex_problem = f"四面体OABCにおいて、\\( \\overrightarrow{{OA}} = \\vec{{a}}, \\overrightarrow{{OB}} = \\vec{{b}}, \\overrightarrow{{OC}} = \\vec{{c}} \\)とする。\n"\
                        f"(1) 辺ABを\\( {l1_latex}:{l2_latex}\\)に内分する点をL, 辺BCを\\( {r1_latex}:{r2_latex}\\)に内分する点をMとする。\n"\
                        f"ここで、線分AMと線分CLの交点をPとしたとき、\\( \\overrightarrow{{OP}} \\)を\\( \\vec{{a}}, \\vec{{b}}, \\vec{{c}} \\)を用いて表せ。\n"\
                        f"(2) 辺OCを\\( {c1_latex}:{c2_latex} \\)に内分する点をN,平面ABNと線分OPの交点をQとするとき、\n"\
                        f"\\( \\overrightarrow{{OQ}} \\)を\\( \\vec{{a}}, \\vec{{b}}, \\vec{{c}} \\)で表せ。"
        
        latex_answer = f"(1) \\( AP:PM = s:1-s, LP:PC=1-t:t \\)とする。\n"\
                       f"点Pは線分AMを\\( s:1-s \\)に内分する点であるため、内分の公式より、\n"\
                       f"\\( \\overrightarrow{{OP}} = (1-s) \\overrightarrow{{OA}} + s \\overrightarrow{{OM}} \\)"\
                       f"\\( = (1-s) \\vec{{a}} + s \\frac{{{r2_latex} \\vec{{b}} + {r1_latex} \\vec{{c}}}}{{{r1_latex} + {r2_latex}}} \\)\n"\
                       f"\\( = (1-s) \\vec{{a}} + {r_b_coeff_latex} s \\vec{{b}} + {r_c_coeff_latex} s \\vec{{c}} \\)と表せる。\n"\
                       f"同様に、点Pは線分LCを\\( LP:PC = 1-t:t \\)に内分する点であるため、\n"\
                       f"\\( \\overrightarrow{{OP}} = t \\overrightarrow{{OL}} + (1-t) \\overrightarrow{{OC}}\\)"\
                       f"\\( = t \\frac{{{l2_latex} \\vec{{a}} + {l1_latex} \\vec{{b}}}}{{{l1_latex} + {l2_latex}}} + (1-t) \\vec{{c}} \\)\n"\
                       f"\\( = {l_a_coeff_latex} t \\vec{{a}} + {l_b_coeff_latex} t \\vec{{b}} + (1-t) \\vec{{c}} \\)と表せる。\n"\
                       "ここで4点OABCは四面体の頂点であり、同一平面上にないことは明らかであるため、\n"\
                       f"\\( \\left\\{{ \\begin{{array}}{{l}} 1 - s = {l_a_coeff_latex} \\\\ {r_b_coeff_latex}s = {l_b_coeff_latex}t \\\\ {r_c_coeff_latex} = 1-t \\end{{array}} \\right. \\)\n"\
                       "が成り立つ。これを解くと、\n"\
                       f"\\( s = {s_latex}, t = {t_latex} \\)となり、\n"\
                       f"\\( \\overrightarrow{{OP}} = {a_coeff_latex} \\vec{{a}} + {b_coeff_latex} \\vec{{b}} + {c_coeff_latex} \\vec{{c}} \\)となる。\n"\
                       f"(2) 点Qは直線OP上の点であるため、\\( \\overrightarrow{{OQ}} = k \\overrightarrow{{OP}} = {a_coeff_latex} k \\vec{{a}} + {b_coeff_latex} k \\vec{{b}} + {c_coeff_latex} k \\vec{{c}} \\)とおける。\n"\
                       f"また、点Nは辺OCを\\( {c1_latex}:{c2_latex} \\)に内分する点であるため、\\( \\overrightarrow{{ON}} = {on_by_c_coeff_latex} \\vec{{c}} \\)となり、これを変形すると、\n"\
                       f"\\( \\vec{{c}} = {c_by_on_latex} \\overrightarrow{{ON}}  \\)と表せる。これを代入すると、\n"\
                       f"\\( \\overrightarrow{{OQ}} = {a_coeff_latex} k \\vec{{a}} + {b_coeff_latex} k \\vec{{b}} + {c_coeff_latex} k \\cdot {c_by_on_latex} \\overrightarrow{{ON}} \\)"\
                       f"\\( = {a_coeff_latex} k \\overrightarrow{{OA}} + {b_coeff_latex} k \\overrightarrow{{OB}} + {oq_on_coeff_latex} k \\overrightarrow{{ON}} \\) となる。\n"\
                       f"ここで、点Qは平面ABN上の点であるため、\\( {a_coeff_latex} k + {b_coeff_latex} k + {oq_on_coeff_latex} k = 1 \\)が成り立つ。これを解くと、\n"\
                       f"\\( k = {k_latex} \\)となり、\\( \\overrightarrow{{OQ}} = {oq_a_coeff_latex} \\vec{{a}} + {oq_b_coeff_latex} \\vec{{b}} + {oq_c_coeff_latex} \\vec{{c}} \\)となる。"

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
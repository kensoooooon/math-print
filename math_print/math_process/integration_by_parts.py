"""
10/27
    random_four_integersで調整完了のはず
    
    後は()の表示が出来ていない点も要調整
        ある程度中括弧で対応できそうだが、細かいところの調整がガバい
        定数項がなければカッコは不要
        掛け算であれば前後はカッコで囲む
        など

10/31
    引き続き表示の問題
    
        latex内では単純な改行が通らない。
            latexの改行コマンドは？
                begin+alignやarrayでどうにかなりそうな雰囲気がある(連立方程式)
                が、今のところうまく動作していない。素の状態でhtml側に書き込むべき？
"""
from random import choice, randint, sample

import sympy as sy


class IntegrationByPartsProblem:
    """部分積分の問題と解答を作成し、出力
    
    Attributes:
        latex_answer (str): latex形式で記述された解答
        latex_problem (str): latex形式で記述された問題
    """
    def __init__(self, **settings):
        """初期設定
        
        Args:   
            settings (dict): 部分積分のタイプと、定積分か不定積分かの指定を含む
        
        Raises:
            ValueError: 想定していないタイプの問題が指定されたときに送出
        """
        sy.init_printing(order='grevlex')
        selected_calculation_type = choice(settings["types_of_integration_by_parts"])
        selected_integral_type = choice(settings["integral_types"])
        if selected_calculation_type == "double_polynomial":
            self.latex_answer, self.latex_problem = self._make_double_polynomial_problem(selected_integral_type)
        else:
            raise ValueError(f"'selected_calculate_type' is {selected_calculation_type}. It isn't expected value.")
    
    def _make_double_polynomial_problem(self, selected_integral_type):
        """(多項式) x (多項式)型の部分積分の問題・解答を作成
        
        Args:
            selected_integral_type (str): indefinite_integral(不定積分)かdefinite_integral(定積分)のいずれかを指定
        
        Returns:
            latex_answer (str): latex形式で記述されていることを前提とした解答
            latex_problem (str): latex形式で記述されていることを前提とした問題
        """
        
        def step_factorial(start, end):
            """startからendまでの階乗を計算するための関数
            
            Args:
                start (int): 起点となる数
                end (int): 終点となる数
            
            Returns:
                result (int): 階乗の結果
                
            Raises:
                ValueError: start, endのいずれかが負の数。またはstartの方がendより大きいときに送出される
            """
            if (start < 0) or (end < 0):
                raise ValueError(f"'start' and 'end' must be more or equal 0. {start} and {end} is invalid value.")
            if start >= end:
                raise ValueError(f"'end' must be more than 'start'. {start} and {end} is invalid value.")
            result = 1
            for i in range(start, end + 1):
                result *= i
            return result

        def random_integer(min_value, max_value, including_zero=True):
            """min_valueからmax_valueまでの範囲のランダムな整数を出力する
            
            Args:
                min_value (int): 最小値
                max_value (int): 最大値
                including_zero (Optional[bool]): 0を含むか否か。デフォルトはTrue(含む)
            
            Returns:
                random_integer(sy.Integer): 条件を満たす整数
            """
            if including_zero:
                random_integer = randint(min_value, max_value)
            else:        
                if min_value <= 0 <= max_value:
                    # 0を避けて範囲を分割
                    random_integer = choice(list(range(min_value, 0)) + list(range(1, max_value + 1)))
                else:
                    # 0が範囲に含まれていない場合
                    random_integer = randint(min_value, max_value)
            return sy.Integer(random_integer)

        def random_four_integers(min_value, max_value, including_zero=True):
            """min_valueからmax_valueまでの範囲で条件を満たす4つの整数を出力する。
            
            Args:
                min_value (int): 最小値
                max_value (int): 最大値
                including_zero (Optional[bool]): 0を含むか否か。デフォルトはTrue(含む)
            
            Returns:
                tuple: (a1, a2, b1, b2) 条件を満たす4つの整数(sy.Integer)
            """
            def generate_candidates():
                """整数候補のリストを生成する関数"""
                if including_zero:
                    return list(range(min_value, max_value + 1))
                else:
                    if min_value <= 0 <= max_value:
                        return list(range(min_value, 0)) + list(range(1, max_value + 1))
                    else:
                        return list(range(min_value, max_value + 1))

            candidates = generate_candidates()

            while True:
                # まず a1 と a2 を選ぶ（a1 = a2 も許可）
                a1 = choice(candidates)
                a2 = choice(candidates)
                
                if (a1 == 0) or (a2 == 0):
                    continue

                # b1 と b2 を選ぶ（b1 = b2 も許可）
                b1 = choice(candidates)
                b2 = choice(candidates)

                # 条件をチェック (a1 = a2 かつ b1 = b2 を避ける)
                if not (a1 == a2 and b1 == b2):
                    return sy.Integer(a1), sy.Integer(a2), sy.Integer(b1), sy.Integer(b2)

        # def latex_with_brackets(formula):
        #     """式にカッコがない場合はそれを補いつつ、latex形式への変換を行う
        #    
        #     Args:
        #        formula (sy.Expr): latexに変換したい数式
        #    
        #    Returns:
        #        latex_formula (str): latex形式の数式
        #    """
        #    if ('(' not in sy.latex(formula)) or (')' not in sy.latex(formula)):
        #        latex_formula = f"( {sy.latex(formula)} )"
        #    else:
        #        latex_formula = sy.latex(formula)
        #    return latex_formula
    
        def latex_with_brackets(formula):
            """シンボルが含まれるが定数項がない場合はカッコを省略し、負の定数項がある場合はカッコを付けてlatex形式に変換する

            Args:
                formula (sy.Expr): latexに変換したい数式

            Returns:
                latex_formula (str): latex形式の数式
            """
            # 定数項の確認
            # 式の中に負の定数が含まれているかをチェック
            has_negative_constant = any(term.is_number and term < 0 for term in formula.as_ordered_terms())
            # シンボルが含まれる場合の処理
            if formula.free_symbols:
                # 定数項が存在しない場合
                if not any(term.is_number for term in formula.as_ordered_terms()):
                    latex_formula = sy.latex(formula)
                # 負の定数項が存在する場合
                elif has_negative_constant:
                    latex_formula = f"( {sy.latex(formula)} )"
                else:
                    latex_formula = sy.latex(formula)
            else:
                latex_formula = sy.latex(formula)

            return latex_formula

        
        x = sy.Symbol('x', real=True)
        if selected_integral_type == "indefinite_integral":
            a1, a2, b1, b2 = random_four_integers(-3, 3)
            less_dimension = random_integer(1, 3, including_zero=False)
            more_dimension = less_dimension + random_integer(1, 3, including_zero=False)
            f = (a1 * x + b1) ** less_dimension
            fs = [f]
            for i in range(1, less_dimension + 1):
                diff_f = sy.diff(f, x, i)
                fs.append(sy.factor(diff_f))
            g = (a2 * x + b2) ** more_dimension
            denom = step_factorial(more_dimension + 1, more_dimension + 1 + less_dimension)
            g_plus = sy.Rational(1, denom) * (a2 * x + b2) ** (more_dimension + (less_dimension + 1))
            gs = [g_plus]
            for i in range(1, less_dimension + 1):
                diff_g_plus = sy.diff(g_plus, x, i)
                gs.append(diff_g_plus)
            gs.reverse()
            result = 0
            for index, (left, right) in enumerate(zip(fs, gs)):
                if index % 2 == 0:
                    sign = +1
                else:
                    sign = -1
                result += sign * (left * right)
            answer = sy.factor(result)
            # 1乗への対応
            f_latex = latex_with_brackets(f)
            g_latex = latex_with_brackets(g)
            latex_problem = f"\\( \\int {f_latex} {g_latex} \\, dx \\)"
            latex_answer = "\\( = \\)"
            """10/31
            直球でいじるならこの辺？
                indexで判定つけて改行すればはみ出しは防げる
                カッコの付け方については、割と元の式に依存しているところがあるので、一律だと自然なカッコつけは難しい？
                    latex化させるのを遅らせて、中身で判定取るか？
                    
            """
            for index, (left, right) in enumerate(zip(fs, gs)):
                if index == 0:
                    sign = ""
                elif index % 2 == 0:
                    sign = "+"
                else:
                    sign = "-"
                # 1乗への対応
                left_latex = latex_with_brackets(left)
                right_latex = latex_with_brackets(right)
                latex_answer += f"\\( {sign} \\left\\{{ {left_latex} {right_latex} \\right\\}} \\)"
                # latex_answer += f"{sign} {left_latex} {right_latex}"
                if index % 3 == 1:
                    latex_answer += '\n'
            latex_answer += "\\( + C \\) \n"
            latex_answer += f"\\( = {sy.latex(answer)} + C \\)"
        elif selected_integral_type == "definite_integral":
            latex_answer = "This is dummy answer."
            latex_problem = "This is dummy problem."
        else:
            raise ValueError(f"'selected_integral_type' must be 'indefinite_integral' or 'definite_integral'. {selected_integral_type} must be wrong.")
        return latex_answer, latex_problem

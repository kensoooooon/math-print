from random import choice, randint, random
from typing import Dict, Union


import sympy as sy


class FormulaWithSymbol:
    """種々の数列の和を求める問題と解答を、指定された条件に応じて作成・格納
    
    Attributes:
        latex_answer (str): latex形式と通常の文字列が混在していることを前提とした解答
        latex_problem (str): latex形式と通常の文字列が混在していることを前提とした問題 
    """
    def __init__(self, **settings: Dict) -> None:
        """初期設定
        
        Args:
            settings (dict): 問題の設定を格納
            - 出力すべき問題のタイプ(式での表現のみ行う、数値の計算もあわせて行うなど)を格納
        
        Raises:
            ValueError: 想定されていないタイプの問題が指定されたときに挙上
        """
        sy.init_printing(order="grevlex")
        selected_problem_type = choice(settings["problem_types"])
        if selected_problem_type == "expression_with_formula":
            self.latex_answer, self.latex_problem = self._make_expression_with_formula_problem()
        elif selected_problem_type == "expression_with_formula_and_calculate":
            self.latex_answer, self.latex_problem = self._make_expression_with_formula_and_calculate_problem()
        elif selected_problem_type == "from_formula_to_condition":
            self.latex_answer, self.latex_problem = self._make_from_formula_to_condition_problem()
        else:
            raise ValueError(f"selected_problem_type is {selected_problem_type}. This isn't concerned value.")
    
    def _make_expression_with_formula_problem(self):
        """文字を用いた式の表現のみを問う問題の作成
        
        Returns:
            Tuple[str, str]: 問題と解答
            - latex_answer (str): latex形式と通常の文字列が混在していることを前提とした解答
            - latex_problem (str): latex形式と通常の文字列が混在していることを前提とした問題 
        """
        # selected_genre = choice(["area", "volume", "weight", "price"])
        selected_genre = "area"
        if selected_genre == "area":
            # selected_shape = choice(["triangle", "parallelogram", ])
            selected_shape = "parallelogram"
            if selected_shape == "triangle":
                if random() > 0.5:
                    base = randint(1, 10)
                    height = sy.Symbol("x")
                else:
                    base = sy.Symbol("x")
                    height = randint(1, 10)
                latex_problem = f"底辺が \\( {base} \\mathrm{{cm}} \\)、高さが\\( {height} \\mathrm{{cm}} \\)の三角形があります。\n"
                latex_problem += f"三角形の面積を、\\( x \\)を使った式で表しなさい。"
                latex_answer = "三角形の面積は、(底辺) \\( \\times \\) (高さ) \\( \\div 2\\)なので、\n"
                latex_answer += f"\\( {base} \\times {height} \\div 2 \\)"
            elif selected_shape == "parallelogram":
                if random() > 0.5:
                    base = randint(1, 10)
                    height = sy.Symbol("x")
                else:
                    base = sy.Symbol("x")
                    height = randint(1, 10)
                latex_problem = f"底辺が \\( {base} \\mathrm{{cm}} \\)、高さが\\( {height} \\mathrm{{cm}} \\)の平行四辺形があります。\n"
                latex_problem += f"平行四辺形の面積を、\\( x \\)を使った式で表しなさい。"
                latex_answer = "平行四辺形の面積は、(底辺) \\( \\times \\) (高さ) \\( \\div 2\\)なので、\n"
                latex_answer += f"\\( {base} \\times {height} \\div 2 \\)"                
        elif selected_genre == "volume":
            item = choice(["ジュース", "お茶"])
            increase_or_decrease = choice(["increase", "decrease"])
            if increase_or_decrease == "increase":
                start_number = randint(1, 15)
                increased_number = randint(2, 4)
                end_number = start_number + increased_number
        return latex_answer, latex_problem
    
    def _make_expression_with_formula_and_calculate_problem(self):
        """文字を用いた式の表現と、数の計算をあわせて問う問題の作成
        
        Returns:
            Tuple[str, str]: 問題と解答
            - latex_answer (str): latex形式と通常の文字列が混在していることを前提とした解答
            - latex_problem (str): latex形式と通常の文字列が混在していることを前提とした問題 
        """
        latex_answer = "dummy answer"
        latex_problem = "dummy problem"
        return latex_answer, latex_problem

    def _make_from_formula_to_condition_problem(self):
        """提示された問題の条件に合致する式を選ぶ問題の作成
        
        Returns:
            Tuple[str, str]: 問題と解答
            - latex_answer (str): latex形式と通常の文字列が混在していることを前提とした解答
            - latex_problem (str): latex形式と通常の文字列が混在していることを前提とした問題 
        """
        latex_answer = "dummy answer"
        latex_problem = "dummy problem"
        return latex_answer, latex_problem
    
    def _random_number_maker(self, min_value: int = 1, max_value: int = 10, mode: str = None) -> Union[sy.Integer, sy.Float, sy.Rational]:
        """指定された最小値以上、最大値以下の数を小数や整数、分数で出力する
        
        Args:
            min_value (int): 最小値。デフォルト値は1
            max_value (int): 最大値。デフォルト値は10。
            mode (str): 指定する数のタイプ。デフォルト値はNone。
        
        Returns:
            number (Union[sy.Integer, sy.Float, sy.Rational]): 指定された諸条件を満たした数
        
        Note:
            整数は指定された最大値、最小値をもとに値を返すが、分数・小数のときは、ランダム生成に利用される最大値と最小値となる。
        """
        if mode is None:
            selected_mode = choice(["integer", "float", "frac"])
        else:
            selected_mode = mode
        if selected_mode == "integer":
            number = sy.Integer(randint(min_value, max_value))
        elif selected_mode == "float":
            number = sy.Float(0.1 * randint(min_value, max_value))
        elif selected_mode == "frac":
            numerator = randint(min_value, max_value)
            denominator= randint(min_value, max_value)
            number = sy.Rational(numerator, denominator)
        else:
            raise ValueError(f"selected_mode is {selected_mode}. This isn't expected value.")
        return number
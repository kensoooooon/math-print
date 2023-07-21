"""
7/20
百分率をどう扱うか？
0.1 = 1/10は計算でも同様に扱えるが、10%になると話が変わる。
->初めの段階で分数に直すようにする？？
->表示をどうするか？
    現実的には問題の表示において、percentageが選択されたときに、問題文を変更する。
    どこで分岐させるべき？根本？途中？？？初手without, with??

7/21
引き続き百分率の扱いについて
    そもそもありうるパターンとして、
    frac
    decimal
    percentage
    frac, decimal
    frac, percentage
    decimal, percentage
    frac, decimal, percentage
    がある。
    
    percentageのありなしだけでも、途中で小数に挟むひと手間がかかる。
    ⇒あとは、最初で分けたほうが良いのか、それとも残り分けたほうがよいのかもんだい
"""

from random import choice, random, randint
from typing import Dict, NamedTuple, Optional, Tuple, Union

import sympy as sy


class RatioProblem:
    """指定された割合関連の値を求める問題とその解答を出力
    
    Attributes:
        _used_numbers_for_ratio (list): 割合に利用する数のタイプ(分数, 小数)が格納されている
        latex_answer (str): latex形式と通常の文字が混在した解答
        latex_problem (str): latex形式と通常の文字が混在した問題
    """
    def __init__(self, **settings: Dict) -> None:
        """初期設定
        
        Args:
            settings (dict): 問題の各種設定を格納
        
        Raises:
            ValueError: 想定されていない問題のタイプが混入したときに挙上
        """
        self._used_numbers_for_ratio = settings["used_numbers_for_ratio"]
        self._used_unit_change = settings["used_unit_change"]
        selected_problem_type = choice(settings["problem_types"])
        if selected_problem_type == "amount_to_compare":
            self.latex_answer, self.latex_problem = self._make_amount_to_compare_problem()
        elif selected_problem_type == "standard_amount":
            self.latex_answer, self.latex_problem = self._make_standard_amount_problem()
        elif selected_problem_type == "ratio":
            self.latex_answer, self.latex_problem = self._make_ratio_problem()
        else:
            raise ValueError(f"'selected_problem_type' is {selected_problem_type}. This isn't expected value.")
    
    def _make_amount_to_compare_problem(self) -> Tuple[str, str]:
        """比べる量を求める問題と解答を出力
        
        Returns:
            latex_answer (str): latex形式と通常の文字が混在した解答
            latex_problem (str): latex形式と通常の文字が混在した問題
        
        Develop:
            重さ、長さ、体積、人数や個数など
            割合以外は整数になるぱたーん
        """
        selected_theme = choice(["weight", "length", "volume", "quantity"])
        selected_ratio = 
        if selected_theme == "weight":
            ratio = self._random_ratio()
            standard_amount = self._random_integer(max_num=30)
            amount_to_compare = standard_amount * ratio
            if not(self._used_unit_change):
                from_to_unit = choice(["kg_to_kg", "g_to_g"])
                if from_to_unit == "kg_to_kg":
                    problem_sentence_checker = random()
                    if problem_sentence_checker < 0.25:
                        latex_problem = f"\\( {sy.latex(standard_amount)} \\mathrm{{kg}} \\)の\\( {sy.latex(ratio)} \\)は\\(  (\\, \\, \\, ) \\mathrm{{kg}} \\)です。"
                        latex_answer = f"\\( {sy.latex(standard_amount)} \\mathrm{{kg}} \\)がもとにする量、\\( {sy.latex(ratio)} \\)が割合なので、\n"
                        latex_answer += f"(比べる量) = (もとにする量) \\( \\times \\) (割合) \\( = {sy.latex(standard_amount)}  \\times {sy.latex(ratio)} = {sy.latex(amount_to_compare)} (\\mathrm{{kg}} ) \\)"
                    elif 0.25 <= problem_sentence_checker < 0.5:
                        item = self._random_item(selected_theme)
                        latex_problem = f"\\( {sy.latex(standard_amount)} \\mathrm{{kg}} \\)あった{item}のうち、\\( {sy.latex(ratio)} \\)を運びました。運んだ{item}の重さは\\( (\\, \\, \\, )  \\mathrm{{kg}} \\)です。"
                        latex_answer = f"\\( {sy.latex(standard_amount)} \\mathrm{{kg}} \\)がもとにする量、\\( {sy.latex(ratio)} \\)が割合なので、\n"
                        latex_answer += f"(比べる量) = (もとにする量) \\( \\times \\) (割合) \\( = {sy.latex(standard_amount)}  \\times {sy.latex(ratio)} = {sy.latex(amount_to_compare)} (\\mathrm{{kg}} )\\)"
                    elif 0.5 <= problem_sentence_checker < 0.75:
                        latex_problem = f"\\( {sy.latex(standard_amount)} \\mathrm{{kg}} \\)あった{item}のうち、\\( {sy.latex(ratio)} \\)を運びました。残った{item}の重さは\\( (\\, \\, \\, ) \\mathrm{{kg}} \\)です。"
                        latex_answer += f"まずは運んだ量を求める。\\( {sy.latex(standard_amount)} \\mathrm{{kg}} \\)がもとにする量、\\( {sy.latex(ratio)} \\)が割合なので、\n"
                        latex_answer += f"(比べる量) = (もとにする量) \\( \\times \\) (割合) \\( = {sy.latex(standard_amount)}  \\times {sy.latex(ratio)} = {sy.latex(amount_to_compare)} (\\mathrm{{kg}} )\\)が運んだ量となる。\n"
                        latex_answer += f"もともとあった{item}は\\( {sy.latex(standard_amount)} \\mathrm{{kg}} \\)なので、残った量は\\( {standard_amount} - {amount_to_compare} = {sy.latex(standard_amount - amount_to_compare)} \\mathrm{{kg}} \\)"
                    else:
                        pass
                elif from_to_unit == "g_to_g":
                    pass
            elif self._used_unit_change:
                from_to_unit = choice(["kg_to_g", "g_to_kg", ""])
        elif selected_theme == "length":
            pass
        elif selected_theme == "volume":
            pass
        elif selected_theme == "quantity":
            pass
        latex_answer = "dummy answer in amount to compare problem."
        latex_problem = "dummy problem in amount to compare problem."
        return latex_answer, latex_problem

    def _make_standard_amount_problem(self) -> Tuple[str, str]:
        """元の量を求める問題と解答を出力
        
        Returns:
            latex_answer (str): latex形式と通常の文字が混在した解答
            latex_problem (str): latex形式と通常の文字が混在した問題
        """
        latex_answer = "dummy answer in standard amount problem."
        latex_problem = "dummy problem in standard amount problem."
        return latex_answer, latex_problem

    def _make_ratio_problem(self) -> Tuple[str, str]:
        """割合を求める問題と解答を出力
        
        Returns:
            latex_answer (str): latex形式と通常の文字が混在した解答
            latex_problem (str): latex形式と通常の文字が混在した問題
        """
        latex_answer = "dummy answer in ratio problem."
        latex_problem = "dummy problem in ratio problem."
        return latex_answer, latex_problem


    def _random_integer(self, min_num: int = 1, max_num: int = 20) -> sy.Integer:
        """指定された範囲で整数を出力

        Args:
            min_num (int, optional): 最小値. Defaults to 1.
            max_num (int, optional): 最大値. Defaults to 20.
        
        Returns:
            integer (sy.Integer): 整数
        """
        integer = sy.Integer(randint(min_num, max_num))
        return integer
    
    def _random_ratio(self, digit_under_decimal_point: int = 1):
        """割合のための0より大きくて1より小さな値を、指定された形に応じて出力->割合の各表現（分数, 小数, 百分率, 歩合）をあわせて格納

        Args:
            digit_under_decimal_point (int, optional): 小数点以下の最大の桁数. デフォルトは1.

        Raises:
            ValueError: 想定されていない形が要求されたときに挙上

        Returns:
            ratio_units (RatioUnits): 計算に必要な値と、それに対応した各種表現を格納したコンテナ
        
        Debelopign:
        In [25]: for (digit, name) in zip(num2_list, names):
    ...:     print(digit)
    ...:     print(name)
    ...:     print("------------------------------------")
    ...:
        """
        class RatioUnits(NamedTuple):
            """割合を表現ごとにあわせて格納
            
            Args:
                ratio (sy.Float): 小数の割合
                decimal_ratio (str): latex表示された小数の割合
                frac_ratio (str): latex表示された分数の割合
                percentage (str): %表示された割合
                japanese_percentage (str): 割, 分, 厘で表示された割合
            """
            ratio: sy.Float
            decimal_ratio: str
            frac_ratio: str
            float_ratio_latex: str
            percentage: str
            japanese_percentage: str
        
        denominator = 10 ** digit_under_decimal_point
        numerator = (1, denominator - 1)
        frac = sy.Rational(numerator, denominator)
        ratio = sy.Float(frac)
        decimal_ratio = sy.latex(ratio)
        frac_ratio = sy.Rational(frac)
        percentage = f"{ratio * 100} \\%"
        digit_list = list(decimal_ratio)[2:]
        japanese_percentage_names = ["割", "分", "厘", "毛"]
        japanese_percentage = ""
        for digit, name in zip(digit_list, japanese_percentage_names):
            japanese_percentage += (digit + name)
        ratio_units = RatioUnits(
            ratio=ratio, decimal_ratio=decimal_ratio,
            frac_ratio=frac_ratio, percentage=percentage
            japanese_percentage=japanese_percentage
        )
        return ratio_units

    def _random_item(self, theme: str) -> str:
        """物品の名前をランダムに出力することで、問題のバリュエーションを増やす

        Args:
            theme (str): 物品をカウントする際に、着目することが多い単位

        Returns:
            selected_item (str): 選択された物品
        """
        if theme == "weight":
            items = [
                "砂", "小麦粉", "米", "水",
                "本", "紙", "アボガド",
            ]
        elif theme == "length":
            items = [
                "ロープ", "ひも", "リボン", "テープ",
                "ワイヤー", "ケーブル", "ロールケーキ",
            ]
        elif theme == "volume":
            items = [
                "水", "りんごジュース", "オレンジジュース", "牛乳",
                "炭酸水", "お茶", "レモネード",
            ]
        elif theme == "quantity":
            items = [
                "りんご", "みかん", "おはじき", "あめ",
                "石", "アボガド", "ビー玉",
            ]
        else:
            raise ValueError(f"'theme' is {theme}. This isn't expected.")
        selected_item = choice(items)
        return selected_item

from random import choice, random, randint
from typing import Dict, Optional, Tuple, Union

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
        if selected_theme == "weight":
            ratio = self._random_ratio
            standard_amount = self._random_integer(max_num=30)
            amount_to_compare = standard_amount * ratio
            if not(self._used_unit_change):
                from_to_unit = choice(["kg_to_kg", "g_to_g"])
                if from_to_unit == "kg_to_kg":
                    problem_sentence_checker = random()
                    if problem_sentence_checker < 0.25:
                        latex_problem = f"\\( {sy.latex(standard_amount)} \\mathrm{{kg}} \\)の\\( {sy.latex(ratio)} \\)は\\(  (\\, \\, \\, ) \\mathrm{{kg}} \\)です。"
                        latex_answer = f"\\( {sy.latex(standard_amount)} \\mathrm{{kg}} \\)がもとにする量、\\( {sy.latex(ratio)} \\)が割合なので、\n"
                        latex_answer += f"(比べる量) = (もとにする量) \\( \\times \\) (割合) \\( = {sy.latex(standard_amount)}  \\times {sy.latex(ratio)} = {sy.latex(amount_to_compare)} (\\mathrm{{kg}} )\\)"
                    elif 0.25 <= problem_sentence_checker < 0.5:
                        item = self._random_item(selected_theme)
                        latex_problem = f"\\( {sy.latex(standard_amount)} \\mathrm{{kg}} \\)あった{item}のうち、\\( {sy.latex(ratio)} \\)を運びました。運んだ{item}の重さは\\( (\\, \\, \\, )  \\mathrm{{kg}} \\)です。"
                        latex_answer = f"\\( {sy.latex(standard_amount)} \\mathrm{{kg}} \\)がもとにする量、\\( {sy.latex(ratio)} \\)が割合なので、\n"
                        latex_answer += f"(比べる量) = (もとにする量) \\( \\times \\) (割合) \\( = {sy.latex(standard_amount)}  \\times {sy.latex(ratio)} = {sy.latex(amount_to_compare)} (\\mathrm{{kg}} )\\)"
                    elif 0.5 <= problem_sentence_checker < 0.75:
                        pass
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
    
    def _random_ratio(self, digit_under_decimal_point: int = 1) -> Union[sy.Float, sy.Rational]:
        """割合のための0より大きくて1より小さな値を、指定された形に応じて出力

        Args:
            digit_under_decimal_point (int, optional): 小数点以下の最大の桁数. デフォルトは1.

        Raises:
            ValueError: 想定されていない形が要求されたときに挙上

        Returns:
            Union[sy.Float, sy.Rational]: 割合のための値
        """
        decimal_or_frac = choice(self._used_numbers_for_ratio)
        denominator = 10 ** digit_under_decimal_point
        numerator = (1, denominator - 1)
        frac_ratio = sy.Rational(numerator, denominator)
        decimal_ratio = sy.Float(decimal_ratio)
        if decimal_or_frac == "frac":
            return frac_ratio
        elif decimal_or_frac == "decimal":
            return decimal_ratio
        elif decimal_or_frac is None:
            if random() > 0.5:
                return frac_ratio
            else:
                return decimal_ratio
        else:
            raise ValueError(f"'decimal_or_frac' is {decimal_or_frac}. This must be 'frac' or 'decimal' or None.")

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

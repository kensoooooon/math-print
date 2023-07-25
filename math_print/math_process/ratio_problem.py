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

7/22
百分率、および割、分、厘の扱いについて
    全部細かく分けるのは正直アレ
    ->1つselectして、そこからざっくり使い分けたい
    
    percentage, japanese_percentageを使って、小数分数が選択されていない場合は？
    →強制的に小数を選ばざるを得ない。もともとの割合が小数を意識して作られているし、初めて学ぶのが小数になるから
    
    値と割合 eg. 34%=0.34, 2割3分=0.23,
    
    いっそ、小数と分数、もっというと6年の内容ではなく、5年の内容にフォーカスするのは？
        fracは抜いて、decimal, percentage, japanese_percentageで統一する

7/24
ratioまわり
    0.6が60.0%になる。
    ->.0patternのみを排除する？re??[:]??
    
    def decimal_normalize(f):
        text = str(f)
        while True:
            if ("." in text and text[-1] == "0") or (text[-1] == "."):
                text = text[:-1]
                continue
            break
        return text
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
        self._digit_under_the_decimal_point = settings["digit_under_the_decimal_point"]
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
        # selected_theme = choice(["weight", "length", "volume", "quantity"])
        selected_theme = "weight"
        if selected_theme == "weight":
            selected_ratio = choice(self._used_numbers_for_ratio)
            selected_digit_under_the_decimal_point = choice(self._digit_under_the_decimal_point)
            ratio, ratio_in_latex = self._random_ratio(selected_ratio=selected_ratio, digit_under_decimal_point=selected_digit_under_the_decimal_point)
            if not(self._used_unit_change):
                from_to_unit = choice(["kg_to_kg", "g_to_g"])
                standard_amount = self._random_integer(max_num=200)
                amount_to_compare = standard_amount * ratio
                if from_to_unit == "kg_to_kg":
                    unit_in_latex = "\\mathrm{kg}"
                elif from_to_unit == "kg_to_g":
                    unit_in_latex = "\\mathrm{g}"
                standard_amount_in_latex = f"\\( {sy.latex(standard_amount)} {unit_in_latex} \\)"
                problem_sentence_checker = random()
                if problem_sentence_checker < 0.25:
                    latex_problem = f"{standard_amount_in_latex}の{ratio_in_latex}は\\(  (\\, \\, \\, ) {unit_in_latex} \\)です。"
                    if selected_ratio == "decimal":
                        latex_answer = f"{standard_amount_in_latex}がもとにする量、{ratio_in_latex}が割合なので、\n"
                    elif (selected_ratio == "percentage") or (selected_ratio == "japanese_percentage"):
                        latex_answer = f"{ratio_in_latex}を小数の割合になおすと、\\( {sy.latex(ratio)} \\)となる。\n"
                        latex_answer += f"{standard_amount_in_latex}がもとにする量、\\( {sy.latex(ratio)} \\)が割合なので、\n"
                    latex_answer += f"(比べる量) = (もとにする量) \\( \\times \\) (割合) \\( = {sy.latex(standard_amount)}  \\times {sy.latex(ratio)} = {sy.latex(amount_to_compare)} ({unit_in_latex}) \\)"
                elif 0.25 <= problem_sentence_checker < 0.5:
                    item = self._random_item(selected_theme)
                    latex_problem = f"{standard_amount_in_latex}あった{item}のうち{ratio_in_latex}を運びました。運んだ{item}の重さは\\( (\\, \\, \\, )  {unit_in_latex} \\)です。"
                    if selected_ratio == "decimal":
                        latex_answer = f"{standard_amount_in_latex}がもとにする量、{ratio_in_latex}が割合なので、\n"
                    elif (selected_ratio == "percentage") or (selected_ratio == "japanese_percentage"):
                        latex_answer = f"{ratio_in_latex}を小数の割合になおすと、\\( {sy.latex(ratio)} \\)となる。\n"
                        latex_answer += f"{standard_amount_in_latex}がもとにする量、\\( {sy.latex(ratio)} \\)が割合なので、\n"
                    latex_answer += f"(比べる量) = (もとにする量) \\( \\times \\) (割合) \\( = {sy.latex(standard_amount)}  \\times {sy.latex(ratio)} = {sy.latex(amount_to_compare)} ({unit_in_latex} )\\)"
                elif 0.5 <= problem_sentence_checker < 0.75:
                    item = self._random_item(selected_theme)
                    latex_problem = f"{standard_amount_in_latex}あった{item}のうち、{ratio_in_latex}を運びました。残った{item}の重さは\\( (\\, \\, \\, ) {unit_in_latex} \\)です。"
                    if selected_ratio == "decimal":
                        latex_answer = f"まずは運んだ量を求めると、{standard_amount_in_latex}がもとにする量、{ratio_in_latex}が割合なので、\n"
                    elif (selected_ratio == "percentage") or (selected_ratio == "japanese_percentage"):
                        latex_answer = f"まずは{ratio_in_latex}を小数の割合になおすと、\\( {sy.latex(ratio)} \\)となる。\n"
                        latex_answer += f"次には運んだ量を求めると、{standard_amount_in_latex}がもとにする量、{ratio_in_latex}が割合なので、\n"
                    latex_answer += f"(比べる量) = (もとにする量) \\( \\times \\) (割合) \\( = {sy.latex(standard_amount)}  \\times {sy.latex(ratio)} = {sy.latex(amount_to_compare)} ({unit_in_latex} )\\)が運んだ量となる。\n"
                    latex_answer += f"もともとあった{item}は{standard_amount_in_latex}なので、残った量は\\( {sy.latex(standard_amount)} - {sy.latex(amount_to_compare)} = {sy.latex(standard_amount - amount_to_compare)} {unit_in_latex} \\)"
                else:
                    item = self._random_item(selected_theme)
                    increase_or_decrease = choice(["increase", "decrease"])
                    if increase_or_decrease == "increase":
                        latex_problem = f"{standard_amount_in_latex}の{item}を{ratio_in_latex}だけ増やしました。増やした後の重さは\\( (\\, \\, \\, ) {unit_in_latex} \\)です。"
                        if selected_ratio == "decimal":
                            latex_answer = f"まずは増やした量をもとめると、{standard_amount_in_latex}がもとにする量、{ratio_in_latex}が割合なので、\n"
                        elif (selected_ratio == "percentage") or (selected_ratio == "japanese_percentage"):
                            latex_answer = f"まずは{ratio_in_latex}を小数の割合になおすと、\\( {sy.latex(ratio)} \\)となる。\n"
                            latex_answer += f"次に増やした量を求めると、{standard_amount_in_latex}がもとにする量、\\( {sy.latex(ratio)} \\)が割合なので、\n"
                        latex_answer += f"(比べる量) = (もとにする量) \\( \\times \\) (割合) \\( = {sy.latex(standard_amount)}  \\times {sy.latex(ratio)} = {sy.latex(amount_to_compare)} ({unit_in_latex} )\\)が増やした量となる。\n" 
                        latex_answer += f"もともとあった{item}は{standard_amount_in_latex}なので、増やした後の重さは\\( {sy.latex(standard_amount)} + {sy.latex(amount_to_compare)} = {sy.latex(standard_amount + amount_to_compare)} {unit_in_latex} \\)"                           
                    elif increase_or_decrease == "decrease":
                        latex_problem = f"{standard_amount_in_latex}の{item}を{ratio_in_latex}だけ減らした。減らした後の重さは\\( (\\, \\, \\, ) {unit_in_latex} \\)です。"
                        if selected_ratio == "decimal":
                            latex_answer = f"まずは減らした量をもとめると、{standard_amount_in_latex}がもとにする量、{ratio_in_latex}が割合なので、\n"
                        elif (selected_ratio == "percentage") or (selected_ratio == "japanese_percentage"):
                            latex_answer = f"まずは{ratio_in_latex}を小数の割合になおすと、\\( {sy.latex(ratio)} \\)となる。\n"
                            latex_answer += f"次に減らした量を求めると、{standard_amount_in_latex}がもとにする量、\\( {sy.latex(ratio)} \\)が割合なので、\n"
                        latex_answer += f"(比べる量) = (もとにする量) \\( \\times \\) (割合) \\( = {sy.latex(standard_amount)}  \\times {sy.latex(ratio)} = {sy.latex(amount_to_compare)} ({unit_in_latex} )\\)が増やした量となる。\n" 
                        latex_answer += f"もともとあった{item}は{standard_amount_in_latex}なので、減らした後の重さは\\( {sy.latex(standard_amount)} - {sy.latex(amount_to_compare)} = {sy.latex(standard_amount - amount_to_compare)} {unit_in_latex} \\)"                    
            elif self._used_unit_change:
                from_to_unit = choice(["kg_to_g", "g_to_kg"])
                if from_to_unit == "kg_to_g":
                    from_unit_in_latex = "\\mathrm{kg}"
                    to_unit_in_latex = "\\mathrm{g}"
                    from_standard_amount = self._random_integer(max_num=20)
                    from_amount_to_compare = from_standard_amount * ratio
                    to_amount_to_compare = from_amount_to_compare * 1000
                elif from_to_unit == "g_to_kg":
                    from_unit_in_latex = "\\mathrm{g}"
                    to_unit_in_latex = "\\mathrm{kg}"
                    from_standard_amount = 250 * self._random_integer(20)
                    from_amount_to_compare = from_standard_amount * ratio
                    to_amount_to_compare = from_amount_to_compare / 1000
                from_standard_amount_in_latex = f"\\( {sy.latex(standard_amount)} {from_unit_in_latex} \\)"
                from_amount_to_compare_in_latex = f"\\( {sy.latex(standard_amount)} {from_unit_in_latex}\\)" 
                to_amount_to_compare_in_latex = f"\\( {sy.latex(to_amount_to_compare)} {to_unit_in_latex} \\)"
                problem_sentence_checker = random()
                if problem_sentence_checker < 0.25:
                    latex_problem = f"{from_standard_amount_in_latex}の{ratio_in_latex}は\\(  (\\, \\, \\, ) {to_unit_in_latex} \\)です。"
                    if selected_ratio == "decimal":
                        latex_answer = f"{from_standard_amount_in_latex}がもとにする量、{ratio_in_latex}が割合なので、\n"
                    elif (selected_ratio == "percentage") or (selected_ratio == "japanese_percentage"):
                        latex_answer = f"{ratio_in_latex}を小数の割合になおすと、\\( {sy.latex(ratio)} \\)となる。\n"
                        latex_answer += f"{standard_amount_in_latex}がもとにする量、\\( {sy.latex(ratio)} \\)が割合なので、\n"
                    latex_answer += f"(比べる量) = (もとにする量) \\( \\times \\) (割合) \\( = {sy.latex(from_standard_amount)}  \\times {sy.latex(ratio)} = {sy.latex(from_amount_to_compare)} ({from_unit_in_latex}) \\)"
                    latex_answer += f"さらにこれを指定された単位になおすと、\\( {to_amount_to_compare_in_latex} \\)となる。"
                # next
                elif 0.25 <= problem_sentence_checker < 0.5:
                    item = self._random_item(selected_theme)
                    latex_problem = f"{from_standard_amount_in_latex}あった{item}のうち{ratio_in_latex}を運びました。運んだ{item}の重さは\\( (\\, \\, \\, )  {to_unit_in_latex} \\)です。"
                    if selected_ratio == "decimal":
                        latex_answer = f"{standard_amount_in_latex}がもとにする量、{ratio_in_latex}が割合なので、\n"
                    elif (selected_ratio == "percentage") or (selected_ratio == "japanese_percentage"):
                        latex_answer = f"{ratio_in_latex}を小数の割合になおすと、\\( {sy.latex(ratio)} \\)となる。\n"
                        latex_answer += f"{standard_amount_in_latex}がもとにする量、\\( {sy.latex(ratio)} \\)が割合なので、\n"
                    latex_answer += f"(比べる量) = (もとにする量) \\( \\times \\) (割合) \\( = {sy.latex(standard_amount)}  \\times {sy.latex(ratio)} = {sy.latex(amount_to_compare)} ({unit_in_latex} )\\)"
                elif 0.5 <= problem_sentence_checker < 0.75:
                    item = self._random_item(selected_theme)
                    latex_problem = f"{standard_amount_in_latex}あった{item}のうち、{ratio_in_latex}を運びました。残った{item}の重さは\\( (\\, \\, \\, ) {unit_in_latex} \\)です。"
                    if selected_ratio == "decimal":
                        latex_answer = f"まずは運んだ量を求めると、{standard_amount_in_latex}がもとにする量、{ratio_in_latex}が割合なので、\n"
                    elif (selected_ratio == "percentage") or (selected_ratio == "japanese_percentage"):
                        latex_answer = f"まずは{ratio_in_latex}を小数の割合になおすと、\\( {sy.latex(ratio)} \\)となる。\n"
                        latex_answer += f"次には運んだ量を求めると、{standard_amount_in_latex}がもとにする量、{ratio_in_latex}が割合なので、\n"
                    latex_answer += f"(比べる量) = (もとにする量) \\( \\times \\) (割合) \\( = {sy.latex(standard_amount)}  \\times {sy.latex(ratio)} = {sy.latex(amount_to_compare)} ({unit_in_latex} )\\)が運んだ量となる。\n"
                    latex_answer += f"もともとあった{item}は{standard_amount_in_latex}なので、残った量は\\( {sy.latex(standard_amount)} - {sy.latex(amount_to_compare)} = {sy.latex(standard_amount - amount_to_compare)} {unit_in_latex} \\)"
                else:
                    item = self._random_item(selected_theme)
                    increase_or_decrease = choice(["increase", "decrease"])
                    if increase_or_decrease == "increase":
                        latex_problem = f"{standard_amount_in_latex}の{item}を{ratio_in_latex}だけ増やしました。増やした後の重さは\\( (\\, \\, \\, ) {unit_in_latex} \\)です。"
                        if selected_ratio == "decimal":
                            latex_answer = f"まずは増やした量をもとめると、{standard_amount_in_latex}がもとにする量、{ratio_in_latex}が割合なので、\n"
                        elif (selected_ratio == "percentage") or (selected_ratio == "japanese_percentage"):
                            latex_answer = f"まずは{ratio_in_latex}を小数の割合になおすと、\\( {sy.latex(ratio)} \\)となる。\n"
                            latex_answer += f"次に増やした量を求めると、{standard_amount_in_latex}がもとにする量、\\( {sy.latex(ratio)} \\)が割合なので、\n"
                        latex_answer += f"(比べる量) = (もとにする量) \\( \\times \\) (割合) \\( = {sy.latex(standard_amount)}  \\times {sy.latex(ratio)} = {sy.latex(amount_to_compare)} ({unit_in_latex} )\\)が増やした量となる。\n" 
                        latex_answer += f"もともとあった{item}は{standard_amount_in_latex}なので、増やした後の重さは\\( {sy.latex(standard_amount)} + {sy.latex(amount_to_compare)} = {sy.latex(standard_amount + amount_to_compare)} {unit_in_latex} \\)"                           
                    elif increase_or_decrease == "decrease":
                        latex_problem = f"{standard_amount_in_latex}の{item}を{ratio_in_latex}だけ減らした。減らした後の重さは\\( (\\, \\, \\, ) {unit_in_latex} \\)です。"
                        if selected_ratio == "decimal":
                            latex_answer = f"まずは減らした量をもとめると、{standard_amount_in_latex}がもとにする量、{ratio_in_latex}が割合なので、\n"
                        elif (selected_ratio == "percentage") or (selected_ratio == "japanese_percentage"):
                            latex_answer = f"まずは{ratio_in_latex}を小数の割合になおすと、\\( {sy.latex(ratio)} \\)となる。\n"
                            latex_answer += f"次に減らした量を求めると、{standard_amount_in_latex}がもとにする量、\\( {sy.latex(ratio)} \\)が割合なので、\n"
                        latex_answer += f"(比べる量) = (もとにする量) \\( \\times \\) (割合) \\( = {sy.latex(standard_amount)}  \\times {sy.latex(ratio)} = {sy.latex(amount_to_compare)} ({unit_in_latex} )\\)が増やした量となる。\n" 
                        latex_answer += f"もともとあった{item}は{standard_amount_in_latex}なので、減らした後の重さは\\( {sy.latex(standard_amount)} - {sy.latex(amount_to_compare)} = {sy.latex(standard_amount - amount_to_compare)} {unit_in_latex} \\)"  
        elif selected_theme == "length":
            latex_answer = "dummy answer in amout to compare problem in length."
            latex_problem = "dummpy problem in amount to compare problem in length."
        elif selected_theme == "volume":
            latex_answer = "dummy answer in amout to compare problem in volume."
            latex_problem = "dummpy problem in amount to compare problem in volume."
        elif selected_theme == "quantity":
            latex_answer = "dummy answer in amout to compare problem in quantity."
            latex_problem = "dummpy problem in amount to compare problem in quantity."
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
    
    def _random_ratio(self, selected_ratio, digit_under_decimal_point: int = 1):
        """割合のための0より大きくて1より小さな値を、指定された形に応じて出力->割合の各表現（分数, 小数, 百分率, 歩合）をあわせて格納

        Args:
            selected_ratio (str): 割合の表示に用いたい形式(小数or百分率or日本式の百分率)
            digit_under_decimal_point (int, optional): 小数点以下の最大の桁数. デフォルトは1.

        Raises:
            ValueError: 想定されていない形が要求されたときに挙上

        Returns:
            ratio_value (sy.Float): 計算に用いる小数の割合
            ratio_in_latex (str): latexが入り混じった問題や解答で、そのまま用いることができる割合

        for _ in range(10):
            under_the_decimal_point = randint(1, 2)
            num = (0.1 ** under_the_decimal_point) * randint(1, 10 ** under_the_decimal_point - 1)
            print(f"num:{num}")
            print(f"latex:{sy.latex(num)}")
            print(f"multi: {num * 100}")
            print(f"percentage: {sy.latex(num * 100)}")
            print("----------------------")
        """        
        # denominator = 10 ** digit_under_decimal_point
        # numerator = randint(1, denominator - 1)
        # frac = sy.Rational(numerator, denominator)
        # ratio_value = sy.Float(frac)
        
        def decimal_normalize(f):
            text = str(f)
            while True:
                if ("." in text and text[-1] == "0") or (text[-1] == "."):
                    text = text[:-1]
                    continue
                break
            return text
        
        ratio_value = (10 ** -digit_under_decimal_point) * randint(1, 10 ** digit_under_decimal_point - 1)
        if selected_ratio == "decimal":
            ratio_in_latex = f"\\( {sy.latex(ratio_value)} \\)"
        elif selected_ratio == "percentage":
            normalized_percentage = decimal_normalize(sy.latex(ratio_value * 100))
            ratio_in_latex = f"\\( {normalized_percentage} \\% \\)"
        elif selected_ratio == "japanese_percentage":
            digit_list = sy.latex(ratio_value)[2:]
            japanese_percentage_names = ["割", "分", "厘", "毛"]
            japanese_percentage_str = ""
            for digit, name in zip(digit_list, japanese_percentage_names):
                japanese_percentage_str += (digit + name)
            ratio_in_latex = japanese_percentage_str
        return ratio_value, ratio_in_latex

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

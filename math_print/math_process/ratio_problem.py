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


7/27
重さの分は完成。ただ、表記がぶれていてすこぶる見づらい

7/28
修正はそこそこ完了。次は単位ごとに大いに重複している記入と、それを他の単位にも使い回せるように
    quantityを省く？単位の変換も使わないし、かなり異質。

7/31
元になる量の計算

8/2
一通り。減らした後＋同じ単位の問題が怪しい

8/3
多分ok。次は解説

8/6
解説進行中。()より、___で下線を使ったほうがわかりやすい？
解説文中で問題に誘導をかける？？
→パラメータの設定とかで若干迷う系だが、ユーザ側からするとわかりやすいかもしれない？
"""

from random import choice, random, randint
from typing import Dict, Tuple, Union

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
        """
        selected_ratio = choice(self._used_numbers_for_ratio)
        selected_digit_under_the_decimal_point = choice(self._digit_under_the_decimal_point)
        ratio_value, ratio_out_of_latex = self._random_ratio(selected_ratio=selected_ratio, digit_under_decimal_point=selected_digit_under_the_decimal_point)
        ratio_value_in_latex = self._decimal_normalize(sy.latex(ratio_value))
        if self._used_unit_change:
            change_unit = choice([True, False])
        else:
            change_unit = False
        selected_theme = choice(["weight", "length", "area", "volume"])
        if not(change_unit):
            if selected_theme == "weight":
                japanese_unit = "重さ"
                from_to_unit = choice(["kg_to_kg", "g_to_g"])
                standard_amount = 10 * self._random_integer(max_num=20)
                amount_to_compare = standard_amount * ratio_value
                amount_to_compare_in_latex = f"{self._decimal_normalize(sy.latex(amount_to_compare))}"
                if from_to_unit == "kg_to_kg":
                    unit_in_latex = "\\mathrm{kg}"
                elif from_to_unit == "g_to_g":
                    unit_in_latex = "\\mathrm{g}"
            elif selected_theme == "length":
                japanese_unit = "長さ"
                from_to_unit = choice(["m_to_m", "cm_to_cm"])
                standard_amount = 10 * self._random_integer(max_num=20)
                amount_to_compare = standard_amount * ratio_value
                amount_to_compare_in_latex = f"{self._decimal_normalize(sy.latex(amount_to_compare))}"
                if from_to_unit == "m_to_m":
                    unit_in_latex = "\\mathrm{m}"
                elif from_to_unit == "cm_to_cm":
                    unit_in_latex = "\\mathrm{cm}"
            elif selected_theme == "area":
                japanese_unit = "面積"
                from_to_unit = choice(["m^2_to_m^2", "cm^2_to_cm^2"])
                standard_amount = 10 * self._random_integer(max_num=20)
                amount_to_compare = standard_amount * ratio_value
                amount_to_compare_in_latex = f"{self._decimal_normalize(sy.latex(amount_to_compare))}"
                if from_to_unit == "m^2_to_m^2":
                    unit_in_latex = "\\mathrm{m^2}"
                elif from_to_unit == "cm^2_to_cm^2":
                    unit_in_latex = "\\mathrm{{cm}^2}"
            elif selected_theme == "volume":
                japanese_unit = "体積"
                from_to_unit = choice(["m^3_to_m^3", "cm^3_to_cm^3"])
                standard_amount = 10 * self._random_integer(max_num=20)
                amount_to_compare = standard_amount * ratio_value
                amount_to_compare_in_latex = f"{self._decimal_normalize(sy.latex(amount_to_compare))}"
                if from_to_unit == "m^3_to_m^3":
                    unit_in_latex = "\\mathrm{m^3}"
                elif from_to_unit == "cm^3_to_cm^3":
                    unit_in_latex = "\\mathrm{{cm}^3}"
            standard_amount_in_latex = f"{self._decimal_normalize(sy.latex(standard_amount))}"
            standard_amount_out_of_latex_with_unit = f"\\( {standard_amount_in_latex} {unit_in_latex} \\)"
            problem_sentence_checker = random()
            if problem_sentence_checker < 0.25:
                latex_problem = f"{standard_amount_out_of_latex_with_unit}の{ratio_out_of_latex}は\\( \\underline{{\\qquad\\qquad}} {unit_in_latex} \\)です。"
                if selected_ratio == "decimal":
                    latex_answer = f"{standard_amount_out_of_latex_with_unit}がもとにする量、{ratio_out_of_latex}が割合なので、\n"
                elif (selected_ratio == "percentage") or (selected_ratio == "japanese_percentage"):
                    latex_answer = f"{ratio_out_of_latex}を小数の割合になおすと、\\( {ratio_value_in_latex} \\)となる。\n"
                    latex_answer += f"{standard_amount_out_of_latex_with_unit}がもとにする量、\\( {ratio_value_in_latex}\\)が割合なので、\n"
                latex_answer += f"(比べる量) = (もとにする量) \\( \\times \\) (割合) \\( = {standard_amount_in_latex} \\times {ratio_value_in_latex} = {amount_to_compare_in_latex} {unit_in_latex} \\)"
            elif 0.25 <= problem_sentence_checker < 0.5:
                item = self._random_item(selected_theme)
                latex_problem = f"{standard_amount_out_of_latex_with_unit}あった{item}のうち{ratio_out_of_latex}を運びました。\n運んだ{item}の{japanese_unit}は\\( \\underline{{\\qquad\\qquad}} {unit_in_latex} \\)です。"
                if selected_ratio == "decimal":
                    latex_answer = f"{standard_amount_out_of_latex_with_unit}がもとにする量、{ratio_out_of_latex}が割合なので、\n"
                elif (selected_ratio == "percentage") or (selected_ratio == "japanese_percentage"):
                    latex_answer = f"{ratio_out_of_latex}を小数の割合になおすと、\\( {ratio_value_in_latex}\\)となる。\n"
                    latex_answer += f"{standard_amount_out_of_latex_with_unit}がもとにする量、\\( {ratio_value_in_latex}\\)が割合なので、\n"
                latex_answer += f"(比べる量) = (もとにする量) \\( \\times \\) (割合) \\( = {standard_amount_in_latex}  \\times {ratio_value_in_latex}= {amount_to_compare_in_latex} {unit_in_latex} \\)"
            elif 0.5 <= problem_sentence_checker < 0.75:
                item = self._random_item(selected_theme)
                latex_problem = f"{standard_amount_out_of_latex_with_unit}あった{item}のうち、{ratio_out_of_latex}を運びました。\n残った{item}の{japanese_unit}は\\( \\underline{{\\qquad\\qquad}} {unit_in_latex} \\)です。"
                if selected_ratio == "decimal":
                    latex_answer = f"まずは運んだ量を求めると、{standard_amount_out_of_latex_with_unit}がもとにする量、{ratio_value_in_latex}が割合なので、\n"
                elif (selected_ratio == "percentage") or (selected_ratio == "japanese_percentage"):
                    latex_answer = f"まずは{ratio_out_of_latex}を小数の割合になおすと、\\( {ratio_value_in_latex}\\)となる。\n"
                    latex_answer += f"次には運んだ量を求めると、{standard_amount_out_of_latex_with_unit}がもとにする量、\\( {ratio_value_in_latex} \\)が割合なので、\n"
                latex_answer += f"(比べる量) = (もとにする量) \\( \\times \\) (割合) \\( = {standard_amount_in_latex}  \\times {ratio_value_in_latex}= {amount_to_compare_in_latex} {unit_in_latex} \\)が運んだ量となる。\n"
                latex_answer += f"もともとあった{item}は{standard_amount_out_of_latex_with_unit}なので、残った量は\\( {standard_amount_in_latex} - {amount_to_compare_in_latex} = {self._decimal_normalize(sy.latex(standard_amount - amount_to_compare))} {unit_in_latex} \\)"
            else:
                item = self._random_item(selected_theme)
                increase_or_decrease = choice(["increase", "decrease"])
                if increase_or_decrease == "increase":
                    latex_problem = f"{standard_amount_out_of_latex_with_unit}の{item}を{ratio_out_of_latex}だけ増やしました。\n増やした後の{japanese_unit}は\\( \\underline{{\\qquad\\qquad}} {unit_in_latex} \\)です。"
                    if selected_ratio == "decimal":
                        latex_answer = f"まずは増やした量をもとめると、{standard_amount_out_of_latex_with_unit}がもとにする量、{ratio_value_in_latex}が割合なので、\n"
                    elif (selected_ratio == "percentage") or (selected_ratio == "japanese_percentage"):
                        latex_answer = f"まずは{ratio_value_in_latex}を小数の割合になおすと、\\( {ratio_value_in_latex}\\)となる。\n"
                        latex_answer += f"次に増やした量を求めると、{standard_amount_out_of_latex_with_unit}がもとにする量、\\( {ratio_value_in_latex}\\)が割合なので、\n"
                    latex_answer += f"(比べる量) = (もとにする量) \\( \\times \\) (割合) \\( = {standard_amount_in_latex}  \\times {ratio_value_in_latex}= {amount_to_compare_in_latex} {unit_in_latex} \\)が増やした量となる。\n" 
                    latex_answer += f"もともとあった{item}は{standard_amount_out_of_latex_with_unit}なので、増やした後の{japanese_unit}は\\( {standard_amount_in_latex} + {amount_to_compare_in_latex} = {self._decimal_normalize(sy.latex(standard_amount + amount_to_compare))} {unit_in_latex} \\)"                           
                elif increase_or_decrease == "decrease":
                    latex_problem = f"{standard_amount_out_of_latex_with_unit}の{item}を{ratio_out_of_latex}だけ減らしました。減らした後の{japanese_unit}は\\( \\underline{{\\qquad\\qquad}} {unit_in_latex} \\)です。"
                    if selected_ratio == "decimal":
                        latex_answer = f"まずは減らした量をもとめると、{standard_amount_out_of_latex_with_unit}がもとにする量、{ratio_value_in_latex}が割合なので、\n"
                    elif (selected_ratio == "percentage") or (selected_ratio == "japanese_percentage"):
                        latex_answer = f"まずは{ratio_value_in_latex}を小数の割合になおすと、\\( {ratio_value_in_latex}\\)となる。\n"
                        latex_answer += f"次に減らした量を求めると、{standard_amount_out_of_latex_with_unit}がもとにする量、\\( {ratio_value_in_latex}\\)が割合なので、\n"
                    latex_answer += f"(比べる量) = (もとにする量) \\( \\times \\) (割合) \\( = {standard_amount_in_latex}  \\times {ratio_value_in_latex}= {amount_to_compare_in_latex} {unit_in_latex} \\)が増やした量となる。\n" 
                    latex_answer += f"もともとあった{item}は{standard_amount_out_of_latex_with_unit}なので、減らした後の{japanese_unit}は\\( {standard_amount_in_latex} - {amount_to_compare_in_latex} = {self._decimal_normalize(sy.latex(standard_amount - amount_to_compare))} {unit_in_latex} \\)"                    
        elif change_unit:
            if selected_theme == "weight":
                japanese_unit = "重さ"
                from_to_unit = choice(["kg_to_g", "g_to_kg"])
                if from_to_unit == "kg_to_g":
                    from_unit_in_latex = "\\mathrm{kg}"
                    to_unit_in_latex = "\\mathrm{g}"
                    from_standard_amount = self._random_integer(max_num=20)
                    from_amount_to_compare = from_standard_amount * ratio_value
                    to_amount_to_compare = from_amount_to_compare * 1000
                elif from_to_unit == "g_to_kg":
                    from_unit_in_latex = "\\mathrm{g}"
                    to_unit_in_latex = "\\mathrm{kg}"
                    from_standard_amount = 250 * self._random_integer(20)
                    from_amount_to_compare = from_standard_amount * ratio_value
                    to_amount_to_compare = from_amount_to_compare / 1000
            elif selected_theme == "length":
                japanese_unit = "長さ"
                from_to_unit = choice(["m_to_cm", "cm_to_m"])
                if from_to_unit == "m_to_cm":
                    from_unit_in_latex = "\\mathrm{m}"
                    to_unit_in_latex = "\\mathrm{cm}"
                    from_standard_amount = self._random_integer(max_num=20)
                    from_amount_to_compare = from_standard_amount * ratio_value
                    to_amount_to_compare = from_amount_to_compare * 100
                elif from_to_unit == "cm_to_m":
                    from_unit_in_latex = "\\mathrm{cm}"
                    to_unit_in_latex = "\\mathrm{m}"
                    from_standard_amount = 25 * self._random_integer(max_num=20)
                    from_amount_to_compare = from_standard_amount * ratio_value
                    to_amount_to_compare = from_amount_to_compare / 100
            elif selected_theme == "area":
                japanese_unit = "面積"
                from_to_unit = choice(["m^2_to_cm^2", "cm^2_to_m^2"])
                if from_to_unit == "m^2_to_cm^2":
                    from_unit_in_latex = "\\mathrm{m^2}"
                    to_unit_in_latex = "\\mathrm{{cm}^2}"
                    from_standard_amount = self._random_integer(max_num=20)
                    from_amount_to_compare = from_standard_amount * ratio_value
                    to_amount_to_compare = from_amount_to_compare * 100
                elif from_to_unit == "cm^2_to_m^2":
                    from_unit_in_latex = "\\mathrm{{cm}^2}"
                    to_unit_in_latex = "\\mathrm{m^2}"
                    from_standard_amount = 250 * self._random_integer(max_num=20)
                    from_amount_to_compare = from_standard_amount * ratio_value
                    to_amount_to_compare = from_amount_to_compare / 100
            elif selected_theme == "volume":
                japanese_unit = "体積"
                from_to_unit = choice(["m^3_to_cm^3", "cm^3_to_m^3"])
                if from_to_unit == "m^3_to_cm^3":
                    from_unit_in_latex = "\\mathrm{m^3}"
                    to_unit_in_latex = "\\mathrm{{cm}^3}"
                    from_standard_amount = self._random_integer(max_num=10)
                    from_amount_to_compare = from_standard_amount * ratio_value
                    to_amount_to_compare = from_amount_to_compare * ((10 ** 2) ** 3)
                elif from_to_unit == "cm^3_to_m^3":
                    from_unit_in_latex = "\\mathrm{{cm}^3}"
                    to_unit_in_latex = "\\mathrm{m^3}"
                    from_standard_amount = 25000 * self._random_integer(20)
                    from_amount_to_compare = from_standard_amount * ratio_value
                    to_amount_to_compare = from_amount_to_compare / ((10 ** 2) ** 3)
            from_standard_amount_in_latex = f"{self._decimal_normalize(sy.latex(from_standard_amount))}"
            from_standard_amount_out_of_latex_with_unit = f"\\( {from_standard_amount_in_latex} {from_unit_in_latex} \\)"
            from_amount_to_compare_in_latex = f"{self._decimal_normalize(sy.latex(from_amount_to_compare))}"
            from_amount_to_compare_in_latex_with_unit = f"{from_amount_to_compare_in_latex} {from_unit_in_latex}" 
            to_amount_to_compare_in_latex = f"{self._decimal_normalize(sy.latex(to_amount_to_compare))}"
            to_amount_to_compare_out_of_latex_with_unit = f"\\( {to_amount_to_compare_in_latex} {to_unit_in_latex} \\)"
            problem_sentence_checker = random()
            if problem_sentence_checker < 0.25:
                latex_problem = f"{from_standard_amount_out_of_latex_with_unit}の{ratio_out_of_latex}は\\( \\underline{{\\qquad\\qquad}} {to_unit_in_latex} \\)です。"
                if selected_ratio == "decimal":
                    latex_answer = f"{from_standard_amount_out_of_latex_with_unit}がもとにする量、\\( {ratio_value_in_latex} \\)が割合なので、\n"
                elif (selected_ratio == "percentage") or (selected_ratio == "japanese_percentage"):
                    latex_answer = f"{ratio_out_of_latex}を小数の割合になおすと、\\( {ratio_value_in_latex}\\)となる。\n"
                    latex_answer += f"{from_standard_amount_out_of_latex_with_unit}がもとにする量、\\( {ratio_value_in_latex}\\)が割合なので、\n"
                latex_answer += f"(比べる量) = (もとにする量) \\( \\times \\) (割合) \\( = {from_standard_amount_in_latex}  \\times {ratio_value_in_latex} = {from_amount_to_compare_in_latex_with_unit} \\)\n"
                latex_answer += f"さらにこれを指定された単位になおすと、{to_amount_to_compare_out_of_latex_with_unit}となる。"
            elif 0.25 <= problem_sentence_checker < 0.5:
                item = self._random_item(selected_theme)
                latex_problem = f"{from_standard_amount_out_of_latex_with_unit}あった{item}のうち{ratio_out_of_latex}を運びました。\n運んだ{item}の{japanese_unit}は\\( \\underline{{\\qquad\\qquad}} {to_unit_in_latex} \\)です。"
                if selected_ratio == "decimal":
                    latex_answer = f"{from_standard_amount_out_of_latex_with_unit}がもとにする量、\\( {ratio_value_in_latex} \\)が割合なので、\n"
                elif (selected_ratio == "percentage") or (selected_ratio == "japanese_percentage"):
                    latex_answer = f"{ratio_out_of_latex}を小数の割合になおすと、\\( {ratio_value_in_latex}\\)となる。\n"
                    latex_answer += f"{from_standard_amount_out_of_latex_with_unit}がもとにする量、\\( {ratio_value_in_latex}\\)が割合なので、\n"
                latex_answer += f"(比べる量) = (もとにする量) \\( \\times \\) (割合) \\( = {from_standard_amount_in_latex} \\times {ratio_value_in_latex} = {from_amount_to_compare_in_latex_with_unit} \\)\n"
                latex_answer += f"さらにこれを指定された単位になおすと、{to_amount_to_compare_out_of_latex_with_unit}となる。"
            elif 0.5 <= problem_sentence_checker < 0.75:
                item = self._random_item(selected_theme)
                latex_problem = f"{from_standard_amount_out_of_latex_with_unit}あった{item}のうち、{ratio_out_of_latex}を運びました。\n残った{item}の{japanese_unit}は\\( \\underline{{\\qquad\\qquad}} {to_unit_in_latex} \\)です。"
                if selected_ratio == "decimal":
                    latex_answer = f"まずは運んだ量を求めると、{from_standard_amount_out_of_latex_with_unit}がもとにする量、\\( {ratio_value_in_latex} \\)が割合なので、\n"
                elif (selected_ratio == "percentage") or (selected_ratio == "japanese_percentage"):
                    latex_answer = f"まずは{ratio_out_of_latex}を小数の割合になおすと、\\( {ratio_value_in_latex}\\)となる。\n"
                    latex_answer += f"次に運んだ量を求めると、{from_standard_amount_out_of_latex_with_unit}がもとにする量、\\( {ratio_value_in_latex}\\)が割合なので、\n"
                latex_answer += f"(比べる量) = (もとにする量) \\( \\times \\) (割合) \\( = {from_standard_amount_in_latex} \\times {ratio_value_in_latex} = {from_amount_to_compare_in_latex_with_unit} \\)が運んだ量となる。\n"
                from_remained = from_standard_amount - from_amount_to_compare
                from_remained_in_latex = f"{self._decimal_normalize(sy.latex(from_remained))}"
                from_remained_in_latex_with_unit = f"{from_remained_in_latex} {from_unit_in_latex}"
                if from_to_unit == "kg_to_g":
                    to_remained = from_remained * 1000
                elif from_to_unit == "g_to_kg":
                    to_remained = from_remained / 1000
                elif from_to_unit == "m_to_cm":
                    to_remained = from_remained * 100
                elif from_to_unit == "cm_to_m":
                    to_remained = from_remained / 100
                elif from_to_unit == "m^2_to_cm^2":
                    to_remained = from_remained * ((10 ** 2) ** 2)
                elif from_to_unit == "cm^2_to_m^2":
                    to_remained = from_remained / ((10 ** 2) ** 2)
                elif from_to_unit == "m^3_to_cm^3":
                    to_remained = from_remained * ((10 ** 2) ** 3)
                elif from_to_unit == "cm^3_to_m^3":
                    to_remained = from_remained / ((10 ** 2) ** 3)
                to_remained_out_of_latex_with_unit = f"\\( {self._decimal_normalize(sy.latex(to_remained))} {to_unit_in_latex} \\)"
                latex_answer += f"もともとあった{item}は{from_standard_amount_out_of_latex_with_unit}なので、残った量は\\( {from_standard_amount_in_latex} - {from_amount_to_compare_in_latex} = {from_remained_in_latex_with_unit} \\)\n"
                latex_answer += f"さらにこれを指定された単位になおすと、{to_remained_out_of_latex_with_unit}となる。"
            else:
                item = self._random_item(selected_theme)
                increase_or_decrease = choice(["increase", "decrease"])
                if increase_or_decrease == "increase":
                    latex_problem = f"{from_standard_amount_out_of_latex_with_unit}の{item}を{ratio_out_of_latex}だけ増やしました。\n増やした後の{japanese_unit}は\\( \\underline{{\\qquad\\qquad}} {to_unit_in_latex} \\)です。"
                    if selected_ratio == "decimal":
                        latex_answer = f"まずは増やした量をもとめると、{from_standard_amount_out_of_latex_with_unit}がもとにする量、\\( {ratio_value_in_latex} \\)が割合なので、\n"
                    elif (selected_ratio == "percentage") or (selected_ratio == "japanese_percentage"):
                        latex_answer = f"まずは{ratio_out_of_latex}を小数の割合になおすと、\\( {ratio_value_in_latex}\\)となる。\n"
                        latex_answer += f"次に増やした量を求めると、{from_standard_amount_out_of_latex_with_unit}がもとにする量、\\( {ratio_value_in_latex}\\)が割合なので、\n"
                    latex_answer += f"(比べる量) = (もとにする量) \\( \\times \\) (割合) \\( = {from_standard_amount_in_latex} \\times {ratio_value_in_latex}= {from_amount_to_compare_in_latex_with_unit} \\)が増やした量となる。\n" 
                    from_added = from_standard_amount + from_amount_to_compare
                    from_added_in_latex = f"{self._decimal_normalize(sy.latex(from_added))}"
                    from_added_in_latex_with_unit = f"{from_added_in_latex} {from_unit_in_latex}"
                    if from_to_unit == "kg_to_g":
                        to_added = from_added * 1000
                    elif from_to_unit == "g_to_kg":
                        to_added = from_added / 1000
                    elif from_to_unit == "m_to_cm":
                        to_added = from_added * 100
                    elif from_to_unit == "cm_to_m":
                        to_added = from_added / 100
                    elif from_to_unit == "m^2_to_cm^2":
                        to_added = from_added * ((10 ** 2) ** 2)
                    elif from_to_unit == "cm^2_to_m^2":
                        to_added = from_added / ((10 ** 2) ** 2)
                    elif from_to_unit == "m^3_to_cm^3":
                        to_added = from_added * ((10 ** 2) ** 3)
                    elif from_to_unit == "cm^3_to_m^3":
                        to_added = from_added / ((10 ** 2) ** 3)
                    to_added_out_of_latex_with_unit = f"\\( {self._decimal_normalize(sy.latex(to_added))} {to_unit_in_latex} \\)"
                    latex_answer += f"もともとあった{item}は{from_standard_amount_out_of_latex_with_unit}なので、増やした後の{japanese_unit}は\\( {from_standard_amount_in_latex} + {from_amount_to_compare_in_latex} = {from_added_in_latex_with_unit} \\)\n"
                    latex_answer += f"さらにこれを指定された単位になおすと、{to_added_out_of_latex_with_unit}となる。"                           
                elif increase_or_decrease == "decrease":
                    latex_problem = f"{from_standard_amount_out_of_latex_with_unit}の{item}を{ratio_out_of_latex}だけ減らしました。減らした後の{japanese_unit}は\\( \\underline{{\\qquad\\qquad}} {to_unit_in_latex} \\)です。"
                    if selected_ratio == "decimal":
                        latex_answer = f"まずは減らした量をもとめると、{from_standard_amount_out_of_latex_with_unit}がもとにする量、\\( {ratio_value_in_latex} \\)が割合なので、\n"
                    elif (selected_ratio == "percentage") or (selected_ratio == "japanese_percentage"):
                        latex_answer = f"まずは{ratio_out_of_latex}を小数の割合になおすと、\\( {ratio_value_in_latex}\\)となる。\n"
                        latex_answer += f"次に減らした量を求めると、{from_standard_amount_out_of_latex_with_unit}がもとにする量、\\( {ratio_value_in_latex}\\)が割合なので、\n"
                    latex_answer += f"(比べる量) = (もとにする量) \\( \\times \\) (割合) \\( = {from_standard_amount_in_latex} \\times {ratio_value_in_latex} = {from_amount_to_compare_in_latex_with_unit} \\)が減らした量となる。\n" 
                    from_remained = from_standard_amount - from_amount_to_compare
                    from_remained_in_latex = f"{self._decimal_normalize(sy.latex(from_remained))}"
                    from_remained_in_latex_with_unit = f"{from_remained_in_latex} {from_unit_in_latex}"
                    if from_to_unit == "kg_to_g":
                        to_remained = from_remained * 1000
                    elif from_to_unit == "g_to_kg":
                        to_remained = from_remained / 1000
                    elif from_to_unit == "m_to_cm":
                        to_remained = from_remained * 100
                    elif from_to_unit == "cm_to_m":
                        to_remained = from_remained / 100
                    elif from_to_unit == "m^2_to_cm^2":
                        to_remained = from_remained * ((10 ** 2) ** 2)
                    elif from_to_unit == "cm^2_to_m^2":
                        to_remained = from_remained / ((10 ** 2) ** 2)
                    elif from_to_unit == "m^3_to_cm^3":
                        to_remained = from_remained * ((10 ** 2) ** 3)
                    elif from_to_unit == "cm^3_to_m^3":
                        to_remained = from_remained / ((10 ** 2) ** 3)
                    to_remained_out_of_latex_with_unit = f"\\( {self._decimal_normalize(sy.latex(to_remained))} {to_unit_in_latex} \\)"
                    latex_answer += f"もともとあった{item}は{from_standard_amount_out_of_latex_with_unit}なので、減らした後の{japanese_unit}は\\( {from_standard_amount_in_latex} - {from_amount_to_compare_in_latex} = {from_remained_in_latex_with_unit} \\)\n"
                    latex_answer += f"さらにこれを指定された単位になおすと、{to_remained_out_of_latex_with_unit}となる。" 
        return latex_answer, latex_problem

    def _make_standard_amount_problem(self) -> Tuple[str, str]:
        """元の量を求める問題と解答を出力
        
        Returns:
            latex_answer (str): latex形式と通常の文字が混在した解答
            latex_problem (str): latex形式と通常の文字が混在した問題
        """
        selected_ratio = choice(self._used_numbers_for_ratio)
        selected_digit_under_the_decimal_point = choice(self._digit_under_the_decimal_point)
        ratio_value, ratio_out_of_latex = self._random_ratio(selected_ratio=selected_ratio, digit_under_decimal_point=selected_digit_under_the_decimal_point)
        ratio_value_in_latex = self._decimal_normalize(sy.latex(ratio_value))
        if self._used_unit_change:
            change_unit = choice([True, False])
        else:
            change_unit = False
        selected_theme = choice(["weight", "length", "area", "volume"])
        if not(change_unit):
            if selected_theme == "weight":
                japanese_unit = "重さ"
                from_to_unit = choice(["kg_to_kg", "g_to_g"])
                standard_amount = 10 * self._random_integer(max_num=20)
                amount_to_compare = standard_amount * ratio_value
                amount_to_compare_in_latex = f"{self._decimal_normalize(sy.latex(amount_to_compare))}"
                if from_to_unit == "kg_to_kg":
                    unit_in_latex = "\\mathrm{kg}"
                elif from_to_unit == "g_to_g":
                    unit_in_latex = "\\mathrm{g}"
            elif selected_theme == "length":
                japanese_unit = "長さ"
                from_to_unit = choice(["m_to_m", "cm_to_cm"])
                standard_amount = 10 * self._random_integer(max_num=20)
                amount_to_compare = standard_amount * ratio_value
                amount_to_compare_in_latex = f"{self._decimal_normalize(sy.latex(amount_to_compare))}"
                if from_to_unit == "m_to_m":
                    unit_in_latex = "\\mathrm{m}"
                elif from_to_unit == "cm_to_cm":
                    unit_in_latex = "\\mathrm{cm}"
            elif selected_theme == "area":
                japanese_unit = "面積"
                from_to_unit = choice(["cm^2_to_cm^2", "m^2_to_m^2"])
                standard_amount = 10 * self._random_integer(max_num=40)
                amount_to_compare = standard_amount * ratio_value
                amount_to_compare_in_latex = f"{self._decimal_normalize(sy.latex(amount_to_compare))}"
                if from_to_unit == "cm^2_to_cm^2":
                    unit_in_latex = "\\mathrm{{cm}^2}"
                elif from_to_unit == "m^2_to_m^2":
                    unit_in_latex = "\\mathrm{m^2}"
            elif selected_theme == "volume":
                japanese_unit = "体積"
                from_to_unit = choice(["m^3_to_m^3", "cm^3_to_cm^3"])
                standard_amount = 10 * self._random_integer(max_num=20)
                amount_to_compare = standard_amount * ratio_value
                amount_to_compare_in_latex = f"{self._decimal_normalize(sy.latex(amount_to_compare))}"
                if from_to_unit == "m^3_to_m^3":
                    unit_in_latex = "\\mathrm{m^3}"
                elif from_to_unit == "cm^3_to_cm^3":
                    unit_in_latex = "\\mathrm{{cm}^3}"
            amount_to_compare_out_of_latex_with_unit = f"\\( {amount_to_compare_in_latex} {unit_in_latex} \\)"
            standard_amount_in_latex = f"{self._decimal_normalize(sy.latex(standard_amount))}"
            standard_amount_in_latex_with_unit = f"{standard_amount_in_latex} {unit_in_latex}"
            standard_amount_out_of_latex_with_unit = f"\\( {standard_amount_in_latex} {unit_in_latex} \\)"
            problem_sentence_checker = random()
            if problem_sentence_checker < 0.25:
                latex_problem = f"ある{japanese_unit}の{ratio_out_of_latex}にあたる量が{amount_to_compare_out_of_latex_with_unit}のとき、ある{japanese_unit}は\\( \\underline{{\\qquad\\qquad}} {unit_in_latex} \\)です。"
                if selected_ratio == "decimal":
                    latex_answer = f"{amount_to_compare_out_of_latex_with_unit}が比べる量、{ratio_out_of_latex}が割合なので、\n"
                elif (selected_ratio == "percentage") or (selected_ratio == "japanese_percentage"):
                    latex_answer = f"{ratio_out_of_latex}を小数の割合になおすと、\\( {ratio_value_in_latex} \\)となる。\n"
                    latex_answer += f"{amount_to_compare_out_of_latex_with_unit}が比べる量、\\( {ratio_value_in_latex} \\)が割合なので、\n"
                latex_answer += f"(もとにする量) = (比べる量) \\( \\div \\) (割合) \\( = {amount_to_compare_in_latex} \\div {ratio_value_in_latex} = {standard_amount_in_latex_with_unit} \\)"
            elif 0.25 <= problem_sentence_checker < 0.5:
                item = self._random_item(selected_theme)
                latex_problem = f"ある{japanese_unit}の{item}のうち{ratio_out_of_latex}を運んだとき、\nその{japanese_unit}は{amount_to_compare_out_of_latex_with_unit}でした。\n運ぶ前にあった{item}の{japanese_unit}は\\( \\underline{{\\qquad\\qquad}} {unit_in_latex} \\)です。"
                if selected_ratio == "decimal":
                    latex_answer = f"{amount_to_compare_out_of_latex_with_unit}が比べる量、{ratio_out_of_latex}が割合なので、\n"
                elif (selected_ratio == "percentage") or (selected_ratio == "japanese_percentage"):
                    latex_answer = f"{ratio_out_of_latex}を小数の割合になおすと、\\( {ratio_value_in_latex}\\)となる。\n"
                    latex_answer += f"{amount_to_compare_out_of_latex_with_unit}が比べる量、\\( {ratio_value_in_latex}\\)が割合なので、\n"
                latex_answer += f"(もとにする量) = (比べる量) \\( \\div \\) (割合) \\( = {amount_to_compare_in_latex} \\div {ratio_value_in_latex} = {standard_amount_in_latex_with_unit} \\)"
            elif 0.5 <= problem_sentence_checker < 0.75:
                item = self._random_item(selected_theme)
                remained = standard_amount - amount_to_compare
                remained_in_latex = f"{self._decimal_normalize(sy.latex(remained))}"
                remained_in_latex_with_unit = f"{remained_in_latex} {unit_in_latex}"
                remained_out_of_latex_with_unit = f"\\( {remained_in_latex_with_unit} \\)"
                remained_ratio = round(1 - ratio_value, 6)
                remained_ratio_in_latex = f"{self._decimal_normalize(sy.latex(remained_ratio))}"
                remained_ratio_out_of_latex = f"\\( {remained_ratio_in_latex} \\)"
                latex_problem = f"ある{japanese_unit}の{item}を{ratio_out_of_latex}運んだとき、\n残りの{item}は{remained_out_of_latex_with_unit}でした。\n運ぶ前にあった{item}の{japanese_unit}は\\( \\underline{{\\qquad\\qquad}} {unit_in_latex} \\)です。"
                if selected_ratio == "decimal":
                    latex_answer = f"{ratio_out_of_latex}運んだということは、残った{japanese_unit}は\\( 1 - {ratio_value_in_latex} = {remained_ratio_in_latex} \\)と等しい。\n"
                elif (selected_ratio == "percentage") or (selected_ratio == "japanese_percentage"):
                    latex_answer = f"まずは{ratio_out_of_latex}を小数の割合になおすと、\\( {ratio_value_in_latex}\\)となる。\n"
                    latex_answer += f"そして、\\( {ratio_value_in_latex} \\)運んだということは、残った{japanese_unit}は\\( 1 - {ratio_value_in_latex} = {remained_ratio_in_latex} \\)と等しい。\n"
                latex_answer += f"よって、(もとにする量) = (比べる量) \\( \\div \\) (割合) \\( = {remained_in_latex} \\div {remained_ratio_in_latex} = {standard_amount_in_latex_with_unit} \\)"
            else:
                item = self._random_item(selected_theme)
                increase_or_decrease = choice(["increase", "decrease"])
                if increase_or_decrease == "increase":
                    added = standard_amount + amount_to_compare
                    added_in_latex = f"{self._decimal_normalize(sy.latex(added))}"
                    added_out_of_latex_with_unit = f"\\( {added_in_latex} {unit_in_latex} \\)"
                    added_ratio = round(1 + ratio_value, 6)
                    added_ratio_in_latex = f"{self._decimal_normalize(sy.latex(added_ratio))}"
                    added_ratio_out_of_latex = f"\\( {added_ratio_in_latex} \\)"
                    latex_problem = f"ある{japanese_unit}の{item}を{ratio_out_of_latex}増やすと、{added_out_of_latex_with_unit}になりました。\n増やす前の{item}の{japanese_unit}は\\( \\underline{{\\qquad\\qquad}} {unit_in_latex} \\)です。"
                    if selected_ratio == "decimal":
                        latex_answer = f"{ratio_out_of_latex}増やしたということは、増やした{japanese_unit}は\\( 1 + {ratio_value_in_latex} = {added_ratio_in_latex} \\)と等しい。\n"
                    elif (selected_ratio == "percentage") or (selected_ratio == "japanese_percentage"):
                        latex_answer = f"まずは{ratio_out_of_latex}を小数の割合になおすと、\\( {ratio_value_in_latex}\\)となる。\n"
                        latex_answer += f"そして、{ratio_out_of_latex}増やしたということは、増やした{japanese_unit}は\\( 1 + {ratio_value_in_latex} = {added_ratio_in_latex} \\)と等しい。\n"
                    latex_answer += f"よって、(もとにする量) = (比べる量) \\( \\div \\) (割合) \\( = {added_in_latex} \\div {added_ratio_in_latex } = {standard_amount_in_latex_with_unit} \\)" 
                elif increase_or_decrease == "decrease":
                    remained = standard_amount - amount_to_compare
                    remained_in_latex = f"{self._decimal_normalize(sy.latex(remained))}"
                    remained_out_of_latex_with_unit = f"\\( {remained_in_latex} {unit_in_latex} \\)"
                    remained_ratio = round(1 - ratio_value, 6)
                    remained_ratio_in_latex = f"{self._decimal_normalize(sy.latex(remained_ratio))}"
                    remained_ratio_out_of_latex = f"\\( {remained_ratio_in_latex} \\)"
                    latex_problem = f"ある{japanese_unit}の{item}を{ratio_out_of_latex}減らすと、{remained_out_of_latex_with_unit}になりました。\n減らす前の{item}の{japanese_unit}は\\( \\underline{{\\qquad\\qquad}} {unit_in_latex} \\)です。"
                    if selected_ratio == "decimal":
                        latex_answer = f"{ratio_out_of_latex}減らしたということは、減らした{japanese_unit}は\\( 1 - {ratio_value_in_latex} = {remained_ratio_in_latex} \\)と等しい。\n"
                    elif (selected_ratio == "percentage") or (selected_ratio == "japanese_percentage"):
                        latex_answer = f"まずは{ratio_out_of_latex}を小数の割合になおすと、\\( {ratio_value_in_latex}\\)となる。\n"
                        latex_answer += f"そして、{ratio_out_of_latex}減らしたということは、減らした{japanese_unit}は\\( 1 - {ratio_value_in_latex} = {remained_ratio_in_latex} \\)と等しい。\n"
                    latex_answer += f"よって、(もとにする量) = (比べる量) \\( \\div \\) (割合) \\( = {remained_in_latex} \\div {remained_ratio_in_latex} = {standard_amount_in_latex_with_unit} \\)"                  
        elif change_unit:
            if selected_theme == "weight":
                japanese_unit = "重さ"
                from_to_unit = choice(["kg_to_g", "g_to_kg"])
                if from_to_unit == "kg_to_g":
                    from_unit_in_latex = "\\mathrm{kg}"
                    to_unit_in_latex = "\\mathrm{g}"
                    from_standard_amount = self._random_integer(max_num=20)
                    to_standard_amount = from_standard_amount * 1000
                    from_amount_to_compare = from_standard_amount * ratio_value
                    to_amount_to_compare = from_amount_to_compare * 1000
                elif from_to_unit == "g_to_kg":
                    from_unit_in_latex = "\\mathrm{g}"
                    to_unit_in_latex = "\\mathrm{kg}"
                    from_standard_amount = 250 * self._random_integer(20)
                    to_standard_amount = from_standard_amount / 1000
                    from_amount_to_compare = from_standard_amount * ratio_value
                    to_amount_to_compare = from_amount_to_compare / 1000
            elif selected_theme == "length":
                japanese_unit = "長さ"
                from_to_unit = choice(["m_to_cm", "cm_to_m"])
                if from_to_unit == "m_to_cm":
                    from_unit_in_latex = "\\mathrm{m}"
                    to_unit_in_latex = "\\mathrm{cm}"
                    from_standard_amount = self._random_integer(max_num=20)
                    to_standard_amount = from_standard_amount * 100
                    from_amount_to_compare = from_standard_amount * ratio_value
                    to_amount_to_compare = from_amount_to_compare * 100
                elif from_to_unit == "cm_to_m":
                    from_unit_in_latex = "\\mathrm{cm}"
                    to_unit_in_latex = "\\mathrm{m}"
                    from_standard_amount = 25 * self._random_integer(max_num=20)
                    to_standard_amount = from_standard_amount / 100
                    from_amount_to_compare = from_standard_amount * ratio_value
                    to_amount_to_compare = from_amount_to_compare / 100
            elif selected_theme == "area":
                japanese_unit = "面積"
                from_to_unit = choice(["m^2_to_cm^2", "cm^2_to_m^2"])
                if from_to_unit == "m^2_to_cm^2":
                    from_unit_in_latex = "\\mathrm{m^2}"
                    to_unit_in_latex = "\\mathrm{cm^2}"
                    from_standard_amount = self._random_integer(15)
                    to_standard_amount = from_standard_amount * ((10 ** 2) ** 2)
                    from_amount_to_compare = from_standard_amount * ratio_value
                    to_amount_to_compare = from_amount_to_compare * ((10 ** 2) ** 2)
                elif from_to_unit == "cm^2_to_m^2":
                    from_unit_in_latex = "\\mathrm{cm^2}"
                    to_unit_in_latex = "\\mathrm{m^2}"
                    from_standard_amount = 250 * self._random_integer(15)
                    to_standard_amount = from_standard_amount / ((10 ** 2) ** 2)
                    from_amount_to_compare = from_standard_amount * ratio_value
                    to_amount_to_compare = from_amount_to_compare / ((10 ** 2) ** 2)
            elif selected_theme == "volume":
                japanese_unit = "体積"
                from_to_unit = choice(["m^3_to_cm^3", "cm^3_to_m^3"])
                if from_to_unit == "m^3_to_cm^3":
                    from_unit_in_latex = "\\mathrm{m^3}"
                    to_unit_in_latex = "\\mathrm{{cm}^3}"
                    from_standard_amount = self._random_integer(max_num=10)
                    to_standard_amount = from_standard_amount * ((10 ** 2) ** 3)
                    from_amount_to_compare = from_standard_amount * ratio_value
                    to_amount_to_compare = from_amount_to_compare * ((10 ** 2) ** 3)
                elif from_to_unit == "cm^3_to_m^3":
                    from_unit_in_latex = "\\mathrm{{cm}^3}"
                    to_unit_in_latex = "\\mathrm{m^3}"
                    from_standard_amount = 25000 * self._random_integer(20)
                    to_standard_amount = from_standard_amount / ((10 ** 2) ** 3)
                    from_amount_to_compare = from_standard_amount * ratio_value
                    to_amount_to_compare = from_amount_to_compare / ((10 ** 2) ** 3)
            from_standard_amount_in_latex = f"{self._decimal_normalize(sy.latex(from_standard_amount))}"
            from_standard_amount_in_latex_with_unit = f"{from_standard_amount_in_latex} {from_unit_in_latex}"
            from_standard_amount_out_of_latex_with_unit = f"\\( {from_standard_amount_in_latex_with_unit} \\)"
            from_amount_to_compare_in_latex = f"{self._decimal_normalize(sy.latex(from_amount_to_compare))}"
            from_amount_to_compare_in_latex_with_unit = f"{from_amount_to_compare_in_latex} {from_unit_in_latex}"
            from_amount_to_compare_out_of_latex_with_unit = f"\\( {from_amount_to_compare_in_latex_with_unit} \\)"
            to_amount_to_compare_in_latex = f"{self._decimal_normalize(sy.latex(to_amount_to_compare))}"
            to_amount_to_compare_out_of_latex_with_unit = f"\\( {to_amount_to_compare_in_latex} {to_unit_in_latex} \\)"
            to_standard_amount_in_latex = f"{self._decimal_normalize(sy.latex(to_standard_amount))}"
            to_standard_amount_out_of_latex_with_unit = f"\\( {to_standard_amount_in_latex} {to_unit_in_latex}\\)"
            problem_sentence_checker = random()
            if problem_sentence_checker < 0.25:
                latex_problem = f"ある{japanese_unit}の{ratio_out_of_latex}にあたる量が{from_amount_to_compare_out_of_latex_with_unit}のとき、ある{japanese_unit}は\\( \\underline{{\\qquad\\qquad}} {to_unit_in_latex} \\)です。"
                if selected_ratio == "decimal":
                    latex_answer = f"{from_amount_to_compare_out_of_latex_with_unit}が比べる量、\\( {ratio_value_in_latex} \\)が割合なので、\n"
                elif (selected_ratio == "percentage") or (selected_ratio == "japanese_percentage"):
                    latex_answer = f"{ratio_out_of_latex}を小数の割合になおすと、\\( {ratio_value_in_latex}\\)となる。\n"
                    latex_answer += f"{from_amount_to_compare_out_of_latex_with_unit}が比べる量、\\( {ratio_value_in_latex} \\)が割合なので、\n"
                latex_answer += f"(もとにする量) = (比べる量) \\( \\div \\) (割合) \\( = {from_amount_to_compare_in_latex}  \\times {ratio_value_in_latex} = {from_standard_amount_in_latex_with_unit} \\)\n"
                latex_answer += f"さらにこれを指定された単位になおすと、{to_standard_amount_out_of_latex_with_unit}となる。"
            elif 0.25 <= problem_sentence_checker < 0.5:
                item = self._random_item(selected_theme)
                latex_problem = f"ある{japanese_unit}の{item}のうち{ratio_out_of_latex}を運んだとき、\nその{japanese_unit}は{from_amount_to_compare_out_of_latex_with_unit}でした。\n運ぶ前にあった{item}の{japanese_unit}は\\( \\underline{{\\qquad\\qquad}} {to_unit_in_latex} \\)です。"
                if selected_ratio == "decimal":
                    latex_answer = f"{from_amount_to_compare_out_of_latex_with_unit}が比べる量、\\( {ratio_value_in_latex} \\)が割合なので、\n"
                elif (selected_ratio == "percentage") or (selected_ratio == "japanese_percentage"):
                    latex_answer = f"{ratio_out_of_latex}を小数の割合になおすと、\\( {ratio_value_in_latex}\\)となる。\n"
                    latex_answer += f"{from_amount_to_compare_out_of_latex_with_unit}が比べる量、\\( {ratio_value_in_latex}\\)が割合なので、\n"
                latex_answer += f"(もとにする量) = (比べる量) \\( \\div \\) (割合) \\( = {from_amount_to_compare_in_latex}  \\times {ratio_value_in_latex} = {from_standard_amount_in_latex_with_unit} \\)\n"
                latex_answer += f"さらにこれを指定された単位になおすと、{to_amount_to_compare_out_of_latex_with_unit}となる。"
            elif 0.5 <= problem_sentence_checker < 0.75:
                item = self._random_item(selected_theme)
                from_remained = from_standard_amount - from_amount_to_compare
                from_remained_in_latex = f"{self._decimal_normalize(sy.latex(from_remained))}"
                from_remained_in_latex_with_unit = f"{from_remained_in_latex} {from_unit_in_latex}"
                from_remained_out_of_latex_with_unit = f"\\( {from_remained_in_latex_with_unit} \\)"
                if from_to_unit == "kg_to_g":
                    to_remained = from_remained * 1000
                elif from_to_unit == "g_to_kg":
                    to_remained = from_remained / 1000
                elif from_to_unit == "m_to_cm":
                    to_remained = from_remained * 100
                elif from_to_unit == "cm_to_m":
                    to_remained = from_remained / 100
                elif from_to_unit == "m^2_to_cm^2":
                    to_remained = from_remained * ((10 ** 2) ** 2)
                elif from_to_unit == "cm^2_to_m^2":
                    to_remained = from_remained / ((10 ** 2) ** 2)
                elif from_to_unit == "m^3_to_cm^3":
                    to_remained = from_remained * ((10 ** 2) ** 3)
                elif from_to_unit == "cm^3_to_m^3":
                    to_remained = from_remained / ((10 ** 2) ** 3)
                to_remained_out_of_latex_with_unit = f"\\( {self._decimal_normalize(sy.latex(to_remained))}  {to_unit_in_latex} \\)"
                remained_ratio = round(1 - ratio_value, 6)
                remained_ratio_in_latex = f"{self._decimal_normalize(sy.latex(remained_ratio))}"
                remained_ratio_out_of_latex = f"\\( {remained_ratio_in_latex} \\)"
                latex_problem = f"ある{japanese_unit}の{item}を{ratio_out_of_latex}運んだとき、\n残りの{item}は{from_remained_out_of_latex_with_unit}でした。\n運ぶ前にあった{item}の{japanese_unit}は\\( \\underline{{\\qquad\\qquad}} {to_unit_in_latex} \\)です。"
                if selected_ratio == "decimal":
                    latex_answer = f"{ratio_out_of_latex}運んだということは、残った{japanese_unit}は\\( 1 - {ratio_value_in_latex} = {remained_ratio_in_latex} \\)と等しい。\n"
                elif (selected_ratio == "percentage") or (selected_ratio == "japanese_percentage"):
                    latex_answer = f"まずは{ratio_out_of_latex}を小数の割合になおすと、\\( {ratio_value_in_latex}\\)となる。\n"
                    latex_answer += f"そして、\\( {ratio_value_in_latex} \\)運んだということは、残った{japanese_unit}は\\( 1 - {ratio_value_in_latex} = {remained_ratio_in_latex} \\)と等しい。\n"
                latex_answer += f"よって、(もとにする量) = (比べる量) \\( \\div \\) (割合) \\( = {from_remained_in_latex} \\div {remained_ratio_in_latex} = {from_standard_amount_in_latex_with_unit} \\)\n"
                latex_answer += f"これを指定された単位に直すと、{to_standard_amount_out_of_latex_with_unit}"
            else:
                item = self._random_item(selected_theme)
                increase_or_decrease = choice(["increase", "decrease"])
                if increase_or_decrease == "increase":
                    from_added = from_standard_amount + from_amount_to_compare
                    from_added_in_latex = f"{self._decimal_normalize(sy.latex(from_added))}"
                    from_added_out_of_latex_with_unit = f"\\( {from_added_in_latex} {from_unit_in_latex} \\)"
                    if from_to_unit == "kg_to_g":
                        to_added = from_added * 1000
                    elif from_to_unit == "g_to_kg":
                        to_added = from_added / 1000
                    elif from_to_unit == "m_to_cm":
                        to_added = from_added * 100
                    elif from_to_unit == "cm_to_m":
                        to_added = from_added / 100
                    elif from_to_unit == "m^2_to_cm^2":
                        to_added = from_added * ((10 ** 2) ** 2)
                    elif from_to_unit == "cm^2_to_m^2":
                        to_added = from_added / ((10 ** 2) ** 2)
                    elif from_to_unit == "m^3_to_cm^3":
                        to_added = from_added * ((10 ** 2) ** 3)
                    elif from_to_unit == "cm^3_to_m^3":
                        to_added = from_added / ((10 ** 2) ** 3)
                    to_added_out_of_latex_with_unit = f"\\( {self._decimal_normalize(sy.latex(to_added))} {to_unit_in_latex} \\)"
                    added_ratio = round(1 + ratio_value, 6)
                    added_ratio_in_latex = f"{self._decimal_normalize(sy.latex(added_ratio))}"
                    added_ratio_out_of_latex = f"\\( {added_ratio_in_latex} \\)"
                    latex_problem = f"ある{japanese_unit}の{item}を{ratio_out_of_latex}増やすと、{from_added_out_of_latex_with_unit}になりました。\n増やす前の{item}の{japanese_unit}は\\( \\underline{{\\qquad\\qquad}} {to_unit_in_latex} \\)です。"
                    if selected_ratio == "decimal":
                        latex_answer = f"{ratio_out_of_latex}増やしたということは、増やした{japanese_unit}は\\( 1 + {ratio_value_in_latex} = {added_ratio_in_latex} \\)と等しい。\n"
                    elif (selected_ratio == "percentage") or (selected_ratio == "japanese_percentage"):
                        latex_answer = f"まずは{ratio_out_of_latex}を小数の割合になおすと、\\( {ratio_value_in_latex}\\)となる。\n"
                        latex_answer += f"そして、{ratio_out_of_latex}増やしたということは、増やした{japanese_unit}は\\( 1 + {ratio_value_in_latex} = {added_ratio_in_latex} \\)と等しい。\n"
                    latex_answer += f"よって、(もとにする量) = (比べる量) \\( \\div \\) (割合) \\( = {from_added_in_latex} \\div {added_ratio_in_latex } = {from_standard_amount_in_latex_with_unit} \\)\n"
                    latex_answer += f"これを指定された単位に直すと、{to_standard_amount_out_of_latex_with_unit}"
                elif increase_or_decrease == "decrease":
                    from_remained = from_standard_amount - from_amount_to_compare
                    from_remained_in_latex = f"{self._decimal_normalize(sy.latex(from_remained))}"
                    from_remained_out_of_latex_with_unit = f"\\( {from_remained_in_latex} {from_unit_in_latex} \\)"
                    if from_to_unit == "kg_to_g":
                        to_remained = from_remained * 1000
                    elif from_to_unit == "g_to_kg":
                        to_remained = from_remained / 1000
                    elif from_to_unit == "m_to_cm":
                        to_remained = from_remained * 100
                    elif from_to_unit == "cm_to_m":
                        to_remained = from_remained / 100
                    elif from_to_unit == "m^2_to_cm^2":
                        to_remained = from_remained * ((10 ** 2) ** 2)
                    elif from_to_unit == "cm^2_to_m^2":
                        to_remained = from_remained / ((10 ** 2) ** 2)
                    elif from_to_unit == "m^3_to_cm^3":
                        to_remained = from_remained * ((10 ** 2) ** 3)
                    elif from_to_unit == "cm^3_to_m^3":
                        to_remained = from_remained / ((10 ** 2) ** 3)
                    to_remained_out_of_latex_with_unit = f"\\( {self._decimal_normalize(sy.latex(to_remained))} {to_unit_in_latex} \\)"
                    remained_ratio = round(1 - ratio_value, 6)
                    remained_ratio_in_latex = f"{self._decimal_normalize(sy.latex(remained_ratio))}"
                    remained_ratio_out_of_latex = f"\\( {remained_ratio_in_latex} \\)"
                    latex_problem = f"ある{japanese_unit}の{item}を{ratio_out_of_latex}減らすと、{to_remained_out_of_latex_with_unit}になりました。\n減らす前の{item}の{japanese_unit}は\\( \\underline{{\\qquad\\qquad}} {to_unit_in_latex} \\)です。"
                    if selected_ratio == "decimal":
                        latex_answer = f"{ratio_out_of_latex}減らしたということは、減らした{japanese_unit}は\\( 1 - {ratio_value_in_latex} = {remained_ratio_in_latex} \\)と等しい。\n"
                    elif (selected_ratio == "percentage") or (selected_ratio == "japanese_percentage"):
                        latex_answer = f"まずは{ratio_out_of_latex}を小数の割合になおすと、\\( {ratio_value_in_latex}\\)となる。\n"
                        latex_answer += f"そして、{ratio_out_of_latex}減らしたということは、減らした{japanese_unit}は\\( 1 - {ratio_value_in_latex} = {remained_ratio_in_latex} \\)と等しい。\n"
                    latex_answer += f"よって、(もとにする量) = (比べる量) \\( \\div \\) (割合) \\( = {from_remained_in_latex} \\div {remained_ratio_in_latex} = {from_standard_amount_in_latex_with_unit} \\)\n"
                    latex_answer += f"これを指定された単位に直すと、{to_standard_amount_out_of_latex_with_unit}"
        return latex_answer, latex_problem

    def _make_ratio_problem(self) -> Tuple[str, str]:
        """割合を求める問題と解答を出力
        
        Returns:
            latex_answer (str): latex形式と通常の文字が混在した解答
            latex_problem (str): latex形式と通常の文字が混在した問題
        """
        selected_ratio = choice(self._used_numbers_for_ratio)
        selected_digit_under_the_decimal_point = choice(self._digit_under_the_decimal_point)
        ratio_value, ratio_out_of_latex = self._random_ratio(selected_ratio=selected_ratio, digit_under_decimal_point=selected_digit_under_the_decimal_point)
        ratio_value_in_latex = f"{self._decimal_normalize(sy.latex(ratio_value))}"
        if self._used_unit_change:
            change_unit = choice([True, False])
        else:
            change_unit = False
        selected_theme = choice(["weight", "length", "area", "volume"])
        if not(change_unit):
            standard_amount = 10 * self._random_integer(max_num=20)
            if selected_theme == "weight":
                japanese_unit = "重さ"
                from_to_unit = choice(["kg_to_kg", "g_to_g"])
                if from_to_unit == "kg_to_kg":
                    unit_in_latex = "\\mathrm{kg}"
                elif from_to_unit == "g_to_g":
                    unit_in_latex = "\\mathrm{g}"
            elif selected_theme == "length":
                japanese_unit = "長さ"
                from_to_unit = choice(["m_to_m", "cm_to_cm"])
                if from_to_unit == "m_to_m":
                    unit_in_latex = "\\mathrm{m}"
                elif from_to_unit == "cm_to_cm":
                    unit_in_latex = "\\mathrm{cm}"
            elif selected_theme == "area":
                japanese_unit = "面積"
                from_to_unit = choice(["m^2_to_m^2", "cm^2_to_cm^2"])
                if from_to_unit == "m^2_to_m^2":
                    unit_in_latex = "\\mathrm{m^2}"
                elif from_to_unit == "cm^2_to_cm^2":
                    unit_in_latex = "\\mathrm{{cm}^2}"
            elif selected_theme == "volume":
                japanese_unit = "体積"
                from_to_unit = choice(["m^3_to_m^3", "cm^3_to_cm^3"])
                if from_to_unit == "m^3_to_m^3":
                    unit_in_latex = "\\mathrm{m^3}"
                elif from_to_unit == "cm^3_to_cm^3":
                    unit_in_latex = "\\mathrm{{cm}^3}"
            amount_to_compare = standard_amount * ratio_value
            amount_to_compare_in_latex = f"{self._decimal_normalize(sy.latex(amount_to_compare))}"
            amount_to_compare_out_of_latex_with_unit = f"\\( {amount_to_compare_in_latex} {unit_in_latex} \\)"
            standard_amount_in_latex = f"{self._decimal_normalize(sy.latex(standard_amount))}"
            standard_amount_out_of_latex = f"\\( {standard_amount_in_latex} \\)"
            standard_amount_in_latex_with_unit = f"{standard_amount_in_latex} {unit_in_latex}"
            standard_amount_out_of_latex_with_unit = f"\\( {standard_amount_in_latex} {unit_in_latex} \\)"
            problem_sentence_checker = random()
            if selected_ratio == "decimal":
                japanese_ratio_name = "小数"
            elif selected_ratio == "percentage":
                japanese_ratio_name = "百分率"
            elif selected_ratio == "japanese_percentage":
                japanese_ratio_name = "歩合"
            if problem_sentence_checker < 0.25:
                latex_problem = f"{standard_amount_out_of_latex_with_unit}をもとにするとき、{amount_to_compare_out_of_latex_with_unit}を{japanese_ratio_name}で表した割合は\\( \\underline{{\\qquad\\qquad}} {unit_in_latex} \\)です。"
                latex_answer = f"{standard_amount_out_of_latex_with_unit}がもとにする量、{amount_to_compare_out_of_latex_with_unit}が比べる量なので、\n"
                latex_answer += f"(割合) = (比べる量) \\( \\div \\) (もとにする量) \\( = {amount_to_compare_in_latex} \\div {standard_amount_in_latex} = {ratio_value_in_latex} \\)"
                if (selected_ratio == "percentage") or (selected_ratio == "japanese_percentage"):
                    latex_answer += f"\n これを{japanese_ratio_name}になおすと、{ratio_out_of_latex}となる。"
            elif 0.25 <= problem_sentence_checker < 0.5:
                item = self._random_item(selected_theme)
                latex_problem = f"{standard_amount_out_of_latex_with_unit}の{japanese_unit}の{item}のうち{amount_to_compare_out_of_latex_with_unit}を運びました。\n{standard_amount_out_of_latex_with_unit}をもとにして、\n"
                latex_problem += f"運んだ{item}の割合を{japanese_ratio_name}で表すと、\\( (\\, \\, \\, ) \\)となります。"
                latex_answer = f"{standard_amount_out_of_latex_with_unit}がもとにする量、{amount_to_compare_out_of_latex_with_unit}が比べる量なので、\n"
                latex_answer += f"(割合) = (比べる量) \\( \\div \\) (もとにする量) \\( = {amount_to_compare_in_latex} \\div {standard_amount_in_latex} = {ratio_value_in_latex} \\)"
                if (selected_ratio == "percentage") or (selected_ratio == "japanese_percentage"):
                    latex_answer += f"\n これを{japanese_ratio_name}になおすと、{ratio_out_of_latex}となる。"
            elif 0.5 <= problem_sentence_checker < 0.75:
                item = self._random_item(selected_theme)
                remained = standard_amount - amount_to_compare
                remained_in_latex = f"{self._decimal_normalize(sy.latex(remained))}"
                remained_in_latex_with_unit = f"{remained_in_latex} {unit_in_latex}"
                remained_out_of_latex_with_unit = f"\\( {remained_in_latex_with_unit} \\)"
                remained_ratio_value = round(1 - ratio_value, 6)
                remained_ratio_in_latex = f"{self._decimal_normalize(sy.latex(remained_ratio_value))}"
                if selected_ratio == "decimal":
                    remained_ratio_out_of_latex = f"\\( {self._decimal_normalize(sy.latex(remained_ratio_value))} \\)"
                elif selected_ratio == "percentage":
                    normalized_percentage = self._decimal_normalize(sy.latex(remained_ratio_value * 100))
                    remained_ratio_out_of_latex = f"\\( {normalized_percentage} \\% \\)"
                elif selected_ratio == "japanese_percentage":
                    digit_list = sy.latex(remained_ratio_value)[2:]
                    japanese_percentage_names = ["割", "分", "厘", "毛"]
                    remained_ratio_out_of_latex = ""
                    for digit, name in zip(digit_list, japanese_percentage_names):
                        if digit != "0":
                            remained_ratio_out_of_latex += (digit + name)
                latex_problem = f"{standard_amount_out_of_latex_with_unit}の{item}を{amount_to_compare_out_of_latex_with_unit}運びました。\n{standard_amount_out_of_latex_with_unit}をもとにして、\n"
                latex_problem += f"残った{item}の割合を{japanese_ratio_name}で表すと、\\( \\underline{{\\qquad\\qquad}} {unit_in_latex} \\)になります。"
                latex_answer = f"初めに残った量を求めると、\n\\( {standard_amount_in_latex} - {amount_to_compare_in_latex} = {remained_in_latex_with_unit} \\)となる。\n"
                latex_answer += f"{standard_amount_out_of_latex_with_unit}をもとにする量、{remained_out_of_latex_with_unit}を比べる量とすると、\n"
                latex_answer += f"(割合) = (比べる量) \\( \\div \\) (もとにする量) \\( = {remained_in_latex} \\div {standard_amount_in_latex} = {remained_ratio_in_latex} \\)"
                if (selected_ratio == "percentage") or (selected_ratio == "japanese_percentage"):
                    latex_answer +=f"\n これを{japanese_ratio_name}になおすと、{remained_ratio_out_of_latex}となる。"
            else:
                item = self._random_item(selected_theme)
                remained = standard_amount - amount_to_compare
                remained_in_latex = f"{self._decimal_normalize(sy.latex(remained))}"
                remained_out_of_latex_with_unit = f"\\( {remained_in_latex} {unit_in_latex} \\)"
                remained_ratio_value = round(1 - ratio_value, 6)
                remained_ratio_in_latex = f"{self._decimal_normalize(sy.latex(remained_ratio_value))}"
                if selected_ratio == "decimal":
                    remained_ratio_out_of_latex = f"\\( {self._decimal_normalize(sy.latex(remained_ratio_value))} \\)"
                elif selected_ratio == "percentage":
                    normalized_percentage = self._decimal_normalize(sy.latex(remained_ratio_value * 100))
                    remained_ratio_out_of_latex = f"\\( {normalized_percentage} \\% \\)"
                elif selected_ratio == "japanese_percentage":
                    digit_list = sy.latex(remained_ratio_value)[2:]
                    japanese_percentage_names = ["割", "分", "厘", "毛"]
                    remained_ratio_out_of_latex = ""
                    for digit, name in zip(digit_list, japanese_percentage_names):
                        if digit != "0":
                            remained_ratio_out_of_latex += (digit + name)
                latex_problem = f"{standard_amount_out_of_latex_with_unit}の{item}を{amount_to_compare_out_of_latex_with_unit}減らしました。\n{standard_amount_out_of_latex_with_unit}をもとにして、\n"
                latex_problem += f"減らしたあとの{item}の割合を{japanese_ratio_name}で表すと、\\( \\underline{{\\qquad\\qquad}} {unit_in_latex} \\)になります。"
                latex_answer = f"初めに減らした後の量を求めると、\n\\( {standard_amount_in_latex} - {amount_to_compare_in_latex} = {remained_in_latex} \\)となる。\n"
                latex_answer += f"{standard_amount_out_of_latex_with_unit}をもとにする量、{remained_out_of_latex_with_unit}を比べる量とすると、\n"
                latex_answer += f"(割合) = (比べる量) \\( \\div \\) (もとにする量) \\( = {remained_in_latex} \\div {standard_amount_in_latex} = {remained_ratio_in_latex} \\)"
                if (selected_ratio == "percentage") or (selected_ratio == "japanese_percentage"):
                    latex_answer += f"\n これを{japanese_ratio_name}になおすと、{remained_ratio_out_of_latex}となる。"
        elif change_unit:
            if selected_theme == "weight":
                japanese_unit = "重さ"
                from_to_unit = choice(["kg_to_g", "g_to_kg"])
                if from_to_unit == "kg_to_g":
                    from_unit_in_latex = "\\mathrm{kg}"
                    to_unit_in_latex = "\\mathrm{g}"
                    from_standard_amount = self._random_integer(max_num=20)
                    to_standard_amount = from_standard_amount * 1000
                    from_amount_to_compare = from_standard_amount * ratio_value
                    to_amount_to_compare = from_amount_to_compare * 1000
                elif from_to_unit == "g_to_kg":
                    from_unit_in_latex = "\\mathrm{g}"
                    to_unit_in_latex = "\\mathrm{kg}"
                    from_standard_amount = 250 * self._random_integer(20)
                    to_standard_amount = from_standard_amount / 1000
                    from_amount_to_compare = from_standard_amount * ratio_value
                    to_amount_to_compare = from_amount_to_compare / 1000
            elif selected_theme == "length":
                japanese_unit = "長さ"
                from_to_unit = choice(["m_to_cm", "cm_to_m"])
                if from_to_unit == "m_to_cm":
                    from_unit_in_latex = "\\mathrm{m}"
                    to_unit_in_latex = "\\mathrm{cm}"
                    from_standard_amount = self._random_integer(max_num=20)
                    to_standard_amount = from_standard_amount * 100
                    from_amount_to_compare = from_standard_amount * ratio_value
                    to_amount_to_compare = from_amount_to_compare * 100
                elif from_to_unit == "cm_to_m":
                    from_unit_in_latex = "\\mathrm{cm}"
                    to_unit_in_latex = "\\mathrm{m}"
                    from_standard_amount = 25 * self._random_integer(max_num=20)
                    to_standard_amount = from_standard_amount / 100
                    from_amount_to_compare = from_standard_amount * ratio_value
                    to_amount_to_compare = from_amount_to_compare / 100
            elif selected_theme == "area":
                japanese_unit = "面積"
                from_to_unit = choice(["m^2_to_cm^2", "cm^2_to_m^2"])
                if from_to_unit == "m^2_to_cm^2":
                    from_unit_in_latex = "\\mathrm{m^2}"
                    to_unit_in_latex = "\\mathrm{{cm}^2}"
                    from_standard_amount = self._random_integer(max_num=20)
                    to_standard_amount = from_standard_amount * ((10 ** 2) ** 2)
                    from_amount_to_compare = from_standard_amount * ratio_value
                    to_amount_to_compare = from_amount_to_compare * ((10 ** 2) ** 2)
                elif from_to_unit == "cm^2_to_m^2":
                    from_unit_in_latex = "\\mathrm{{cm}^2}"
                    to_unit_in_latex = "\\mathrm{{m}^2}"
                    from_standard_amount = 25 * self._random_integer(max_num=20)
                    to_standard_amount = from_standard_amount / ((10 ** 2) ** 2)
                    from_amount_to_compare = from_standard_amount * ratio_value
                    to_amount_to_compare = from_amount_to_compare / ((10 ** 2) ** 2)
            elif selected_theme == "volume":
                japanese_unit = "体積"
                from_to_unit = choice(["m^3_to_cm^3", "cm^3_to_m^3"])
                if from_to_unit == "m^3_to_cm^3":
                    from_unit_in_latex = "\\mathrm{m^3}"
                    to_unit_in_latex = "\\mathrm{{cm}^3}"
                    from_standard_amount = self._random_integer(max_num=10)
                    to_standard_amount = from_standard_amount * ((10 ** 2) ** 3)
                    from_amount_to_compare = from_standard_amount * ratio_value
                    to_amount_to_compare = from_amount_to_compare * ((10 ** 2) ** 3)
                elif from_to_unit == "cm^3_to_m^3":
                    from_unit_in_latex = "\\mathrm{{cm}^3}"
                    to_unit_in_latex = "\\mathrm{m^3}"
                    from_standard_amount = 25000 * self._random_integer(20)
                    to_standard_amount = from_standard_amount / ((10 ** 2) ** 3)
                    from_amount_to_compare = from_standard_amount * ratio_value
                    to_amount_to_compare = from_amount_to_compare / ((10 ** 2) ** 3)
            from_standard_amount_in_latex = f"{self._decimal_normalize(sy.latex(from_standard_amount))}"
            from_standard_amount_in_latex_with_unit = f"{from_standard_amount_in_latex} {from_unit_in_latex}"
            from_standard_amount_out_of_latex_with_unit = f"\\( {from_standard_amount_in_latex_with_unit} \\)"
            from_amount_to_compare_in_latex = f"{self._decimal_normalize(sy.latex(from_amount_to_compare))}"
            from_amount_to_compare_in_latex_with_unit = f"{from_amount_to_compare_in_latex} {from_unit_in_latex}"
            from_amount_to_compare_out_of_latex_with_unit = f"\\( {from_amount_to_compare_in_latex_with_unit} \\)"
            to_amount_to_compare_in_latex = f"{self._decimal_normalize(sy.latex(to_amount_to_compare))}"
            to_amount_to_compare_out_of_latex_with_unit = f"\\( {to_amount_to_compare_in_latex} {to_unit_in_latex} \\)"
            to_standard_amount_in_latex = f"{self._decimal_normalize(sy.latex(to_standard_amount))}"
            to_standard_amount_out_of_latex_with_unit = f"\\( {to_standard_amount_in_latex} {to_unit_in_latex}\\)"
            if selected_ratio == "decimal":
                japanese_ratio_name = "小数"
            elif selected_ratio == "percentage":
                japanese_ratio_name = "百分率"
            elif selected_ratio == "japanese_percentage":
                japanese_ratio_name = "歩合"
            problem_sentence_checker = random()
            if problem_sentence_checker < 0.25:
                latex_problem = f"{from_standard_amount_out_of_latex_with_unit}をもとにしたとき、{to_amount_to_compare_out_of_latex_with_unit}の割合を{japanese_ratio_name}で表すと、\\( \\underline{{\\qquad\\qquad}} \\)です。"
                if from_standard_amount > to_standard_amount:
                    latex_answer = f"まず、{to_amount_to_compare_out_of_latex_with_unit}をもとにする量と同じ単位である\\( {from_unit_in_latex} \\)になおすと、{from_amount_to_compare_out_of_latex_with_unit}となる。\n"
                    latex_answer += f"{from_amount_to_compare_out_of_latex_with_unit}が比べる量、{from_standard_amount_out_of_latex_with_unit}がもとにする量なので、\n"
                    latex_answer += f"(割合) \\( = \\) (比べる量) \\( \\div \\) (もとにする量) \\( = {from_amount_to_compare_in_latex} \\div {from_standard_amount_in_latex} = {ratio_value_in_latex} \\)"
                else:
                    latex_answer = f"まず、{from_standard_amount_out_of_latex_with_unit}を比べる量と同じ単位である\\( {to_unit_in_latex} \\)になおすと、{to_standard_amount_out_of_latex_with_unit}となる。\n"
                    latex_answer += f"{to_amount_to_compare_out_of_latex_with_unit}が比べる量、{to_standard_amount_out_of_latex_with_unit}がもとにする量なので、\n"
                    latex_answer += f"(割合) \\( = \\) (比べる量) \\( \\div \\) (もとにする量) \\( = {to_amount_to_compare_in_latex} \\div {to_standard_amount_in_latex} = {ratio_value_in_latex} \\)"
                if (selected_ratio == "百分率") or (selected_ratio == "歩合"):
                    latex_answer += f"\n これを指定された割合になおすと、{ratio_out_of_latex}となる。"
            elif 0.25 <= problem_sentence_checker < 0.5:
                item = self._random_item(selected_theme)
                latex_problem = f"{from_standard_amount_out_of_latex_with_unit}の{japanese_unit}の{item}のうち、 {to_amount_to_compare_out_of_latex_with_unit}を運びました。\n{from_standard_amount_out_of_latex_with_unit}をもとにして、\n"
                latex_problem += f"運んだ{item}の割合を{japanese_ratio_name}で表すと、\\( \\underline{{\\qquad\\qquad}} {to_unit_in_latex} \\)となります。"
                if from_standard_amount > to_standard_amount:
                    latex_answer = f"まず、{to_amount_to_compare_out_of_latex_with_unit}をもとにする量と同じ単位である\\( {from_unit_in_latex} \\)になおすと、{from_amount_to_compare_out_of_latex_with_unit}となる。\n"
                    latex_answer += f"{from_amount_to_compare_out_of_latex_with_unit}が比べる量、{from_standard_amount_out_of_latex_with_unit}がもとにする量なので、\n"
                    latex_answer += f"(割合) = (比べる量) \\( \\div \\) (もとにする量) \\( = {from_amount_to_compare_in_latex} \\div {from_standard_amount_in_latex} = {ratio_value_in_latex} \\)"
                else:
                    latex_answer = f"まず、{from_standard_amount_out_of_latex_with_unit}を比べる量と同じ単位である\\( {to_unit_in_latex} \\)になおすと、{to_standard_amount_out_of_latex_with_unit}となる。\n"
                    latex_answer += f"{to_amount_to_compare_out_of_latex_with_unit}が比べる量、{to_standard_amount_out_of_latex_with_unit}がもとにする量なので、\n"
                    latex_answer += f"(割合) = (比べる量) \\( \\div \\) (もとにする量) \\( = {to_amount_to_compare_in_latex} \\div {to_standard_amount_in_latex} = {ratio_value_in_latex} \\)"
                if (selected_ratio == "百分率") or (selected_ratio == "歩合"):
                    latex_answer += f"\n これを指定された割合になおすと、{ratio_out_of_latex}となる。"
            elif 0.5 <= problem_sentence_checker < 0.75:
                item = self._random_item(selected_theme)
                from_remained = from_standard_amount - from_amount_to_compare
                from_remained_in_latex = f"{self._decimal_normalize(sy.latex(from_remained))}"
                from_remained_in_latex_with_unit = f"{from_remained_in_latex} {from_unit_in_latex}"
                from_remained_out_of_latex_with_unit = f"\\( {from_remained_in_latex_with_unit} \\)"
                if from_to_unit == "kg_to_g":
                    to_remained = from_remained * 1000
                elif from_to_unit == "g_to_kg":
                    to_remained = from_remained / 1000
                elif from_to_unit == "m_to_cm":
                    to_remained = from_remained * 100
                elif from_to_unit == "cm_to_m":
                    to_remained = from_remained / 100
                elif from_to_unit == "m^2_to_cm^2":
                    to_remained = from_remained * ((10 ** 2) ** 2)
                elif from_to_unit == "cm^2_to_m^2":
                    to_remained = from_remained / ((10 ** 2) ** 2)
                elif from_to_unit == "m^3_to_cm^3":
                    to_remained = from_remained * ((10 ** 2) ** 3)
                elif from_to_unit == "cm^3_to_m^3":
                    to_remained = from_remained / ((10 ** 2) ** 3)
                to_remained_in_latex = f"{self._decimal_normalize(sy.latex(to_remained))}"
                to_remained_out_of_latex_with_unit = f"\\( {to_remained_in_latex} {to_unit_in_latex} \\)"
                remained_ratio_value = round(1 - ratio_value, 6)
                remained_ratio_in_latex = f"{self._decimal_normalize(sy.latex(remained_ratio_value))}"
                if selected_ratio == "decimal":
                    remained_ratio_out_of_latex = f"\\( {self._decimal_normalize(sy.latex(remained_ratio_value))} \\)"
                elif selected_ratio == "percentage":
                    normalized_percentage = self._decimal_normalize(sy.latex(remained_ratio_value * 100))
                    remained_ratio_out_of_latex = f"\\( {normalized_percentage} \\% \\)"
                elif selected_ratio == "japanese_percentage":
                    digit_list = sy.latex(remained_ratio_value)[2:]
                    japanese_percentage_names = ["割", "分", "厘", "毛"]
                    remained_ratio_out_of_latex = ""
                    for digit, name in zip(digit_list, japanese_percentage_names):
                        if digit != "0":
                            remained_ratio_out_of_latex += (digit + name)
                latex_problem = f"{from_standard_amount_out_of_latex_with_unit}の{item}を{to_amount_to_compare_out_of_latex_with_unit}運びました。\n{from_standard_amount_out_of_latex_with_unit}をもとにして、\n"
                latex_problem += f"残った{item}の割合を{japanese_ratio_name}で表すと、\\( \\underline{{\\qquad\\qquad}} \\)になります。"
                if from_standard_amount > to_standard_amount:
                    latex_answer = f"まず、{to_amount_to_compare_out_of_latex_with_unit}をもとにする量と同じ単位である\\( {from_unit_in_latex} \\)になおすと、{from_amount_to_compare_out_of_latex_with_unit}となる。\n"
                    latex_answer += f"次に、残った量を求めると、\n\\( {from_standard_amount_in_latex} - {from_amount_to_compare_in_latex} = {from_remained_in_latex_with_unit} \\)となる。\n"
                    latex_answer += f"ここで、{from_standard_amount_out_of_latex_with_unit}をもとにする量、{from_remained_out_of_latex_with_unit}を比べる量とすると、\n"
                    latex_answer += f"(割合) = (比べる量) \\( \\div \\) (もとにする量) \\( = {from_remained_in_latex} \\div {from_standard_amount_in_latex} = {remained_ratio_in_latex} \\)"
                else:
                    latex_answer = f"まず、{from_standard_amount_out_of_latex_with_unit}を比べる量と同じ単位である\\( {to_unit_in_latex} \\)になおすと、{to_standard_amount_out_of_latex_with_unit}となる。\n"
                    latex_answer += f"次に、残った量を求めると、\n\\( {to_standard_amount_in_latex} - {to_amount_to_compare_in_latex} = {to_remained_in_latex} \\)となる。\n"
                    latex_answer += f"ここで、{to_standard_amount_out_of_latex_with_unit}をもとにする量、{to_remained_out_of_latex_with_unit}を比べる量とすると、\n"
                    latex_answer += f"(割合) = (比べる量) \\( \\div \\) (もとにする量) \\( = {to_remained_in_latex} \\div {to_standard_amount_in_latex} = {remained_ratio_in_latex} \\)"
                if (selected_ratio == "percentage") or (selected_ratio == "japanese_percentage"):
                    latex_answer += f"\n これを{japanese_ratio_name}になおすと、{remained_ratio_out_of_latex}となる。"
            else:
                item = self._random_item(selected_theme)
                from_remained = from_standard_amount - from_amount_to_compare
                from_remained_in_latex = f"{self._decimal_normalize(sy.latex(from_remained))}"
                from_remained_in_latex_with_unit = f"{self._decimal_normalize(sy.latex(from_remained))} {from_unit_in_latex}"
                from_remained_out_of_latex_with_unit = f"\\( {from_remained_in_latex_with_unit} \\)"
                if from_to_unit == "kg_to_g":
                    to_remained = from_remained * 1000
                elif from_to_unit == "g_to_kg":
                    to_remained = from_remained / 1000
                elif from_to_unit == "m_to_cm":
                    to_remained = from_remained * 100
                elif from_to_unit == "cm_to_m":
                    to_remained = from_remained / 100
                elif from_to_unit == "m^2_to_cm^2":
                    to_remained = from_remained * ((10 ** 2) ** 2)
                elif from_to_unit == "cm^2_to_m^2":
                    to_remained = from_remained / ((10 ** 2) ** 2)
                elif from_to_unit == "m^3_to_cm^3":
                    to_remained = from_remained * ((10 ** 2) ** 3)
                elif from_to_unit == "cm^3_to_m^3":
                    to_remained = from_remained / ((10 ** 2) ** 3)
                to_remained_in_latex = f"{self._decimal_normalize(sy.latex(to_remained))}"
                to_remained_in_latex_with_unit = f"{to_remained_in_latex} {to_unit_in_latex}"
                to_remained_out_of_latex_with_unit = f"\\( {to_remained_in_latex_with_unit} \\)"
                remained_ratio_value = round(1 - ratio_value, 6)
                remained_ratio_in_latex = f"{self._decimal_normalize(sy.latex(remained_ratio_value))}"
                if selected_ratio == "decimal":
                    remained_ratio_out_of_latex = f"\\( {remained_ratio_in_latex} \\)"
                elif selected_ratio == "percentage":
                    normalized_percentage = self._decimal_normalize(sy.latex(remained_ratio_value * 100))
                    remained_ratio_out_of_latex = f"\\( {normalized_percentage} \\% \\)"
                elif selected_ratio == "japanese_percentage":
                    digit_list = sy.latex(remained_ratio_value)[2:]
                    japanese_percentage_names = ["割", "分", "厘", "毛"]
                    remained_ratio_out_of_latex = ""
                    for digit, name in zip(digit_list, japanese_percentage_names):
                        if digit != "0":
                            remained_ratio_out_of_latex += (digit + name)
                latex_problem = f"{from_standard_amount_out_of_latex_with_unit}の{item}を{to_amount_to_compare_out_of_latex_with_unit}減らしました。\n{from_standard_amount_out_of_latex_with_unit}をもとにして、\n"
                latex_problem += f"減らしたあとの{item}の割合を{japanese_ratio_name}で表すと、\\( \\underline{{\\qquad\\qquad}} \\)になります。"
                if from_standard_amount > to_standard_amount:
                    latex_answer = f"まず、{to_amount_to_compare_out_of_latex_with_unit}をもとにする量と同じ単位である\\( {from_unit_in_latex} \\)になおすと、{from_amount_to_compare_out_of_latex_with_unit}となる。\n"
                    latex_answer += f"次に、残った量を求めると、\n\\( {from_standard_amount_in_latex} - {from_amount_to_compare_in_latex} = {from_remained_in_latex_with_unit} \\)となる。\n"
                    latex_answer += f"ここで、{from_standard_amount_out_of_latex_with_unit}をもとにする量、{from_remained_out_of_latex_with_unit}を比べる量とすると、\n"
                    latex_answer += f"(割合) = (比べる量) \\( \\div \\) (もとにする量) \\( = {from_remained_in_latex} \\div {from_standard_amount_in_latex} = {remained_ratio_in_latex} \\)"
                else:
                    latex_answer = f"まず、{from_standard_amount_out_of_latex_with_unit}を比べる量と同じ単位である\\( {to_unit_in_latex} \\)になおすと、{to_standard_amount_out_of_latex_with_unit}となる。\n"
                    latex_answer += f"次に、残った量を求めると、\n\\( {to_standard_amount_in_latex} - {to_amount_to_compare_in_latex} = {to_remained_in_latex_with_unit} \\)となる。\n"
                    latex_answer += f"ここで、{to_standard_amount_out_of_latex_with_unit}をもとにする量、{to_remained_out_of_latex_with_unit}を比べる量とすると、\n"
                    latex_answer += f"(割合) = (比べる量) \\( \\div \\) (もとにする量) \\( = {to_remained_in_latex} \\div {to_standard_amount_in_latex} = {remained_ratio_in_latex} \\)"
                if (selected_ratio == "percentage") or (selected_ratio == "japanese_percentage"):
                    latex_answer += f"\n これを{japanese_ratio_name}になおすと、{remained_ratio_out_of_latex}となる。"
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
            ValueError: 小数点以下4桁、すなわち毛より下を要求されたときに挙上

        Returns:
            ratio_value (sy.Float): 計算に用いる小数の割合
            ratio_out_of_latex (str): latexの外側で使われることを想定した割合
        """        
        # ratio_value = (10 ** -digit_under_decimal_point) * randint(1, 10 ** digit_under_decimal_point - 1)
        if digit_under_decimal_point == 1:
            ratio_value = 0.1 * randint(1, 9)
        elif digit_under_decimal_point == 2:
            ratio_value = 0.01 * randint(1, 99)
        elif digit_under_decimal_point == 3:
            ratio_value = 0.001 * randint(1, 999)
        elif digit_under_decimal_point == 4:
            ratio_value = 0.0001 * randint(1, 9999)
        else:
            raise ValueError(f"'digit_under_the_decimal_point' is {digit_under_decimal_point}. This must be 4 or less.")
        ratio_value = round(ratio_value, 6)
        if selected_ratio == "decimal":
            ratio_out_of_latex = f"\\( {sy.latex(ratio_value)} \\)"
        elif selected_ratio == "percentage":
            normalized_percentage = self._decimal_normalize(sy.latex(ratio_value * 100))
            ratio_out_of_latex = f"\\( {normalized_percentage} \\% \\)"
        elif selected_ratio == "japanese_percentage":
            digit_list = sy.latex(ratio_value)[2:]
            japanese_percentage_names = ["割", "分", "厘", "毛"]
            japanese_percentage_str = ""
            for digit, name in zip(digit_list, japanese_percentage_names):
                if digit != "0":
                    japanese_percentage_str += (digit + name)
            ratio_out_of_latex = japanese_percentage_str
        return ratio_value, ratio_out_of_latex
    

    def _decimal_normalize(self, number: Union[str, sy.Integer, sy.Float]) -> str:
        """小数点以下で末尾まで続いている連続した0を消去した文字列を返す。(eg. 100.00->100, 31.0010->31.001)

        Args:
            number (Union[str, sy.Integer, sy.Float]): 処理したい数

        Returns:
            number_str (str): 0が消去された文字列 
        """
        number_str = str(number)
        while True:
            if ("." in number_str and number_str[-1] == "0") or (number_str[-1] == "."):
                number_str = number_str[:-1]
                continue
            break
        return number_str

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
        elif theme == "area":
            items = [
                "紙", "布",
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
        else:
            raise ValueError(f"'theme' is {theme}. This isn't expected.")
        selected_item = choice(items)
        return selected_item

from random import choice, randint, random, sample, shuffle
from typing import Dict, Union, Tuple


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
        # selected_theme = choice(["area", "volume", "weight", "price"])
        selected_theme = "weight"
        if selected_problem_type == "expression_with_formula":
            if selected_theme == "area":
                self.latex_answer, self.latex_problem = self._make_expression_with_formula_area_problem()
            elif selected_theme == "volume":
                self.latex_answer, self.latex_problem = self._make_expression_with_formula_volume_problem()
            elif selected_theme == "weight":
                self.latex_answer, self.latex_problem = self._make_expression_with_formula_weight_problem()
            elif selected_theme == "price":
                self.latex_answer, self.latex_problem = self._make_expression_with_formula_price_problem()
        elif selected_problem_type == "expression_with_formula_and_calculate":
            if selected_theme == "area":
                self.latex_answer, self.latex_problem = self._make_expression_with_formula_and_calculate_area_problem()
            elif selected_theme == "volume":
                self.latex_answer, self.latex_problem = self._make_expression_with_formula_and_calculate_volume_problem()
            elif selected_theme == "weight":
                self.latex_answer, self.latex_problem = self._make_expression_with_formula_and_calculate_weight_problem()
            elif selected_theme == "price":
                self.latex_answer, self.latex_problem = self._make_expression_with_formula_and_calculate_price_problem()
        elif selected_problem_type == "expression_with_formula_and_solve":
            if selected_theme == "area":
                self.latex_answer, self.latex_problem = self._make_expression_with_formula_and_solve_area_problem()
            elif selected_theme == "volume":
                self.latex_answer, self.latex_problem = self._make_expression_with_formula_and_solve_volume_problem()
            elif selected_theme == "weight":
                self.latex_answer, self.latex_problem = self._make_expression_with_formula_and_solve_weight_problem()
            elif selected_theme == "price":
                self.latex_answer, self.latex_problem = self._make_expression_with_formula_and_solve_price_problem()
        elif selected_problem_type == "from_formula_to_condition":
            self.latex_answer, self.latex_problem = self._make_from_formula_to_condition_problem()
        else:
            raise ValueError(f"selected_problem_type is {selected_problem_type}. This isn't concerned value.")
    
    def _make_expression_with_formula_area_problem(self) -> Tuple[str, str]:
        """面積をテーマとした式の表現のみを問う問題の作成
        
        Returns:
            Tuple[str, str]: 問題と解答
            - latex_answer (str): latex形式と通常の文字列が混在していることを前提とした解答
            - latex_problem (str): latex形式と通常の文字列が混在していることを前提とした問題
        """
        x = sy.Symbol("x")
        selected_shape = choice(["triangle", "parallelogram"])
        base, height = sample([x, sy.Integer(randint(1, 10))], k=2)
        unit = "\\mathrm{{cm}}"
        answer_unit = "\\mathrm{{cm^2}}"
        base_latex_with_unit = self._make_latex_with_unit(base, unit, with_parentheses=False)
        height_latex_with_unit = self._make_latex_with_unit(height, unit, with_parentheses=False)
        if selected_shape == "triangle":
            area_latex_with_unit = self._make_latex_with_unit(f"{sy.latex(base)} \\times {sy.latex(height)} \\div 2", answer_unit, with_parentheses=True)
            latex_problem = f"底辺が\\( {base_latex_with_unit} \\)、高さが\\( {height_latex_with_unit} \\)の三角形があります。\n"
            latex_problem += "三角形の面積を\\( x \\)を使った式で表しなさい。"
            latex_answer = "三角形の面積は、(底辺) \\( \\times \\) (高さ) \\( \\div 2 \\)なので、\n"
            latex_answer += f"\\( {area_latex_with_unit} \\)"
        elif selected_shape == "parallelogram":
            area_latex_with_unit = self._make_latex_with_unit(f"{sy.latex(base)} \\times {sy.latex(height)}", answer_unit, with_parentheses=True)
            latex_problem = f"底辺が\\( {base_latex_with_unit} \\)、高さが\\( {height_latex_with_unit} \\)の平行四辺形があります。\n"
            latex_problem += "平行四辺形の面積を\\( x \\)を使った式で表しなさい。"
            latex_answer = "平行四辺形の面積は、(底辺) \\( \\times \\) (高さ)なので、\n"
            latex_answer += f"\\( {area_latex_with_unit} \\)"
        return latex_answer, latex_problem
    
    def _make_expression_with_formula_volume_problem(self) -> Tuple[str, str]:
        """文字を使った体積の問題と解答を作成
        
        Returns:
            Tuple[str, str]: 問題と解答
            - latex_answer (str): latex形式と通常の文字列が混在していることを前提とした解答
            - latex_problem (str): latex形式と通常の文字列が混在していることを前提とした問題
        """
        x = sy.Symbol("x")
        item = choice(["ジュース", "お茶", "コーヒー", "水", "チャイ"])
        start_amount, delta = sample([x, sy.Integer(randint(1, 10))], k=2)
        start_unit, delta_unit = choice([("L", "L"), ("dL", "dL"), ("dL", "L"), ("L", "dL")])
        answered_unit = choice([start_unit, delta_unit])
        start_amount_latex_in_problem = self._make_latex_with_unit(start_amount, start_unit, with_parentheses=False)
        delta_latex_in_problem = self._make_latex_with_unit(delta, delta_unit, with_parentheses=False)
        if start_unit == answered_unit:
            start_amount_latex_in_answer = self._make_latex_with_unit(start_amount, start_unit, with_parentheses=True)
        else:
            non_adjusted_start_amount = self._make_latex_with_unit(start_amount, start_unit, with_parentheses=True)
            adjusted_start_amount = self._unit_adjuster(start_amount, from_unit=start_unit, to_unit=answered_unit, with_parentheses=True)
            start_amount_latex_in_answer = f"{non_adjusted_start_amount} = {adjusted_start_amount}"
        if delta_unit == answered_unit:
            delta_latex_in_answer = self._make_latex_with_unit(delta, delta_unit, with_parentheses=True)
        else:
            non_adjusted_delta_latex_in_answer = self._make_latex_with_unit(delta, delta_unit, with_parentheses=True)
            adjusted_delta_latex_in_answer = self._unit_adjuster(delta, from_unit=delta_unit, to_unit=answered_unit, with_parentheses=True)
            delta_latex_in_answer= f"{non_adjusted_delta_latex_in_answer} = {adjusted_delta_latex_in_answer}"
        start_amount_in_answer = self._amount_adjuster(start_amount, from_unit=start_unit, to_unit=answered_unit)
        delta_amount_in_answer = self._amount_adjuster(delta, from_unit=delta_unit, to_unit=answered_unit)
        increase_or_decrease = choice(["increase", "decrease"])
        if increase_or_decrease == "increase":
            action = "増やした"
            added_amount = f"{start_amount_in_answer} + {delta_amount_in_answer}"
            answer = self._make_latex_with_unit(added_amount, answered_unit, with_parentheses=True)
        elif increase_or_decrease == "decrease":
            action = "減らした"
            subtracted_amount = f"{start_amount_in_answer} - {delta_amount_in_answer}"
            answer = self._make_latex_with_unit(subtracted_amount, answered_unit, with_parentheses=True)
        latex_problem = f"初めに{item}が\\( {start_amount_latex_in_problem} \\)ありました。\n"
        latex_problem += f"\\( {delta_latex_in_problem} \\){action}後の体積\\( (\\mathrm{{{answered_unit}}}) \\)を、\\( x \\)を使った式で表しなさい。"
        latex_answer = f"初めの量が\\( {start_amount_latex_in_answer} \\)で、"
        latex_answer += f"{action}量が、\\( {delta_latex_in_answer} \\)なので、\n"
        latex_answer += f"答えは、\\( {answer} \\)となる。"
        return latex_answer, latex_problem
    
    def _make_expression_with_formula_weight_problem(self) -> Tuple[str, str]:
        """文字を用いた質量の問題と解答を出力
        
        Returns:
            Tuple [str, str]: 問題と解答
            - latex_answer (str): latex形式と通常の文字列が混在していることを前提とした解答
            - latex_problem (str): latex形式と通常の文字列が混在していることを前提とした問題
        """
        x = sy.Symbol("x")
        item = choice(["米", "小麦粉", "水", "塩"])
        start_amount, delta_amount = sample([x, sy.Integer(randint(1, 10) * 10)], k=2)
        start_unit, delta_unit = choice([("kg", "kg"), ("g", "g"), ("kg", "g"), ("g", "kg")])
        answered_unit = choice([start_unit, delta_unit])
        start_amount_in_problem = self._make_latex_with_unit(start_amount, start_unit, with_parentheses=False)
        delta_amount_in_problem = self._make_latex_with_unit(delta_amount, delta_unit, with_parentheses=False)
        if start_unit == answered_unit:
            start_amount_in_answer = self._make_latex_with_unit(start_amount, start_unit, with_parentheses=True)
        else:
            not_adjusted_start_amount = self._make_latex_with_unit(start_amount, start_unit, with_parentheses=True)
            adjusted_start_amount = self._unit_adjuster(start_amount, from_unit=start_unit, to_unit=answered_unit, with_parentheses=True)
            start_amount_in_answer = f"{not_adjusted_start_amount} = {adjusted_start_amount}"
        if delta_unit == answered_unit:
            delta_amount_in_answer = self._make_latex_with_unit(delta_amount, delta_unit, with_parentheses=True)
        else:
            not_adjusted_delta_amount = self._make_latex_with_unit(delta_amount, delta_unit, with_parentheses=True)
            adjusted_delta_amount = self._unit_adjuster(delta_amount, from_unit=delta_unit, to_unit=answered_unit, with_parentheses=True)
            delta_amount_in_answer = f"{not_adjusted_delta_amount} = {adjusted_delta_amount}"
        start_amount_for_calculation = self._amount_adjuster(start_amount, from_unit=start_unit, to_unit=answered_unit)
        delta_amount_for_calculation = self._amount_adjuster(delta_amount, from_unit=delta_unit, to_unit=answered_unit)
        increase_or_decrease = choice(["increase", "decrease"])
        if increase_or_decrease == "increase":
            action = "増やした"
            added_amount = f"{start_amount_for_calculation} + {delta_amount_for_calculation}"
            answer = self._make_latex_with_unit(added_amount, answered_unit, with_parentheses=True)
        elif increase_or_decrease == "decrease":
            action = "減らした"
            subtracted_amount = f"{start_amount_for_calculation} - {delta_amount_for_calculation}"
            answer = self._make_latex_with_unit(subtracted_amount, answered_unit, with_parentheses=True)
        latex_problem = f"初めに{item}が\\( {start_amount_in_problem} \\)ありました。\n"
        latex_problem += f"\\( {delta_amount_in_problem} \\){action}後の重さ\\( (\\mathrm{{{answered_unit}}}) \\)を、\\( x \\)を使った式で表しなさい。"
        latex_answer = f"初めの量が\\( {start_amount_in_answer} \\)で、"
        latex_answer += f"{action}量が、\\( {delta_amount_in_answer} \\)なので、\n"
        latex_answer += f"答えは、\\( {answer} \\)となる。"
        return latex_answer, latex_problem  
    
    def _make_expression_with_formula_price_problem(self) -> Tuple[str, str]:
        """文字を用いた価格の問題と解答を出力

        Returns:
            Tuple[str, str]: 解答と問題
            - latex_answer (str): latex形式と通常の文字列が混在していることを前提とした解答
            - latex_problem (str): latex形式と通常の文字列が混在していることを前提とした問題
        """
        
        def random_ratio(selected_ratio: str) -> Tuple[sy.Float, str]:
            """ランダムな割合と、その日本語表示をあわせて出力する

            Args:
                selected_ratio (str): 百分率(percentage)と割合(japanese_ratio)の2つから選択する
                digit_under_decimal_point (int, optional): 小数点以下の桁数(2桁まで)を決定。デフォルトは1

            Raises:
                ValueError: digit_under_decimalに1,2以外の値が指定された場合に挙上
                ValueError: selected_ratioにpercentage, japanese_percentage以外のものが指定された場合に挙上する

            Returns:
                Tuple[sy.Float, str]: 計算用の値と、出力用の日本語
                - ratio_value (sy.Float())

            Remind:
                出力用の日本語は、\\( \\)で囲まないことを前提としている
            """
            digit_under_decimal_point = 1
            if digit_under_decimal_point == 1:
                ratio_value = 0.1 * sy.Integer(randint(1, 9))
            ratio_value = round(ratio_value, 6)
            if selected_ratio == "percentage":
                normalized_percentage = self._decimal_normalize(sy.latex(ratio_value * 100))
                ratio_out_of_latex = f"\\( {normalized_percentage} \\% \\)"
            elif selected_ratio == "japanese_percentage":
                digit_list = sy.latex(ratio_value)[2:]
                japanese_percentage_names = ["割", "分"]
                japanese_percentage_str = ""
                for digit, name in zip(digit_list, japanese_percentage_names):
                    if digit != "0":
                        japanese_percentage_str += (digit + name)
                ratio_out_of_latex = japanese_percentage_str
            else:
                raise ValueError(f"'selected_ratio' must be 'japanese_percentage' or 'percentage'. {selected_ratio} is unconcerned value.")
            return ratio_value, ratio_out_of_latex

        x = sy.Symbol("x")
        items = ["お菓子", "ジュース", "お弁当", "洗剤"]
        problem_theme = choice(["discount", "multiple_items_without_discount", "multiple_items_with_discount"])
        if problem_theme == "discount":
            item = choice(items)
            price_before_discount = x
            discount_ratio_value, discount_ratio_out_of_latex = random_ratio(choice(["percentage", "japanese_percentage"]))
            remained_ratio_value = 1 - discount_ratio_value
            remained_ratio_str = self._decimal_normalize(remained_ratio_value)
            price_after_discount = self._multiply_or_divide(price_before_discount, remained_ratio_value, multiply_or_divide="multiply")
            latex_problem = f"初めに\\( {sy.latex(x)} \\)円の{item}がありました。"
            latex_problem += f"{discount_ratio_out_of_latex}だけ値引きされたときの金額を、\\( x \\)を用いて表しなさい。"
            latex_answer = f"{discount_ratio_out_of_latex}だけ値引きされたということは、"
            latex_answer += f"値引きされた後の金額を小数の割合で示すと、\\( {remained_ratio_str} \\)となる。\n"
            latex_answer += f"よって答えは、\\( {price_after_discount} \\)円。"
        elif problem_theme == "multiple_items_without_discount":
            first_item, second_item = sample(items, k=2)
            first_price, second_price = sample([x, sy.Integer(randint(1, 10) * 50)], k=2)
            first_price_in_answer = sy.latex(first_price)
            second_price_in_answer = sy.latex(second_price)
            latex_problem = f"\\( {sy.latex(first_price)} \\)円の{first_item}と、"
            latex_problem += f"\\( {sy.latex(second_price)} \\)円の{second_item}がありました。\n"
            latex_problem += "2つを一緒に買ったときの金額を、\\( x \\)を用いて表しなさい。"
            latex_answer = "1つ目の価格と2つ目の価格を合わせると、\n"
            latex_answer += f"\\( {first_price_in_answer} + {second_price_in_answer} \\)円となる。"
        elif problem_theme == "multiple_items_with_discount":
            first_item, second_item = sample(items, k=2)
            first_price, second_price = sample([x, sy.Integer(randint(1, 10) * 100)], k=2)
            discount_type = choice(["first_item", "second_item", "both"])
            if discount_type == "first_item":
                discount_ratio_value, discount_ratio_out_of_latex = random_ratio(choice(["percentage", "japanese_percentage"]))
                remained_ratio_value = 1 - discount_ratio_value
                remained_ratio_str = self._decimal_normalize(remained_ratio_value)
                first_price_after_discount = self._multiply_or_divide(first_price, remained_ratio_value, multiply_or_divide="multiply")
                latex_problem = f"\\( {first_price} \\)円の{first_item}と、\\( {second_price} \\)円の{second_item}がありました。\n"
                latex_problem += f"{first_item}が{discount_ratio_out_of_latex}だけ値引きされた後に、2つを一緒に買った時の金額を、\\( x \\)を用いて表しなさい。"
                latex_answer = f"{discount_ratio_out_of_latex}だけ値引きされたということは、\n"
                latex_answer += f"値引きされた後の{first_item}の金額を小数の割合で示すと\\( {remained_ratio_str} \\)、"
                latex_answer += f"金額は\\( {first_price_after_discount} \\)円となる。\n"
                latex_answer += f"{second_item}の金額と合わせると、\\( {first_price_after_discount} + {second_price} \\)円となる。"
            elif discount_type == "second_item":
                discount_ratio_value, discount_ratio_out_of_latex = random_ratio(choice(["percentage", "japanese_percentage"]))
                remained_ratio_value = 1 - discount_ratio_value
                remained_ratio_str = self._decimal_normalize(remained_ratio_value)
                second_price_after_discount = self._multiply_or_divide(second_price, remained_ratio_value, multiply_or_divide="multiply")
                latex_problem = f"\\( {first_price} \\)円の{first_item}と、\\( {second_price} \\)円の{second_item}がありました。\n"
                latex_problem += f"{second_item}が{discount_ratio_out_of_latex}だけ値引きされた後に、2つを一緒に買った時の金額を、\\( x \\)を用いて表しなさい。"
                latex_answer = f"{discount_ratio_out_of_latex}だけ値引きされたということは、\n"
                latex_answer += f"値引きされた後の{second_item}の金額を小数の割合で示すと\\( {remained_ratio_str} \\)、"
                latex_answer += f"金額は\\( {second_price_after_discount} \\)円となる。\n"
                latex_answer += f"{first_item}の金額と合わせると、\\( {first_price} + {second_price_after_discount} \\)円となる。"
            elif discount_type == "both":
                discount_ratio_value1, discount_ratio_out_of_latex1 = random_ratio(choice(["percentage", "japanese_percentage"]))
                remained_ratio_value1 = 1 - discount_ratio_value1
                remained_ratio_str1 = self._decimal_normalize(remained_ratio_value1)
                first_price_after_discount = self._multiply_or_divide(first_price, remained_ratio_value1, multiply_or_divide="multiply")
                discount_ratio_value2, discount_ratio_out_of_latex2 = random_ratio(choice(["percentage", "japanese_percentage"]))
                remained_ratio_value2 = 1 - discount_ratio_value2
                remained_ratio_str2 = self._decimal_normalize(remained_ratio_value2)
                second_price_after_discount = self._multiply_or_divide(second_price, remained_ratio_value2, multiply_or_divide="multiply")
                latex_problem = f"\\( {first_price} \\)円の{first_item}と、\\( {second_price} \\)円の{second_item}がありました。\n"
                latex_problem += f"{first_item}が{discount_ratio_out_of_latex1}、"
                latex_problem += f"{second_item}が{discount_ratio_out_of_latex2}だけそれぞれ値引きされた後に、\n"
                latex_problem += f"2つを一緒に買った時の金額を、\\( x \\)を用いて表しなさい。"
                latex_answer = f"{discount_ratio_out_of_latex1}だけ値引きされたということは、\n"
                latex_answer += f"値引きされた後の{first_item}の金額を小数の割合で示すと\\( {remained_ratio_str1} \\)、"
                latex_answer += f"金額は\\( {first_price_after_discount} \\)円となる。\n"
                latex_answer += f"また、同じように値引きされた後の{second_item}の金額を小数の割合で示すと\\( {remained_ratio_str2} \\)、"
                latex_answer += f"金額は\\( {second_price_after_discount} \\)円となる。\n"
                latex_answer += f"2つの金額と合わせると、\\( {first_price_after_discount} + {second_price_after_discount} \\)円となる。"
        return latex_answer, latex_problem
        
    def _make_expression_with_formula_and_calculate_area_problem(self) -> Tuple[str, str]:
        """面積をテーマとした式の表現と計算の問題と解答を出力する
        
        Returns:
            Tuple[str, str]: 問題と解答
            - latex_answer (str): latex形式と通常の文字列が混在していることを前提とした解答
            - latex_problem (str): latex形式と通常の文字列が混在していることを前提とした問題
        """
        x = sy.Symbol("x")
        base, height = sample([x, sy.Integer(randint(1, 10))], k=2)
        unit = "\\mathrm{{cm}}"
        answer_unit = "\\mathrm{{cm^2}}"
        base_latex_with_unit = self._make_latex_with_unit(base, unit, with_parentheses=False)
        height_latex_with_unit = self._make_latex_with_unit(height, unit, with_parentheses=False)
        if base == x:
            substitute_target = "底辺"
        elif height == x:
            substitute_target = "高さ"
        substitute_value = sy.Integer(randint(1, 10))
        substitute_value_with_unit = self._make_latex_with_unit(substitute_value, unit, with_parentheses=False)
        selected_shape = choice(["triangle", "parallelogram"])
        if selected_shape == "triangle":
            shape = "三角形"
            area_formula = "(底辺) \\( \\times \\) (高さ) \\( \\div 2 \\)"
            area_formula_after_substitution = self._make_latex_with_unit(f"{sy.latex(base)} \\times {sy.latex(height)} \\div 2", answer_unit, with_parentheses=True)
            area_value = (base * height).subs(x, substitute_value) * sy.Rational(1, 2)
        elif selected_shape == "parallelogram":
            shape = "平行四辺形"
            area_formula = "(底辺) \\( \\times \\) (高さ)"
            area_formula_after_substitution = self._make_latex_with_unit(f"{sy.latex(base)} \\times {sy.latex(height)}", answer_unit, with_parentheses=True)
            area_value = (base * height).subs(x, substitute_value)
        area_value_latex_with_unit = self._make_latex_with_unit(area_value, answer_unit, with_parentheses=False)
        latex_problem = f"底辺が\\( {base_latex_with_unit} \\), 高さが\\( {height_latex_with_unit} \\)の{shape}があります。\n"
        latex_problem += f"(1){shape}の面積を\\( x \\)を使った式で表しなさい。\n"
        latex_problem += f"(2){substitute_target}が\\( {substitute_value_with_unit} \\)のときの面積を求めなさい。"
        latex_answer = f"(1){shape}の面積は、{area_formula}なので、\n"
        latex_answer += f"\\( {area_formula_after_substitution} \\)\n"
        latex_answer += f"(2)(1)で表した式の\\( x \\)が\\( {sy.latex(substitute_value)} \\)になるので、\n"
        latex_answer += f"面積は、\\( {area_value_latex_with_unit} \\)"
        return latex_answer, latex_problem
    
    def _make_expression_with_formula_and_calculate_volume_problem(self) -> Tuple[str, str]:
        """体積をテーマとした式の表現と計算の問題と解答を出力する。

        Returns:
            Tuple[str, str]: 問題と解答
            - latex_answer (str): latex形式と通常の文字列が混在していることを前提とした解答
            - latex_problem (str): latex形式と通常の文字列が混在していることを前提とした問題
        """
        item = choice(["ジュース", "お茶", "コーヒー", "水", "チャイ"])
        a_unit, b_unit = choice([("L", "L"), ("dL", "dL"), ("dL", "L"), ("L", "dL")])
        k_unit = choice([a_unit, b_unit])
        increase_or_decrease = choice(["increase", "decrease"])
        # a + b = k (by k_unit)
        if increase_or_decrease == "increase":
            action = "増やした"
            a = sy.Integer(randint(1, 10) * 10)
            b = sy.Integer(randint(1, 10) * 10)
            k = a + b
        # a - b = k (by k_unit)
        elif increase_or_decrease == "decrease":
            action = "減らした"
            k = sy.Integer(randint(1, 10) * 10)
            b = k + sy.Integer(randint(1, 10) * 10)
            a = b + k
        x = sy.Symbol("x")
        # which is x?
        replaced_by_x = choice(["a", "b"])
        if replaced_by_x == "a":
            # for problem(2)
            substitute_target = "初めの量"
            # substitute_value = self._amount_calculator_for_adjustment(a, from_unit=k_unit, to_unit=a_unit)
            substitute_value = self._unit_adjuster(a, from_unit=k_unit, to_unit=a_unit, with_parentheses=False)
            a_in_problem1_with_unit = self._make_latex_with_unit(x, a_unit, with_parentheses=False)
            b_in_problem1_with_unit = self._unit_adjuster(b, from_unit=k_unit, to_unit=b_unit, with_parentheses=False)
            if a_unit == k_unit:
                a_in_answer1 = self._make_latex_with_unit(x, a_unit, with_parentheses=True)
            else:
                a_before_adjustment = self._make_latex_with_unit(x, a_unit, with_parentheses=True)
                a_after_adjustment = self._unit_adjuster(x, from_unit=a_unit, to_unit=k_unit, with_parentheses=True)
                a_in_answer1 = f"{a_before_adjustment} = {a_after_adjustment}"
            if b_unit == k_unit:
                b_in_answer1 = self._make_latex_with_unit(b, b_unit, with_parentheses=True)
            else:
                b_before_adjustment = self._unit_adjuster(b, from_unit=k_unit, to_unit=b_unit, with_parentheses=True)
                b_after_adjustment = self._make_latex_with_unit(b, k_unit, with_parentheses=True)
                b_in_answer1 = f"{b_before_adjustment} = {b_after_adjustment}"
            a_in_formula_in_answer1 = self._amount_adjuster(x, from_unit=a_unit, to_unit=k_unit)
            if increase_or_decrease == "increase":
                answer1 = f"{a_in_formula_in_answer1} + {b}"
            elif increase_or_decrease == "decrease":
                answer1 = f"{a_in_formula_in_answer1} - {b}"
        elif replaced_by_x == "b":
            if increase_or_decrease == "increase":
                substitute_target = "増えた量"
            elif increase_or_decrease == "decrease":
                substitute_target = "減らした量"
            substitute_value = self._unit_adjuster(b, from_unit=k_unit, to_unit=b_unit, with_parentheses=False)
            a_in_problem1_with_unit = self._unit_adjuster(a, from_unit=k_unit, to_unit=a_unit, with_parentheses=False)
            b_in_problem1_with_unit = self._make_latex_with_unit(x, b_unit, with_parentheses=False)
            if a_unit == k_unit:
                a_in_answer1 = self._make_latex_with_unit(a, a_unit, with_parentheses=True)
            else:
                a_before_adjustment = self._unit_adjuster(a, from_unit=k_unit, to_unit=a_unit, with_parentheses=True)
                a_after_adjustment = self._make_latex_with_unit(a, k_unit, with_parentheses=True)
                a_in_answer1 = f"{a_before_adjustment} = {a_after_adjustment}"
            if b_unit == k_unit:
                b_in_answer1 = self._make_latex_with_unit(x, b_unit, with_parentheses=True)
            else:
                b_before_adjustment = self._make_latex_with_unit(x, b_unit, with_parentheses=True)
                b_after_adjustment = self._unit_adjuster(x, from_unit=b_unit, to_unit=k_unit, with_parentheses=True)
                b_in_answer1 = f"{b_before_adjustment} = {b_after_adjustment}"
            b_in_formula_in_answer1 = self._amount_adjuster(x, from_unit=b_unit, to_unit=k_unit)
            if increase_or_decrease == "increase":
                answer1 = f"{a} + {b_in_formula_in_answer1}"
            elif increase_or_decrease == "decrease":
                answer1 = f"{a} - {b_in_formula_in_answer1}"
        latex_problem = f"初めに{item}が\\( {a_in_problem1_with_unit} \\)ありました。\n"
        latex_problem += f"(1)\\( {b_in_problem1_with_unit} \\)だけ{action}した後の体積\\( (\\mathrm{{{k_unit}}}) \\)を、\\( x \\)を使って表しなさい。\n"
        latex_problem += f"(2){substitute_target}が\\( {substitute_value} \\)のときの値を計算しなさい。"
        latex_answer = f"(1)初めの量が、\\( {a_in_answer1} \\), {action}量が\\( {b_in_answer1} \\)なので、\n"
        latex_answer += f"\\( {answer1} \\)\n"
        latex_answer += f"(2)(1)の式の\\( x \\)が\\( {substitute_value} \\)になるので、"
        answer2 = self._make_latex_with_unit(k, k_unit, with_parentheses=False)
        latex_answer += f"\\( {answer2} \\)"
        return latex_answer, latex_problem

    def _make_expression_with_formula_and_calculate_weight_problem(self) -> Tuple[str, str]:
        """重さをテーマとした式の表現と計算の問題と解答を出力する。

        Returns:
            Tuple[str, str]: 問題と解答
            - latex_answer (str): latex形式と通常の文字列が混在していることを前提とした解答
            - latex_problem (str): latex形式と通常の文字列が混在していることを前提とした問題
        """
        item = choice(["米", "小麦粉", "水", "塩"])
        a_unit, b_unit = choice([("kg", "kg"), ("g", "g"), ("kg", "g"), ("g", "kg")])
        k_unit = choice([a_unit, b_unit])
        increase_or_decrease = choice(["increase", "decrease"])
        # a + b = k (by k_unit)
        if increase_or_decrease == "increase":
            action = "増やした"
            a = sy.Integer(randint(1, 10) * 100)
            b = sy.Integer(randint(1, 10) * 100)
            k = a + b
        # a - b = k (by k_unit)
        elif increase_or_decrease == "decrease":
            action = "減らした"
            k = sy.Integer(randint(1, 10) * 100)
            b = k + sy.Integer(randint(1, 10) * 100)
            a = b + k
        x = sy.Symbol("x")
        # which is x?
        replaced_by_x = choice(["a", "b"])
        if replaced_by_x == "a":
            # for problem(2)
            substitute_target = "初めの量"
            # substitute_value = self._amount_calculator_for_adjustment(a, from_unit=k_unit, to_unit=a_unit)
            substitute_value = self._unit_adjuster(a, from_unit=k_unit, to_unit=a_unit, with_parentheses=False)
            a_in_problem1_with_unit = self._make_latex_with_unit(x, a_unit, with_parentheses=False)
            b_in_problem1_with_unit = self._unit_adjuster(b, from_unit=k_unit, to_unit=b_unit, with_parentheses=False)
            if a_unit == k_unit:
                a_in_answer1 = self._make_latex_with_unit(x, a_unit, with_parentheses=True)
            else:
                a_before_adjustment = self._make_latex_with_unit(x, a_unit, with_parentheses=True)
                a_after_adjustment = self._unit_adjuster(x, from_unit=a_unit, to_unit=k_unit, with_parentheses=True)
                a_in_answer1 = f"{a_before_adjustment} = {a_after_adjustment}"
            if b_unit == k_unit:
                b_in_answer1 = self._make_latex_with_unit(b, b_unit, with_parentheses=True)
            else:
                b_before_adjustment = self._unit_adjuster(b, from_unit=k_unit, to_unit=b_unit, with_parentheses=True)
                b_after_adjustment = self._make_latex_with_unit(b, k_unit, with_parentheses=True)
                b_in_answer1 = f"{b_before_adjustment} = {b_after_adjustment}"
            a_in_formula_in_answer1 = self._amount_adjuster(x, from_unit=a_unit, to_unit=k_unit)
            if increase_or_decrease == "increase":
                answer1 = f"{a_in_formula_in_answer1} + {b}"
            elif increase_or_decrease == "decrease":
                answer1 = f"{a_in_formula_in_answer1} - {b}"
        elif replaced_by_x == "b":
            if increase_or_decrease == "increase":
                substitute_target = "増えた量"
            elif increase_or_decrease == "decrease":
                substitute_target = "減らした量"
            # substitute_value = self._amount_calculator_for_adjustment(b, from_unit=k_unit, to_unit=b_unit)
            substitute_value = self._unit_adjuster(b, from_unit=k_unit, to_unit=b_unit, with_parentheses=False)
            a_in_problem1_with_unit = self._unit_adjuster(a, from_unit=k_unit, to_unit=a_unit, with_parentheses=False)
            b_in_problem1_with_unit = self._make_latex_with_unit(x, b_unit, with_parentheses=False)
            if a_unit == k_unit:
                a_in_answer1 = self._make_latex_with_unit(a, a_unit, with_parentheses=True)
            else:
                a_before_adjustment = self._unit_adjuster(a, from_unit=k_unit, to_unit=a_unit, with_parentheses=True)
                a_after_adjustment = self._make_latex_with_unit(a, k_unit, with_parentheses=True)
                a_in_answer1 = f"{a_before_adjustment} = {a_after_adjustment}"
            if b_unit == k_unit:
                b_in_answer1 = self._make_latex_with_unit(x, b_unit, with_parentheses=True)
            else:
                b_before_adjustment = self._make_latex_with_unit(x, b_unit, with_parentheses=True)
                b_after_adjustment = self._unit_adjuster(x, from_unit=b_unit, to_unit=k_unit, with_parentheses=True)
                b_in_answer1 = f"{b_before_adjustment} = {b_after_adjustment}"
            b_in_formula_in_answer1 = self._amount_adjuster(x, from_unit=b_unit, to_unit=k_unit)
            if increase_or_decrease == "increase":
                answer1 = f"{a} + {b_in_formula_in_answer1}"
            elif increase_or_decrease == "decrease":
                answer1 = f"{a} - {b_in_formula_in_answer1}"
        latex_problem = f"初めに{item}が\\( {a_in_problem1_with_unit} \\)ありました。\n"
        latex_problem += f"(1)\\( {b_in_problem1_with_unit} \\)だけ{action}した後の重さ\\( (\\mathrm{{{k_unit}}}) \\)を、\\( x \\)を使って表しなさい。\n"
        latex_problem += f"(2){substitute_target}が\\( {substitute_value} \\)のときの値を計算しなさい。"
        latex_answer = f"(1)初めの量が、\\( {a_in_answer1} \\), {action}量が\\( {b_in_answer1} \\)なので、\n"
        latex_answer += f"\\( {answer1} \\)\n"
        latex_answer += f"(2)(1)の式の\\( x \\)が\\( {substitute_value} \\)になるので、"
        answer2 = self._make_latex_with_unit(k, k_unit, with_parentheses=False)
        latex_answer += f"\\( {answer2} \\)"
        return latex_answer, latex_problem
    
    def _make_expression_with_formula_and_calculate_price_problem(self) -> Tuple[str, str]:
        """値段をテーマとした式の表現と計算の問題と解答を出力する。

        Returns:
            Tuple[str, str]: 問題と解答
            - latex_answer (str): latex形式と通常の文字列が混在していることを前提とした解答
            - latex_problem (str): latex形式と通常の文字列が混在していることを前提とした問題
        """
        
        def random_ratio() -> Tuple[sy.Float, str]:
            """ランダムな割合と、その日本語表示をあわせて出力する
            
            Returns:
                Tuple[sy.Float, str]: 計算用の値と、出力用の日本語
                - ratio_value (sy.Float())

            Remind:
                出力用の日本語は、\\( \\)で囲まないことを前提としている
            """
            digit_under_decimal_point = 1
            if digit_under_decimal_point == 1:
                ratio_value = 0.1 * sy.Integer(randint(1, 9))
            ratio_value = round(ratio_value, 6)
            selected_ratio = choice(["percentage", "japanese_percentage"])
            if selected_ratio == "percentage":
                normalized_percentage = self._decimal_normalize(sy.latex(ratio_value * 100))
                ratio_out_of_latex = f"\\( {normalized_percentage} \\% \\)"
            elif selected_ratio == "japanese_percentage":
                digit_list = sy.latex(ratio_value)[2:]
                japanese_percentage_names = ["割", "分"]
                japanese_percentage_str = ""
                for digit, name in zip(digit_list, japanese_percentage_names):
                    if digit != "0":
                        japanese_percentage_str += (digit + name)
                ratio_out_of_latex = japanese_percentage_str
            else:
                raise ValueError(f"")
            return ratio_value, ratio_out_of_latex
        
        x = sy.Symbol("x")
        items = ["お菓子", "ジュース", "お弁当", "洗剤"]
        problem_theme = choice(["discount", "multiple_items_without_discount", "multiple_items_with_discount"])
        if problem_theme == "discount":
            item = choice(items)
            price_before_discount = sy.Integer(randint(1, 50) * 100)
            discount_ratio_value, discount_ratio = random_ratio()
            remained_ratio_value = 1 - discount_ratio_value
            remained_ratio_str = self._decimal_normalize(remained_ratio_value)
            price_after_discount = self._decimal_normalize(price_before_discount * remained_ratio_value)
            price_after_discount_for_problem1 = self._multiply_or_divide(x, remained_ratio_value, multiply_or_divide="multiply")
            latex_problem = f"\\( x \\)円の{item}がありました。\n"
            latex_problem += f"(1){discount_ratio}だけ値引きされたときの金額を、\\( x \\)を用いて表しなさい。\n"
            latex_problem += f"(2){item}の元の値段が\\( {price_before_discount} \\)円だったときの金額を求めなさい。"
            latex_answer = f"(1){discount_ratio}だけ値引きされたということは、"
            latex_answer += f"値引きされた後の金額を小数の割合で示すと、\\( {remained_ratio_str} \\)となる。\n"
            latex_answer += f"よって答えは、\\( {price_after_discount_for_problem1} \\)円。\n"
            latex_answer += f"(2)(1)で使われた\\( x \\)が\\( {price_before_discount} \\)になるので、\n"
            latex_answer += f"\\( {price_after_discount} \\)円が答えとなる。"
        elif problem_theme == "multiple_items_without_discount":
            first_item, second_item = sample(items, k=2)
            first_price, second_price = sy.Integer(randint(1, 50) * 100), sy.Integer(randint(1, 50) * 100)
            total_price = first_price + second_price
            substitute_item = choice([first_item, second_item])
            if substitute_item == first_item:
                first_price_in_problem = x
                second_price_in_problem = second_price
                substitute_value = first_price
            elif substitute_item == second_item:
                first_price_in_problem = first_price
                second_price_in_problem = x
                substitute_value = second_price
            total_price_in_answer1 = f"{first_price_in_problem} + {second_price_in_problem}"
            latex_problem = f"\\( {first_price_in_problem} \\)円の{first_item}と、\\( {second_price_in_problem} \\)円の{second_item}がありました。\n"
            latex_problem += f"(1)2つを一緒に買ったときの金額を、\\( x \\)を用いて表しなさい。\n"
            latex_problem += f"(2){substitute_item}が\\( {substitute_value} \\)円だったときの金額を求めなさい。"
            latex_answer = f"(1)1つ目の価格と2つ目の価格を合わせると、\\( {total_price_in_answer1} \\)となる。\n"
            latex_answer += f"(2)(1)で表した式の\\( x \\)が\\( {substitute_value} \\)になるので、\\( {total_price} \\)円が答えとなる。"
        elif problem_theme == "multiple_items_with_discount":
            first_item, second_item = sample(items, k=2)
            first_price_before_discount, second_price_before_discount = sy.Integer(randint(1, 50) * 100), sy.Integer(randint(1, 50) * 100)
            substitute_item = choice([first_item, second_item])
            # condition variance
            if substitute_item == first_item:
                first_price_in_problem1 = x
                second_price_in_problem1 = second_price_before_discount
                substitute_value = first_price_before_discount
            elif substitute_item == second_item:
                first_price_in_problem1 = first_price_before_discount
                second_price_in_problem1 = x
                substitute_value = second_price_before_discount
            discount_type = choice(["first_item_only", "second_item_only", "both"])
            if discount_type != "both":
                if discount_type == "first_item_only":
                    discount_ratio_value, discount_ratio = random_ratio()
                    discount_item = first_item
                    remained_ratio = 1 - discount_ratio_value
                    remained_ratio_str = self._decimal_normalize(remained_ratio)
                    not_discount_item = second_item
                    discount_item_price = self._multiply_or_divide(first_price_in_problem1, remained_ratio, multiply_or_divide="multiply")
                    not_discount_item_price = second_price_in_problem1
                    total_price_in_answer1 = f"{discount_item_price} + {not_discount_item_price}"
                    total_price_in_answer2 = self._decimal_normalize(first_price_before_discount * remained_ratio + second_price_before_discount)
                elif discount_type == "second_item_only":
                    discount_ratio_value, discount_ratio = random_ratio()
                    discount_item = second_item
                    remained_ratio = 1 - discount_ratio_value
                    remained_ratio_str = self._decimal_normalize(remained_ratio)
                    not_discount_item = first_item
                    discount_item_price = self._multiply_or_divide(second_price_in_problem1, remained_ratio, multiply_or_divide="multiply")
                    not_discount_item_price = first_price_in_problem1
                    total_price_in_answer1 = f"{not_discount_item_price} + {discount_item_price}"
                    total_price_in_answer2 = self._decimal_normalize(first_price_before_discount + second_price_before_discount * remained_ratio)
                latex_problem = f"\\( {first_price_in_problem1} \\)円の{first_item}と、\\( {second_price_in_problem1} \\)円の{second_item}がありました。\n"
                latex_problem += f"(1){discount_item}が{discount_ratio}だけ値引きされたときの合計の金額を、\\( x \\)を用いて表しなさい。\n"
                latex_problem += f"(2){substitute_item}が\\( {substitute_value} \\)円だったときの合計の金額を求めなさい。"
                latex_answer = f"(1){discount_ratio}だけ値引きされるということは、\n"
                latex_answer += f"値引きされた後の金額を小数の割合で示すと\\( {remained_ratio_str} \\)、金額は\\( {discount_item_price} \\)となる。\n"
                latex_answer += f"{not_discount_item}と合わせると、\\( {total_price_in_answer1} \\)円となる。\n"
                latex_answer += f"(2)(1)で表した式の\\( x \\)が\\( {substitute_value} \\)になるので、\n"
                latex_answer += f"\\( {total_price_in_answer2} \\)円となる。"
            else:
                discount_ratio_value1, discount_ratio1 = random_ratio()
                discount_ratio_value2, discount_ratio2 = random_ratio()
                remained_ratio1 = 1 - discount_ratio_value1
                remained_ratio_str1 = self._decimal_normalize(remained_ratio1)
                remained_ratio2 = 1 - discount_ratio_value2
                remained_ratio_str2 = self._decimal_normalize(remained_ratio2)
                discount_item1_price = self._multiply_or_divide(first_price_in_problem1, remained_ratio1, multiply_or_divide="multiply")
                discount_item2_price = self._multiply_or_divide(second_price_in_problem1, remained_ratio2, multiply_or_divide="multiply")
                total_price_in_answer1 = f"{discount_item1_price} + {discount_item2_price}"
                total_price_in_answer2 = self._decimal_normalize(first_price_before_discount * remained_ratio1 + second_price_before_discount * remained_ratio2)
                latex_problem = f"\\( {first_price_in_problem1} \\)円の{first_item}と、\\( {second_price_in_problem1} \\)円の{second_item}がありました。\n"
                latex_problem += f"(1){first_item}が{discount_ratio1}、{second_item}が{discount_ratio2}だけ値引きされたときの合計の金額を、\n"
                latex_problem += f"\\( x \\)を用いて表しなさい。\n"
                latex_problem += f"(2){substitute_item}が\\( {substitute_value} \\)円だったときの合計の金額を求めなさい。"
                latex_answer = f"(1){discount_ratio1}と{discount_ratio2}だけ値引きされるということは、\n"
                latex_answer += f"値引きされた後の金額を小数の割合で示すと、{first_item}は\\( {remained_ratio_str1} \\)、{second_item}は\\( {remained_ratio_str2} \\)、\n"
                latex_answer += f"金額は\\( {discount_item1_price}, {discount_item2_price} \\)となる。\n"
                latex_answer += f"両方を合わせると、\\( {total_price_in_answer1} \\)となる。\n"
                latex_answer += f"(2)(1)で表した式の\\( x \\)が\\( {substitute_value} \\)になるので、\n"
                latex_answer += f"\\( {total_price_in_answer2} \\)円となる。"
        return latex_answer, latex_problem
    
    def _make_expression_with_formula_and_solve_area_problem(self) -> Tuple[str, str]:
        """式での表現と、xを求める面積の問題と解答を出力

        Returns:
            Tuple[str, str]: 問題と解答
            - latex_answer (str): latex形式と通常の文字列が混在していることを前提とした解答
            - latex_problem (str): latex形式と通常の文字列が混在していることを前提とした問題
        """
        x = sy.Symbol("x")
        base, height = sample([x, sy.Integer(randint(1, 10))], k=2)
        unit = "\\mathrm{{cm}}"
        answer_unit = "\\mathrm{{cm^2}}"
        base_latex_with_unit = self._make_latex_with_unit(base, unit, with_parentheses=False)
        height_latex_with_unit = self._make_latex_with_unit(height, unit, with_parentheses=False)
        if base == x:
            substitute_target = "底辺"
        elif height == x:
            substitute_target = "高さ"
        substitute_value = sy.Integer(randint(1, 5))
        substitute_value_with_unit = self._make_latex_with_unit(substitute_value, unit, with_parentheses=False)
        selected_shape = choice(["triangle", "parallelogram"])
        if selected_shape == "triangle":
            shape = "三角形"
            area_formula = "(底辺) \\( \\times \\) (高さ) \\( \\div 2 \\)"
            area_formula_after_substitution = self._make_latex_with_unit(f"{sy.latex(base)} \\times {sy.latex(height)} \\div 2", answer_unit, with_parentheses=True)
            area_value = (base * height).subs(x, substitute_value) * sy.Rational(1, 2)
        elif selected_shape == "parallelogram":
            shape = "平行四辺形"
            area_formula = "(底辺) \\( \\times \\) (高さ)"
            area_formula_after_substitution = self._make_latex_with_unit(f"{sy.latex(base)} \\times {sy.latex(height)}", answer_unit, with_parentheses=True)
            area_value = (base * height).subs(x, substitute_value)
        area_value_latex_with_unit = self._make_latex_with_unit(area_value, answer_unit, with_parentheses=False)
        latex_problem = f"底辺が\\( {base_latex_with_unit} \\), 高さが\\( {height_latex_with_unit} \\)の{shape}があります。\n"
        latex_problem += f"(1){shape}の面積を\\( x \\)を使った式で表しなさい。\n"
        latex_problem += f"(2)面積が\\( {area_value_latex_with_unit} \\)のときの{substitute_target}は何\\( \\mathrm{{cm}} \\)ですか。\n"
        latex_problem += "\\( x \\)に\\( 1, 2, 3, \\cdots \\)を当てはめて求めなさい。"
        latex_answer = f"(1){shape}の面積は、{area_formula}なので、\n"
        latex_answer += f"\\( {area_formula_after_substitution} \\)\n"
        latex_answer += "(2)(1)で表した式の\\( x \\)に、指定された数を当てはめていくと、\n"
        latex_answer += f"\\( x = {sy.latex(substitute_value)} \\)で面積が\\( {area_value_latex_with_unit} \\)になる。"
        latex_answer += f"よって答えは、\\( {substitute_value_with_unit} \\)"
        return latex_answer, latex_problem
    
    def _make_expression_with_formula_and_solve_volume_problem(self) -> Tuple[str, str]:
        """式での表現と、xを求める体積の問題と解答を作成
        
        Returns:
            Tuple[str, str]: 問題と解答
            - latex_answer (str): latex形式と通常の文字列が混在していることを前提とした解答
            - latex_problem (str): latex形式と通常の文字列が混在していることを前提とした問題
        
        Note:
            負の数を登場させないために、初めに計算結果の方で単位を統一して計算してから変換している
        """
        item = choice(["ジュース", "お茶", "コーヒー", "水", "チャイ"])
        a_unit, b_unit = choice([("L", "L"), ("dL", "dL"), ("dL", "L"), ("L", "dL")])
        k_unit = choice([a_unit, b_unit])
        increase_or_decrease = choice(["increase", "decrease"])
        # a + b = k (by k_unit)
        if increase_or_decrease == "increase":
            action = "増やした"
            a = sy.Integer(randint(1, 5) * 10)
            b = sy.Integer(randint(1, 5) * 10)
            k = a + b
        # a - b = k (by k_unit)
        elif increase_or_decrease == "decrease":
            action = "減らした"
            k = sy.Integer(randint(1, 5) * 10)
            b = k + sy.Integer(randint(1, 5) * 10)
            a = b + k
        x = sy.Symbol("x")
        replaced_by_x = choice(["a", "b"])
        if replaced_by_x == "a":
            substitute_value = self._amount_calculator_for_adjustment(a, from_unit=k_unit, to_unit=a_unit)
            a_in_problem1_with_unit = self._make_latex_with_unit(x, a_unit, with_parentheses=False)
            b_in_problem1_with_unit = self._unit_adjuster(b, from_unit=k_unit, to_unit=b_unit, with_parentheses=False)
            if a_unit == k_unit:
                a_in_answer1 = self._make_latex_with_unit(x, a_unit, with_parentheses=True)
            else:
                a_before_adjustment = self._make_latex_with_unit(x, a_unit, with_parentheses=True)
                a_after_adjustment = self._unit_adjuster(x, from_unit=a_unit, to_unit=k_unit, with_parentheses=True)
                a_in_answer1 = f"{a_before_adjustment} = {a_after_adjustment}"
            if b_unit == k_unit:
                b_in_answer1 = self._make_latex_with_unit(b, b_unit, with_parentheses=True)
            else:
                b_before_adjustment = self._unit_adjuster(b, from_unit=k_unit, to_unit=b_unit, with_parentheses=True)
                b_after_adjustment = self._make_latex_with_unit(b, k_unit, with_parentheses=True)
                b_in_answer1 = f"{b_before_adjustment} = {b_after_adjustment}"
            a_in_formula_in_answer1 = self._amount_adjuster(x, from_unit=a_unit, to_unit=k_unit)
            if increase_or_decrease == "increase":
                answer1 = f"{a_in_formula_in_answer1} + {b}"
            elif increase_or_decrease == "decrease":
                answer1 = f"{a_in_formula_in_answer1} - {b}"
            search_unit = a_unit
        elif replaced_by_x == "b":
            substitute_value = self._amount_calculator_for_adjustment(b, from_unit=k_unit, to_unit=b_unit)
            a_in_problem1_with_unit = self._unit_adjuster(a, from_unit=k_unit, to_unit=a_unit, with_parentheses=False)
            b_in_problem1_with_unit = self._make_latex_with_unit(x, b_unit, with_parentheses=False)
            if a_unit == k_unit:
                a_in_answer1 = self._make_latex_with_unit(a, a_unit, with_parentheses=True)
            else:
                a_before_adjustment = self._unit_adjuster(a, from_unit=k_unit, to_unit=a_unit, with_parentheses=True)
                a_after_adjustment = self._make_latex_with_unit(a, k_unit, with_parentheses=True)
                a_in_answer1 = f"{a_before_adjustment} = {a_after_adjustment}"
            if b_unit == k_unit:
                b_in_answer1 = self._make_latex_with_unit(x, b_unit, with_parentheses=True)
            else:
                b_before_adjustment = self._make_latex_with_unit(x, b_unit, with_parentheses=True)
                b_after_adjustment = self._unit_adjuster(x, from_unit=b_unit, to_unit=k_unit, with_parentheses=True)
                b_in_answer1 = f"{b_before_adjustment} = {b_after_adjustment}"
            b_in_formula_in_answer1 = self._amount_adjuster(x, from_unit=b_unit, to_unit=k_unit)
            if increase_or_decrease == "increase":
                answer1 = f"{a} + {b_in_formula_in_answer1}"
            elif increase_or_decrease == "decrease":
                answer1 = f"{a} - {b_in_formula_in_answer1}"
            search_unit = b_unit
        if ((search_unit, k_unit) == ("L", "L")) or ((search_unit, k_unit) == ("dL", "dL")):
            search_number = "10, 20, 30, \\ldots"
        elif (search_unit, k_unit) == ("dL", "L"):
            search_number = "100, 200, 300, \\ldots"
        elif (search_unit, k_unit) == ("L", "dL"):
            search_number = "1, 2, 3, \\ldots"
        k_with_unit = self._make_latex_with_unit(k, k_unit, with_parentheses=False)
        latex_problem = f"初めに{item}が\\( {a_in_problem1_with_unit} \\)ありました。\n"
        latex_problem += f"(1)\\( {b_in_problem1_with_unit} \\)だけ{action}した後の体積\\( (\\mathrm{{{k_unit}}}) \\)を、\\( x \\)を使って表しなさい。\n"
        latex_problem += f"(2){action}後の体積が\\( {k_with_unit} \\)になるときの\\( x \\)の値を、\\( {search_number} \\)と当てはめていくことで求めなさい。"
        latex_answer = f"(1)初めの量が、\\( {a_in_answer1} \\), {action}量が\\( {b_in_answer1} \\)なので、\n"
        latex_answer += f"\\( {answer1} \\)\n"
        latex_answer += f"(2)(1)の式に指定された数を順番に当てはめていくと、\n"
        latex_answer += f"\\( x = {substitute_value} \\)のときに\\( {k_with_unit} \\)になるので、"
        latex_answer += f"答えは\\( {substitute_value} \\)となる。"
        return latex_answer, latex_problem
    
    def _make_expression_with_formula_and_solve_weight_problem(self) -> Tuple[str, str]:
        """式での表現と、xを求める重さの問題と解答を作成
        
        Returns:
            Tuple[str, str]: 問題と解答
            - latex_answer (str): latex形式と通常の文字列が混在していることを前提とした解答
            - latex_problem (str): latex形式と通常の文字列が混在していることを前提とした問題

        Developing:

        """
        item = choice(["米", "小麦粉", "水", "塩"])
        a_unit, b_unit = choice([("kg", "kg"), ("g", "g"), ("kg", "g"), ("g", "kg")])
        k_unit = choice([a_unit, b_unit])
        increase_or_decrease = choice(["increase", "decrease"])
        # a + b = k (by k_unit)
        if increase_or_decrease == "increase":
            action = "増やした"
            a = sy.Integer(randint(1, 10) * 100)
            b = sy.Integer(randint(1, 10) * 100)
            k = a + b
        # a - b = k (by k_unit)
        elif increase_or_decrease == "decrease":
            action = "減らした"
            k = sy.Integer(randint(1, 10) * 100)
            b = k + sy.Integer(randint(1, 10) * 100)
            a = b + k
        x = sy.Symbol("x")
        # which is x?
        replaced_by_x = choice(["a", "b"])
        if replaced_by_x == "a":
            substitute_value = self._amount_calculator_for_adjustment(a, from_unit=k_unit, to_unit=a_unit)
            a_in_problem1_with_unit = self._make_latex_with_unit(x, a_unit, with_parentheses=False)
            b_in_problem1_with_unit = self._unit_adjuster(b, from_unit=k_unit, to_unit=b_unit, with_parentheses=False)
            if a_unit == k_unit:
                a_in_answer1 = self._make_latex_with_unit(x, a_unit, with_parentheses=True)
            else:
                a_before_adjustment = self._make_latex_with_unit(x, a_unit, with_parentheses=True)
                a_after_adjustment = self._unit_adjuster(x, from_unit=a_unit, to_unit=k_unit, with_parentheses=True)
                a_in_answer1 = f"{a_before_adjustment} = {a_after_adjustment}"
            if b_unit == k_unit:
                b_in_answer1 = self._make_latex_with_unit(b, b_unit, with_parentheses=True)
            else:
                b_before_adjustment = self._unit_adjuster(b, from_unit=k_unit, to_unit=b_unit, with_parentheses=True)
                b_after_adjustment = self._make_latex_with_unit(b, k_unit, with_parentheses=True)
                b_in_answer1 = f"{b_before_adjustment} = {b_after_adjustment}"
            a_in_formula_in_answer1 = self._amount_adjuster(x, from_unit=a_unit, to_unit=k_unit)
            if increase_or_decrease == "increase":
                answer1 = f"{a_in_formula_in_answer1} + {b}"
            elif increase_or_decrease == "decrease":
                answer1 = f"{a_in_formula_in_answer1} - {b}"
            search_unit = a_unit
        elif replaced_by_x == "b":
            substitute_value = self._amount_calculator_for_adjustment(b, from_unit=k_unit, to_unit=b_unit)
            a_in_problem1_with_unit = self._unit_adjuster(a, from_unit=k_unit, to_unit=a_unit, with_parentheses=False)
            b_in_problem1_with_unit = self._make_latex_with_unit(x, b_unit, with_parentheses=False)
            if a_unit == k_unit:
                a_in_answer1 = self._make_latex_with_unit(a, a_unit, with_parentheses=True)
            else:
                a_before_adjustment = self._unit_adjuster(a, from_unit=k_unit, to_unit=a_unit, with_parentheses=True)
                a_after_adjustment = self._make_latex_with_unit(a, k_unit, with_parentheses=True)
                a_in_answer1 = f"{a_before_adjustment} = {a_after_adjustment}"
            if b_unit == k_unit:
                b_in_answer1 = self._make_latex_with_unit(x, b_unit, with_parentheses=True)
            else:
                b_before_adjustment = self._make_latex_with_unit(x, b_unit, with_parentheses=True)
                b_after_adjustment = self._unit_adjuster(x, from_unit=b_unit, to_unit=k_unit, with_parentheses=True)
                b_in_answer1 = f"{b_before_adjustment} = {b_after_adjustment}"
            b_in_formula_in_answer1 = self._amount_adjuster(x, from_unit=b_unit, to_unit=k_unit)
            if increase_or_decrease == "increase":
                answer1 = f"{a} + {b_in_formula_in_answer1}"
            elif increase_or_decrease == "decrease":
                answer1 = f"{a} - {b_in_formula_in_answer1}"
            search_unit = b_unit
        if ((search_unit, k_unit) == ("kg", "kg")) or ((search_unit, k_unit) == ("g", "g")):
            search_number = "100, 200, 300, \\ldots"
        elif (search_unit, k_unit) == ("g", "kg"):
            search_number = "100000, 200000, 3000000, \\ldots"
        elif (search_unit, k_unit) == ("kg", "g"):
            search_number = "0.1, 0.2, 0.3, \\ldots"
        k_with_unit = self._make_latex_with_unit(k, k_unit, with_parentheses=False)
        latex_problem = f"初めに{item}が\\( {a_in_problem1_with_unit} \\)ありました。\n"
        latex_problem += f"(1)\\( {b_in_problem1_with_unit} \\)だけ{action}した後の重さ\\( (\\mathrm{{{k_unit}}}) \\)を、\\( x \\)を使って表しなさい。\n"
        latex_problem += f"(2){action}後の重さが\\( {k_with_unit} \\)になるときの\\( x \\)の値を、\\( {search_number} \\)と当てはめていくことで求めなさい。"
        latex_answer = f"(1)初めの量が、\\( {a_in_answer1} \\), {action}量が\\( {b_in_answer1} \\)なので、\n"
        latex_answer += f"\\( {answer1} \\)\n"
        latex_answer += f"(2)(1)の式に指定された数を順番に当てはめていくと、\n"
        latex_answer += f"\\( x = {substitute_value} \\)のときに\\( {k_with_unit} \\)になるので、"
        latex_answer += f"答えは\\( {substitute_value} \\)となる。"
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


    def _make_latex_with_unit(self, amount: Union[sy.Symbol, sy.Integer, sy.Float, sy.Rational, str], unit: str, *, with_parentheses: bool) -> str:
        """与えられた量と単位をlatex形式で返すための関数

        Args:
            amount (Union[sy.Integer, sy.Float, sy.Rational, str]): 量
            unit (str): 単位
            with_parentheses (bool): 単位にカッコを付けるか否か
        
        Returns:
            amount_with_unit_latex (str): 量と単位を合わせたもの
        """
        if isinstance(amount, str):
            if with_parentheses:
                amount_with_unit_latex = f"{amount} (\\mathrm{{{unit}}})"
            else:
                amount_with_unit_latex = f"{amount} \\mathrm{{{unit}}}"
        else:
            if with_parentheses:
                amount_with_unit_latex = f"{sy.latex(amount)} (\\mathrm{{{unit}}})"
            else:
                amount_with_unit_latex = f"{sy.latex(amount)} \\mathrm{{{unit}}}"
        return amount_with_unit_latex
    
    def _amount_adjuster(self, from_amount: Union[sy.Symbol, sy.Integer, sy.Rational, sy.Float], *, from_unit: str, to_unit: str) -> str:
        """量の変換を行う関数

        Args:
            from_amount (Union[sy.Symbol, sy.Integer, sy.Rational, sy.Float]): 基準となる量
            from_unit (str): 変換元の単位
            to_unit (str): 変換先の単位

        Returns:
            adjusted_amount_latex (str): 指定された単位に合わせた量
        
        Developing:
            どこまで分割する？
            今は単位ごとに分けている
                ここから単位のありなしで考えてよい？あるいは変換のありなしまで含めるべき？
        """
        # no symbol
        if not(from_amount.free_symbols):
            adjusted_amount = self._amount_calculator_for_adjustment(from_amount, from_unit=from_unit, to_unit=to_unit)
            adjusted_amount_latex = sy.latex(adjusted_amount)
        # volume
        # no change
        if ((from_unit == "L") and (to_unit == "L")):
            adjusted_amount_latex = sy.latex(from_amount)
        # no change
        elif ((from_unit == "dL") and (to_unit == "dL")):
            adjusted_amount_latex = sy.latex(from_amount)
        # * 10
        elif (from_unit == "L") and (to_unit == "dL"):
            if from_amount.free_symbols:
                adjusted_amount_latex = f"{from_amount} \\times 10"
            else:
                adjusted_amount = self._amount_calculator_for_adjustment(from_amount, from_unit=from_unit, to_unit=to_unit)
                adjusted_amount_latex = sy.latex(adjusted_amount)
        # / 10
        elif (from_unit == "dL") and (to_unit == "L"):
            if from_amount.free_symbols:
                adjusted_amount_latex = f"{from_amount} \\div 10"
            else:
                adjusted_amount = self._amount_calculator_for_adjustment(from_amount, from_unit=from_unit, to_unit=to_unit)
                adjusted_amount_latex = sy.latex(adjusted_amount)
        # weight
        # no change
        elif (from_unit == "kg") and (to_unit == "kg"):
            adjusted_amount_latex = sy.latex(from_amount)
        # no change
        elif (from_unit == "g") and (to_unit == "g"):
            adjusted_amount_latex = sy.latex(from_amount)
        # * 1000
        elif (from_unit == "kg") and (to_unit == "g"):
            if from_amount.free_symbols:
                adjusted_amount_latex = f"{from_amount} \\times 1000"
            else:
                adjusted_amount = self._amount_calculator_for_adjustment(from_amount, from_unit=from_unit, to_unit=to_unit)
                adjusted_amount_latex = sy.latex(adjusted_amount)
        # / 1000
        elif (from_unit == "g") and (to_unit == "kg"):
            if from_amount.free_symbols:
                adjusted_amount_latex = f"{from_amount} \\div 1000"
            else:
                adjusted_amount = self._amount_calculator_for_adjustment(from_amount, from_unit=from_unit, to_unit=to_unit)
                adjusted_amount_latex = sy.latex(adjusted_amount)
        else:
            raise ValueError(f"'from_unit' is {from_unit}, and 'to_unit' is {to_unit}.")
        return adjusted_amount_latex
    
    def _amount_calculator_for_adjustment(self, from_amount: Union[sy.Symbol, sy.Integer, sy.Rational, sy.Float], *, from_unit: str, to_unit: str) -> Union[sy.Symbol, sy.Integer, sy.Rational, sy.Float]:
        """単位変換の作業のうち、計算のみを請け負う関数

        Args:
            from_amount (Union[sy.Symbol, sy.Integer, sy.Rational, sy.Float]): _description_   
            from_unit (str): _description_
            to_unit (str): _description_

        Returns:
            Union[sy.Symbol, sy.Integer, sy.Rational, sy.Float]: 代入可能な値
        """
        # volume (standard is dl)
        # no change
        if ((from_unit == "L") and (to_unit == "L")):
            adjusted_amount = from_amount
        # no change
        elif ((from_unit == "dL") and (to_unit == "dL")):
            adjusted_amount = from_amount
        # * 10
        elif (from_unit == "L") and (to_unit == "dL"):
            adjusted_amount = from_amount * sy.Integer(10)
        # / 10
        elif (from_unit == "dL") and (to_unit == "L"):
            adjusted_amount = from_amount * sy.Rational(1, 10)
        # weight
        # no change
        elif (from_unit == "kg") and (to_unit == "kg"):
            adjusted_amount = from_amount
        # no change
        elif (from_unit == "g") and (to_unit == "g"):
            adjusted_amount = from_amount
        # * 1000
        elif (from_unit == "kg") and (to_unit == "g"):
            adjusted_amount = from_amount * sy.Integer(1000)
        # / 1000
        elif (from_unit == "g") and (to_unit == "kg"):
            adjusted_amount = from_amount * sy.Rational(1, 1000)
        else:
            raise ValueError(f"'from_unit' is {from_unit}, and 'to_unit' is {to_unit}.")
        return adjusted_amount

    def _unit_adjuster(self, from_amount: Union[sy.Symbol, sy.Integer, sy.Rational, sy.Float], *, from_unit: str, to_unit: str, with_parentheses: bool) -> str:
        """指定された単位へと与えられた量を変換した上で、latex形式で返す関数

        Args:
            from_amount (Union[sy.Symbol, sy.Integer, sy.Rational]): 元となる量
            from_unit (str): 元となる単位
            to_unit (str): 変換先となる単位
            with_parentheses (bool): 単位にカッコを付けるか否か

        Returns:
            adjusted_amount_with_unit (str): 変換先への単位に合わせたlatex形式
        """
        adjusted_amount = self._amount_adjuster(from_amount, from_unit=from_unit, to_unit=to_unit)
        adjusted_amount_with_unit = self._make_latex_with_unit(adjusted_amount, to_unit, with_parentheses=with_parentheses)
        return adjusted_amount_with_unit
    
    def _multiply_or_divide(self, first_amount: Union[sy.Symbol, sy.Integer, sy.Float, sy.Rational], second_amount: Union[sy.Symbol, sy.Integer, sy.Float, sy.Rational], *, multiply_or_divide: str) -> str:
        """2つの量のかけ算や割り算を行う

        Args:
            first_amount (Union[sy.Symbol, sy.Integer, sy.Float, sy.Rational]): 1つ目の量
            second_amount (Union[sy.Symbol, sy.Integer, sy.Float, sy.Rational]): 2つ目の量
            multiply_or_divide (str): かけ算か割り算かの指定

        Returns:
            calculated_amount (str) : 計算した式
        """
        # latex済想定
        if isinstance(first_amount, str):
            raise ValueError(f"'first_amount' must not be str.{first_amount} is wrong.")
        if isinstance(second_amount, str):
            raise ValueError(f"'first_amount' must not be str.{second_amount} is wrong.")
        if not(isinstance(first_amount, sy.Symbol)) and not(isinstance(second_amount, sy.Symbol)):
            calculated_amount = self._decimal_normalize(sy.latex(first_amount * second_amount))
        else:
            if multiply_or_divide == "multiply":
                calculated_amount = f"{sy.latex(first_amount)} \\times {sy.latex(second_amount)}"
            elif multiply_or_divide == "divide":
                calculated_amount = f"{sy.latex(first_amount)} \\div {sy.latex(second_amount)}"
            else:
                raise ValueError(f"'multiply_or_divide' must be 'multiply' or 'divide'. {multiply_or_divide} is wrong.")
        return calculated_amount

    def _decimal_normalize(self, number: Union[str, sy.Integer, sy.Float]) -> str:
        """
        小数点以下で末尾まで続いている連続した0を消去した文字列を返す。(eg. 100.00->100, 31.0010->31.001)

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
    

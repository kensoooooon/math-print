from random import choice, randint, random, shuffle
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
        selected_genre = "weight"
        x = sy.Symbol("x")
        if selected_genre == "area":
            selected_shape = choice(["triangle", "parallelogram"])
            if selected_shape == "triangle":
                if random() > 0.5:
                    base = randint(1, 10)
                    height = x
                else:
                    base = x
                    height = randint(1, 10)
                latex_problem = f"底辺が \\( {base} \\mathrm{{cm}} \\)、高さが\\( {height} \\mathrm{{cm}} \\)の三角形があります。\n"
                latex_problem += f"三角形の面積を、\\( x \\)を使った式で表しなさい。"
                latex_answer = "三角形の面積は、(底辺) \\( \\times \\) (高さ) \\( \\div 2\\)なので、\n"
                latex_answer += f"\\( {base} \\times {height} \\div 2 \\)"
            elif selected_shape == "parallelogram":
                if random() > 0.5:
                    base = randint(1, 10)
                    height = x
                else:
                    base = x
                    height = randint(1, 10)
                latex_problem = f"底辺が \\( {base} \\mathrm{{cm}} \\)、高さが\\( {height} \\mathrm{{cm}} \\)の平行四辺形があります。\n"
                latex_problem += f"平行四辺形の面積を、\\( x \\)を使った式で表しなさい。"
                latex_answer = "平行四辺形の面積は、(底辺) \\( \\times \\) (高さ) \\( \\div 2\\)なので、\n"
                latex_answer += f"\\( {base} \\times {height} \\div 2 \\)"                
        elif selected_genre == "volume":
            item = choice(["ジュース", "お茶", "コーヒー"])
            increase_or_decrease = choice(["increase", "decrease"])
            if increase_or_decrease == "increase":
                list_to_shuffle = [randint(1, 10), x]
                shuffle(list_to_shuffle)
                start_amount, increment = list_to_shuffle
                from_to_unit = choice(["l_to_l", "dl_to_dl", "dl_to_l", "l_to_dl"])
                if from_to_unit == "l_to_l":
                    start_amount_latex = f"\\( {sy.latex(start_amount)} \\mathrm{{L}} \\)"
                    increment_latex = f"\\( {sy.latex(increment)} \\mathrm{{L}} \\)"
                    latex_problem = f"初めに{item}が{start_amount_latex}ありました。\n"
                    latex_problem += f"{increment_latex}増やした後の体積\\( (\\mathrm{{L}}) \\)を、\\( x \\)を使った式で表しなさい。"
                    end_amount_latex = f"\\( {sy.latex(start_amount)} + {sy.latex(increment)} (\\mathrm{{L}})\\)"
                    latex_answer = f"初めの量が{start_amount_latex}で、{increment_latex}が増やした量なので、\n"
                    latex_answer += f"この2つを足すと、{end_amount_latex}"
                elif from_to_unit == "dl_to_dl":
                    start_amount_latex = f"\\( {sy.latex(start_amount)} \\mathrm{{dL}} \\)"
                    increment_latex = f"\\( {sy.latex(increment)} \\mathrm{{dL}} \\)"
                    latex_problem = f"初めに{item}が{start_amount_latex}ありました。\n"
                    latex_problem += f"{increment_latex}増やした後の体積\\( (\\mathrm{{dL}}) \\)を、\\( x \\)を使った式で表しなさい。"
                    end_amount_latex = f"\\( {sy.latex(start_amount)} + {sy.latex(increment)} (\\mathrm{{dL}}) \\)"
                    latex_answer = f"初めの量が{start_amount_latex}で、{increment_latex}が増やした量なので、\n"
                    latex_answer += f"この2つを足すと、{end_amount_latex}"
                elif from_to_unit == "dl_to_l":
                    start_amount_latex = f"\\( {sy.latex(start_amount)} \\mathrm{{dL}} \\)"
                    increment_latex = f"\\( {sy.latex(increment)} \\mathrm{{L}} \\)"
                    latex_problem = f"初めに{item}が{start_amount_latex}ありました。\n"
                    # answered by dL
                    if random() > 0.5:
                        latex_problem += f"{increment_latex}増やした後の体積\\( \\mathrm{{(dL)}} \\)を、\\( x \\)を使った式で表しなさい。"
                        latex_answer = f"初めの量が{start_amount_latex}で、"
                        if increment == x:
                            latex_answer += f"\\( {sy.latex(increment)} \\mathrm{{L}} = {sy.latex(increment)} \\times 10 \\mathrm{{dL}} \\)が増やした量なので、\n"
                            end_amount_latex = f"\\( {sy.latex(start_amount)} + {sy.latex(increment)} \\times 10 (\\mathrm{{dL}}) \\)"
                        else:
                            latex_answer += f"\\( {sy.latex(increment)} \\mathrm{{L}} = {sy.latex(increment * 10)} \\mathrm{{dL}} \\)が増やした量なので、\n"
                            end_amount_latex = f"\\( {sy.latex(start_amount)} + {sy.latex(increment * 10)} (\\mathrm{{dL}}) \\)"
                        latex_answer += f"この2つを足すと、{end_amount_latex}"
                    # answered by L
                    else:
                        latex_problem += f"{increment_latex}増やした後の体積\\( (\\mathrm{{L}}) \\)を、\\( x \\)を使った式で表しなさい。"
                        if start_amount == x:
                            latex_answer = f"初めの量が\\( {sy.latex(start_amount)} (\\mathrm{{dL}}) = {sy.latex(start_amount)} \\div 10 (\\mathrm{{L}})  \\)で、"
                            end_amount_latex = f"\\( {sy.latex(start_amount)} \\div 10 + {sy.latex(increment)} (\\mathrm{{L}}) \\)"
                        else:
                            latex_answer = f"初めの量が\\( {sy.latex(start_amount)} (\\mathrm{{dL}}) = {sy.latex(start_amount * sy.Rational(1, 10))} (\\mathrm{{L}})  \\)で、"
                            end_amount_latex = f"\\( {sy.latex(start_amount * sy.Rational(1, 10))} + {sy.latex(increment)}  (\\mathrm{{L}}) \\)"
                        latex_answer += f"{increment_latex}が増やした量なので、\n"
                        latex_answer += f"この2つを足すと、{end_amount_latex}"
                elif from_to_unit == "l_to_dl":
                    start_amount_latex = f"\\( {sy.latex(start_amount)} \\mathrm{{L}} \\)"
                    increment_latex = f"\\( {sy.latex(increment)} \\mathrm{{dL}} \\)"
                    latex_problem = f"初めに{item}が{start_amount_latex}ありました。\n"
                    # answered by dL
                    if random() > 0.5:
                        latex_problem += f"{increment_latex}増やした後の体積\\( (\\mathrm{{dL}}) \\)を、\\( x \\)を使った式で表しなさい。"
                        if start_amount == x:
                            latex_answer = f"初めの量が\\( {sy.latex(start_amount)} (\\mathrm{{L}}) = {sy.latex(start_amount)} \\times 10 (\\mathrm{{dL}}) \\)で、"
                            end_amount_latex = f"\\( {sy.latex(start_amount)} \\times 10 + {sy.latex(increment)} (\\mathrm{{dL}}) \\)"
                        else:
                            latex_answer = f"初めの量が\\( {sy.latex(start_amount)} (\\mathrm{{L}}) = {sy.latex(start_amount * 10)} (\\mathrm{{dL}}) \\)で、"
                            end_amount_latex = f"\\( {sy.latex(start_amount * 10)} + {sy.latex(increment)} (\\mathrm{{dL}}) \\)"
                        latex_answer += f"{increment_latex}が増やした量なので、\n"
                        latex_answer += f"この2つを足すと、{end_amount_latex}"
                    # answered by L
                    else:
                        latex_problem += f"{increment_latex}増やした後の体積\\( (\\mathrm{{L}}) \\)を、\\( x \\)を使った式で表しなさい。"
                        latex_answer = f"初めの量が{start_amount_latex}で、"
                        if increment == x:
                            latex_answer += f"増やした量が、\\( {sy.latex(increment)} (\\mathrm{{dL}}) = {sy.latex(increment)} \\div 10 (\\mathrm{{L}}) \\)なので、\n"
                            end_amount_latex = f"\\( {sy.latex(start_amount)} + {sy.latex(increment)} \\div 10 (\\mathrm{{L}}) \\)"
                        else:
                            latex_answer += f"増やした量が、\\( {sy.latex(increment)} (\\mathrm{{dL}}) = {sy.latex(increment * sy.Rational(1, 10))} (\\mathrm{{L}}) \\)なので、\n"
                            end_amount_latex = f"\\( {sy.latex(start_amount)} + {sy.latex(increment * sy.Rational(1, 10))} (\\mathrm{{L}}) \\)"
                        latex_answer += f"この2つを足すと、{end_amount_latex}"
            elif increase_or_decrease == "decrease":
                list_to_shuffle = [randint(1, 10), x]
                shuffle(list_to_shuffle)
                start_amount, decrement = list_to_shuffle
                from_to_unit = choice(["l_to_l", "dl_to_dl", "dl_to_l", "l_to_dl"])
                if from_to_unit == "l_to_l":
                    start_amount_latex = f"\\( {sy.latex(start_amount)} \\mathrm{{L}} \\)"
                    decrement_latex = f"\\( {sy.latex(decrement)} \\mathrm{{L}} \\)"
                    latex_problem = f"初めに{item}が{start_amount_latex}ありました。\n"
                    latex_problem += f"{decrement_latex}減らした後の体積\\( (\\mathrm{{L}}) \\)を、\\( x \\)を使った式で表しなさい。"
                    end_amount_latex = f"\\( {sy.latex(start_amount)} - {sy.latex(decrement)} (\\mathrm{{L}})\\)"
                    latex_answer = f"初めの量が{start_amount_latex}で、{decrement_latex}が減らした量なので、\n"
                    latex_answer += f"初めの量から減らした量を引くと、{end_amount_latex}"
                elif from_to_unit == "dl_to_dl":
                    start_amount_latex = f"\\( {sy.latex(start_amount)} \\mathrm{{dL}} \\)"
                    decrement_latex = f"\\( {sy.latex(decrement)} \\mathrm{{dL}} \\)"
                    latex_problem = f"初めに{item}が{start_amount_latex}ありました。\n"
                    latex_problem += f"{decrement_latex}減らした後の体積\\( (\\mathrm{{dL}}) \\)を、\\( x \\)を使った式で表しなさい。"
                    end_amount_latex = f"\\( {sy.latex(start_amount)} - {sy.latex(decrement)} (\\mathrm{{dL}}) \\)"
                    latex_answer = f"初めの量が{start_amount_latex}で、{decrement_latex}が減らした量なので、\n"
                    latex_answer += f"初めの量から減らした量を引くと、{end_amount_latex}"
                elif from_to_unit == "dl_to_l":
                    start_amount_latex = f"\\( {sy.latex(start_amount)} \\mathrm{{dL}} \\)"
                    decrement_latex = f"\\( {sy.latex(decrement)} \\mathrm{{L}} \\)"
                    latex_problem = f"初めに{item}が{start_amount_latex}ありました。\n"
                    # answered by dL
                    if random() > 0.5:
                        latex_problem += f"{decrement_latex}減らした後の体積\\( \\mathrm{{(dL)}} \\)を、\\( x \\)を使った式で表しなさい。"
                        latex_answer = f"初めの量が{start_amount_latex}で、"
                        if decrement == x:
                            latex_answer += f"\\( {sy.latex(decrement)} \\mathrm{{L}} = {sy.latex(decrement)} \\times 10 \\mathrm{{dL}} \\)が減らした量なので、\n"
                            end_amount_latex = f"\\( {sy.latex(start_amount)} - {sy.latex(decrement)} \\times 10 (\\mathrm{{dL}}) \\)"
                        else:
                            latex_answer += f"\\( {sy.latex(decrement)} \\mathrm{{L}} = {sy.latex(decrement * 10)} \\mathrm{{dL}} \\)が減らした量なので、\n"
                            end_amount_latex = f"\\( {sy.latex(start_amount)} - {sy.latex(decrement * 10)} (\\mathrm{{dL}}) \\)"
                        latex_answer += f"初めの量から減らした量を引くと、{end_amount_latex}"
                    # answered by L
                    else:
                        latex_problem += f"{decrement_latex}減らした後の体積\\( (\\mathrm{{L}}) \\)を、\\( x \\)を使った式で表しなさい。"
                        if start_amount == x:
                            latex_answer = f"初めの量が\\( {sy.latex(start_amount)} (\\mathrm{{dL}}) = {sy.latex(start_amount)} \\div 10 (\\mathrm{{L}})  \\)で、"
                            end_amount_latex = f"\\( {sy.latex(start_amount)} \\div 10 - {sy.latex(decrement)} (\\mathrm{{L}}) \\)"
                        else:
                            latex_answer = f"初めの量が\\( {sy.latex(start_amount)} (\\mathrm{{dL}}) = {sy.latex(start_amount * sy.Rational(1, 10))} (\\mathrm{{L}})  \\)で、"
                            end_amount_latex = f"\\( {sy.latex(start_amount * sy.Rational(1, 10))} - {sy.latex(decrement)}  (\\mathrm{{L}}) \\)"
                        latex_answer += f"{decrement_latex}が減らした量なので、\n"
                        latex_answer += f"初めの量から減らした量を引くと、{end_amount_latex}"
                elif from_to_unit == "l_to_dl":
                    start_amount_latex = f"\\( {sy.latex(start_amount)} \\mathrm{{L}} \\)"
                    decrement_latex = f"\\( {sy.latex(decrement)} \\mathrm{{dL}} \\)"
                    latex_problem = f"初めに{item}が{start_amount_latex}ありました。\n"
                    # answered by dL
                    if random() > 0.5:
                        latex_problem += f"{decrement_latex}減らした後の体積\\( (\\mathrm{{dL}}) \\)を、\\( x \\)を使った式で表しなさい。"
                        if start_amount == x:
                            latex_answer = f"初めの量が\\( {sy.latex(start_amount)} (\\mathrm{{L}}) = {sy.latex(start_amount)} \\times 10 (\\mathrm{{dL}}) \\)で、"
                            end_amount_latex = f"\\( {sy.latex(start_amount)} \\times 10 - {sy.latex(decrement)} (\\mathrm{{dL}}) \\)"
                        else:
                            latex_answer = f"初めの量が\\( {sy.latex(start_amount)} (\\mathrm{{L}}) = {sy.latex(start_amount * 10)} (\\mathrm{{dL}}) \\)で、"
                            end_amount_latex = f"\\( {sy.latex(start_amount * 10)} - {sy.latex(decrement)} (\\mathrm{{dL}}) \\)"
                        latex_answer += f"{decrement_latex}が減らした量なので、\n"
                        latex_answer += f"初めの量から減らした量を引くと、{end_amount_latex}"
                    # answered by L
                    else:
                        latex_problem += f"{decrement_latex}減らした後の体積\\( (\\mathrm{{L}}) \\)を、\\( x \\)を使った式で表しなさい。"
                        latex_answer = f"初めの量が{start_amount_latex}で、"
                        if decrement == x:
                            latex_answer += f"減らした量が、\\( {sy.latex(decrement)} (\\mathrm{{dL}}) = {sy.latex(decrement)} \\div 10 (\\mathrm{{L}}) \\)なので、\n"
                            end_amount_latex = f"\\( {sy.latex(start_amount)} - {sy.latex(decrement)} \\div 10 (\\mathrm{{L}}) \\)"
                        else:
                            latex_answer += f"減らした量が、\\( {sy.latex(decrement)} (\\mathrm{{dL}}) = {sy.latex(decrement * sy.Rational(1, 10))} (\\mathrm{{L}}) \\)なので、\n"
                            end_amount_latex = f"\\( {sy.latex(start_amount)} - {sy.latex(decrement * sy.Rational(1, 10))} (\\mathrm{{L}}) \\)"
                        latex_answer += f"初めの量から減らした量を引くと、{end_amount_latex}"
        elif selected_genre == "weight":
            item = choice(["米", "小麦粉", "みそ"])
            increase_or_decrease = choice(["increase", "decrease"])
            if increase_or_decrease == "increase":
                action = "増やした"
            elif increase_or_decrease == "decrease":
                action = "減らした"
            list_to_shuffle = [randint(1, 10), x]
            shuffle(list_to_shuffle)
            start_amount, delta = list_to_shuffle
            # start_and_delta_unit = choice(["g_and_g", "kg_and_kg", "kg_and_g", "g_and_kg"])
            start_and_delta_unit = "kg_and_kg"
            if (start_and_delta_unit == "g_and_g") or (start_and_delta_unit == "kg_and_kg"):
                if start_and_delta_unit == "g_and_g":
                    start_unit = "\\mathrm{g}"
                    delta_unit = "\\mathrm{g}"
                    answered_unit = "\\mathrm{g}"
                if start_and_delta_unit == "kg_and_kg":
                    start_unit = "\\mathrm{{kg}}"
                    delta_unit = "\\mathrm{{kg}}"
                    answered_unit = "\\mathrm{{kg}}"
                start_amount_latex_in_problem = f"\\( {sy.latex(start_amount)}  {start_unit}\\)"
                delta_latex_in_problem = f"\\( {sy.latex(delta)} {delta_unit} \\)"
                start_amount_latex_in_answer = start_amount_latex_in_problem
                delta_latex_in_answer = delta_latex_in_problem
                if increase_or_decrease == "increase":
                    action_in_answer = "この2つを足すと"
                    end_amount_latex_in_answer = f"\\( {sy.latex(start_amount)} + {sy.latex(delta)} ({answered_unit}) \\)"
                elif increase_or_decrease == "decrease":
                    action_in_answer = "初めの量から減らした量を引くと"
                    end_amount_latex_in_answer = f"\\( {sy.latex(start_amount)} - {sy.latex(delta)} ({answered_unit}) \\)"
            elif start_and_delta_unit == "kg_and_g":
                start_unit = "\\mathrm{kg}"
                delta_unit = "\\mathrm{g}"
                answered_unit = choice(["\\mathrm{g}", "\\mathrm{kg}"])
                start_amount_latex_in_problem = f"\\( {sy.latex(start_amount)}  {start_unit}\\)"
                delta_latex_in_problem = f"\\( {sy.latex(delta)} {delta_unit} \\)"
                if answered_unit == "\\mathrm{g}":
                    delta_latex_in_answer = delta_latex_in_problem
                    if start_amount == x:
                        start_amount_latex_in_answer = f"\\( {sy.latex(start_amount)} ({start_unit}) = {sy.latex(start_amount)} \\times 1000 ({answered_unit}) \\)"
                        if increase_or_decrease == "increase":
                            action_in_answer = "この2つを足すと"
                            end_amount_latex_in_answer = f"\\( {sy.latex(start_amount)} \\times 1000 + {sy.latex(delta)} ({answered_unit})\\)"
                        elif increase_or_decrease == "decrease":
                            action_in_answer = "初めの量から減らした量を引くと"
                            end_amount_latex_in_answer = f"\\( {sy.latex(start_amount)} \\times 1000 - {sy.latex(delta)} ({answered_unit})\\)"
                    else:
                        start_amount_latex_in_answer = f"\\( {sy.latex(start_amount)} ({start_unit}) = {sy.latex(start_amount * 1000)} ({answered_unit}) \\)"
                        if increase_or_decrease == "increase":
                            action_in_answer = "この2つを足すと"
                            end_amount_latex_in_answer = f"\\( {sy.latex(start_amount * 1000)}  + {sy.latex(delta)} ({answered_unit})\\)"
                        elif increase_or_decrease == "decrease":
                            action_in_answer = "初めの量から減らした量を引くと"
                            end_amount_latex_in_answer = f"\\( {sy.latex(start_amount * 1000)} - {sy.latex(delta)} ({answered_unit})\\)"
                elif answered_unit == "\\mathrm{kg}":
                    start_amount_latex_in_answer = start_amount_latex_in_problem
                    if delta == x:
                        delta_latex_in_answer = f"\\( {sy.latex(delta)} ({delta_unit}) = {sy.latex(delta)} \\div 1000 {answered_unit} \\)"
                        if increase_or_decrease == "increase":
                            action_in_answer = "この2つを足すと"
                            end_amount_latex_in_answer = f"\\( {sy.latex(start_amount)} + {sy.latex(delta)} \\div 1000 {answered_unit}\\)"
                        elif increase_or_decrease == "decrease":
                            action_in_answer = "初めの量から減らした量を引くと"
                            end_amount_latex_in_answer = f"\\( {sy.latex(start_amount)} - {sy.latex(delta)} \\div 1000 {answered_unit} \\)"
                    else:
                        delta_latex_in_answer = f"\\( {sy.latex(delta)} ({delta_unit}) = {sy.latex(delta * sy.Rational(1, 1000))} {answered_unit} \\)"
                        if increase_or_decrease == "increase":
                            action_in_answer = "この2つを足すと"
                            end_amount_latex_in_answer = f"\\( {sy.latex(start_amount)}  + {sy.latex(delta * sy.Rational(1, 1000))} ({answered_unit})\\)"
                        elif increase_or_decrease == "decrease":
                            action_in_answer = "初めの量から減らした量を引くと"
                            end_amount_latex_in_answer = f"\\( {sy.latex(start_amount)} - {sy.latex(delta * sy.Rational(1, 1000))}({answered_unit})\\)"
            elif start_and_delta_unit == "g_and_kg":
                start_unit = "\\mathrm{g}"
                delta_unit = "\\mathrm{kg}"
                answered_unit = choice(["\\mathrm{g}", "\\mathrm{kg}"])
                start_amount_latex_in_problem = f"\\( {sy.latex(start_amount)}  {start_unit}\\)"
                delta_latex_in_problem = f"\\( {sy.latex(delta)} {delta_unit} \\)"
                if answered_unit == "\\mathrm{g}":
                    start_amount_latex_in_answer = start_amount_latex_in_problem
                    if delta == x:
                        delta_latex_in_answer = f"\\( {sy.latex(delta)} ({delta_unit}) = {sy.latex(delta)} \\div 1000 {answered_unit} \\)"
                        if increase_or_decrease == "increase":
                            action_in_answer = "この2つを足すと"
                            end_amount_latex_in_answer = f"\\( {sy.latex(start_amount)} + {sy.latex(delta)} \\div 1000 {answered_unit}\\)"
                        elif increase_or_decrease == "decrease":
                            action_in_answer = "初めの量から減らした量を引くと"
                            end_amount_latex_in_answer = f"\\( {sy.latex(start_amount)} - {sy.latex(delta)} \\div 1000 {answered_unit} \\)"
                    else:
                        delta_latex_in_answer = f"\\( {sy.latex(delta)} ({delta_unit}) = {sy.latex(delta * sy.Rational(1, 1000))} {answered_unit} \\)"
                        if increase_or_decrease == "increase":
                            action_in_answer = "この2つを足すと"
                            end_amount_latex_in_answer = f"\\( {sy.latex(start_amount)}  + {sy.latex(delta * sy.Rational(1, 1000))} ({answered_unit})\\)"
                        elif increase_or_decrease == "decrease":
                            action_in_answer = "初めの量から減らした量を引くと"
                            end_amount_latex_in_answer = f"\\( {sy.latex(start_amount)} - {sy.latex(delta * sy.Rational(1, 1000))}({answered_unit})\\)"
                elif answered_unit == "\\mathrm{kg}":
                    delta_latex_in_answer = delta_latex_in_problem
                    if start_amount == x:
                        start_amount_latex_in_answer = f"\\( {sy.latex(start_amount)} ({start_unit}) = {sy.latex(start_amount)} \\times 1000 ({answered_unit}) \\)"
                        if increase_or_decrease == "increase":
                            action_in_answer = "この2つを足すと"
                            end_amount_latex_in_answer = f"\\( {sy.latex(start_amount)} \\times 1000 + {sy.latex(delta)} ({answered_unit})\\)"
                        elif increase_or_decrease == "decrease":
                            action_in_answer = "初めの量から減らした量を引くと"
                            end_amount_latex_in_answer = f"\\( {sy.latex(start_amount)} \\times 1000 - {sy.latex(delta)} ({answered_unit})\\)"
                    else:
                        start_amount_latex_in_answer = f"\\( {sy.latex(start_amount)} ({start_unit}) = {sy.latex(start_amount * 1000)} ({answered_unit}) \\)"
                        if increase_or_decrease == "increase":
                            action_in_answer = "この2つを足すと"
                            end_amount_latex_in_answer = f"\\( {sy.latex(start_amount * 1000)}  + {sy.latex(delta)} ({answered_unit})\\)"
                        elif increase_or_decrease == "decrease":
                            action_in_answer = "初めの量から減らした量を引くと"
                            end_amount_latex_in_answer = f"\\( {sy.latex(start_amount * 1000)} - {sy.latex(delta)} ({answered_unit})\\)"
            start_amount_latex = f"\\( {sy.latex(start_amount)} {start_unit} \\)"
            delta_latex = f"\\( {sy.latex(delta)} {delta_unit} \\)"
            latex_problem = f"初めに{item}が{start_amount_latex}ありました。\n"
            latex_problem += f"{delta_latex}{action}した後の重さ{answered_unit}を、\\( x \\)を使った式で表しなさい。"
            latex_answer = f"初めの量が{start_amount_latex_in_answer}で、{delta_latex_in_answer}が{action}量なので、\n"
            latex_answer += f"{action_in_answer}、{end_amount_latex_in_answer}"
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

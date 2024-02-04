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
        if selected_problem_type == "expression_with_formula":
            # selected_theme = choice(["area", "volume", "weight", "price"])
            selected_theme = "price"
            if selected_theme == "area":
                self.latex_answer, self.latex_problem = self._make_expression_with_formula_area_problem()
            elif selected_theme == "volume":
                self.latex_answer, self.latex_problem = self._make_expression_with_formula_volume_problem()
            elif selected_theme == "weight":
                self.latex_answer, self.latex_problem = self._make_expression_with_formula_weight_problem()
            elif selected_theme == "price":
                self.latex_answer, self.latex_problem = self._make_expression_with_formula_price_problem()
            # self.latex_answer, self.latex_problem = self._make_expression_with_formula_problem()
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
        
        Developing:
            共通処理を関数として引っこ抜いて、多少見やすくする
            \\( \\)で返すべきか否か？
            →\\( \\)つきで返せば、problem, answer側の表現はシンプルになる一方で、式の中身は触りづらくなる
            →\\( \\)なしで返せば、多少はノイジーになるが、一方で式同士の足し合わせ等にも利用できる
            →→とりあえずなしで返す方向で
            
            関数に与える方の単位はどのようにすべきか？
            \\型で与えれば、中での処理は軽減できるが、それを外側で処理でしておかなければならなくなる
            →→メイン側のノイジーな感じを軽減したいので、関数側で処理する形で
        """
        # selected_genre = choice(["area", "volume", "weight", "price"])
        selected_genre = "weight"
        x = sy.Symbol("x")
        if selected_genre == "area":
            selected_shape = choice(["triangle", "parallelogram"])
            if selected_shape == "triangle":
                if random() > 0.5:
                    base = sy.Integer(randint(1, 10))
                    height = x
                else:
                    base = x
                    height = sy.Integer(randint(1, 10))
                latex_problem = f"底辺が \\( {base} \\mathrm{{cm}} \\)、高さが\\( {height} \\mathrm{{cm}} \\)の三角形があります。\n"
                latex_problem += f"三角形の面積を、\\( x \\)を使った式で表しなさい。"
                latex_answer = "三角形の面積は、(底辺) \\( \\times \\) (高さ) \\( \\div 2\\)なので、\n"
                latex_answer += f"\\( {base} \\times {height} \\div 2 \\)"
            elif selected_shape == "parallelogram":
                if random() > 0.5:
                    base = sy.Integer(randint(1, 10))
                    height = x
                else:
                    base = x
                    height = sy.Integer(randint(1, 10))
                latex_problem = f"底辺が \\( {base} \\mathrm{{cm}} \\)、高さが\\( {height} \\mathrm{{cm}} \\)の平行四辺形があります。\n"
                latex_problem += f"平行四辺形の面積を、\\( x \\)を使った式で表しなさい。"
                latex_answer = "平行四辺形の面積は、(底辺) \\( \\times \\) (高さ) \\( \\div 2\\)なので、\n"
                latex_answer += f"\\( {base} \\times {height} \\div 2 \\)"                
        elif selected_genre == "volume":
            item = choice(["ジュース", "お茶", "コーヒー"])
            increase_or_decrease = choice(["increase", "decrease"])
            if increase_or_decrease == "increase":
                list_to_shuffle = [sy.Integer(randint(1, 10)), x]
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
                list_to_shuffle = [sy.Integer(randint(1, 10)), x]
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
            list_to_shuffle = [sy.Integer(randint(1, 10)), x]
            shuffle(list_to_shuffle)
            start_amount, delta = list_to_shuffle
            start_and_delta_unit = choice(["g_and_g", "kg_and_kg", "kg_and_g", "g_and_kg"])
            # start_and_delta_unit = "g_and_kg"
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
                        delta_latex_in_answer = f"\\( {sy.latex(delta)} ({delta_unit}) = {sy.latex(delta)} \\div 1000 ({answered_unit}) \\)"
                        if increase_or_decrease == "increase":
                            action_in_answer = "この2つを足すと"
                            end_amount_latex_in_answer = f"\\( {sy.latex(start_amount)} + {sy.latex(delta)} \\div 1000 ({answered_unit}) \\)"
                        elif increase_or_decrease == "decrease":
                            action_in_answer = "初めの量から減らした量を引くと"
                            end_amount_latex_in_answer = f"\\( {sy.latex(start_amount)} - {sy.latex(delta)} \\div 1000 ({answered_unit}) \\)"
                    else:
                        delta_latex_in_answer = f"\\( {sy.latex(delta)} ({delta_unit}) = {sy.latex(delta * sy.Rational(1, 1000))} ({answered_unit}) \\)"
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
                        delta_latex_in_answer = f"\\( {sy.latex(delta)} ({delta_unit}) = {sy.latex(delta)} \\times 1000 ({answered_unit}) \\)"
                        if increase_or_decrease == "increase":
                            action_in_answer = "この2つを足すと"
                            end_amount_latex_in_answer = f"\\( {sy.latex(start_amount)} + {sy.latex(delta)} \\times 1000 ({answered_unit}) \\)"
                        elif increase_or_decrease == "decrease":
                            action_in_answer = "初めの量から減らした量を引くと"
                            end_amount_latex_in_answer = f"\\( {sy.latex(start_amount)} - {sy.latex(delta)} \\times 1000 ({answered_unit}) \\)"
                    else:
                        delta_latex_in_answer = f"\\( {sy.latex(delta)} ({delta_unit}) = {sy.latex(delta * 1000)} {answered_unit} \\)"
                        if increase_or_decrease == "increase":
                            action_in_answer = "この2つを足すと"
                            end_amount_latex_in_answer = f"\\( {sy.latex(start_amount)}  + {sy.latex(delta * 1000)} ({answered_unit})\\)"
                        elif increase_or_decrease == "decrease":
                            action_in_answer = "初めの量から減らした量を引くと"
                            end_amount_latex_in_answer = f"\\( {sy.latex(start_amount)} - {sy.latex(delta * 1000)} ({answered_unit})\\)"
                elif answered_unit == "\\mathrm{kg}":
                    delta_latex_in_answer = delta_latex_in_problem
                    if start_amount == x:
                        start_amount_latex_in_answer = f"\\( {sy.latex(start_amount)} ({start_unit}) = {sy.latex(start_amount)} \\div 1000 ({answered_unit}) \\)"
                        if increase_or_decrease == "increase":
                            action_in_answer = "この2つを足すと"
                            end_amount_latex_in_answer = f"\\( {sy.latex(start_amount)} \\div 1000 + {sy.latex(delta)} ({answered_unit})\\)"
                        elif increase_or_decrease == "decrease":
                            action_in_answer = "初めの量から減らした量を引くと"
                            end_amount_latex_in_answer = f"\\( {sy.latex(start_amount)} \\div 1000 - {sy.latex(delta)} ({answered_unit})\\)"
                    else:
                        start_amount_latex_in_answer = f"\\( {sy.latex(start_amount)} ({start_unit}) = {sy.latex(start_amount * sy.Rational(1, 1000))} ({answered_unit}) \\)"
                        if increase_or_decrease == "increase":
                            action_in_answer = "この2つを足すと"
                            end_amount_latex_in_answer = f"\\( {sy.latex(start_amount * sy.Rational(1, 1000))}  + {sy.latex(delta)} ({answered_unit})\\)"
                        elif increase_or_decrease == "decrease":
                            action_in_answer = "初めの量から減らした量を引くと"
                            end_amount_latex_in_answer = f"\\( {sy.latex(start_amount * sy.Rational(1, 1000))} - {sy.latex(delta)} ({answered_unit})\\)"
            start_amount_latex = f"\\( {sy.latex(start_amount)} {start_unit} \\)"
            delta_latex = f"\\( {sy.latex(delta)} {delta_unit} \\)"
            latex_problem = f"初めに{item}が{start_amount_latex}ありました。\n"
            latex_problem += f"{delta_latex}{action}した後の重さ\\( ({answered_unit}) \\)を、\\( x \\)を使った式で表しなさい。"
            latex_answer = f"初めの量が{start_amount_latex_in_answer}で、{delta_latex_in_answer}が{action}量なので、\n"
            latex_answer += f"{action_in_answer}、{end_amount_latex_in_answer}"
        return latex_answer, latex_problem
    
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
        
        Developing:
            円の足し引きだけで考えるならば、単位の変換は特に必要ない
            一方で、個数の増減、割増割引まで考えると計算は必須
            単位を付けるにしても、\\mathrm{{円}}はおそらく対応していないと思われる
            
            使えそうな関数は、特になし
                _make_latex_with_unitは円に対応していない
                _amount_adjusterはそもそも単位の変換が不要
                _unit_adjusterも同上
            関数内関数で対応する？
                そもそもどのような機能が必要になるか
                足し引き、割増割引
                    足し引きは同じ手法で行けそうだが、割増割引は計算としては単位の変換と同じような処理が必要になる（文字なら…数字なら…）
                    個数の増減も同様に、1000円が2個と、x円が2個では扱いが異なる
                    一応分けておく？それとも関数内関数にする？
                        とりあえず分けておく形で。あとで結局つかなければ中に入れておく。
            
            問題のパターンとしては、単純な商品の加算、個数の増減と加算、割引あたりが考えられる
            シンプルな順番だと、割引パターンが考えられる。また、個数も同じく掛け算のみで処理可能。
            複数の商品のパタンは、単純な加算なら細かい処理はいらない（これまでの量とかと同じ）だが、割増割引や個数との兼ね合わせになると少し複雑になる
            まずは割引、個数から実装していく
            
            商品名も、複数のパターンと一つだけのパターンがある。
            いったん、候補を並べておいて、そこからsampleで必要個数だけ抜き出す？
            
            割引率をどのように動作させるか？ratio_problemでは、以下のように
            ・割引率を一旦小数で与えて、そこから同時に計算まで行う関数？を用意していた
        def _random_ratio(self, selected_ratio, digit_under_decimal_point: int = 1):   
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
            
            採用するかどうかは、どこまで割合を複雑に取りたいかで変わってくる感じ
            シンプルに◯割引だけを採用するのであれば、
                discount_rate = sy.Integer(randint(1, 9)) * sy.Float(0.1)
                discount_ratio_in_japanese = f"{discount_rate * 10}割"でイケる。ただ、0の表示がどうなるか
                    0の表示がやばい
                    そのままは使えない。関数を桁を減らして使い回す？
                    ~割までに留めて、さらに小数の表示を省く。あるいは、割分と％で利用。いずれにしろ小数は不要
                    小数第二位まで使う感じで？

            表示の問題もある
            decimal_normalizeをどこから引っ張る？
        def _decimal_normalize(self, number: Union[str, sy.Integer, sy.Float]) -> str:
            ----
            小数点以下で末尾まで続いている連続した0を消去した文字列を返す。(eg. 100.00->100, 31.0010->31.001)

            Args:
                number (Union[str, sy.Integer, sy.Float]): 処理したい数

            Returns:
                number_str (str): 0が消去された文字列 
            ----
            number_str = str(number)
            while True:
                if ("." in number_str and number_str[-1] == "0") or (number_str[-1] == "."):
                    number_str = number_str[:-1]
                    continue
                break
            return number_str
            
            そこまで煩雑な処理ではないので中に入れても良い。関数として独立させても良い。
            とりあえず独立させておいて、random_ratio経由でしか利用しないようであれば、しれっと中に入れる感じで
            それでも主に桁絡みで何かしらの修正は必要そう
            あとは割合の表示の方では、\\( \\)のありなしで多少の齟齬がある可能性
        """
        def decimal_normalize(number: Union[str, sy.Integer, sy.Float]) -> str:
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
        
        def random_ratio(selected_ratio: str, digit_under_decimal_point: int = 1) -> Tuple[sy.Float, str]:
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
            if digit_under_decimal_point == 1:
                ratio_value = 0.1 * sy.Integer(randint(1, 9))
            elif digit_under_decimal_point == 2:
                ratio_value = 0.01 * sy.Integer(randint(1, 99))
            else:
                raise ValueError(f"'digit_under_the_decimal_point' is {digit_under_decimal_point}. This must be 1 or 2.")
            ratio_value = round(ratio_value, 6)
            if selected_ratio == "percentage":
                normalized_percentage = decimal_normalize(sy.latex(ratio_value * 100))
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
        # problem_theme = choice(["discount", "multiple_items_without_discount", "multiple_items_with_discount"])
        problem_theme = "multiple_items_with_discount"
        if problem_theme == "discount":
            item = choice(items)
            price_before_discount = x
            discount_ratio_value, discount_ratio_out_of_latex = random_ratio(choice(["percentage", "japanese_percentage"]), randint(1, 2))
            remained_ratio_value = 1 - discount_ratio_value
            remained_ratio_str = decimal_normalize(remained_ratio_value)
            price_after_discount = self._multiply_or_divide(price_before_discount, remained_ratio_value, multiply_or_divide="multiply")
            latex_problem = f"初めに\\( {sy.latex(x)} \\)円の{item}がありました。"
            latex_problem += f"{discount_ratio_out_of_latex}だけ値引きしたときの金額を、\\( x \\)を用いて表しなさい。"
            latex_answer = f"{discount_ratio_out_of_latex}だけ値引きしたということは、"
            latex_answer += f"値引きした後の金額を小数の割合で示すと、\\( {remained_ratio_str} \\)となる。\n"
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
            first_price, second_price = sample([x, sy.Integer(randint(1, 10) * 50)], k=2)
            """
            1つ目か2つ目、あるいは両方を値引きする
                素直に場合分けしておいたほうが良さそう？
                あるいは、何かしらの共通項を見出して、まとめられる分だけまとめるか。
                あるいは、処理の方と本文の方と、いずれかに共通化を行い、残ったものを扱う
                「◯円のアイテム1と、△円のアイテム2がありました。
                (アイテム1/アイテム2)....」
                処理の面倒さに噛み合っていない気もする。せいぜい3パターンなら書いたほうが見通しよくなるって感じでとりあえず。
                もし、書いていてまとめられそうな点があったら検討する形で。
                    item1だけ、item2だけであれば良さそう
            """
            discount_type = choice(["item1", ""])
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
        """量の変換のみの対応を行う関数

        Args:
            from_amount (Union[sy.Symbol, sy.Integer, sy.Rational, sy.Float]): 基準となる量
            from_unit (str): 変換元の単位
            to_unit (str): 変換先の単位

        Returns:
            adjusted_amount (str): 指定された単位に合わせた量 
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
            if from_amount.free_symbols:
                adjusted_amount = f"{from_amount} \\times 10"
            else:
                adjusted_amount = sy.latex(from_amount * sy.Integer(10))
        # / 10
        elif (from_unit == "dL") and (to_unit == "L"):
            if from_amount.free_symbols:
                adjusted_amount = f"{from_amount} \\div 10"
            else:
                adjusted_amount = sy.latex(from_amount * sy.Rational(1, 10))
        # weight
        # no change
        elif (from_unit == "kg") and (to_unit == "kg"):
            adjusted_amount = from_amount
        # no change
        elif (from_unit == "g") and (to_unit == "g"):
            adjusted_amount = from_amount
        # * 1000
        elif (from_unit == "kg") and (to_unit == "g"):
            if from_amount.free_symbols:
                adjusted_amount = f"{from_amount} \\times 1000"
            else:
                adjusted_amount = sy.latex(from_amount * 1000)
        # / 1000
        elif (from_unit == "g") and (to_unit == "kg"):
            if from_amount.free_symbols:
                adjusted_amount = f"{from_amount} \\div 1000"
            else:
                adjusted_amount = sy.latex(from_amount * sy.Rational(1, 1000))
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
        
        Developing:
            first_amountに違いは存在する？しない？
            多分しない。xだろうが1000だろうが同じ
                何を受け取るか？には検討の余地がある？問題がふわふわしてる？
                一応strでもそれ以外でも受け取れる形にしておく??
                    数やかけ算の対応が難しくなるのでは？？
                    数か文字しか入れないように押さえておく
            
            考えられるパターンは、
            数×数, 数÷数←特に操作必要なし。普通に計算
            文字×数, 数×文字, 文字÷数, 数÷文字←いずれも文字をそのままキープしておく
            
            もう一歩踏み込むと、1個目は数だろうと文字だろうと、通常のまま？
                2 * x = 2 \\times x
                2 * 300 = 600
                保留で良い？
                あるいは、数々のパターンの時には、さっさと計算する。いずれかが文字であれば、そのまま置いて、計算記号を挟む
        """
        # latex済想定
        if isinstance(first_amount, str):
            raise ValueError(f"'first_amount' must not be str.{first_amount} is wrong.")
        if isinstance(second_amount, str):
            raise ValueError(f"'first_amount' must not be str.{second_amount} is wrong.")
        if not(isinstance(first_amount, sy.Symbol)) and not(isinstance(second_amount, sy.Symbol)):
            calculated_amount = sy.latex(first_amount * second_amount)
        else:
            if multiply_or_divide == "multiply":
                calculated_amount = f"{sy.latex(first_amount)} \\times {sy.latex(second_amount)}"
            elif multiply_or_divide == "divide":
                calculated_amount = f"{sy.latex(first_amount)} \\div {sy.latex(second_amount)}"
            else:
                raise ValueError(f"'multiply_or_divide' must be 'multiply' or 'divide'. {multiply_or_divide} is wrong.")
        return calculated_amount

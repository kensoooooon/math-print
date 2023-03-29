from random import choice, randint, random, shuffle


import sympy as sy


class SameDenominatorCalculate:
    """同じ分母の足し算・引き算の問題を出力
    
    Attributes:
        _calculate_type (list): 計算に使用される演算子が格納
        _term_numbers (list): 問題の項数が格納
        latex_answer (str): latex形式で記述された解答
        latex_problem (str): latex形式で記述された問題
    """
    def __init__(self, **settings):
        """初期設定
        
        Args:
            settings (dict): 問題の各種設定
        """
        sy.init_printing(order='grevlex')
        self._calculate_type = settings["calculate_type"]
        self._term_numbers = settings["term_number"]
        self.latex_answer, self.latex_problem = self._make_problem()
    
    def _make_problem(self):
        """指定された計算の条件を満たす問題と解答を出力するコントローラ
        
        Returns:
            latex_answer (str): latex形式で記述された解答
            latex_problem (str): latex形式で記述された問題 
        
        Developing:
            真分数のみ
            計算結果は約分しない正の値
            途中表示も約分は不可
        """
        if self._calculate_type == ["addition"]:
            latex_answer, latex_problem = self._make_addition_only_problem()
        elif self._calculate_type == ["subtraction"]:
            latex_answer = "dummy answer"
            latex_problem = "dummy problem"
        elif self._calculate_type == ["addition", "subtraction"]:
            latex_answer = "dummy answer"
            latex_problem = "dummy problem"
        return latex_answer, latex_problem
    
    def _make_addition_only_problem(self):
        """足し算だけの計算問題を作成
        
        Returns:
            latex_answer (str): latex形式で記述された解答
            latex_problem (str): latex形式で記述された問題
        
        Developing:
            真分数のみ（帯分数、仮分数はなし）
            -> 4項は厳しい？
            -> 分母は最低5以上？
            -> 分子は最低3以上(1 + 1 + 1)
            
        from random import randint, choice


        import sympy as sy


        # in 3 terms

        for _ in range(20):
            same_denominator = randint(5, 18)
            max_numerator = randint(4, same_denominator)
            print(f"same_denominator: {same_denominator}")
            print(f"max_numerator: {max_numerator}")
            numerator1 = randint(1, max_numerator - 3)
            print(f"numerator1: {numerator1}")
            # numerator1 + numerator2 < same_denominator
            # numerator2 < same_denominator - numeartor1
            numerator2 = randint(1, max_numerator - numerator1 - 2)
            print(f"numerator2: {numerator2}")
            numerator3 = randint(1, max_numerator - numerator1 - numerator2 - 1)
            print(f"numerator3: {numerator3}")
            print(f"numerator1 + numerator2 + numerator3: {numerator1 + numerator2 + numerator3}")
            print("-------------------------")
        """
        common_denominator = randint(5, 18)
        term_number = int(choice(self._term_numbers))
        # divided?
        if term_number == 2:
            numerator1 = randint(1, int(common_denominator / 2))
            numerator2 = randint(1, common_denominator - numerator1 - 1)
            latex_answer = f"= \\frac{{{numerator1 + numerator2}}}{{{common_denominator}}}"
            if random() > 0.5:
                numerator1, numerator2 = numerator2, numerator1
            latex_problem = f"\\frac{{{numerator1}}}{{{common_denominator}}} + \\frac{{{numerator2}}}{{{common_denominator}}}"
            latex_answer = f"= \\frac{{{numerator1 + numerator2}}}{{{common_denominator}}}"
        elif term_number == 3:
            pass
        else:
            raise ValueError(f"'term_number' is {term_number}. This must be 2 or 3.")
        return latex_answer, latex_problem

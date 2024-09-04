"""
9/4
"出題に利用される数の最大値"を100以下でも通るようにするための処理
値自体は別にhtmlの方でmaxを解除すれば済む話だが、生成のロジックがうまく回るかが不明。というか、ロジックがよく理解できていない
    現状は、与えられた最大値を満たすように、適当な数→公倍数や公約数の流れで計算している
    処理が面倒になっていることの一端はここにある気がする
    
    _base_num_makerの動作がよく理解できていない。なにか面倒なことをしているのはわかるが...
        self._max_problem_numberを超えないような自然数の指数を求めて、そこからランダムに数をかけて扱っている感じがある。
"""

from random import choice, randint, shuffle

import sympy as sy


class LCMAndGCD:
    """公倍数と公約数を求める問題
    
    Attributes:
        _problem_type_list (list): 問題タイプ
        _max_problem_number (int): 問題に登場する数の最大値
        latex_answer (str): latexで記述された解答
        latex_problem (str): latexで記述された問題
    """
    def __init__(self, **settings):
        """
        Args:
            settings (dict): 問題の設定
        """
        self._problem_type_list = settings["problem_type_list"]
        self._max_problem_number = settings["max_problem_number"]
        self.latex_answer, self.latex_problem = self._make_problem()
    
    def _make_problem(self):
        """問題作成のコントローラー

        Returns:
            latex_answer (str): latexで記述された解答
            latex_problem (str): latexで記述された問題
        """
        selected_problem_type = choice(self._problem_type_list)
        if selected_problem_type == "lcm":
            latex_answer, latex_problem = self._make_lcm_problem()
        elif selected_problem_type == "gcd":
            latex_answer, latex_problem = self._make_gcd_problem()
        return latex_answer, latex_problem

    def _make_lcm_problem(self):
        """公倍数を求める問題の生成

        Returns:
            latex_answer (str): latexで記述された最小公倍数
            latex_problem (str): latexで記述された問題文
        
        Note:
            latex_problemに日本語を含むため、\(\)は手動で追加すること。
        """
        def lcms(x, y):
            """2つの数x,yの公倍数を小さい順に出力する関数

            Args:
                x (int): もととなる数その1
                y (int): もととなる数その2

            Returns:
                lcms (list): 最小公倍数を含め5つの公倍数が含まれたリスト
            """
            import math
            lcms = [((x * y) // math.gcd(x, y)) * i for i in range(1, 6)]
            return lcms
        
        num1, num2 = self._base_num_maker()
        latex_problem = f"\\({num1}, {num2}\\)の公倍数を、小さい順に5つ求めよ。"
        lcms_list = lcms(num1, num2)
        lcms_str = str(lcms_list).replace("[", "").replace("]", "")
        latex_answer = f"{lcms_str}"
        return latex_answer, latex_problem

    def _make_gcd_problem(self):
        """公約数を求める問題の生成
        
        Returns:
            latex_answer (str): latex形式で記述された解答
            latex_problem (str): latex形式で記述された問題

        Note:
            latex_problemに日本語を含むため、\(\)は手動で追加すること。
        """
        def divisors(x, y):
            """2つの数x,yの公約数をすべて出力する関数

            Args:
                x (_type_): _description_
                y (_type_): _description_

            Returns:
                _type_: _description_
            """
            import math
            gcd = math.gcd(x, y)
            lower_divisors, upper_divisors = [], []
            i = 1
            while i * i <= gcd:
                if gcd % i == 0:
                    lower_divisors.append(i)
                    if i != gcd // i:
                        upper_divisors.append(gcd // i)
                i += 1
            return lower_divisors + upper_divisors[::-1]
        
        num1, num2 = self._base_num_maker()
        latex_problem = f"\\({num1}, {num2}\\)の公約数をすべて求めよ。"
        gcds_list = divisors(num1, num2)
        gcds_str = str(gcds_list).replace("[", "").replace("]", "")
        latex_answer = f"{gcds_str}"
        return latex_answer, latex_problem
    
    def _base_num_maker(self):
        """最小公倍数と最大公約数を求める問題の生成に利用する2つの数を求める関数
        
        Return:
            num1 (int): 対象となる数その1
            num2 (int): 対象となる数その2
        
        Note:
            いずれの数も1以上100以下
            等しくない数を生成する
        """
        def max_indexer(num, base):
            """その数にかけたときに、max_problem_numberを超えない最大の指数を求める関数

            Args:
                num (int): 対象となる数
                base (int): かけられる数の指数となる値

            Returns:
                max_index (int): max_problem_numberを超えない最大の指数
            Note:
                max_value (floor): num * (base ** max_value) - max_problem_number = 0の解を、solveでなく手計算で求めている値
            """
            from math import floor
            max_value = (sy.log(self._max_problem_number) - sy.log(num)) / (sy.log(base))
            max_index = floor(max_value)
            return max_index

        bases = [2, 3, 4, 5, 6, 7, 8]
        shuffle(bases)
        while True:
            num1, num2 = 1, 1
            for base in bases:
                min_index = 0
                max_index1 = max_indexer(num1, base)
                max_index2 = max_indexer(num2, base)
                if (max_index1 == 0) and (max_index2 == 0):
                    break
                num1_index = randint(min_index, max_index1)
                num2_index = randint(min_index, max_index2)
                num1 *= (base ** num1_index)
                num2 *= (base ** num2_index)
            if (num1 != 1) and (num2 != 1) and (num1 != num2):
                break
        return num1, num2
            
    
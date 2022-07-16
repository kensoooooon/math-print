"""
kaizenban

import math, random

import sympy as sy

def divisors(x, y):
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

def lcms(x, y):
    lst = [((x * y) // math.gcd(x, y)) * i for i in range(1, 6)]
    return lst

def max_indexer(now_num, base_candidate):
    x = sy.Symbol("x", real=True)
    max_value = (sy.log(100) - sy.log(now_num)) / (sy.log(base))
    max_index = math.floor(max_value)
    return max_index

for _ in range(5):
    bases = [2, 3, 5, 7, 11, 13]
    # random.shuffle(bases)
    num1, num2 = 1, 1
    for base in bases:
        print(f"base: {base}")
        print(f"num1: {num1}")
        print(f"num2: {num2}")
        min_index = 0
        max_index1 = max_indexer(num1, base)
        print(f"max_index1: {max_index1}")
        max_index2 = max_indexer(num2, base)
        print(f"max_index1: {max_index1}")
        if (max_index1 == 0) and (max_index2 == 0):
            break
        num1_index = random.randint(min_index, max_index1)
        num2_index = random.randint(min_index, max_index2)
        num1 *= (base ** num1_index)
        num2 *= (base ** num2_index)
        print("-------------")
    print(f"num1: {num1}")
    print(f"num2: {num2}")
    print(f"divisors: {divisors(num1, num2)}")
    print(f"lcms: {lcms(num1, num2)}")
    print("-------------------------------------------------------------")

"""

from random import choice, randint

import sympy as sy


class LCMAndGCD:
    
    def __init__(self, **settings):
        self._problem_type_list = settings["problem_type_list"]
        self.latex_answer, self.latex_problem = self._make_problem()
    
    def _make_problem(self):
        selected_problem_type = choice(self._problem_type_list)
        if selected_problem_type == "lcm":
            latex_answer, latex_problem = self._make_lcm_problem()
        elif selected_problem_type == "gcd":
            latex_answer, latex_problem = self._make_gcd_problem()
        return latex_answer, latex_problem

    def _make_lcm_problem(self):
        """最小公倍数を求める問題の生成

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
                lcms (list): 最大公約数を含め5つの公倍数が含まれたリスト
            """
            import math
            lcms = [((x * y) // math.gcd(x, y)) * i for i in range(1, 6)]
            return lcms
        
        num1, num2 = self._base_num_maker()
        latex_problem = f"\({num1}, {num2}\)の公倍数を、小さい順に5つ求めよ。"
        lcms_list = lcms(num1, num2)
        latex_answer = str(lcms_list).replace("[", "").replace("]", "")
        
        return latex_answer, latex_problem

    def _make_gcd_problem(self):
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
            """その数にかけたときに、100を超えない最大の指数を求める関数

            Args:
                num (int): 対象となる数
                base (int): かけられる数の指数となる値

            Returns:
                max_index (int): 100を超えない最大の指数
            Note:
                max_value (floor): num * (base ** max_value) - 100 = 0の解を、solveでなく手計算で求めている値
            Making:
                どこでbreak?また、同じ値になったときにはじく判定は？
            """
            from math import floor
            max_value = (sy.log(100) - sy.log(num)) / (sy.log(base))
            max_index = floor(max_value)
            return max_index

        bases = [2, 3, 4, 5, 6, 7, 8]
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
            
    
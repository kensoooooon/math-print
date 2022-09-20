from random import choice, randint, random, sample, shuffle

import sympy as sy

class CommonDenominatorProblem:
    """通分の問題を出力する
    
    Attributes:
        _fraction_types (list): 問題に使用される分数の候補が格納されたリスト
        _fraction_numbers (list): 問題に登場する分数の個数
        latex_answer (str): latex形式で記述された解答
        latex_problem (str): latex形式で記述された問題
    """
        
    def __init__(self, **settings):
        """初期処理
        
        Args:
            settings (dict): 問題の設定が格納されている
        """
        sy.init_printing(order='grevlex')
        self._fraction_types = settings["fraction_type_list"]
        self._fraction_numbers = settings["fraction_numbers_list"]
        self.latex_answer, self.latex_problem = self._make_problem()

    def _make_problem(self):
        """候補となる分数からランダムに選択を行い、それに応じた問題と解答を出力させる

        Raises:
            ValueError: 存在しない分数のタイプを選択したときに挙上される

        Returns:
            latex_answer (str): latex形式で記述された解答
            latex_problem (str): latex形式で記述された問題
        
        Developing:
            分数のタイプごとに問題をわけるんじゃなくて、出力される分数が変化するようにする?
        """
        selected_fraction_number = choice(self._fraction_numbers)
        prime_numbers = [2, 3, 5, 7]
        shuffle(prime_numbers)
        # coprime denominator
        if random() < 0.4:
            denominators = sample(prime_numbers, selected_fraction_number)
        # not coprime denominator
        else:
            denominator_base = choice(prime_numbers)
            multiplied_numbers = sample(list(range(1, 7)), selected_fraction_number)
            denominators = [denominator_base * multiplied_number for multiplied_number in multiplied_numbers]
        lcm = sy.ilcm(*denominators)
        latex_answer = ""
        latex_problem = ""              
        for denominator in denominators:
            selected_fraction_type = choice(self._fraction_types)               
            if selected_fraction_type == "proper_fraction":
                numerator = denominator - randint(1, denominator-1)
                fraction = Fraction(numerator, denominator)
            elif selected_fraction_type == "improper_fraction":
                numerator = denominator + randint(1, denominator)
                fraction = Fraction(numerator, denominator)
            elif selected_fraction_type == "mixed_fraction":
                numerator = denominator - randint(1, denominator-1)
                integer_part = randint(1, 7)
                fraction = Fraction(numerator, denominator, integer_part=integer_part)
            latex_problem += f"{fraction.latex()},"
            fraction.change_denominator_to(lcm)
            latex_answer += f"{fraction.latex()},"
        latex_problem = latex_problem.rstrip(",")
        latex_answer = latex_answer.rstrip(",")
        return latex_answer, latex_problem


class Fraction:
    """分数を分子、分母、整数部にわけて格納するクラス
    
    Attributes:
        self._numerator (int): 分子
        self._denominator (int): 分母
        self._integer_part (int): 整数部
    """
    def __init__(self, numerator, denominator, integer_part=0):
        """初期処理

        Args:
            numerator (int): 分子
            denominator (int): 分母
            integer_part (int, optional): 整数部。デフォルトは0

        Raises:
            TypeError: 分子、分母、整数部のいずれかが整数でなかったときに挙上
        """
        if not isinstance(numerator, int):
            raise TypeError(f"Type of 'numerator' is {type(numerator)}. 'numerator' must be integer.")
        self._numerator = numerator
        if not isinstance(denominator, int):
            raise TypeError(f"Type of 'denominator' is {type(denominator)}. 'denominator' must be integer.")
        self._denominator = denominator
        if not isinstance(integer_part, int):
            raise TypeError(f"Type of 'integer_part' is {type(integer_part)}. 'integer_part' must be integer.")
        self._integer_part = integer_part
    
    def __str__(self):
        return f"Fraction<{self.integer_part} {self.numerator} / {self.denominator}>"
    
    def latex(self):
        """格納された値からlatex形式の分数を出力する

        Returns:
            latex_fraction (str): latex形式の分数
        """
        if self.integer_part == 0:
            latex_fraction = f"\\dfrac{{ {self.numerator} }}{{ {self.denominator} }}"
        else:
            latex_fraction = f"{self.integer_part} \\dfrac{{ {self.numerator} }}{{ {self.denominator} }}"
        return latex_fraction

    def change_denominator_to(self, number):
        """分数自体の値はそのままに、分母を指定された値に変化させる

        Args:
            number (int): 分母の変化先
        """
        multiplied_value = int(number / self.denominator)
        self.denominator *= multiplied_value
        self.numerator *= multiplied_value
    
    @property
    def numerator(self):
        return self._numerator
    
    @property
    def denominator(self):
        return self._denominator
    
    @property
    def integer_part(self):
        return self._integer_part
    
    @numerator.setter
    def numerator(self, numerator):
        if not isinstance(numerator, int):
            raise TypeError(f"Type of 'numerator' is {type(numerator)}. 'numerator' must be integer.")
        self._numerator = numerator
        
    @denominator.setter
    def denominator(self, denominator):
        if not isinstance(denominator, int):
            raise TypeError(f"Type of 'denominator' is {type(denominator)}. 'denominator' must be integer.")
        self._denominator = denominator

    @integer_part.setter
    def integer_part(self, integer_part):
        if not isinstance(integer_part, int):
            raise TypeError(f"Type of 'integer_part' is {type(integer_part)}. 'integer_part' must be integer.")
        self._integer_part = integer_part

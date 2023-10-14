from random import choice, randint, random, sample
from typing import Dict, Tuple, Union

import sympy as sy


class MultiplicationAndDivisionOfFractionFor6thGrade:
    """分数と整数の掛け算と割り算を指定された条件に応じて作成・格納
    
    Attributes:
        latex_answer (str): latex形式で記述された解答
        latex_problem (str): latex形式で記述された問題
    """
    def __init__(self, **settings: Dict) -> None:
        """初期設定
        
        Args:
            settings (dict): 問題の設定を格納
    
        Raises:
            ValueError: 想定されていないタイプの問題が指定されたときに挙上
        """
        selected_calculation_type = choice(settings["fraction_calculation_types"])
        if selected_calculation_type == "fraction_multiplied_by_integer":
            self.latex_answer, self.latex_problem = self._make_fraction_multiplied_by_integer_problem()
        elif selected_calculation_type == "fraction_divided_by_integer":
            self.latex_answer, self.latex_problem = self._make_fraction_divided_by_integer_problem()
        elif selected_calculation_type == "integer_multiplied_by_fraction":
            self.latex_answer, self.latex_problem = self._make_integer_multiplied_by_fraction_problem()
        elif selected_calculation_type == "integer_divided_by_fraction":
            self.latex_answer, self.latex_problem = self._make_integer_divided_by_fraction_problem()
        elif selected_calculation_type == "fraction_multiplied_by_fraction":
            self.latex_answer, self.latex_problem = self._make_fraction_multiplied_by_fraction_problem()
        elif selected_calculation_type == "fraction_divided_by_fraction":
            self.latex_answer, self.latex_problem = self._make_fraction_divided_by_fraction_problem()
        else:
            raise ValueError(f"'selected_calculation_type' is {selected_calculation_type}. This isn't expected value.")
    
    def _make_fraction_multiplied_by_integer_problem(self) -> Tuple[str, str]:
        """分数×整数型の問題と解答を作成

        Returns:
            Tuple[str, str]: 問題と解答
            - latex_answer (str): latex形式であることを前提とした解答
            - latex_problem (str): latex形式であることを前提とした問題
        """
        num1 = self._random_frac()
        num2 = self._random_integer()
        latex_problem = f"{sy.latex(num1)} \\times {sy.latex(num2)}"
        answer = num1 * num2
        latex_answer = f" = {sy.latex(answer)}"
        return latex_answer, latex_problem
    
    def _make_fraction_divided_by_integer_problem(self) -> Tuple[str, str]:
        """分数÷整数型の問題と解答を作成

        Returns:
            Tuple[str, str]: 問題と解答
            - latex_answer (str): latex形式であることを前提とした解答
            - latex_problem (str): latex形式であることを前提とした問題
        """
        num1 = self._random_frac()
        num2 = self._random_integer()
        latex_problem = f"{sy.latex(num1)} \\div {sy.latex(num2)}"
        answer = num1 / num2
        latex_answer = f" = {sy.latex(answer)}"
        return latex_answer, latex_problem
    
    def _make_integer_multiplied_by_fraction_problem(self) -> Tuple[str, str]:
        """整数×分数型の問題と解答を作成

        Returns:
            Tuple[str, str]: 問題と解答
            - latex_answer (str): latex形式であることを前提とした解答
            - latex_problem (str): latex形式であることを前提とした問題
        """
        num1 = self._random_integer()
        num2 = self._random_frac()
        latex_problem = f"{sy.latex(num1)} \\times {sy.latex(num2)}"
        answer = num1 * num2
        latex_answer = f" = {sy.latex(answer)}"
        return latex_answer, latex_problem
    
    def _make_integer_divided_by_fraction_problem(self) -> Tuple[str, str]:
        """整数÷分数型の問題と解答を作成

        Returns:
            Tuple[str, str]: 問題と解答
            - latex_answer (str): latex形式であることを前提とした解答
            - latex_problem (str): latex形式であることを前提とした問題
        """
        num1 = self._random_integer()
        num2 = self._random_frac()
        latex_problem = f"{sy.latex(num1)} \\div {sy.latex(num2)}"
        answer = num1 / num2
        latex_answer = f" = {sy.latex(answer)}"
        return latex_answer, latex_problem
    
    def _make_fraction_multiplied_by_fraction_problem(self) -> Tuple[str, str]:
        """分数×分数型の問題と解答を作成

        Returns:
            Tuple[str, str]: 問題と解答
            - latex_answer (str): latex形式であることを前提とした解答
            - latex_problem (str): latex形式であることを前提とした問題
        """
        num1 = self._random_frac()
        num2 = self._random_frac()
        latex_problem = f"{sy.latex(num1)} \\times {sy.latex(num2)}"
        answer = num1 * num2
        latex_answer = f" = {sy.latex(answer)}"
        return latex_answer, latex_problem
    
    def _make_fraction_divided_by_fraction_problem(self) -> Tuple[str, str]:
        """分数÷分数型の問題と解答を作成

        Returns:
            Tuple[str, str]: 問題と解答
            - latex_answer (str): latex形式であることを前提とした解答
            - latex_problem (str): latex形式であることを前提とした問題
        """
        num1 = self._random_frac()
        num2 = self._random_frac()
        latex_problem = f"{sy.latex(num1)} \\div {sy.latex(num2)}"
        answer = num1 / num2
        latex_answer = f" = {sy.latex(answer)}"
        return latex_answer, latex_problem

    def _random_frac(self) -> sy.Rational:
        """ランダムな分数を作成
        
        Returns:
            frac (sy.Rational): 分数
        
        Developing:
            denominator: 8
            numerators: {3, 5, 6, 7, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24}
            numerator: 16
            
            ->仮分数になるので、そこから整数に派生することがある。
            -->%==0の判定?setで倍数を含めて消去?
        """
        denominator = randint(2, 25)
        numerators_without_divisors = set(range(1, 25)) - set(sy.divisors(denominator))
        numerators = [num for num in numerators_without_divisors if num % denominator != 0]
        numerator = choice(numerators)
        frac = sy.Rational(numerator, denominator)
        if frac.denominator == 1:
            print(f"denominator: {denominator}")
            print(f"numerators: {numerators}")
            print(f"numerator: {numerator}")
            raise ValueError(f"frac is {frac}. This shouldn't be integer.")
        return frac
    
    def _random_integer(self) -> sy.Integer:
        """ランダムな整数を作成

        Returns:
            integer (sy.Integer): 整数
        """
        integer = sy.Integer(randint(2, 10))
        return integer

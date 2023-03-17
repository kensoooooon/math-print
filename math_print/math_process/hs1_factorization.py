from random import choice, randint, random

import sympy as sy


class HS1FactorizationProblem:

    def __init__(self, **settings):
        sy.init_printing(order='grevlex')
        self._factorization_type_list = settings["factorization_type_list"]
        self._another_character_existence = settings["another_character_existence"]
        self._used_character_dict = {}
        for symbol in ["x", "y", "z"]:
            self._used_character_dict[symbol] = sy.Symbol(symbol, real=True)
        self.latex_answer, self.latex_problem = self._make_problem()
    
    def _make_problem(self):
        selected_factorization_type = choice(self._factorization_type_list)
        
        """
        factorization_type_list.append('a^2+2ab+b^2=(a+b)^2')
        factorization_type_list.append('a^2-2ab+b^2=(a-b)^2')
        factorization_type_list.append('a^2-b^2=(a+b)(a-b)')
        factorization_type_list.append('acx^2+(ad+bc)x+ab=(ax+b)(cx+d)')
        factorization_type_list.append('a^2+b^2+c^2+2ab+2bc+2ca=(a+b+c)^2')
        factorization_type_list.append('a^3+3a^2b+3ab^2+b^3=(a+b)^3')
        factorization_type_list.append('a^3-3a^2b+3ab^2-b^3=(a-b)^3')
        factorization_type_list.append('a^3+b^3=(a+b)(a^2-ab+b^2)')
        factorization_type_list.append('a^3-b^3=(a-b)(a^2+ab+b^2)')
        """
        
        if selected_factorization_type == 'a^2+2ab+b^2=(a+b)^2':
            latex_answer, latex_problem = self._make_to_plus_square()
        elif selected_factorization_type == 'a^2-2ab+b^2=(a-b)^2':
            latex_answer, latex_problem = self._make_to_minus_square()
        elif selected_factorization_type == 'a^2-b^2=(a+b)(a-b)':
            latex_answer, latex_problem = self._make_to_plus_minus()
        elif selected_factorization_type == 'acx^2+(ad+bc)x+ab=(ax+b)(cx+d)':
            latex_answer, latex_problem = self._make_to_cross_multiplication()
        elif selected_factorization_type == 'a^2+b^2+c^2+2ab+2bc+2ca=(a+b+c)^2':
            latex_answer, latex_problem = self._make_to_triple_square()
        elif selected_factorization_type == 'a^3+3a^2b+3ab^2+b^3=(a+b)^3':
            latex_answer, latex_problem = self._make_to_plus_cubed()
        elif selected_factorization_type == 'a^3-3a^2b+3ab^2-b^3=(a-b)^3':
            latex_answer, latex_problem = self._make_to_minus_cubed()
        elif selected_factorization_type == 'a^3+b^3=(a+b)(a^2-ab+b^2)':
            latex_answer, latex_problem = self._make_from_plus_cubed()
        elif selected_factorization_type == 'a^3-b^3=(a-b)(a^2+ab+b^2)':
            latex_answer, latex_problem = self._make_from_minus_cubed()

        return latex_answer, latex_problem
    
    def _make_to_plus_square(self):
        # 'a^2+2ab+b^2=(a+b)^2'
        a_num = self._make_random_number(positive_or_negative="positive")
        a_term = a_num * self._used_character_dict["x"]
        b_num = self._make_random_number(positive_or_negative="positive")
        
        if self._another_character_existence:
            b_term = b_num * self._used_character_dict["y"]
        else:
            b_term = b_num
        
        answer = (a_term + b_term) ** 2
        latex_answer = f"= {sy.latex(answer)}"
        problem = sy.expand(answer)
        latex_problem = sy.latex(problem)
        
        return latex_answer, latex_problem

    def _make_to_minus_square(self):
        # 'a^2-2ab+b^2=(a-b)^2'
        a_num = self._make_random_number(positive_or_negative="positive")
        a_term = a_num * self._used_character_dict["x"]
        b_num = self._make_random_number(positive_or_negative="negative")
        
        if self._another_character_existence:
            b_term = b_num * self._used_character_dict["y"]
        else:
            b_term = b_num
        
        answer = (a_term + b_term) ** 2
        latex_answer = f"= {sy.latex(answer)}"
        problem = sy.expand(answer)
        latex_problem = sy.latex(problem)
        
        return latex_answer, latex_problem
    
    def _make_to_plus_minus(self):
        # 'a^2-b^2=(a+b)(a-b)'
        a_num = self._make_random_number(positive_or_negative="positive")
        a_term = a_num * self._used_character_dict["x"]
        
        b_num = self._make_random_number(positive_or_negative="positive")
        if self._another_character_existence:
            b_term = b_num * self._used_character_dict["y"]
        else:
            b_term = b_num
        
        answer = (a_term + b_term) * (a_term - b_term)
        latex_answer = f"= {sy.latex(answer)}"
        problem = sy.expand(answer)
        latex_problem = sy.latex(problem)
        
        return latex_answer, latex_problem

    def _make_to_cross_multiplication(self):
        # 'acx^2+(ad+bc)x+ab=(ax+b)(cx+d)'
        """たすき掛け型の因数分解問題と解答を出力
        
        Returns:
            latex_answer (str): latex形式で記述された解答
            latex_problem (str): latex形式で記述された問題
        
        Developing:
            a,bとc,dは互いに素でないと、中でくくれてしまう.
            -> 辞書で組み込む？
            
            いったん完全ランダムにして展開、因数分解で問題解答を作る？
        """
        x = self._used_character_dict["x"]
        a_num = self._make_random_number(max_number=5)
        b_num = self._make_random_number(max_number=5)
        c_num = self._make_random_number(max_number=5)
        d_num = self._make_random_number(max_number=5)
        
        if self._another_character_existence:
            y = self._used_character_dict["y"]
            left = (a_num * x + b_num * y) * (c_num * x + d_num * y)
        else:
            left = (a_num * x + b_num) * (c_num * x + d_num)
        
        latex_problem = sy.latex(sy.expand(left))
        latex_answer = f"= {sy.latex(sy.factor(left))}"
        
        return latex_answer, latex_problem

    def _make_to_triple_square(self):
        # 'a^2+b^2+c^2+2ab+2bc+2ca=(a+b+c)^2'
        a_num = self._make_random_number(positive_or_negative="positive")
        a_term = a_num * self._used_character_dict["x"]
        
        b_num = self._make_random_number()
        c_num = self._make_random_number()
        if self._another_character_existence:
            b_term = b_num * self._used_character_dict["y"]
            c_term = c_num * self._used_character_dict["z"]
        else:
            b_term = b_num
            c_term = c_num
        
        answer = (a_term + b_term + c_term) ** 2
        latex_answer = f"= {sy.latex(answer)}"
        problem = sy.expand(answer)
        latex_problem = sy.latex(problem)
        
        return latex_answer, latex_problem

    def _make_to_plus_cubed(self):
        # 'a^3+3a^2b+3ab^2+b^3=(a+b)^3':
        a_num = self._make_random_number(positive_or_negative="positive")
        a_term = a_num * self._used_character_dict["x"]
        
        b_num = self._make_random_number(positive_or_negative="positive")
        if self._another_character_existence:
            b_term = b_num * self._used_character_dict["y"]
        else:
            b_term = b_num
        
        answer = (a_term + b_term) ** 3
        latex_answer= f"= {sy.latex(answer)}"
        problem = sy.expand(answer)
        latex_problem = sy.latex(problem)
        
        return latex_answer, latex_problem
           
    def _make_to_minus_cubed(self):
        # 'a^3-3a^2b+3ab^2-b^3=(a-b)^3':
        a_num = self._make_random_number(positive_or_negative="positive")
        a_term = a_num * self._used_character_dict["x"]
        
        b_num = self._make_random_number(positive_or_negative="negative")
        if self._another_character_existence:
            b_term = b_num * self._used_character_dict["y"]
        else:
            b_term = b_num
        
        answer = (a_term + b_term) ** 3
        latex_answer= f"= {sy.latex(answer)}"
        problem = sy.expand(answer)
        latex_problem = sy.latex(problem)
        
        return latex_answer, latex_problem

    def _make_from_plus_cubed(self):
        # 'a^3+b^3=(a+b)(a^2-ab+b^2)':
        a_num = self._make_random_number(positive_or_negative="positive")
        a_term = a_num * self._used_character_dict["x"]
        
        b_num = self._make_random_number(positive_or_negative="positive")
        if self._another_character_existence:
            b_term = b_num * self._used_character_dict["y"]
        else:
            b_term = b_num
        
        answer = (a_term + b_term) * ((a_term ** 2) - a_term * b_term + (b_term ** 2))
        latex_answer = f"= {sy.latex(answer)}"
        problem = sy.expand(answer)
        latex_problem = sy.latex(problem)
        
        return latex_answer, latex_problem

    def _make_from_minus_cubed(self):
        # 'a^3-b^3=(a-b)(a^2+ab+b^2)':
        a_num = self._make_random_number(positive_or_negative="positive")
        a_term = a_num * self._used_character_dict["x"]
        
        b_num = self._make_random_number(positive_or_negative="positive")
        if self._another_character_existence:
            b_term = b_num * self._used_character_dict["y"]
        else:
            b_term = b_num
        
        answer = (a_term - b_term) * ((a_term ** 2) + a_term * b_term + (b_term ** 2))
        latex_answer = f"= {sy.latex(answer)}"
        problem = sy.expand(answer)
        latex_problem = sy.latex(problem)
        
        return latex_answer, latex_problem

    def _make_random_number(self, positive_or_negative=None, min_number=1, max_number=6):
        """指定された条件を満たす整数を返す

        Args:
            positive_or_negative (_type_, optional): 正か負の指定
            min_number (int, optional): 最小値
            max_number (int, optional): 最大値

        Returns:
            number (sy.Integer): 返す整数
        """
        number = sy.Integer(randint(min_number, max_number))
        
        if positive_or_negative is None:
            if random() > 0.5:
                number = -1 * number
        elif positive_or_negative == "negative":
            number = -1 * number
        elif positive_or_negative == "positive":
            pass
        
        return number

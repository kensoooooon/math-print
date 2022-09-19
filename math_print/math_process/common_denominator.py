from random import choice, randint, random, shuffle

import sympy as sy

class CommonDenominatorProblem:
    """通分の問題を出力する
    
    Attributes:
        _fraction_type_list (list): 問題に使用される分数の候補が格納されたリスト
        _fraction_numbers_list (list): 問題に登場する分数の個数
        latex_answer (str): latex形式で記述された解答
        latex_problem (str): latex形式で記述された問題
    """
    def __init__(self, **settings):
        """初期処理
        
        Args:
            settings (dict): 問題の設定が格納されている
        """
        sy.init_printing(order='grevlex')
        self._fraction_type_list = settings["fraction_type_list"]
        self._fraction_numbers_list = settings["fraction_numbers_list"]
        self.latex_answer, self.latex_problem = self._make_problem()

    def _make_problem(self):
        """候補となる分数からランダムに選択を行い、それに応じた問題と解答を出力させる

        Raises:
            ValueError: 存在しない分数のタイプを選択したときに挙上される

        Returns:
            latex_answer (str): latex形式で記述された解答
            latex_problem (str): latex形式で記述された問題
        """
        selected_fraction_type = choice(self._fraction_type_list)
        selected_fraction_number = choice(self._fraction_numbers_list)
        if selected_fraction_type == "proper_fraction":
            latex_answer, latex_problem = self._make_proper_fraction_problem(selected_fraction_number)
        """
        elif selected_fraction_type == "improper_fraction":
            latex_answer, latex_problem = self._make_improper_fraction_problem()
        elif selected_fraction_type == "mixed_fraction":
            latex_answer, latex_problem = self._make_mixed_fraction_problem()
        else:
            raise ValueError(f"selected_fraction_type is '{selected_fraction_type}'. This may be wrong.")
        """
        return latex_answer, latex_problem
    
    def _make_proper_fraction_problem(self, selected_fraction_number):
        """真分数の約分問題を出力
        
        Args:
            selected_fraction_number (int): 問題に登場する分数の個数
        
        Returns:
            latex_answer (str): latex形式で記述された解答
            latex_problem (str): latex形式で記述された問題
        
        Developing:
            まんまかければいいやつと、共通因数みていいかんじにかけるやつの2タイプ
            ↑をそこそこの割合で出力させたい: random()で対応4:6くらい？
            そのままsy.Rationalすると、確か約分されてしまうはず
            ↑gcd=1指定でok
            
            まんまかければいい＝互いに素である数
                素数であれば必ず互いに素だが、9,2も互いに素
                ->2,3,5,7,11,,でリストを用意してあげて、適当に2乗とか3乗とかする感じで、
                絶対に素因数がかぶらないようにしてあげる？
            
            共通因数を見抜くやつは、場合によっては同じ分母が出力されてしまって、分数にならない可能性がある
            eg. common=3, multi=2,2 ->結局6,6
            中で読み込んで判定取るか、かけられた数を残しておくか
            -->前者の方がわかりやすそう？
            
        common base type.
        existing denominator: [13]
        denominator: 13
        after_denominator: 39
        fractions: [1/13, 6/13]
        """
        # まんまかければいいやつ
        prime_numbers = [2, 3, 5, 7, 11, 13]
        shuffle(prime_numbers)
        fractions = []
        if random() < 0.4:
            print("prime base type.")
            for _ in range(selected_fraction_number):
                denominator_base = prime_numbers.pop()
                denominator_index = randint(1, 2)
                denominator = denominator_base ** denominator_index
                numerator = denominator - randint(1, denominator-1)
                fraction = sy.Rational(numerator, denominator)
                fractions.append(fraction)          
        # 共通因数を見抜くやつ
        # よくわからんエラー
        # 反応してないexisting
        else:
            print("common base type.")
            common_denominator_base = prime_numbers.pop()
            for _ in range(selected_fraction_number):
                number_for_multiplication = randint(1, 3)
                denominator = common_denominator_base * number_for_multiplication
                if fractions:
                    existing_denominator = [fraction.denominator for fraction in fractions]
                    if denominator in existing_denominator:
                        print(f"existing denominator: {existing_denominator}")
                        print(f"denominator: {denominator}")
                        denominator *= randint(2, 3)
                        print(f"after_denominator: {denominator}")
                numerator = randint(1, denominator-1)
                # ここで結局約分という？
                """
                numeratorが悪さしてそう
                ->約分できない数をかけることで、約分を事前に防ぐ？
                全体が既約分数でなければならない？
                """
                fraction = sy.Rational(numerator, denominator, gcd=1)
                fractions.append(fraction)
        print(f"fractions: {fractions}")
        shuffle(fractions)
        latex_answer = self._fractions_to_latex_answer(fractions)
        latex_problem = self._fractions_to_latex_problem(fractions)
        return latex_answer, latex_problem
    
    def _fractions_to_latex_problem(self, numbers):
        """分数からlatex形式の問題を出力

        Args:
            numbers (list): 分数が格納されたリスト
        
        Returns:
            latex_problem (str): latex形式で記述された問題
        """
        latex_problem = ""
        for number in numbers:
            latex_problem += f"{sy.latex(number)}, "
        latex_problem = latex_problem.rstrip(", ")
        return latex_problem
    
    def _fractions_to_latex_answer(self, numbers):
        """分数から共通分母に揃えられたlatex形式の解答を出力
        
        Args:
            numbers (list): 分数が格納されたリスト
        
        Returns:
            latex_answer (str): latex形式で記述された解答
        
        Raises:
            TypeError: 渡された数がsy.Rationalでない、あるいは変換できず、denominator属性が読み取れない時に挙上
        """
        denominator_list = []
        for number in numbers:
            if isinstance(number, sy.Rational):
                denominator_list.append(number.denominator)
            else:
                TypeError(f"cannot read denominator in {number} in {numbers}.")
        lcm = sy.ilcm(*denominator_list)
        latex_answer = ""
        for number in numbers:
            number_for_multiplication = lcm / number.denominator
            new_numerator = number.numerator * number_for_multiplication
            new_denominator = number.denominator * number_for_multiplication
            common_denominator_number = sy.Rational(new_numerator, new_denominator, gcd=1)
            number_latex = sy.latex(common_denominator_number)
            latex_answer += f"{number_latex}, "
        latex_answer = latex_answer.rstrip(", ")
        return latex_answer
    
from random import choice

import sympy as sy

class CommonDenominatorProblem:
    """通分の問題を出力する
    
    Attributes:
        _fraction_type_list (list): 問題に使用される分数の候補が格納されたリスト
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
        if selected_fraction_type == "proper_fraction":
            latex_answer, latex_problem = self._make_proper_fraction_problem()
        elif selected_fraction_type == "improper_fraction":
            latex_answer, latex_problem = self._make_improper_fraction_problem()
        elif selected_fraction_type == "mixed_fraction":
            latex_answer, latex_problem = self._make_mixed_fraction_problem()
        else:
            raise ValueError(f"selected_fraction_type is '{selected_fraction_type}'. This may be wrong.")

        return latex_answer, latex_problem
    
    def _make_proper_fraction_problem(self):
        """真分数の約分問題を出力
        
        Returns:
            latex_answer (str): latex形式で記述された解答
            latex_problem (str): latex形式で記述された問題
        
        Developing:
            まんまかければいいやつと、共通因数みていいかんじにかけるやつの2タイプ
            ↑をそこそこの割合で出力させたい
        """
    
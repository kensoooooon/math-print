from random import choice, randint, random
from typing import NamedTuple

import sympy as sy


class Elementary5SectorWithFigureProblem:
    """図表がついた扇形の面積を求める問題を出力
    
    Attributes:
        _problem_type_list (list): 選択された問題タイプが格納されている
        selected_problem_type (str): 選択された問題形式
        latex_answer (str): latex形式で記述された問題
        sector (Sector): 扇形のステータス
    
    Developing:
        ・一律で扇形を表示していた中2用とは異なり、そもそもステータス自体が共通のものではなくなっている
        ・それに伴い、選択された問題形式の扱いも少し変わると思われる
            選択された問題形式は変わらずに、ステータスを場合によって切り替える？
    """
    def __init__(self, **settings):
        """
        Args:
            settings (dict): 問題の設定
        """
        sy.init_printing(order='grevlex')
        self._problem_type_list = settings["problem_type_list"]
        selected_problem_type = choice(self._problem_type_list)
        self.selected_problem_type = selected_problem_type
        if selected_problem_type == "standard_sector":
            self.latex_answer, self.sector = self._make_standard_sector_problem()
        elif selected_problem_type == "in_rugby":
            self.latex_answer, self.one_side_of_square_str = self._make_in_rugby_problem()
        elif selected_problem_type == "out_rugby":
            self.latex_answer, self.one_side_of_square_str = self._make_out_rugby_problem()
    
    def _make_standard_sector_problem(self):
        """標準的な扇形問題の解答と描画に必要な情報を返す
        
        Returns:
            latex_answer (str): latex形式で記述された解答
            sector (Sector): 扇形のステータス
        """
        def decide_sector_status():
            """扇形のステータスを決定する
            
            Return:
                sector (Sector): 扇形のステータスを内包している
            """
            class Sector(NamedTuple):
                """扇形のステータスを内包する
                
                Attributes:
                    radius (str): 扇形の半径
                    area (str): 扇形の面積
                    central_angle(str): 扇形の中心角
                """
                radius: str
                area: str
                central_angle: str

            if random() > 0.5:
                central_angle = 30 * randint(1, 11)
            else:
                central_angle = 45 * randint(1, 7)
            ratio_by_circle = sy.Rational(central_angle, 360)
            radius = ratio_by_circle.denominator
            area = str(sy.Integer(radius**2) * sy.Rational(central_angle, 360) * 3.14).replace("0", "")
            central_angle = str(central_angle)
            radius = str(radius)
            sector = Sector(radius=radius, area=area, central_angle=central_angle)
            return sector     
        sector = decide_sector_status()
        latex_answer = f"\( {sy.latex(sector.area)} \\mathrm{{ cm^2 }} \)".replace("\\", "\\\\")
        return latex_answer, sector
    
    def _make_in_star_problem(self):
        """星型の内側の面積を求める問題の解答と描画に必要な情報を返す
        
        Returns:
            latex_answer (str): latex形式で記述された解答
            one_side_of_square (str): 星型を作る正方形の一辺
        
        Note:
            値の複雑化を防ぐために、正方形の一辺を2の倍数に限定している。必要があれば複数候補からの選出等に切り替え
        """
        one_side_of_square = randint(1, 10) * 2
        one_side_of_square_str = str(one_side_of_square)
        square_area = sy.Integer(one_side_of_square ** 2)
        inner_sector_total_area = 3.14 * ((one_side_of_square / 2) ** 2)
        area = square_area - inner_sector_total_area
        area_str = sy.latex(area).replace("0", "").rstrip(".")
        latex_answer = f"\( {sy.latex(area_str)} \\mathrm{{ cm^2 }} \)".replace("\\", "\\\\")
        return latex_answer, one_side_of_square_str
    
    def _make_out_star_problem(self):
        """星型の外側の面積を求める問題の解凍と描画に必要な情報を返す
        
        Returns:
            latex_answer (str): latex形式で記述された解答
            one_side_of_square (str): 星型を作る正方形の一辺

        Note:
            値の複雑化を防ぐために、正方形の一辺を2の倍数に限定している。必要があれば複数候補からの選出等に切り替え
        """
        one_side_of_square = randint(1, 10) * 2
        one_side_of_square_str = str(one_side_of_square)
        inner_sector_total_area = 3.14 * ((one_side_of_square / 2) ** 2)
        area = inner_sector_total_area
        area_str = sy.latex(area).replace("0", "").rstrip(".")
        latex_answer = f"\( {sy.latex(area_str)} \\mathrm{{ cm^2 }} \)".replace("\\", "\\\\")
        return latex_answer, one_side_of_square_str
    
    def _make_in_rugby_problem(self):
        """ラグビーボール型の内側の面積を求める問題の解答と描画に必要な情報を返す

        Returns:
            latex_answer (str): latex形式で記述された解答
            one_side_of_square_str (str): ラグビーボール型を作る正方形の一辺
        
        Note:
            値の複雑化を防ぐために、正方形の一辺を5の倍数に限定している。必要があれば複数候補からの選出等に切り替え
        """
        one_side_of_square = randint(1, 10) * 5
        one_side_of_square_str = str(one_side_of_square)
        sector_area = (one_side_of_square ** 2) * 3.14 *  sy.Rational(90, 360)
        triangle_area = sy.Rational(1, 2) * (one_side_of_square) ** 2
        area = 2 * (sector_area - triangle_area)
        area_str = sy.latex(area).replace("0", "").rstrip(".")
        latex_answer = f"\( {sy.latex(area_str)} \\mathrm{{ cm^2 }} \)".replace("\\", "\\\\")
        return latex_answer, one_side_of_square_str
    
    def _make_out_rugby_problem(self):
        """ラグビーボール型の外側の面積を求める問題の解答と、描画に必要な情報を返す
        
        Returns:
            latex_answer (str): latex形式で記述された解答
            one_side_of_square_str (str): ラグビーボール型を作る正方形の一辺
        
        Note:
            値の複雑化を防ぐために、正方形の一辺を5の倍数に限定している。必要があれば複数候補からの選手等に切り替え
        """
        one_side_of_square = randint(1, 10) * 5
        one_side_of_square_str = str(one_side_of_square)
        square_area = sy.Integer(one_side_of_square ** 2)
        sector_area = sy.Float(3.14) * (one_side_of_square ** 2) * sy.Rational(90, 360)
        triangle_area = sy.Rational(1, 2) * (one_side_of_square ** 2)
        in_rugby_area = 2 * (sector_area - triangle_area)
        out_rugby_area = square_area - in_rugby_area
        area_str = sy.latex(out_rugby_area).replace("0", "").rstrip(".")
        latex_answer = f"\( {sy.latex(area_str)} \\mathrm{{ cm^2 }} \)".replace("\\", "\\\\")
        return latex_answer, one_side_of_square_str
    
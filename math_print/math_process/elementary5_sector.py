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
    """
    def __init__(self, **settings):
        """
        Args:
            settings (dict): 問題の設定が格納されている
        
        Raises:
            ValueError: 問題の設定に存在しないものが選択されたときに挙上
        """
        sy.init_printing(order='grevlex')
        self._problem_type_list = settings["problem_type_list"]
        selected_problem_type = choice(self._problem_type_list)
        self.selected_problem_type = selected_problem_type
        if selected_problem_type == "standard_sector":
            self.latex_answer, self.sector = self._make_standard_sector_problem()
        elif selected_problem_type == "in_star":
            self.latex_answer, self.one_side_of_square_str = self._make_in_star_problem()
        elif selected_problem_type == "out_star":
            self.latex_answer, self.one_side_of_square_str = self._make_out_star_problem()
        elif selected_problem_type == "in_rugby":
            self.latex_answer, self.one_side_of_square_str = self._make_in_rugby_problem()
        elif selected_problem_type == "out_rugby":
            self.latex_answer, self.one_side_of_square_str = self._make_out_rugby_problem()
        elif selected_problem_type == "in_seed_and_flower":
            self.latex_answer, self.radius_of_quarter_circle_str = self._make_in_seed_and_flower_problem()
        else:
            raise ValueError(f"'selected_problem_type' is {selected_problem_type}. This may be wrong.")
    
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
        latex_answer = self._area_value_to_latex_answer(sector.area)
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
        in_star_area = square_area - inner_sector_total_area
        latex_answer = self._area_value_to_latex_answer(in_star_area)
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
        out_star_area = 3.14 * ((one_side_of_square / 2) ** 2)
        latex_answer = self._area_value_to_latex_answer(out_star_area)
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
        in_rugby_area = 2 * (sector_area - triangle_area)
        latex_answer = self._area_value_to_latex_answer(in_rugby_area)
        return latex_answer, one_side_of_square_str
    
    def _make_out_rugby_problem(self):
        """ラグビーボール型の外側の面積を求める問題の解答と、描画に必要な情報を返す
        
        Returns:
            latex_answer (str): latex形式で記述された解答
            one_side_of_square_str (str): ラグビーボール型を作る正方形の一辺
        
        Note:
            値の複雑化を防ぐために、正方形の一辺を5の倍数に限定している。必要があれば候補の拡大
        """
        one_side_of_square = randint(1, 10) * 5
        one_side_of_square_str = str(one_side_of_square)
        square_area = sy.Integer(one_side_of_square ** 2)
        sector_area = sy.Float(3.14) * (one_side_of_square ** 2) * sy.Rational(90, 360)
        triangle_area = sy.Rational(1, 2) * (one_side_of_square ** 2)
        in_rugby_area = 2 * (sector_area - triangle_area)
        out_rugby_area = square_area - in_rugby_area
        latex_answer = self._area_value_to_latex_answer(out_rugby_area)
        return latex_answer, one_side_of_square_str
    
    def _make_in_seed_and_flower_problem(self):
        """四分円の中に配置された種と花型の内側の面積を求める問題の解答と、描画に必要な情報を返す
        
        Returns:
            latex_answer (str): latex形式で記述された解答
            radius_of_quarter_circle_str (str): 四分円の半径
        
        Note:
            値の複雑化を防ぐために、四分円の半径を偶数に限定している。必要があれば候補の拡大

        Developing:
            quarter_circle_area: 28.2600000000000
            triangle_area: 18
            in_seed_and_flower_area: 10.2600000000000
            latex_answer: \\( \\mathtt{\\text{1.26}} \\mathrm{ cm^2 } \\)
            が発生。途中のゼロを消してしまっている。
            ->正規表現かなにかに切り替えるべき？
            ->
            def decimal_normalize(f):
                text = str(f)
                while True:
                    if ("." in text and text[-1] == "0") or (text[-1] == "."):
                        text = text[:-1]
                        continue
                    break
                return text
            がある。大体全部の面積がこれを必要としているので、self中で関数化してしまうのがよさそう
        """
        radius_of_quarter_circle = randint(1, 20) * 2
        radius_of_quarter_circle_str = str(radius_of_quarter_circle)
        quarter_circle_area = sy.Float(3.14) * (radius_of_quarter_circle **2) * sy.Rational(90, 360)
        triangle_area = sy.Rational(1, 2) * (radius_of_quarter_circle ** 2)
        in_seed_and_flower_area = quarter_circle_area - triangle_area
        latex_answer = self._area_value_to_latex_answer(in_seed_and_flower_area)
        return latex_answer, radius_of_quarter_circle_str    
    
    def _area_value_to_latex_answer(self, area_value):
        """面積の値を受け取って、小数点以下で連続する0を切り捨てて、単位がついた面積の文字列を返す

        Args:
            area_value (Union[sy.Integer, sy.Float]): 計算で出てきた面積
        Returns:
            latex_area_with_unit (str): latex形式で記述された単位付きの面積
        """
        area_text = str(area_value)
        while True:
            if ("." in area_text and area_text[-1] == "0") or (area_text[-1] == "."):
                area_text = area_text[:-1]
                continue
            break                
        latex_area_with_unit = f"\( {sy.latex(area_text)} \\mathrm{{ cm^2 }} \)".replace("\\", "\\\\")
        return latex_area_with_unit
    
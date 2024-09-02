from random import choice, randint, random, sample
from typing import Dict, List, NamedTuple, Optional, Tuple, Union

import sympy as sy


class AreaWithLinearFunction:
    """中学2年生用の、直線で囲まれた面積の問題と解答を出力
    
    Attributes:
        latex_answer (str): LaTeX形式を前提とした解答
        latex_problem (str): LaTeX形式を前提とした問題
    """
    class Point(NamedTuple):
        x: Union[sy.Integer, sy.Rational]
        y: Union[sy.Integer, sy.Rational]
        label: Optional[str] = None
        
    class LinearFunction(NamedTuple):
        """1次関数の通る点と式を格納

        Args:
            x1, y1, x2, y2 (str): 1次関数が通る2点
            latex (str): latex形式で記述された1次関数の式
        """
        x1: str
        y1: str
        x2: str
        y2: str
        latex: str
    
    def __init__(self, **settings: Dict):
        sy.init_printing(order='grevlex')
        selected_problem_type = choice(settings["problem_types"])
        if selected_problem_type == "one_side_on_axis":
            self.latex_answer, self.latex_problem, self.linear_function1, self.linear_function2, self.linear_function3 = self._make_one_side_on_axis_problem()
        elif selected_problem_type == "no_side_on_axis":
            self.latex_answer, self.latex_problem, self.linear_function1, self.linear_function2, self.linear_function3 = self._make_no_side_on_axis_problem()
    
    def _make_one_side_on_axis_problem(self):
        """3辺のうち、1辺が軸上にある三角形の面積を求める問題、解答、描画用情報の作成
        
        Returns:
            latex_answer (str): latex混じりで記述された解答
            latex_problem (str): latex混じりで記述された問題
            linear_function1, linear_function2, linear_function3 (sy.Eq): 三角形を作る1次関数
        """
        def make_three_points() -> Tuple[str, self.Point, self.Point, self.Point]:
            """3点のうち、いずれか2点が軸上に存在する点を作成する

            Returns:
                Tuple[zero_coordinate, self.Point, self.Point, self.Point]: どちらに0を取っているかとう表示+条件を満たす3点
            """
            zero_coordinate = choice(["x", "y"])
            if zero_coordinate == "x":
                x1 = 0
                y1 = self._random_integer(min_num=3, max_num=12, removing_zero=False)  # 絶対値3以上12以下
                x2 = 0
                y2 = self._random_integer(min_num=-12, max_num=-3, removing_zero=False)  # 絶対値3以上12以下
                x3 = self._random_integer(min_num=3, max_num=12, removing_zero=True) * choice([1, -1])  # 絶対値3以上12以下
                y3 = self._random_integer(min_num=-12, max_num=12, removing_zero=False)  # 絶対値3以上12以下
            elif zero_coordinate == "y":
                x1 = self._random_integer(min_num=3, max_num=12, removing_zero=False)  # 絶対値3以上12以下
                y1 = 0
                x2 = self._random_integer(min_num=-12, max_num=-3, removing_zero=False)  # 絶対値3以上12以下
                y2 = 0
                x3 = self._random_integer(min_num=3, max_num=12, removing_zero=True) * choice([1, -1])  # 絶対値3以上12以下
                y3 = self._random_integer(min_num=-12, max_num=12, removing_zero=True)  # 絶対値3以上12以下
            p1_on_axis = self.Point(x1, y1)
            p2_on_axis = self.Point(x2, y2)
            p3_not_on_axis = self.Point(x3, y3)
            return zero_coordinate, p1_on_axis, p2_on_axis, p3_not_on_axis
        
        zero_coordinate, p1_on_axis, p2_on_axis, p3_not_on_axis = make_three_points()
        linear_function_without_axis1 = self._calculate_linear_function_by_two_points(p1_on_axis, p3_not_on_axis)
        linear_function_without_axis2 = self._calculate_linear_function_by_two_points(p2_on_axis, p3_not_on_axis)
        line_in_parallel_with_y_axis = self._calculate_linear_function_by_two_points(p1_on_axis, p2_on_axis)
        latex_problem = f"2直線{linear_function_without_axis1.latex}…①, {linear_function_without_axis2.latex}…②が、"
        latex_problem += "1点で交わっている。\n"
        latex_problem += "①と②の交点をA,"
        if zero_coordinate == "x":
            latex_problem += "①とy軸の交点をB, ②とy軸の交点をCとするとき、\n"
        elif zero_coordinate == "y":
            latex_problem += "①とx軸の交点をB, ②とx軸の交点をCとするとき、\n"
        triangle_ABC = self._latex_maker("\\triangle ABC")
        latex_problem += f"{triangle_ABC}の面積を求めよ。"
        cross_point_A = self._latex_maker(f'({p3_not_on_axis.x}, {p3_not_on_axis.y})')
        latex_answer = f"交点Aは{cross_point_A}となる。\n"
        cross_point_B = self._latex_maker(f'({p1_on_axis.x}, {p1_on_axis.y})')
        cross_point_C = self._latex_maker(f'({p2_on_axis.x}, {p2_on_axis.y})')
        latex_answer += f"また、交点Bは{cross_point_B}, 交点Cは{cross_point_C}となる。\n"
        if zero_coordinate == 'x':
            width = sy.Abs(p1_on_axis.y - p2_on_axis.y)
            height = sy.Abs(p3_not_on_axis.x)
        elif zero_coordinate == 'y':
            width = sy.Abs(p1_on_axis.x - p2_on_axis.x)
            height = sy.Abs(p3_not_on_axis.y)
        width_latex = self._latex_maker(width)
        height_latex = self._latex_maker(height)
        latex_answer += f"よって、{triangle_ABC}は底辺が{width_latex}, 高さが{height_latex}の三角形となるため、"
        area = sy.Rational(1, 2) * width * height
        area_to_check = self._calculate_area_by_three_points(p1_on_axis, p2_on_axis, p3_not_on_axis)
        if area != area_to_check:
            raise ValueError(f"area is {area}, area_to_check is {area_to_check}. These two values must be equal.")
        area_latex = self._latex_maker(area)
        latex_answer += f"面積は{area_latex}となる。" 
        return latex_answer, latex_problem, linear_function_without_axis1, linear_function_without_axis2, line_in_parallel_with_y_axis
    
    def _make_no_side_on_axis_problem(self):
        """3辺のうち、いずれの辺も軸上に存在しない三角形の問題、解答、描画用情報の作成

        Returns:
            latex_answer (str): latex混じりで記述された解答
            latex_problem (str): latex混じりで記述された問題
            linear_function1, linear_function2, linear_function3 (sy.Eq): 三角形を作る1次関数        
        """
        
        def make_three_points() -> Tuple[self.Point, self.Point, self.Point]:
            """3点のうち、2点は軸上に存在しない点を作成する

            Returns:
                Tuple[self.Point, self.Point, self.Point]: x,y軸上に2点以上存在していない点
            
            Note:
                描画である程度距離を離すため、象限ごとに点を選択する方式を採用。
                また、描画範囲を10pixelから5pixelに変更し、与えられる座標の幅を拡大
            """
            quadrants = {
                1: lambda: (sy.Integer(choice(range(3, 13))), sy.Integer(choice(range(3, 13)))),
                2: lambda: (sy.Integer(choice(range(-12, -2))), sy.Integer(choice(range(3, 13)))),
                3: lambda: (sy.Integer(choice(range(-12, -2))), sy.Integer(choice(range(-12, -2)))),
                4: lambda: (sy.Integer(choice(range(3, 13))), sy.Integer(choice(range(-12, -2))))
            }
            
            while True:
                selected_quadrants = sample(list(quadrants.keys()), 3)
                points = [quadrants[q]() for q in selected_quadrants]
                x1, y1 = points[0]
                x2, y2 = points[1]
                x3, y3 = points[2]
                slope1 = sy.Rational(y2 - y1, x2 - x1)
                slope2 = sy.Rational(y3 - y2, x3 - x2)
                if slope1 != slope2:
                    if (len(set((x1, x2, x3))) == 3) and (len(set((y1, y2, y3))) == 3):
                        break
            x1, x2, x3 = sy.Integer(x1), sy.Integer(x2), sy.Integer(x3)
            y1, y2, y3 = sy.Integer(y1), sy.Integer(y2), sy.Integer(y3)
            p1 = self.Point(x1, y1, '交点C')
            p2 = self.Point(x2, y2, '交点A')
            p3 = self.Point(x3, y3, '交点B')
            return p1, p2, p3
        
        def check_points_to_cut(point1: self.Point, point2: self.Point, point3: self.Point) -> Tuple[str, self.Point, self.Point]:
            """与えられた3点から切断方向、切断の基準となる点、切断先となる点を求める
            
            Args:
                point1 (self.Point): 三角形を作る点その1
                point2 (self.Point): 三角形を作る点その2
                point3 (self.Point): 三角形を作る点その3
            
            Returns:
                direction (str): 切断方向(上下左右のいずれか)
                standard_point (self.Point): 切断の基準となる点
                cut_point (self.Point): 切断先の点
            """
            
            def cut_parallel_to_x_axis(point1, point2, point3) -> Tuple[str, self.Point, self.Point]:
                """
                Args:
                    point1 (self.Point): 三角形を作る点その1
                    point2 (self.Point): 三角形を作る点その2
                    point3 (self.Point): 三角形を作る点その3
            
                Returns:
                    direction (str): 切断方向(上下左右のいずれか)
                    standard_point (self.Point): 切断の基準となる点
                    cut_point (self.Point): 切断先の点
                """
                points_sorted_by_y = sorted([point1, point2, point3], key=lambda point: point.y)
                standard_point_to_cut = points_sorted_by_y[1]
                xs, ys = standard_point_to_cut.x, standard_point_to_cut.y
                another_point1, another_point2 = points_sorted_by_y[0], points_sorted_by_y[2]
                x1, y1 = another_point1.x, another_point1.y
                x2, y2 = another_point2.x, another_point2.y
                x = sy.Symbol('x', real=True)
                a = sy.Rational(y2 - y1, x2 - x1)
                b = y1 - sy.Rational(y2 - y1, x2 - x1) * x1
                y_of_cut_point = ys
                x_of_cut_point = sy.Rational(y_of_cut_point - b, a)
                if xs < x_of_cut_point:
                    direction = "右方向"
                elif xs > x_of_cut_point:
                    direction = "左方向"
                else:
                    raise ValueError(f"xs must not be equal to x_of_cut_point.")
                cut_point = self.Point(x_of_cut_point, y_of_cut_point)
                standard_point = standard_point_to_cut
                return direction, standard_point, cut_point

            def cut_parallel_to_y_axis(point1, point2, point3) -> Tuple[str, self.Point, self.Point]:
                points_sorted_by_x = sorted([point1, point2, point3], key=lambda point: point.x)
                standard_point_to_cut = points_sorted_by_x[1]
                xs, ys = standard_point_to_cut.x, standard_point_to_cut.y
                another_point1, another_point2 = points_sorted_by_x[0], points_sorted_by_x[2]
                x1, y1 = another_point1.x, another_point1.y
                x2, y2 = another_point2.x, another_point2.y
                x = sy.Symbol('x', real=True)
                a = sy.Rational(y2 - y1, x2 - x1)
                b = y1 - sy.Rational(y2 - y1, x2 - x1) * x1
                x_of_cut_point = xs
                y_of_cut_point = sy.Rational(a * xs + b)
                if ys < y_of_cut_point:
                    direction = "上方向"
                elif ys > y_of_cut_point:
                    direction = "下方向"
                else:
                    raise ValueError(f"ys must not be equal to y_of_cut_point.")
                cut_point = self.Point(x_of_cut_point, y_of_cut_point)
                standard_point = standard_point_to_cut
                return direction, standard_point, cut_point

            if random() > 0.5:
                direction, standard_point, cut_point = cut_parallel_to_x_axis(point1, point2, point3)
            else:
                direction, standard_point, cut_point = cut_parallel_to_y_axis(point1, point2, point3)
            return direction, standard_point, cut_point
        
        def calculate_common_base_length(cut_direction: str, standard_point: self.Point, cut_point: self.Point) -> sy.Rational:
            """共通の底辺の長さを計算する

            Args:
                cut_direction (str): 切断方向
                standard_point (self.Point): 切断の基準点
                cut_point (self.Point): 切断先の点
            
            Returns:
                (sy.Rational): 共通の底辺
            """
            if (cut_direction == "右方向") or (cut_direction == "左方向"):
                return sy.Abs(cut_point.x - standard_point.x)
            elif (cut_direction == "上方向") or (cut_direction == "下方向"):
                return sy.Abs(cut_point.y - standard_point.y)

        def calculate_heights(cut_direction: str, point1: self.Point, point2: self.Point, point3: self.Point, *, standard_point: self.Point) -> Tuple[sy.Rational, sy.Rational]:
            """切断した三角形の高さを計算する
            
            Args:
                cut_direction (str): 切断方向
                point1, point2, point3 (self.Point): 三角形を構成する3点
                standard_point (self.Point): 切断の基準となった点
            
            Returns:
                height1, height2 (sy.Rational): 三角形の面積を求めるための高さとして扱われる値
            """
            another_points = []
            if (point1.x != standard_point.x) and (point1.y != standard_point.y):
                another_points.append(point1)
            if (point2.x != standard_point.x) and (point2.y != standard_point.y):
                another_points.append(point2)
            if (point3.x != standard_point.x) and (point3.y != standard_point.y):
                another_points.append(point3)
            if len(another_points) != 2:
                raise ValueError(f"length of 'another_points' must be 2. let's check {another_points}.")
            another_point1, another_point2 = another_points
            if (cut_direction == "右方向") or (cut_direction == "左方向"):
                height1 = sy.Abs(another_point1.y - standard_point.y)
                height2 = sy.Abs(another_point2.y - standard_point.y)
            elif (cut_direction == "上方向") or (cut_direction == "下方向"):
                height1 = sy.Abs(another_point1.x - standard_point.x)
                height2 = sy.Abs(another_point2.x - standard_point.x)
            return height1, height2

        def calculate_triangle_areas(common_base: sy.Rational, height1: sy.Rational, height2: sy.Rational) -> Tuple[sy.Rational, sy.Rational]:
            """分割した三角形の面積を個別に求める
            
            Args:
                common_base (sy.Rational): 共通の底辺
                height1, height2(sy.Rational): 三角形の高さ
            
            Returns:
                area1, area2 (sy.Rational): 計算された面積
            """
            area1 = (common_base * height1) * sy.Rational(1, 2)
            area2 = (common_base * height2) * sy.Rational(1, 2)
            return area1, area2

        p1, p2, p3 = make_three_points()
        linear_function1 = self._calculate_linear_function_by_two_points(p1, p2)
        linear_function2 = self._calculate_linear_function_by_two_points(p2, p3)
        linear_function3 = self._calculate_linear_function_by_two_points(p3, p1)
        latex_problem = f"3直線{linear_function1.latex}…①, {linear_function2.latex}…②, {linear_function3.latex}…③が一点で交わっている。\n"
        latex_problem += f"①と②の交点をA, ②と③の交点をB, ③と①の交点をCとするとき、"
        triangle_ABC = self._latex_maker("\\triangle ABC")
        latex_problem += f"{triangle_ABC}の面積を求めよ。"
        cross_point_A = self._latex_maker(f'({p2.x}, {p2.y})')
        cross_point_B = self._latex_maker(f'({p3.x}, {p3.y})')
        cross_point_C = self._latex_maker(f'({p1.x}, {p1.y})')
        latex_answer = f"それぞれの交点を求めると、交点Aは{cross_point_A}, 交点Bは{cross_point_B}, 交点Cは{cross_point_C}となる。\n"
        cut_direction, standard_point, cut_point = check_points_to_cut(p1, p2, p3)
        latex_answer += f"ここで、{standard_point.label}から{cut_direction}に向けて線を伸ばしていくと、\n"
        x_of_cut_point = sy.latex(cut_point.x)
        y_of_cut_point = sy.latex(cut_point.y)
        cut_point_latex = self._latex_maker(f'({x_of_cut_point}, {y_of_cut_point})')
        latex_answer += f"{cut_point_latex}で残りの辺と交わる。\n"
        latex_answer += "ここを境目に三角形を2つに分けると、それぞれの三角形は、\n" 
        common_base = calculate_common_base_length(cut_direction, standard_point, cut_point)
        common_base_latex = self._latex_maker(common_base)
        height1, height2 = calculate_heights(cut_direction, p1, p2, p3 , standard_point=standard_point)
        height1_latex = self._latex_maker(height1)
        height2_latex = self._latex_maker(height2)
        latex_answer += f"底辺が{common_base_latex}, 高さがそれぞれ{height1_latex}, {height2_latex}の三角形となり、\n"
        area1, area2 = calculate_triangle_areas(common_base, height1, height2)
        area1_latex = self._latex_maker(area1)
        area2_latex = self._latex_maker(area2)
        latex_answer += f"面積はそれぞれ{area1_latex}, {area2_latex}となる。\n"
        total_area = area1 + area2
        total_area_to_check = self._calculate_area_by_three_points(p1, p2, p3)
        if total_area != total_area_to_check:
            raise ValueError(f"sum of area1({area1}) and area2({area2}) must be equal to total_area_to_check({total_area_to_check}).")
        total_area_latex = self._latex_maker(total_area)
        latex_answer += f"これらの面積を合わせると、答えは{total_area_latex}となる。"
        return latex_answer, latex_problem, linear_function1, linear_function2, linear_function3
    
    def _random_integer(self, min_num: int=-7, max_num: int=7, *, removing_zero: Optional[bool]=None) -> sy.Integer:
        """指定された条件を満たすランダムな整数を出力
        
        Args:
            min_num (int): 出力される整数の最小値。デフォルトは-7
            max_num (int): 出力される整数の最大値。デフォルトは7
            removing_zero (Optional[bool]): 0を含むか否か。デフォルトはNone(どちらでも良い)
        
        Returns:
            integer (sy.Integer): 指定された条件を満たす整数
        """
        if min_num >= max_num:
            raise ValueError(f"'max_num' must be more than 'min_num'. Now, 'min_num' is {min_num}, and 'max_num' is {max_num}.")
        numbers = list(range(min_num, max_num+1))
        if removing_zero is None:
            removing_zero = choice((True, False))
        if removing_zero and (0 in numbers):
            numbers.remove(0)
        integer = sy.Integer(choice(numbers))
        return integer
    
    def _calculate_linear_function_by_two_points(self, p1: Point, p2: Point, /) -> LinearFunction:
        """与えられた2点から直線の式を計算する

        Args:
            p1 (Point): 通る点その1
            p2 (Point): 通る点その2

        Returns:
            linear_function (sy.core.relational.Equality): 1次関数
        """
        x = sy.Symbol("x", real=True)
        y = sy.Symbol("y", real=True)
        if p1.x == p2.x:
            line_in_parallel_with_y_axis = sy.Eq(x, p1.x)
            line_in_parallel_with_y_axis_latex = self._latex_maker(line_in_parallel_with_y_axis)
            linear_function = self.LinearFunction(
                x1 = str(p1.x), y1 = str(p1.y),
                x2 = str(p2.x), y2 = str(p2.y),
                latex= line_in_parallel_with_y_axis_latex
            )
        else:
            a = sy.Rational(p2.y - p1.y, p2.x - p1.x)
            right = sy.simplify(a * (x - p1.x) + p1.y)
            linear_function_equation = sy.Eq(y, right)
            linear_function_latex = self._latex_maker(linear_function_equation)
            linear_function = self.LinearFunction(
                x1 = str(p1.x), y1 = str(p1.y),
                x2 = str(p2.x), y2 = str(p2.y),
                latex = linear_function_latex
            )
        return linear_function

    def _calculate_area_by_three_points(self, p1: Point, p2: Point, p3: Point) -> Union[sy.Integer, sy.Rational]:
        """指定された3点を通る三角形の面積を計算する
        
        Args:
            p1, p2, p3 (Point): 指定された3点
        
        Returns:
            area (Union[sy.Integer, sy.Rational]): 計算された面積
        """
        area = sy.Rational(1, 2) * sy.Abs((p1.x - p3.x) * (p2.y - p3.y) - (p2.x - p3.x) * (p1.y - p3.y))
        if area <= 0:
            raise ValueError(f"area must be more than 0. Let's check each value of Point: {p1}, {p2}, {p3}")
        return area
    
    def _latex_maker(self, formula: Union[sy.Equality, str, sy.Rational, sy.Integer]) -> str:
        """与えられた式をLaTex形式にカッコ込で変形する。すでにlatex形式である場合は、カッコのみ追加する
        
        Args:
            formula (Union[sy.Equality, str, sy.Rational, sy.Integer]): y = 3x - 4や、y = 0などの公式。あるいは整数や分数などのシンボル
        
        Returns:
            latex (str): LaTex形式とカッコが複合された文字列
        """
        if isinstance(formula, str):
            latex = f"\( {formula} \)"
        else:
            latex = f"\( {sy.latex(formula)} \)"
        return latex
    
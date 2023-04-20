"""直線と平面の位置関係を問う問題を出力する

直線と直線、直線と平面、平面と平面の位置関係のいずれかを設定に応じて出力する。
    ・直線と直線
    平行、ねじれ、垂直のいずれかを問う
    ・直線と平面
    ふくまれる、垂直に交わる、平行のいずれかを問う
    ・平面と平面
    垂直に交わる、平行のいずれかを問う
使用する立体は、直方体と三角柱

Developing:
    4/18
    ・問題と解答の出力がうまくいかないため、latex_answer, latex_problemをリストに変更
    
    4/19
    ・直線と平面の位置関係に着手
"""
from random import choice, random, randint

import sympy as sy


class LineAndFlatPositionalRelationship:
    """直線と平面の位置関係の問題と解答を出力
    
    Attributes:
        latex_answers (list): latex形式で記述された解答が3問分格納されたリスト
        latex_problems (list): latex形式で記述された問題が3問分格納されたリスト
        solid_body (str): 問題に使用される立体
    """
    def __init__(self, **settings):
        """初期設定
        
        Args:
            settings (dict): 問題に使用する各種設定を格納
        """
        problem_types = settings["used_problems"]
        selected_solid_body = choice(settings["used_solid_bodies"])
        if selected_solid_body == "quadrangular_prism":
            self.solid_body = "quadrangular_prism"
            self.latex_answers, self.latex_problems = self._make_quadrangular_prism_problem(problem_types)
        elif selected_solid_body == "triangular_prism":
            self.solid_body = "triangular_prism"
            self.latex_answers, self.latex_problems = self._make_triangular_prism_problem(problem_types)
        else:
            raise ValueError(f"'selected_solid_body' is {selected_solid_body}. This must be 'quadrangular_prism' or 'triangular_prism.")
    
    def _make_quadrangular_prism_problem(self, problem_types):
        """直方体を用いた直線と平面の位置関係の問題を作成

        Args:
            problem_types (list): 使用される問題(直線と直線, 直線と平面, 平面と平面)が格納されている

        Returns:
            latex_answers (list): latex形式で記述された解答が3問分格納されたリスト
            latex_problems (list): latex形式で記述された問題が3問分格納されたリスト
        
        Note:
            平行な辺は手動で指定している。
            垂直な辺は、辺とアルファベットを共有するものはすべて垂直である点を利用(eg. 辺AB->AD, AE, BC, BF)。
            ねじれの位置にある辺は、すべての辺のうち、平行でも垂直でもないものを差し引いて求めている。
        """
        latex_answers = []
        latex_problems = []
        for problem_number in range(1, 4):
            selected_problem_type = choice(problem_types)
            if selected_problem_type == "line_and_line":
                problem_checker = random()
                # parallel edge
                if problem_checker < 0.33:                        
                    parallel_edges_group = (
                        ["辺AB", "辺CD", "辺EF", "辺GH",],
                        ["辺AD", "辺BC", "辺EH", "辺FG",],
                        ["辺AE", "辺BF", "辺CG", "辺DH",],
                        )
                    selected_parallel_edges = choice(parallel_edges_group)
                    edge_used_for_problem = selected_parallel_edges.pop(randint(0, len(selected_parallel_edges) - 1))
                    remained_edges = ", ".join(selected_parallel_edges)
                    latex_answers.append(f"({problem_number}) {remained_edges}")
                    latex_problems.append(f"({problem_number}) {edge_used_for_problem}と平行な辺を答えなさい。")
                # skew edge
                elif 0.33 <= problem_checker < 0.66:
                    all_edges = [
                        "辺AB", "辺BC", "辺CD", "辺AD",
                        "辺AE", "辺BF", "辺CG", "辺DH",
                        "辺EF", "辺FG", "辺GH", "辺EH",
                    ]
                    edge_used_for_problem = choice(all_edges)
                    latex_problems.append(f"({problem_number}) {edge_used_for_problem}とねじれの位置にある辺を答えなさい。")
                    parallel_edges_group = (
                        ["辺AB", "辺CD", "辺EF", "辺GH",],
                        ["辺AD", "辺BC", "辺EH", "辺FG",],
                        ["辺AE", "辺BF", "辺CG", "辺DH",],
                        )
                    for parallel_edges in parallel_edges_group:
                        if edge_used_for_problem in parallel_edges:
                            parallel_edges_with_edge_used_for_problem = parallel_edges
                            break
                    edges_without_parallel = list(set(all_edges) - set(parallel_edges_with_edge_used_for_problem))
                    first_alphabet = edge_used_for_problem[1]
                    second_alphabet = edge_used_for_problem[2]
                    skew_edges = [edge for edge in edges_without_parallel if (first_alphabet not in edge) and (second_alphabet not in edge)]
                    latex_answers.append(f"({problem_number}) {', '.join(skew_edges)}")
                # vertical edge
                else:
                    all_edges = [
                        "辺AB", "辺BC", "辺CD", "辺AD",
                        "辺AE", "辺BF", "辺CG", "辺DH",
                        "辺EF", "辺FG", "辺GH", "辺EH",
                    ]
                    edge_used_for_problem = choice(all_edges)
                    latex_problems.append(f"({problem_number}) {edge_used_for_problem}と垂直に交わる辺を答えなさい。")
                    parallel_edges_group = (
                        ["辺AB", "辺CD", "辺EF", "辺GH",],
                        ["辺AD", "辺BC", "辺EH", "辺FG",],
                        ["辺AE", "辺BF", "辺CG", "辺DH",],
                        )
                    for parallel_edges in parallel_edges_group:
                        if edge_used_for_problem in parallel_edges:
                            parallel_edges_with_edge_used_for_problem = parallel_edges
                            break
                    edges_without_parallel = list(set(all_edges) - set(parallel_edges_with_edge_used_for_problem))
                    first_alphabet = edge_used_for_problem[1]
                    second_alphabet = edge_used_for_problem[2]
                    vertical_edges = [edge for edge in edges_without_parallel if (first_alphabet in edge) or (second_alphabet in edge)]
                    latex_answers.append(f"({problem_number}) {', '.join(vertical_edges)}")
            elif selected_problem_type == "line_and_flat":
                """
                Developing:
                    直線と平面の位置関係は、"ふくまれる", "交わる", "交わらない"の3種。
                    これを問題用に考えると、
                        "ふくまれる"はとりあえず除外？ABCDなら、AB,BC,CD,DAで答えやすいから？
                            ↑3:3で対比が取れてないと気持ち悪いし、もしかしたらわかっていない人もいるかもなので、追加
                        "交わる"は実質垂直に交わる
                        "交わらない"は平行
                    
                    面の示し方は一番若いアルファベットから時計回りに統一しといたほうがよいかも？
                """
                problem_checker = random()
                # parallel between line and flat
                if problem_checker < 0.33:
                    """
                    ある面に平行な直線は、面とアルファベットを共有していない直線になる？
                    逆に、ある直線に平行な面は、
                        辺を1本選んだ際に、6面のうち2面は含まれる。2面は垂直。2面は平行（交わらない）

                    # 指定された平面から、垂直な直線、含まれる直線、平行を考える
                    from random import choice


                    all_edges = ['辺AB', '辺AD', '辺AE', '辺BC', '辺BF', '辺CD', '辺CG', '辺DH', '辺EF', '辺EH', '辺FG', '辺GH']
                    all_flats = ['面ABCD', '面AEFB', '面AEHD', '面BCGF', '面CDHG', '面EFGH']
                    # selected_flat = choice(all_flats)
                    selected_flat = "面ABCD"
                    # アルファベットが含まれている直線は、すべて垂直
                    # じゃなくて、一文字だけ含まれる場合は垂直で、二文字含まれる場合は含む(順番は一致しない eg. ABCDのAD
                    parallel_edges = [edge for edge in all_edges if (edge[1] in selected_flat) and (edge[2] in selected_flat)]
                    print(sorted(parallel_edges))
                    
                    ↑垂直の、一文字だけ含まれる、をどう表現するか？？素直にfor文の中でちまちま？
                    """
            elif selected_problem_type == "flat_and_flat":
                latex_answers = ["dummy answer1 in flat_and_flat", "dummy answer2 in flat_and_flat", "dummy answer3 in flat_and_flat"]
                latex_problems = ["dummy problem1 in flat_and_flat", "dummy problem2 in flat_and_flat", "dummy problem3 in flat_and_flat"]
            else:
                raise ValueError(f"'selected_problem_type' is {selected_problem_type}."\
                                 "This must be 'line_and_line', 'line_and_flat' or 'flat_and_flat'.")
        return latex_answers, latex_problems
    
    def _make_triangular_prism_problem(self):
        """三角柱を用いた直線と平面の位置関係の問題を作成

        Returns:
            latex_answers (list): latex形式で記述された解答が格納されている
            latex_problems (list): latex形式で記述された問題が格納されている
        """
        latex_answers = ["dummy answer1 in triangular prism", "dummy answer2 in triangular prism", "dummy answer3 in triangular prism"]
        latex_problems = ["dummy problem1 in triangular prism", "dummy problem2 in triangular prism", "dummy problem3 in triangular prism"]
        return latex_answers, latex_problems

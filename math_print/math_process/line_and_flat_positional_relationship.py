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
    
    4/21
    ・直線と平面の位置関係のうち、平面→直線は完了。次は直線→平面
    
    4/22
    ・直線と平面の位置関係は完了。次は平面の位置関係
    ・「使用される問題のタイプも基準となる直線や平面も同じ」という状況がそこそこにありうる。特に平面は択が少ないため、結構かぶりうるかもしれない
    →三角柱は多分平面も辺も少なめだから、この確率は上がりそう
    ↑要対処
        問題に使った平面や辺を記録しておく系？中で3問回してるからいけそうっぽい？
        逆に候補を別枠で仕切ってあげて、どんどんpopなりしていって消えていく形？
"""
from random import choice, random, randint

import sympy as sy


class LineAndFlatPositionalRelationship:
    """直線と平面の位置関係の問題と解答を出力
    
    Attributes:
        latex_answers (list[str]): latex形式で記述された解答が3問分格納されたリスト
        latex_problems (list[str]): latex形式で記述された問題が3問分格納されたリスト
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
            problem_types (list[str]): 使用される問題(直線と直線, 直線と平面, 平面と平面)が格納されている

        Returns:
            latex_answers (list[str]): latex形式で記述された解答が3問分格納されたリスト
            latex_problems (list[str]): latex形式で記述された問題が3問分格納されたリスト
        
        Raises:
            ValueError: 想定されていない問題の種類が指定されたときに挙上
        
        Note:
            平行な辺は手動で指定している。
            垂直な辺は、辺とアルファベットを共有するものはすべて垂直である点を利用(eg. 辺AB->AD, AE, BC, BF)。
            ねじれの位置にある辺は、すべての辺のうち、平行でも垂直でもないものを差し引いて求めている。
        """
        latex_answers = []
        latex_problems = []
        """
        4/23
        ここで候補を用意して、ループ内で問題がかぶらないようにする？
        用途によって使い分けなければならない同じ中身のやつがあるとややこしくなりそうな感じ
        あとはpop?とか使っているやつはそもそも動作がやばそう？
        →別のやり方を考える
        →候補系は残しつつ、中での処理を考える
        あと、コピーの深さを意識していないと、意図せず消えたり残ったりしそうではある
        他の問題との兼ね合いも注意
        コピーの候補を残すやつは悪くなさそう？弾き方に工夫はいる
        問題自体のifとかの枝を別の感じで組み直す？結構手間はかかる系だが、すっきりさせるのには近いやり方？
        
        結局、edge_used_for_problemがかぶらなければそれでいい。
        読み出すときに、減少する候補があればよい？
        あと、一緒に使いまわしてるとこには重ね重ね注意がいる
        
        結局、初めに存在しているあれこれ（不変）と、使用した情報を記録するやつを個別に用意しておいたほうが良いっぽい？
        
        skew_edgeの参照を切る?
        →少なくとも文字だけを見て切ることはできない。平行もねじれも、いずれも文字を共有しないから
        """
        parallel_edges_groups = (
            ["辺AB", "辺CD", "辺EF", "辺GH",],
            ["辺AD", "辺BC", "辺EH", "辺FG",],
            ["辺AE", "辺BF", "辺CG", "辺DH",],
            )
        used_parallel_edges_groups = []
        all_edges = (
            "辺AB", "辺BC", "辺CD", "辺AD",
            "辺AE", "辺BF", "辺CG", "辺DH",
            "辺EF", "辺FG", "辺GH", "辺EH",
        )
        used_edges = []
        all_flats = ('面ABCD', '面AEFB', '面AEHD', '面BCGF', '面CDHG', '面EFGH')
        used_flats = []
        for problem_number in range(1, 4):
            selected_problem_type = choice(problem_types)
            if selected_problem_type == "line_and_line":
                problem_checker = random()
                # parallel edge
                # parallel_edges_groupsが減っていく
                # 大本を参照してはいない？
                if problem_checker < 0.33:                        
                    parallel_edges_group = (
                        ["辺AB", "辺CD", "辺EF", "辺GH",],
                        ["辺AD", "辺BC", "辺EH", "辺FG",],
                        ["辺AE", "辺BF", "辺CG", "辺DH",],
                        )
                    selected_parallel_edges = choice(parallel_edges_group)
                    edge_used_for_problem = selected_parallel_edges.pop(randint(0, len(selected_parallel_edges) - 1))
                    remained_edges = ", ".join(sorted(selected_parallel_edges))
                    latex_answers.append(f"({problem_number}) {remained_edges}")
                    latex_problems.append(f"({problem_number}) {edge_used_for_problem}と平行な辺を全て答えなさい。")
                # skew edge
                # 全ての辺から平行な辺をぬいたあと、一文字も含んでいない辺を読み出している
                # all_edgesが減っていく
                # 大本は参照している。全ての辺から、該当する
                elif 0.33 <= problem_checker < 0.66:
                    all_edges = [
                        "辺AB", "辺BC", "辺CD", "辺AD",
                        "辺AE", "辺BF", "辺CG", "辺DH",
                        "辺EF", "辺FG", "辺GH", "辺EH",
                    ]
                    edge_used_for_problem = choice(all_edges)
                    latex_problems.append(f"({problem_number}) {edge_used_for_problem}とねじれの位置にある辺を全て答えなさい。")
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
                    skew_edges.sort()
                    latex_answers.append(f"({problem_number}) {', '.join(skew_edges)}")
                # vertical edge
                # 全ての辺のうち、平行なものを取り除いて、さらにいずれかを含んでいる系の処理
                # ↑これ、!=とかで代用できない？いずれかを含んでいれば垂直な辺になりそう。なんとなくしばっていたほうが良い気が？
                # all_edgesが減っていく
                # 大本との比較はやってない
                else:
                    all_edges = [
                        "辺AB", "辺BC", "辺CD", "辺AD",
                        "辺AE", "辺BF", "辺CG", "辺DH",
                        "辺EF", "辺FG", "辺GH", "辺EH",
                    ]
                    edge_used_for_problem = choice(all_edges)
                    latex_problems.append(f"({problem_number}) {edge_used_for_problem}と垂直に交わる辺を全て答えなさい。")
                    vertical_edges = [edge for edge in all_edges if (edge_used_for_problem[1] in edge) != (edge_used_for_problem[2] in edge)]
                    vertical_edges.sort()
                    latex_answers.append(f"({problem_number}) {', '.join(vertical_edges)}")
            elif selected_problem_type == "line_and_flat":
                all_edges = ['辺AB', '辺AD', '辺AE', '辺BC', '辺BF', '辺CD', '辺CG', '辺DH', '辺EF', '辺EH', '辺FG', '辺GH']
                all_flats = ['面ABCD', '面AEFB', '面AEHD', '面BCGF', '面CDHG', '面EFGH']
                # from flat to edge
                if random() > 0.5:
                    problem_checker = random()
                    selected_flat = choice(all_flats)
                    if problem_checker < 0.33:
                        latex_problems.append(f"({problem_number}) {selected_flat}にふくまれる辺を全て答えなさい。")
                        including_edges = [edge for edge in all_edges if (edge[1] in selected_flat) and (edge[2] in selected_flat)]
                        including_edges.sort()
                        latex_answers.append(f"({problem_number}) {', '.join(including_edges)}")
                    elif 0.33 <= problem_checker < 0.66:
                        latex_problems.append(f"({problem_number}) {selected_flat}と垂直な辺を全て答えなさい。")
                        vertical_edges = [edge for edge in all_edges if (edge[1] in selected_flat) != (edge[2] in selected_flat)]
                        vertical_edges.sort()
                        latex_answers.append(f"({problem_number}) {', '.join(vertical_edges)}")
                    else:
                        latex_problems.append(f"({problem_number}) {selected_flat}と平行な辺を全て答えなさい。")
                        parallel_edges = [edge for edge in all_edges if (edge[1] not in (selected_flat)) and (edge[2] not in (selected_flat))]
                        latex_answers.append(f"({problem_number}) {', '.join(parallel_edges)}")
                # from edge to flat
                else:
                    problem_checker = random()
                    selected_edge = choice(all_edges)
                    if problem_checker < 0.33:
                        latex_problems.append(f"({problem_number}) {selected_edge}をふくむ平面を全て答えなさい。")
                        including_flats = [flat for flat in all_flats if (selected_edge[1] in flat) and (selected_edge[2] in flat)]
                        including_flats.sort()
                        latex_answers.append(f"({problem_number}) {', '.join(including_flats)}")
                    elif 0.33 <= problem_checker < 0.66:
                        latex_problems.append(f"({problem_number}) {selected_edge}に垂直な平面を全て答えなさい。")
                        vertical_flats = [flat for flat in all_flats if (selected_edge[1] in flat) != (selected_edge[2] in flat)]
                        vertical_flats.sort()
                        latex_answers.append(f"({problem_number}) {', '.join(vertical_flats)}")
                    else:
                        latex_problems.append(f"({problem_number}) {selected_edge}に平行な平面を全て答えなさい。")
                        parallel_flats = [flat for flat in all_flats if (selected_edge[1] not in flat) and (selected_edge[2] not in flat)]
                        parallel_flats.sort()
                        latex_answers.append(f"({problem_number}) {', '.join(parallel_flats)}")
            elif selected_problem_type == "flat_and_flat":
                
                def including_checker(selected_flat: str, flat_to_check: str) -> bool:
                    """平面の位置関係を把握するために、平面同士のアルファベット部分を比較する

                    Args:
                        selected_flat (str): 基準となる平面
                        flat_to_check (str): チェックしたい平面

                    Returns:
                        True or False (bool): 一文字も含まれない場合はFalse, そうでないならTrue
                    """
                    for alphabet in selected_flat[1:]:
                        if alphabet in flat_to_check:
                            return True
                    return False
                
                all_flats = ['面ABCD', '面AEFB', '面AEHD', '面BCGF', '面CDHG', '面EFGH']
                selected_flat = choice(all_flats)
                if random() > 0.5:
                    latex_problems.append(f"({problem_number}) {selected_flat}と垂直に交わる平面を全て答えなさい。")
                    vertical_flats = [flat for flat in all_flats if including_checker(selected_flat, flat)]
                    vertical_flats.sort()
                    latex_answers.append(f"({problem_number}) {', '.join(vertical_flats)}")
                else:
                    latex_problems.append(f"({problem_number}) {selected_flat}と平行な平面をすべて答えなさい。")
                    parallel_flats = [flat for flat in all_flats if not including_checker(selected_flat, flat)]
                    parallel_flats.sort()
                    latex_answers.append(f"({problem_number}) {', '.join(parallel_flats)}")
            else:
                raise ValueError(f"'selected_problem_type' is {selected_problem_type}."\
                                 "This must be 'line_and_line', 'line_and_flat' or 'flat_and_flat'.")
        return latex_answers, latex_problems
    
    def _make_triangular_prism_problem(self):
        """三角柱を用いた直線と平面の位置関係の問題を作成

        Returns:
            latex_answers (list): latex形式で記述された解答が格納されている
            latex_problems (list): latex形式で記述された問題が格納されている
        
        Developing:

        """
        latex_answers = ["dummy answer1 in triangular prism", "dummy answer2 in triangular prism", "dummy answer3 in triangular prism"]
        latex_problems = ["dummy problem1 in triangular prism", "dummy problem2 in triangular prism", "dummy problem3 in triangular prism"]
        return latex_answers, latex_problems

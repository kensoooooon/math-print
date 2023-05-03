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
    
    4/25
    ・for_display.html側に三角柱を出力できるように。問題作成
    
    4/26
    ・三角柱の問題の方に、四角柱の問題をそのまま組み入れているので、整合しているかチェック
    ↑とりあえず辺とか平面とかは揃えたが、ルール自体が異なっている可能性がある。
    
    ・とりあえず表示自体はできるように変更
    名前の変更が必要？命名が何かごちゃごちゃしてる
    
    ・三角柱の平面平面間にもガバ
    ・直方体の平面平面間にもガバがある。自分自身がふくまれている
    
    4/27
    ・平面間のガバの修正開始
        四角柱は垂直の判定にガバ
    ↑おそらく修正完了。次は選択型問題の作成
    
    4/28
    ・選択型の問題を引き続き作成
    
    別件で、記述型のときのpopが怪しい<-しれっとlistに変換しているからセーフっぽい。が、popを使うのは何かとあれかも？
    直線直線間は完了。次は直線と平面
    
    4/30
    ・引き続き選択式の問題
    平面間の問題において、垂直を取るようにしてしまうと、大抵の面が答えに当てはまるので、とりあえず除外しておく
    また、自身が問題に登場する可能性があるので、そこも修正が必要
    
    5/1
    三角柱の平面平面間の問題
    
    表記修正
    from line to flat, from flat to lineでは自身をさっぴく工程が不要
    (1) 面BEFCと垂直な辺を以下から一つ選びなさい。 (辺BE, 辺AD, 辺EF, 辺DE)で、辺DEが出力される問題（そもそも垂直じゃない）
    →おそらく判定ガバ（直方体と同じ判定が通じることはないっぽい）
    →→なんなら記述型のほうもやばいのでは案件
    →→→やばかった。
    ↑とりあえず三角柱の直線平面組は全チェック案件
    →平行と垂直の問題については、上面と下面のみ受け付け可能
    →→問題がかぶってしまう問題をどう解決する？選択肢を変える？？？？シンプルにしゃーないにする？？？？
    
    5/2
    引き続き
    
    5/3
    三角柱がらみの修正は一応終了。とりあえずチェックする
    →all_flats_candidatesをしっかりと利用していない（all_flats側から候補を読み込んでいる場所を修正
    多分ok?
    
        三角柱の方で、「選択型」の「垂直」問題は適当に答えても正解する確率の方が高い。
        →平行を答えさせる問題にチェンジ
        →選択肢が減ってもいいから、垂直も加える？さすがに1/2は・・・・？
    
        三角柱の「記述型」の辺と辺にも自身が登場する問題あり
        →平行な辺を答えさせる問題は修正完了。次はねじれと垂直のチェック（l.711~）
"""
from random import choice, random, randint, sample, shuffle
from typing import List, Tuple


class LineAndFlatPositionalRelationship:
    """直線と平面の位置関係の問題と解答を出力
    
    Attributes:
        latex_answers (list[str]): latex形式で記述された解答が3問分格納されたリスト
        latex_problems (list[str]): latex形式で記述された問題が3問分格納されたリスト
        solid_body (str): 問題に使用される立体
        _question_format (str): choice(選択式)かwrite(記述式)かが格納されている
    """
    def __init__(self, **settings):
        """初期設定
        
        Args:
            settings (dict): 問題に使用する各種設定を格納
        """
        problem_types = settings["used_problems"]
        question_format = settings["question_format"]
        selected_solid_body = choice(settings["used_solid_bodies"])
        if selected_solid_body == "quadrangular_prism":
            self.solid_body = "quadrangular_prism"
            if question_format == "choice":
                self.latex_answers, self.latex_problems = self._make_quadrangular_prism_choice_problem(problem_types)
            elif question_format == "write":
                self.latex_answers, self.latex_problems = self._make_quadrangular_prism_write_problem(problem_types)
        elif selected_solid_body == "triangular_prism":
            self.solid_body = "triangular_prism"
            if question_format == "choice":
                self.latex_answers, self.latex_problems = self._make_triangular_prism_choice_problem(problem_types)
            elif question_format == "write":
                self.latex_answers, self.latex_problems = self._make_triangular_prism_write_problem(problem_types)
        else:
            raise ValueError(f"'selected_solid_body' is {selected_solid_body}. This must be 'quadrangular_prism' or 'triangular_prism.")
    
    def _make_quadrangular_prism_choice_problem(self, problem_types: List[str]) -> Tuple[List[str]]:
        """直方体を用いた直線と平面の位置関係の選択式問題を作成

        Args:
            problem_types (List[str]): 使用される問題(直線と直線, 直線と平面, 平面と平面)が格納されている

        Returns:
            latex_answers (Tuple[List[str]]): latex形式で記述された解答
            latex_problems (Tuple[List[str]]): latex形式で記述された問題

        Raises:
            ValueError: 想定されていない問題の種類が指定されたときに挙上
        
        Note:
            辺は常に若いほうのアルファベットを前にするように命名
            面は一番若いほうのアルファベットから反時計回りになるように命名
            同じ問題が重複して出題されるのを避けるため、一度問題に使用された辺、平面については、ランダムな選択の候補から除外されている
        """
        latex_answers = []
        latex_problems = []
        parallel_edges_groups = (
            ("辺AB", "辺CD", "辺EF", "辺GH"),
            ("辺AD", "辺BC", "辺EH", "辺FG"),
            ("辺AE", "辺BF", "辺CG", "辺DH")
            )
        all_edges = (
            "辺AB", "辺BC", "辺CD", "辺AD",
            "辺AE", "辺BF", "辺CG", "辺DH",
            "辺EF", "辺FG", "辺GH", "辺EH",
        )
        all_flats = ('面ABCD', '面AEFB', '面ADHE', '面BFGC', '面CGHD', '面EFGH')
        vertical_flats_groups = {
            "面ABCD": ("面AEFB", "面BFGC", "面CGHD", "面ADHE"),
            "面AEFB": ("面ABCD", "面BFGC", "面ADHE", "面EFGH"),
            "面BFGC": ("面ABCD", "面AEFB", "面CGHD", "面EFGH"),
            "面CGHD": ("面ABCD", "面BFGC", "面ADHE", "面EFGH"),
            "面ADHE": ("面ABCD", "面AEFB", "面CGHD", "面EFGH"),
            "面EFGH": ("面AEFB", "面BFGC", "面CDHD", "面ADHE"),
        }
        used_parallel_edges_groups = []
        used_edges_for_skew = []
        used_edges_for_vertical = []
        used_edges_for_flat = []
        used_flats_for_edge = []
        used_flats_for_flat = []
        for problem_number in range(1, 4):
            selected_problem_type = choice(problem_types)
            if selected_problem_type == "line_and_line":
                problem_checker = random()
                if problem_checker < 0.33:
                    parallel_edges_candidates = list(set(parallel_edges_groups) - set(used_parallel_edges_groups))
                    selected_parallel_edges = choice(parallel_edges_candidates)
                    used_parallel_edges_groups.append(selected_parallel_edges)
                    edge_used_for_problem, collect_edge = sample(selected_parallel_edges, 2)
                    wrong_edges = sample(set(all_edges) - set(selected_parallel_edges) - set([edge_used_for_problem]), 3)
                    edges_choice = wrong_edges + [collect_edge]
                    shuffle(edges_choice)
                    latex_problem = f"({problem_number}) {edge_used_for_problem}と平行な辺を以下から一つ選びなさい。 "
                    latex_problem += f"({', '.join(edges_choice)})"
                    latex_problems.append(latex_problem)
                    latex_answers.append(f"({(problem_number)}) {collect_edge}")
                elif 0.33 <= problem_checker < 0.66:
                    all_edges_candidates = list(set(all_edges) - set(used_edges_for_skew))
                    edge_used_for_problem = choice(all_edges_candidates)
                    used_edges_for_skew.append(edge_used_for_problem)
                    for parallel_edges in parallel_edges_groups:
                        if edge_used_for_problem in parallel_edges:
                            parallel_edges_with_edge_used_for_problem = parallel_edges
                            break
                    edges_without_parallel = list(set(all_edges) - set(parallel_edges_with_edge_used_for_problem))
                    first_alphabet = edge_used_for_problem[1]
                    second_alphabet = edge_used_for_problem[2]
                    skew_edges = [edge for edge in edges_without_parallel if (first_alphabet not in edge) and (second_alphabet not in edge)]
                    collect_edge = choice(skew_edges)
                    wrong_edges = sample(set(all_edges) - set(skew_edges) - set([edge_used_for_problem]), 3)
                    edges_choice = wrong_edges + [collect_edge]
                    shuffle(edges_choice)
                    latex_problem = f"({problem_number}) {edge_used_for_problem}とねじれの位置にある辺を以下から一つ選びなさい。 "
                    latex_problem += f"({', '.join(edges_choice)})"
                    latex_problems.append(latex_problem)
                    latex_answers.append(f"({problem_number}) {collect_edge}")
                else:
                    all_edges_candidates = list(set(all_edges) - set(used_edges_for_vertical))
                    edge_used_for_problem = choice(all_edges_candidates)
                    used_edges_for_vertical.append(edge_used_for_problem)
                    vertical_edges = [edge for edge in all_edges if (edge_used_for_problem[1] in edge) != (edge_used_for_problem[2] in edge)]
                    collect_edge = choice(vertical_edges)
                    wrong_edges = sample(set(all_edges) - set(vertical_edges) - set([edge_used_for_problem]), 3)
                    edges_choice = wrong_edges + [collect_edge]
                    shuffle(edges_choice)
                    latex_problem = f"({problem_number}) {edge_used_for_problem}と垂直に交わる辺を以下から一つ選びなさい。 "
                    latex_problem += f"({', '.join(edges_choice)})"
                    latex_problems.append(latex_problem)
                    latex_answers.append(f"({problem_number}) {collect_edge}")
            elif selected_problem_type == "line_and_flat":
                # flat to line
                if random() > 0.5:
                    problem_checker = random()
                    all_flats_candidates = list(set(all_flats) - set(used_flats_for_edge))
                    selected_flat = choice(all_flats)
                    used_flats_for_edge.append(selected_flat)
                    if problem_checker < 0.33:
                        including_edges = [edge for edge in all_edges if (edge[1] in selected_flat) and (edge[2] in selected_flat)]
                        collect_edge = choice(including_edges)
                        wrong_edges = sample(set(all_edges) - set(including_edges), 3)
                        edges_choice = wrong_edges + [collect_edge]
                        shuffle(edges_choice)
                        latex_problem = f"({problem_number}) {selected_flat}にふくまれる辺を以下から一つ選びなさい。 "
                        latex_problem += f"({', '.join(edges_choice)})"
                        latex_problems.append(latex_problem)
                        latex_answers.append(f"({problem_number}) {collect_edge}")
                    elif 0.33 <= problem_checker < 0.66:
                        vertical_edges = [edge for edge in all_edges if (edge[1] in selected_flat) != (edge[2] in selected_flat)]
                        collect_edge = choice(vertical_edges)
                        wrong_edges = sample(set(all_edges) - set(vertical_edges), 3)
                        edges_choice = wrong_edges + [collect_edge]
                        shuffle(edges_choice)
                        latex_problem = f"({problem_number}) {selected_flat}と垂直な辺を以下から一つ選びなさい。 "
                        latex_problem += f"({', '.join(edges_choice)})"
                        latex_problems.append(latex_problem)
                        latex_answers.append(f"({problem_number}) {collect_edge}")
                    else:
                        parallel_edges = [edge for edge in all_edges if (edge[1] not in (selected_flat)) and (edge[2] not in (selected_flat))]
                        collect_edge = choice(parallel_edges)
                        wrong_edges = sample(set(all_edges) - set(parallel_edges), 3)
                        edges_choice = wrong_edges + [collect_edge]
                        shuffle(edges_choice)
                        latex_problem = f"({problem_number}) {selected_flat}と平行な辺を以下から一つ選びなさい。 "
                        latex_problem += f"({', '.join(edges_choice)})"
                        latex_problems.append(latex_problem)
                        latex_answers.append(f"({problem_number}) {collect_edge}")
                # line to flat
                else:
                    problem_checker = random()
                    all_edges_candidates = list(set(all_edges) - set(used_edges_for_flat))
                    selected_edge = choice(all_edges_candidates)
                    used_edges_for_flat.append(selected_edge)
                    if problem_checker < 0.33:
                        including_flats = [flat for flat in all_flats if (selected_edge[1] in flat) and (selected_edge[2] in flat)]
                        collect_flat = choice(including_flats)
                        wrong_flats = sample(set(all_flats) - set(including_flats), 3)
                        flats_choice = wrong_flats + [collect_flat]
                        shuffle(flats_choice)
                        latex_problem = f"({problem_number}) {selected_edge}をふくむ面を以下から一つ選びなさい。 "
                        latex_problem += f"({', '.join(flats_choice)})"
                        latex_problems.append(latex_problem)
                        latex_answers.append(f"({problem_number}) {collect_flat}")
                    elif 0.33 <= problem_checker < 0.66:
                        vertical_flats = [flat for flat in all_flats if (selected_edge[1] in flat) != (selected_edge[2] in flat)]
                        collect_flat = choice(vertical_flats)
                        wrong_flats = sample(set(all_flats) - set(vertical_flats), 3)
                        flats_choice = wrong_flats + [collect_flat]
                        shuffle(flats_choice)
                        latex_problem = f"({problem_number}) {selected_edge}に垂直な面を以下から一つ選びなさい。 "
                        latex_problem += f"({', '.join(flats_choice)})"
                        latex_problems.append(latex_problem)
                        latex_answers.append(f"({problem_number}) {collect_flat}")
                    else:
                        parallel_flats = [flat for flat in all_flats if (selected_edge[1] not in flat) and (selected_edge[2] not in flat)]
                        collect_flat = choice(parallel_flats)
                        wrong_flats = sample(set(all_flats) - set(parallel_flats), 3)
                        flats_choice = wrong_flats + [collect_flat]
                        shuffle(flats_choice)
                        latex_problem = f"({problem_number}) {selected_edge}に平行な面を以下から一つ選びなさい。 "
                        latex_problem += f"({', '.join(flats_choice)})"
                        latex_problems.append(latex_problem)
                        latex_answers.append(f"({problem_number}) {collect_flat}")
            elif selected_problem_type == "flat_and_flat":
                all_flats_candidates = list(set(all_flats) - set(used_flats_for_flat))
                selected_flat = choice(all_flats_candidates)
                used_flats_for_flat.append(selected_flat)
                parallel_flats = list(set(all_flats) - set([selected_flat]) - set(vertical_flats_groups[selected_flat]))
                collect_flat = choice(parallel_flats)
                print(f"all_flats: {all_flats}")
                print(f"parallel_flats: {parallel_flats}")
                print(f"selected_flat: {selected_flat}")
                wrong_flats = sample(set(all_flats) - (set(parallel_flats)) - set([selected_flat]), 3)
                flats_choice = wrong_flats + [collect_flat]
                shuffle(flats_choice)
                latex_problem = f"({problem_number}) {selected_flat}に平行な面を以下から一つ選びなさい。 :"
                latex_problem += f"({', '.join(flats_choice)})"
                latex_problems.append(latex_problem)
                latex_answers.append(f"({problem_number}) {collect_flat}")
            else:
                raise ValueError(f"'selected_problem_type' is {selected_problem_type}."\
                                 "This must be 'line_and_line', 'line_and_flat' or 'flat_and_flat'.")
        return latex_answers, latex_problems
    
    def _make_quadrangular_prism_write_problem(self, problem_types: List[str]) -> Tuple[List[str]]:
        """直方体を用いた直線と平面の位置関係の記述式問題を作成

        Args:
            problem_types (list[str]): 使用される問題(直線と直線, 直線と平面, 平面と平面)が格納されている

        Returns:
            latex_answers (list[str]): latex形式で記述された解答が3問分格納されたリスト
            latex_problems (list[str]): latex形式で記述された問題が3問分格納されたリスト
        
        Raises:
            ValueError: 想定されていない問題の種類が指定されたときに挙上
        
        Note:
            辺は常に若いほうのアルファベットを前にするように命名
            面は一番若いほうのアルファベットから反時計回りになるように命名
            同じ問題が重複して出題されるのを避けるため、一度問題に使用された辺、平面については、ランダムな選択の候補から除外されている
        """
        latex_answers = []
        latex_problems = []
        parallel_edges_groups = (
            ("辺AB", "辺CD", "辺EF", "辺GH"),
            ("辺AD", "辺BC", "辺EH", "辺FG"),
            ("辺AE", "辺BF", "辺CG", "辺DH")
            )
        all_edges = (
            "辺AB", "辺BC", "辺CD", "辺AD",
            "辺AE", "辺BF", "辺CG", "辺DH",
            "辺EF", "辺FG", "辺GH", "辺EH",
        )
        all_flats = ('面ABCD', '面AEFB', '面ADHE', '面BFGC', '面CGHD', '面EFGH')
        vertical_flats_groups = {
            "面ABCD": ("面AEFB", "面BFGC", "面CGHD", "面ADHE"),
            "面AEFB": ("面ABCD", "面BFGC", "面ADHE", "面EFGH"),
            "面BFGC": ("面ABCD", "面AEFB", "面CGHD", "面EFGH"),
            "面CGHD": ("面ABCD", "面BFGC", "面ADHE", "面EFGH"),
            "面ADHE": ("面ABCD", "面AEFB", "面CGHD", "面EFGH"),
            "面EFGH": ("面AEFB", "面BFGC", "面CGHD", "面ADHE"),
        }
        used_parallel_edges_groups = []
        used_edges_for_skew = []
        used_edges_for_vertical = []
        used_edges_for_flat = []
        used_flats_for_edge = []
        used_flats_for_flat = []
        for problem_number in range(1, 4):
            selected_problem_type = choice(problem_types)
            if selected_problem_type == "line_and_line":
                problem_checker = random()
                if problem_checker < 0.33:
                    parallel_edges_candidates = list(set(parallel_edges_groups) - set(used_parallel_edges_groups))
                    selected_parallel_edges = choice(parallel_edges_candidates)
                    used_parallel_edges_groups.append(selected_parallel_edges)
                    edge_used_for_problem = list(selected_parallel_edges).pop(randint(0, len(selected_parallel_edges) - 1))
                    latex_problems.append(f"({problem_number}) {edge_used_for_problem}と平行な辺を全て答えなさい。")
                    remained_edges = ", ".join(sorted(selected_parallel_edges))
                    latex_answers.append(f"({problem_number}) {remained_edges}")
                elif 0.33 <= problem_checker < 0.66:
                    all_edges_candidates = list(set(all_edges) - set(used_edges_for_skew))
                    edge_used_for_problem = choice(all_edges_candidates)
                    used_edges_for_skew.append(edge_used_for_problem)
                    latex_problems.append(f"({problem_number}) {edge_used_for_problem}とねじれの位置にある辺を全て答えなさい。")
                    for parallel_edges in parallel_edges_groups:
                        if edge_used_for_problem in parallel_edges:
                            parallel_edges_with_edge_used_for_problem = parallel_edges
                            break
                    edges_without_parallel = list(set(all_edges) - set(parallel_edges_with_edge_used_for_problem))
                    first_alphabet = edge_used_for_problem[1]
                    second_alphabet = edge_used_for_problem[2]
                    skew_edges = [edge for edge in edges_without_parallel if (first_alphabet not in edge) and (second_alphabet not in edge)]
                    skew_edges.sort()
                    latex_answers.append(f"({problem_number}) {', '.join(skew_edges)}")
                else:
                    all_edges_candidates = list(set(all_edges) - set(used_edges_for_vertical))
                    edge_used_for_problem = choice(all_edges_candidates)
                    used_edges_for_vertical.append(edge_used_for_problem)
                    latex_problems.append(f"({problem_number}) {edge_used_for_problem}と垂直に交わる辺を全て答えなさい。")
                    vertical_edges = [edge for edge in all_edges if (edge_used_for_problem[1] in edge) != (edge_used_for_problem[2] in edge)]
                    vertical_edges.sort()
                    latex_answers.append(f"({problem_number}) {', '.join(vertical_edges)}")
            elif selected_problem_type == "line_and_flat":
                if random() > 0.5:
                    problem_checker = random()
                    all_flats_candidates = list(set(all_flats) - set(used_flats_for_edge))
                    selected_flat = choice(all_flats)
                    used_flats_for_edge.append(selected_flat)
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
                else:
                    problem_checker = random()
                    all_edges_candidates = list(set(all_edges) - set(used_edges_for_flat))
                    selected_edge = choice(all_edges_candidates)
                    used_edges_for_flat.append(selected_edge)
                    if problem_checker < 0.33:
                        latex_problems.append(f"({problem_number}) {selected_edge}をふくむ面を全て答えなさい。")
                        including_flats = [flat for flat in all_flats if (selected_edge[1] in flat) and (selected_edge[2] in flat)]
                        including_flats.sort()
                        latex_answers.append(f"({problem_number}) {', '.join(including_flats)}")
                    elif 0.33 <= problem_checker < 0.66:
                        latex_problems.append(f"({problem_number}) {selected_edge}に垂直な面を全て答えなさい。")
                        vertical_flats = [flat for flat in all_flats if (selected_edge[1] in flat) != (selected_edge[2] in flat)]
                        vertical_flats.sort()
                        latex_answers.append(f"({problem_number}) {', '.join(vertical_flats)}")
                    else:
                        latex_problems.append(f"({problem_number}) {selected_edge}に平行な面を全て答えなさい。")
                        parallel_flats = [flat for flat in all_flats if (selected_edge[1] not in flat) and (selected_edge[2] not in flat)]
                        parallel_flats.sort()
                        latex_answers.append(f"({problem_number}) {', '.join(parallel_flats)}")
            elif selected_problem_type == "flat_and_flat":
                all_flats_candidates = list(set(all_flats) - set(used_flats_for_flat))
                selected_flat = choice(all_flats_candidates)
                used_flats_for_flat.append(selected_flat)
                if random() > 0.5:
                    latex_problems.append(f"({problem_number}) {selected_flat}と垂直に交わる面を全て答えなさい。")
                    vertical_flats = list(vertical_flats_groups[selected_flat])
                    vertical_flats.sort()
                    latex_answers.append(f"({problem_number}) {', '.join(vertical_flats)}")
                else:
                    latex_problems.append(f"({problem_number}) {selected_flat}と平行な面を全て答えなさい。")
                    parallel_flats = list(set(all_flats) - set([selected_flat]) - set(vertical_flats_groups[selected_flat]))
                    parallel_flats.sort()
                    latex_answers.append(f"({problem_number}) {', '.join(parallel_flats)}")
            else:
                raise ValueError(f"'selected_problem_type' is {selected_problem_type}."\
                                 "This must be 'line_and_line', 'line_and_flat' or 'flat_and_flat'.")
        return latex_answers, latex_problems

    def _make_triangular_prism_choice_problem(self, problem_types: List[str]) -> Tuple[List[str]]:
        """三角柱を用いた直線と平面の位置関係の選択式問題を作成
        
        Args:
            problem_types (list[str]): 使用される問題(直線と直線, 直線と平面, 平面と平面)が格納されている
            
        Returns:
            latex_answers (list[str]): latex形式で記述された解答が格納されている
            latex_problems (list[str]): latex形式で記述された問題が格納されている
        
        Raises:
            ValueError: 指定された問題タイプが存在しないものだったときに挙上
        
        Note:
            辺は常に若いほうのアルファベットを前にするように命名
            面は一番若いほうのアルファベットから反時計回りになるように命名
            同じ問題が重複して出題されるのを避けるため、一度問題に使用された辺、平面については、ランダムな選択の候補から除外されている
        """
        latex_answers = []
        latex_problems = []
        parallel_edges_groups = (
            ("辺AB", "辺DE"), ("辺BC", "辺EF"),
            ("辺AC", "辺DF"), ("辺AD", "辺BE", "辺CF")
        )
        all_edges = (
            "辺AB", "辺BC", "辺AC",
            "辺DE", "辺EF", "辺DF",
            "辺AD", "辺BE", "辺CF"
        )
        all_flats = ("面ABC", "面DEF", "面ADEB", "面BEFC", "面ADFC")
        vertical_edges_groups = {
            "辺AB": ("辺AD", "辺BE"), "辺BC": ("辺BE", "辺CF"), "辺AC": ("辺AD", "辺CF"),
            "辺AD": ("辺AB", "辺AC", "辺DE", "辺DF"), "辺BE": ("辺AB", "辺BC", "辺DE", "辺EF"), "辺CF": ("辺AC", "辺DF", "辺BC", "辺EF"),
            "辺DE": ("辺AD", "辺BE"), "辺EF": ("辺BE", "辺CF"), "辺DF": ("辺AD", "辺CF")
        }
        vertical_flats_groups = {
            "面ABC": ("面ADEB", "面BEFC", "面ADFC"),
            "面ADEB": ("面ABC", "面DEF"), "面BEFC": ("面ABC", "面DEF"), "面ADFC": ("面ABC", "面DEF"),
            "面DEF": ("面ADEB", "面BEFC", "面ADFC")
        }
        used_parallel_edges_groups = []
        used_flats_for_edge = []
        used_edges_for_vertical = []
        used_edges_for_skew = []
        used_edges_for_flat = []
        used_flats_for_flat = []
        for problem_number in range(1, 4):
            selected_problem_type = choice(problem_types)
            if selected_problem_type == "line_and_line":
                problem_checker = random()
                """
                ある辺に平行な辺は、縦の辺以外は全部一本だけ
                sample(..., 2)で通るはず?
                """
                if problem_checker < 0.33:
                    parallel_edges_candidates = list(set(parallel_edges_groups) - set(used_parallel_edges_groups))
                    selected_parallel_edges = choice(parallel_edges_candidates)
                    used_parallel_edges_groups.append(selected_parallel_edges)
                    edge_used_for_problem, collect_edge = sample(selected_parallel_edges, 2)
                    wrong_edges = sample(set(all_edges) - set(selected_parallel_edges) - set([edge_used_for_problem]), 3)
                    edges_choice = wrong_edges + [collect_edge]
                    shuffle(edges_choice)
                    latex_problem = f"({problem_number}) {edge_used_for_problem}と平行な辺を以下から一つ選びなさい。 "
                    latex_problem += f"({', '.join(edges_choice)})"
                    latex_problems.append(latex_problem)
                    latex_answers.append(f"({problem_number}) {collect_edge}")
                elif 0.33 <= problem_checker < 0.66:
                    all_edges_candidates = list(set(all_edges) - set(used_edges_for_vertical))
                    edge_used_for_problem = choice(all_edges_candidates)
                    used_edges_for_skew.append(edge_used_for_problem)
                    for parallel_edges in parallel_edges_groups:
                        if edge_used_for_problem in parallel_edges:
                            parallel_edges_with_edge_used_for_problem = parallel_edges
                            break
                    edges_without_parallel = list(set(all_edges) - set(parallel_edges_with_edge_used_for_problem))
                    skew_edges = [edge for edge in edges_without_parallel if (edge_used_for_problem[1] not in edge) and (edge_used_for_problem[2] not in edge)]
                    collect_edge = choice(skew_edges)
                    wrong_edges = sample(set(all_edges) - set(skew_edges) - set([edge_used_for_problem]), 3)
                    edges_choice = wrong_edges + [collect_edge]
                    shuffle(edges_choice)
                    latex_problem = f"({problem_number}) {edge_used_for_problem}とねじれの位置にある辺を以下から一つ選びなさい。 "
                    latex_problem += f"({', '.join(edges_choice)})"
                    latex_problems.append(latex_problem)
                    latex_answers.append(f"({problem_number}) {collect_edge}")
                else:
                    all_edges_candidates = list(set(all_edges) - set(used_edges_for_vertical))
                    edge_used_for_problem = choice(all_edges_candidates)
                    used_edges_for_vertical.append(edge_used_for_problem)
                    vertical_edges = list(vertical_edges_groups[edge_used_for_problem])
                    collect_edge = choice(vertical_edges)
                    wrong_edges = sample(set(all_edges) - set(vertical_edges) - set([edge_used_for_problem]), 3)
                    edges_choice = wrong_edges + [collect_edge]
                    shuffle(edges_choice)
                    latex_problem = f"({problem_number}) {edge_used_for_problem}と垂直に交わる辺を以下から一つ選びなさい。 "
                    latex_problem += f"({', '.join(edges_choice)})"
                    latex_problems.append(latex_problem)
                    latex_answers.append(f"({problem_number}) {collect_edge}")
            elif selected_problem_type == "line_and_flat":
                if random() > 0.5:
                    problem_checker = random()
                    # ふくまれている辺→どの平面でもok
                    if problem_checker < 0.33:
                        all_flats_candidates = list(set(all_flats) - set(used_flats_for_edge))
                        selected_flat = choice(all_flats_candidates)
                        used_flats_for_edge.append(selected_flat)
                        # 多分判定もok
                        including_edges = [edge for edge in all_edges if (edge[1] in selected_flat) and (edge[2] in selected_flat)]
                        collect_edge = choice(including_edges)
                        wrong_edges = sample(set(all_edges) - set(including_edges), 3)
                        edges_choice = wrong_edges + [collect_edge]
                        shuffle(edges_choice)
                        latex_problem = f"({problem_number}) {selected_flat}にふくまれる辺を以下から一つ選びなさい。 "
                        latex_problem += f"({', '.join(edges_choice)})"
                        latex_problems.append(latex_problem)
                        latex_answers.append(f"({problem_number}) {collect_edge}")
                    # 垂直な辺→上面と下面のみ可能
                    elif 0.33 <= problem_checker < 0.66:
                        # all_flats_candidates = list(set(all_flats) - set(used_flats_for_edge))
                        all_flats_candidates = ["面ABC", "面DEF"]
                        selected_flat = choice(all_flats_candidates)
                        # used_flats_for_edge.append(selected_flat)
                        # vertical_edges = [edge for edge in all_edges if (edge[1] in selected_flat) != (edge[2] in selected_flat)]
                        vertical_edges = ["辺AD", "辺BE", "辺CF"]
                        collect_edge = choice(vertical_edges)
                        wrong_edges = sample(set(all_edges) - set(vertical_edges), 3)
                        edges_choice = wrong_edges + [collect_edge]
                        shuffle(edges_choice)
                        latex_problem = f"({problem_number}) {selected_flat}と垂直な辺を以下から一つ選びなさい。 "
                        latex_problem += f"({', '.join(edges_choice)})"
                        latex_problems.append(latex_problem)
                        latex_answers.append(f"({problem_number}) {collect_edge}")
                    # 平行な辺→上面と下面のみ可能
                    else:
                        # all_flats_candidates = list(set(all_flats) - set(used_flats_for_edge))
                        all_flats_candidates = ["面ABC", "面DEF"]
                        selected_flat = choice(all_flats_candidates)
                        # used_flats_for_edge.append(selected_flat)
                        # parallel_edges = [edge for edge in all_edges if (edge[1] not in (selected_flat)) and (edge[2] not in (selected_flat))]
                        if selected_flat == "面ABC":
                            parallel_edges = ["辺DE", "辺EF", "辺DF"]
                        elif selected_flat == "面DEF":
                            parallel_edges = ["辺AB", "辺BC", "辺AC"]
                        collect_edge = choice(parallel_edges)
                        wrong_edges = sample(set(all_edges) - set(parallel_edges), 3)
                        edges_choice = wrong_edges + [collect_edge]
                        shuffle(edges_choice)
                        latex_problem = f"({problem_number}) {selected_flat}と平行な辺を以下から一つ選びなさい。 "
                        latex_problem += f"({', '.join(edges_choice)})"
                        latex_problems.append(latex_problem)
                        latex_answers.append(f"({problem_number}) {collect_edge}")
                else:
                    problem_checker = random()
                    all_edges_candidates = list(set(all_edges) - set(used_edges_for_flat))
                    selected_edge = choice(all_edges_candidates)
                    used_edges_for_flat.append(selected_edge)
                    if problem_checker < 0.33:
                        including_flats = [flat for flat in all_flats if (selected_edge[1] in flat) and (selected_edge[2] in flat)]
                        collect_flat = choice(including_flats)
                        wrong_flats = sample(set(all_flats) - set(including_flats), 3)
                        flats_choice = wrong_flats + [collect_flat]
                        shuffle(flats_choice)
                        latex_problem = f"({problem_number}) {selected_edge}をふくむ面を以下から一つ選びなさい。 "
                        latex_problem += f"({', '.join(flats_choice)})"
                        latex_problems.append(latex_problem)
                        latex_answers.append(f"({problem_number}) {collect_flat}")
                    elif 0.33 <= problem_checker < 0.66:
                        vertical_flats = [flat for flat in all_flats if (selected_edge[1] in flat) != (selected_edge[2] in flat)]
                        collect_flat = choice(vertical_flats)
                        wrong_flats = sample(set(all_flats) - set(vertical_flats), 3)
                        flats_choice = wrong_flats + [collect_flat]
                        shuffle(flats_choice)
                        latex_problem = f"({problem_number}) {selected_edge}に垂直な面を以下から一つ選びなさい。 "
                        latex_problem += f"({', '.join(flats_choice)})"
                        latex_problems.append(latex_problem)
                        latex_answers.append(f"({problem_number}) {collect_flat}")
                    else:
                        parallel_flats = [flat for flat in all_flats if (selected_edge[1] not in flat) and (selected_edge[2] not in flat)]
                        collect_flat = choice(parallel_flats)
                        wrong_flats = sample(set(all_flats) - set(parallel_flats), 3)
                        flats_choice = wrong_flats + [collect_flat]
                        shuffle(flats_choice)
                        latex_problem = f"({problem_number}) {selected_edge}に平行な面を以下から一つ選びなさい。"
                        latex_problem += f"({', '.join(flats_choice)})"
                        latex_problems.append(latex_problem)
                        latex_answers.append(f"({problem_number}) {collect_flat}")
            elif selected_problem_type == "flat_and_flat":
                all_flats_candidates = ["面ABC", "面DEF"]
                selected_flat, collect_flat = sample(all_flats_candidates, 2)
                flats_choice = list(set(all_flats) - set([selected_flat]))
                shuffle(flats_choice)
                latex_problem = f"({problem_number}) {selected_flat}と平行な面を以下から一つ選びなさい。 "
                latex_problem += f"({', '.join(flats_choice)})"
                latex_problems.append(latex_problem)
                latex_answers.append(f"({problem_number}) {collect_flat}")
            else:
                raise ValueError(f"'selected_problem_type' is {selected_problem_type}."\
                                 "This must be 'line_and_line', 'line_and_flat' or 'flat_and_flat'.")
        return latex_answers, latex_problems
    
    def _make_triangular_prism_write_problem(self, problem_types: List[str]) -> Tuple[List[str]]:
        """三角柱を用いた直線と平面の位置関係の記述式問題を作成
        
        Args:
            problem_types (list[str]): 使用される問題(直線と直線, 直線と平面, 平面と平面)が格納されている
            
        Returns:
            latex_answers (list[str]): latex形式で記述された解答が格納されている
            latex_problems (list[str]): latex形式で記述された問題が格納されている
        
        Raises:
            ValueError: 指定された問題タイプが存在しないものだったときに挙上
        
        Note:
            辺は常に若いほうのアルファベットを前にするように命名
            面は一番若いほうのアルファベットから反時計回りになるように命名
            同じ問題が重複して出題されるのを避けるため、一度問題に使用された辺、平面については、ランダムな選択の候補から除外されている
        """
        latex_answers = []
        latex_problems = []
        parallel_edges_groups = (
            ("辺AB", "辺DE"), ("辺BC", "辺EF"),
            ("辺AC", "辺DF"), ("辺AD", "辺BE", "辺CF")
        )
        all_edges = (
            "辺AB", "辺BC", "辺AC",
            "辺DE", "辺EF", "辺DF",
            "辺AD", "辺BE", "辺CF"
        )
        all_flats = ("面ABC", "面DEF", "面ADEB", "面BEFC", "面ADFC")
        vertical_edges_groups = {
            "辺AB": ("辺AD", "辺BE"), "辺BC": ("辺BE", "辺CF"), "辺AC": ("辺AD", "辺CF"),
            "辺AD": ("辺AB", "辺AC", "辺DE", "辺DF"), "辺BE": ("辺AB", "辺BC", "辺DE", "辺EF"), "辺CF": ("辺AC", "辺DF", "辺BC", "辺EF"),
            "辺DE": ("辺AD", "辺BE"), "辺EF": ("辺BE", "辺CF"), "辺DF": ("辺AD", "辺CF")
        }
        vertical_flats_groups = {
            "面ABC": ("面ADEB", "面BEFC", "面ADFC"),
            "面ADEB": ("面ABC", "面DEF"), "面BEFC": ("面ABC", "面DEF"), "面ADFC": ("面ABC", "面DEF"),
            "面DEF": ("面ADEB", "面BEFC", "面ADFC")
        }
        used_parallel_edges_groups = []
        used_flats_for_edge = []
        used_edges_for_vertical = []
        used_edges_for_skew = []
        used_edges_for_flat = []
        used_flats_for_flat = []
        for problem_number in range(1, 4):
            selected_problem_type = choice(problem_types)
            if selected_problem_type == "line_and_line":
                problem_checker = random()
                if problem_checker < 0.33:
                    """
                    平行な辺はそもそも一組ワンセット
                    水平な辺だと一つ、垂直な辺だと二つ
                    """
                    parallel_edges_candidates = list(set(parallel_edges_groups) - set(used_parallel_edges_groups))
                    selected_parallel_edges = choice(parallel_edges_candidates)
                    used_parallel_edges_groups.append(selected_parallel_edges)
                    # edge_used_for_problem, collect_edge = sample(selected_parallel_edges, 2)
                    # edge_used_for_problem = list(selected_parallel_edges).pop(randint(0, len(selected_parallel_edges) - 1))
                    edge_used_for_problem = choice(selected_parallel_edges)
                    latex_problems.append(f"({problem_number}) {edge_used_for_problem}と平行な辺を全て答えなさい。")
                    parallel_edges_without_edge_used_for_problem = list(set(selected_parallel_edges) - set([edge_used_for_problem]))
                    latex_answers.append(f"({problem_number}) {', '.join(parallel_edges_without_edge_used_for_problem)}")
                elif 0.33 <= problem_checker < 0.66:
                    all_edges_candidates = list(set(all_edges) - set(used_edges_for_vertical))
                    edge_used_for_problem = choice(all_edges_candidates)
                    used_edges_for_skew.append(edge_used_for_problem)
                    latex_problems.append(f"({problem_number}) {edge_used_for_problem}とねじれの位置にある辺を全て答えなさい。")
                    for parallel_edges in parallel_edges_groups:
                        if edge_used_for_problem in parallel_edges:
                            parallel_edges_with_edge_used_for_problem = parallel_edges
                            break
                    edges_without_parallel = list(set(all_edges) - set(parallel_edges_with_edge_used_for_problem))
                    skew_edges = [edge for edge in edges_without_parallel if (edge_used_for_problem[1] not in edge) and (edge_used_for_problem[2] not in edge)]
                    skew_edges.sort()
                    latex_answers.append(f"({problem_number}) {', '.join(skew_edges)}")
                else:
                    all_edges_candidates = list(set(all_edges) - set(used_edges_for_vertical))
                    edge_used_for_problem = choice(all_edges_candidates)
                    used_edges_for_vertical.append(edge_used_for_problem)
                    latex_problems.append(f"({problem_number}) {edge_used_for_problem}と垂直に交わる辺を全て答えなさい。")
                    vertical_edges = list(vertical_edges_groups[edge_used_for_problem])
                    vertical_edges.sort()
                    latex_answers.append(f"({problem_number}) {', '.join(vertical_edges)}")
            elif selected_problem_type == "line_and_flat":
                if random() > 0.5:
                    problem_checker = random()
                    """
                    all_flats_candidates = list(set(all_flats) - set(used_flats_for_edge))
                    selected_flat = choice(all_flats_candidates)
                    used_flats_for_edge.append(selected_flat)
                    """
                    if problem_checker < 0.33:
                        all_flats_candidates = list(set(all_flats) - set(used_flats_for_edge))
                        selected_flat = choice(all_flats)
                        used_flats_for_edge.append(selected_flat)
                        latex_problems.append(f"({problem_number}) {selected_flat}にふくまれる辺を全て答えなさい。")
                        including_edges = [edge for edge in all_edges if (edge[1] in selected_flat) and (edge[2] in selected_flat)]
                        including_edges.sort()
                        latex_answers.append(f"({problem_number}) {', '.join(including_edges)}")
                    elif 0.33 <= problem_checker < 0.66:
                        all_flats_candidates = ["面ABC", "面DEF"]
                        selected_flat = choice(all_flats_candidates)
                        latex_problems.append(f"({problem_number}) {selected_flat}と垂直な辺を全て答えなさい。")
                        vertical_edges = ["辺AD", "辺BE", "辺CF"]
                        latex_answers.append(f"({problem_number}) {', '.join(vertical_edges)}")
                    else:
                        all_flats_candidates = ["面ABC", "面DEF"]
                        selected_flat = choice(all_flats_candidates)
                        latex_problems.append(f"({problem_number}) {selected_flat}と平行な辺を全て答えなさい。")
                        if selected_flat == "面ABC":
                            parallel_edges = ["辺DE", "辺EF", "辺DF"]
                        elif selected_flat == "面DEF":
                            parallel_edges = ["辺AB", "辺BC", "辺AC"] 
                        latex_answers.append(f"({problem_number}) {', '.join(parallel_edges)}")
                else:
                    problem_checker = random()
                    all_edges_candidates = list(set(all_edges) - set(used_edges_for_flat))
                    selected_edge = choice(all_edges_candidates)
                    used_edges_for_flat.append(selected_edge)
                    if problem_checker < 0.33:
                        latex_problems.append(f"({problem_number}) {selected_edge}をふくむ面を全て答えなさい。")
                        including_flats = [flat for flat in all_flats if (selected_edge[1] in flat) and (selected_edge[2] in flat)]
                        including_flats.sort()
                        latex_answers.append(f"({problem_number}) {', '.join(including_flats)}")
                    elif 0.33 <= problem_checker < 0.66:
                        latex_problems.append(f"({problem_number}) {selected_edge}に垂直な面を全て答えなさい。")
                        vertical_flats = [flat for flat in all_flats if (selected_edge[1] in flat) != (selected_edge[2] in flat)]
                        vertical_flats.sort()
                        latex_answers.append(f"({problem_number}) {', '.join(vertical_flats)}")
                    else:
                        latex_problems.append(f"({problem_number}) {selected_edge}に平行な面を全て答えなさい。")
                        parallel_flats = [flat for flat in all_flats if (selected_edge[1] not in flat) and (selected_edge[2] not in flat)]
                        parallel_flats.sort()
                        latex_answers.append(f"({problem_number}) {', '.join(parallel_flats)}")
            elif selected_problem_type == "flat_and_flat":
                all_flats_candidates = list(set(all_flats) - set(used_flats_for_flat))
                selected_flat = choice(all_flats_candidates)
                used_flats_for_flat.append(selected_flat)
                latex_problems.append(f"({problem_number}) {selected_flat}と垂直に交わる面を全て答えなさい。")
                vertical_flats = list(vertical_flats_groups[selected_flat])
                vertical_flats.sort()
                latex_answers.append(f"({problem_number}) {', '.join(vertical_flats)}")
            else:
                raise ValueError(f"'selected_problem_type' is {selected_problem_type}."\
                                 "This must be 'line_and_line', 'line_and_flat' or 'flat_and_flat'.")
        return latex_answers, latex_problems

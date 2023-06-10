from random import choice, random, sample, shuffle
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
            "面EFGH": ("面AEFB", "面BFGC", "面CGHD", "面ADHE"),
        }
        used_parallel_edges_groups = []
        used_edges_for_skew = []
        used_edges_for_vertical = []
        used_edges_for_flat = []
        used_flats_for_edge = []
        used_flats_for_parallel_flat = []
        used_flats_for_vertical_flat = []
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
                if random() > 0.5:
                    all_flats_candidates = list(set(all_flats) - set(used_flats_for_parallel_flat))
                    selected_flat = choice(all_flats_candidates)
                    used_flats_for_parallel_flat.append(selected_flat)
                    parallel_flats = list(set(all_flats) - set([selected_flat]) - set(vertical_flats_groups[selected_flat]))
                    collect_flat = choice(parallel_flats)
                    wrong_flats = sample(set(all_flats) - (set(parallel_flats)) - set([selected_flat]), 3)
                    flats_choice = wrong_flats + [collect_flat]
                    shuffle(flats_choice)
                    latex_problem = f"({problem_number}) {selected_flat}に平行な面を以下から一つ選びなさい。 "
                    latex_problem += f"({', '.join(flats_choice)})"
                    latex_problems.append(latex_problem)
                    latex_answers.append(f"({problem_number}) {collect_flat}")
                else:
                    all_flats_candidates = list(set(all_flats) - set(used_flats_for_vertical_flat))
                    selected_flat = choice(all_flats_candidates)
                    used_flats_for_vertical_flat.append(selected_flat)
                    vertical_flats = vertical_flats_groups[selected_flat]
                    collect_flat = choice(vertical_flats)
                    wrong_flat = list(set(all_flats) - set(vertical_flats) - set([selected_flat]))
                    flats_choice = [collect_flat] + wrong_flat
                    shuffle(flats_choice)
                    latex_problem = f"({problem_number}) {selected_flat}に垂直な面を以下から一つ選びなさい。 "
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
                    edge_used_for_problem, *remained_edges = sample(selected_parallel_edges, 4)
                    latex_problems.append(f"({problem_number}) {edge_used_for_problem}と平行な辺を全て答えなさい。")
                    remained_edges = ", ".join(sorted(remained_edges))
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
        used_edges_for_skew_edge = []
        used_edges_for_vertical_edge = []
        used_edges_for_including_flat = []
        used_edges_for_vertical_flat = []
        used_edges_for_parallel_flat = []
        used_flats_for_including_edge = []
        used_flats_for_vertical_flat = []
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
                    latex_answers.append(f"({problem_number}) {collect_edge}")
                elif 0.33 <= problem_checker < 0.66:
                    all_edges_candidates = list(set(all_edges) - set(used_edges_for_skew_edge))
                    edge_used_for_problem = choice(all_edges_candidates)
                    used_edges_for_skew_edge.append(edge_used_for_problem)
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
                    all_edges_candidates = list(set(all_edges) - set(used_edges_for_vertical_edge))
                    edge_used_for_problem = choice(all_edges_candidates)
                    used_edges_for_vertical_edge.append(edge_used_for_problem)
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
                    if problem_checker < 0.33:
                        all_flats_candidates = list(set(all_flats) - set(used_flats_for_including_edge))
                        selected_flat = choice(all_flats_candidates)
                        used_flats_for_including_edge.append(selected_flat)
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
                        all_flats_candidates = ["面ABC", "面DEF"]
                        selected_flat = choice(all_flats_candidates)
                        vertical_edges = ["辺AD", "辺BE", "辺CF"]
                        collect_edge = choice(vertical_edges)
                        wrong_edges = sample(set(all_edges) - set(vertical_edges), 3)
                        edges_choice = wrong_edges + [collect_edge]
                        shuffle(edges_choice)
                        latex_problem = f"({problem_number}) {selected_flat}と垂直な辺を以下から一つ選びなさい。 "
                        latex_problem += f"({', '.join(edges_choice)})"
                        latex_problems.append(latex_problem)
                        latex_answers.append(f"({problem_number}) {collect_edge}")
                    else:
                        all_flats_candidates = ["面ABC", "面DEF"]
                        selected_flat = choice(all_flats_candidates)
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
                    if problem_checker < 0.33:
                        all_edges_candidates = list(set(all_edges) - set(used_edges_for_including_flat))
                        selected_edge = choice(all_edges_candidates)
                        used_edges_for_including_flat.append(selected_edge)
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
                        all_edges_candidates = list(set(["辺AD", "辺BE", "辺CF"]) - set(used_edges_for_vertical_flat))
                        selected_edge = choice(all_edges_candidates)
                        used_edges_for_vertical_flat.append(selected_edge)
                        vertical_flats = ["面ABC", "面DEF"]
                        collect_flat = choice(vertical_flats)
                        wrong_flats = list(set(all_flats) - set(vertical_flats))
                        flats_choice = wrong_flats + [collect_flat]
                        shuffle(flats_choice)
                        latex_problem = f"({problem_number}) {selected_edge}に垂直な面を以下から一つ選びなさい。 "
                        latex_problem += f"({', '.join(flats_choice)})"
                        latex_problems.append(latex_problem)
                        latex_answers.append(f"({problem_number}) {collect_flat}")
                    else:
                        all_edges_candidates = list(set(["辺AB", "辺BC", "辺AC", "辺DE", "辺EF", "辺DF"]) - set(used_edges_for_parallel_flat))
                        selected_edge = choice(all_edges_candidates)
                        used_edges_for_parallel_flat.append(selected_edge)
                        if ("A" in selected_edge) or ("B" in selected_edge) or ("C" in selected_edge):
                            collect_flat = "面DEF"
                        else:
                            collect_flat = "面ABC"
                        wrong_flats = sample(set(all_flats) - set([collect_flat]), 3)
                        flats_choice = wrong_flats + [collect_flat]
                        shuffle(flats_choice)
                        latex_problem = f"({problem_number}) {selected_edge}に平行な面を以下から一つ選びなさい。"
                        latex_problem += f"({', '.join(flats_choice)})"
                        latex_problems.append(latex_problem)
                        latex_answers.append(f"({problem_number}) {collect_flat}")
            elif selected_problem_type == "flat_and_flat":
                if random() > 0.5:
                    all_flats_candidates = list(set(all_flats) - set(used_flats_for_vertical_flat))
                    selected_flat = choice(all_flats_candidates)
                    used_flats_for_vertical_flat.append(selected_flat)
                    vertical_flats = vertical_flats_groups[selected_flat]
                    collect_flat = choice(vertical_flats)
                    wrong_flats = list(set(all_flats) - set(vertical_flats) - set([selected_flat]))
                    flats_choice = [collect_flat] + wrong_flats
                    shuffle(flats_choice)
                    latex_problem = f"({problem_number}) {selected_flat}と垂直な面を以下から一つ選びなさい。"
                    latex_problem += f"({', '.join(flats_choice)})"
                    latex_problems.append(latex_problem)
                    latex_answers.append(f"({problem_number}) {collect_flat}")
                else:
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
        used_edges_for_vertical_edge = []
        used_edges_for_skew_edge = []
        used_edges_for_including_flat = []
        used_edges_for_vertical_flat = []
        used_edges_for_parallel_flat = []
        used_flats_for_including_edge = []
        used_flats_for_vertical_flat = []
        for problem_number in range(1, 4):
            selected_problem_type = choice(problem_types)
            if selected_problem_type == "line_and_line":
                problem_checker = random()
                if problem_checker < 0.33:
                    parallel_edges_candidates = list(set(parallel_edges_groups) - set(used_parallel_edges_groups))
                    selected_parallel_edges = choice(parallel_edges_candidates)
                    used_parallel_edges_groups.append(selected_parallel_edges)
                    edge_used_for_problem = choice(selected_parallel_edges)
                    latex_problems.append(f"({problem_number}) {edge_used_for_problem}と平行な辺を全て答えなさい。")
                    parallel_edges_without_edge_used_for_problem = list(set(selected_parallel_edges) - set([edge_used_for_problem]))
                    latex_answers.append(f"({problem_number}) {', '.join(parallel_edges_without_edge_used_for_problem)}")
                elif 0.33 <= problem_checker < 0.66:
                    all_edges_candidates = list(set(all_edges) - set(used_edges_for_skew_edge))
                    edge_used_for_problem = choice(all_edges_candidates)
                    used_edges_for_skew_edge.append(edge_used_for_problem)
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
                    all_edges_candidates = list(set(all_edges) - set(used_edges_for_vertical_edge))
                    edge_used_for_problem = choice(all_edges_candidates)
                    used_edges_for_vertical_edge.append(edge_used_for_problem)
                    latex_problems.append(f"({problem_number}) {edge_used_for_problem}と垂直に交わる辺を全て答えなさい。")
                    vertical_edges = list(vertical_edges_groups[edge_used_for_problem])
                    vertical_edges.sort()
                    latex_answers.append(f"({problem_number}) {', '.join(vertical_edges)}")
            elif selected_problem_type == "line_and_flat":
                if random() > 0.5:
                    problem_checker = random()
                    if problem_checker < 0.33:
                        all_flats_candidates = list(set(all_flats) - set(used_flats_for_including_edge))
                        selected_flat = choice(all_flats)
                        used_flats_for_including_edge.append(selected_flat)
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
                    if problem_checker < 0.33:
                        all_edges_candidates = list(set(all_edges) - set(used_edges_for_including_flat))
                        selected_edge = choice(all_edges_candidates)
                        used_edges_for_including_flat.append(selected_edge)
                        latex_problems.append(f"({problem_number}) {selected_edge}をふくむ面を全て答えなさい。")
                        including_flats = [flat for flat in all_flats if (selected_edge[1] in flat) and (selected_edge[2] in flat)]
                        including_flats.sort()
                        latex_answers.append(f"({problem_number}) {', '.join(including_flats)}")
                    elif 0.33 <= problem_checker < 0.66:
                        all_edges_candidates = list(set(["辺AD", "辺BE", "辺CF"]) - set(used_edges_for_vertical_flat))
                        selected_edge = choice(all_edges_candidates)
                        used_edges_for_vertical_flat.append(selected_edge)
                        latex_problems.append(f"({problem_number}) {selected_edge}に垂直な面を全て答えなさい。")
                        used_edges_for_vertical_flat.append(selected_edge)
                        vertical_flats = ["面ABC", "面DEF"]
                        latex_answers.append(f"({problem_number}) {', '.join(vertical_flats)}")
                    else:
                        all_edges_candidates = list(set(["辺AB", "辺BC", "辺AC", "辺DE", "辺EF", "辺DF"]) - set(used_edges_for_parallel_flat))
                        selected_edge = choice(all_edges_candidates)
                        used_edges_for_parallel_flat.append(selected_edge)
                        latex_problems.append(f"({problem_number}) {selected_edge}に平行な面を全て答えなさい。")
                        used_edges_for_parallel_flat.append(selected_edge)
                        if ("A" in selected_edge) or ("B" in selected_edge) or ("C" in selected_edge):
                            parallel_flat = "面DEF"
                        else:
                            parallel_flat = "面ABC"
                        latex_answers.append(f"({problem_number}) {parallel_flat}")
            elif selected_problem_type == "flat_and_flat":
                if random() > 0.5:
                    all_flats_candidates = list(set(all_flats) - set(used_flats_for_vertical_flat))
                    selected_flat = choice(all_flats_candidates)
                    used_flats_for_vertical_flat.append(selected_flat)
                    latex_problems.append(f"({problem_number}) {selected_flat}と垂直に交わる面を全て答えなさい。")
                    vertical_flats = list(vertical_flats_groups[selected_flat])
                    vertical_flats.sort()
                    latex_answers.append(f"({problem_number}) {', '.join(vertical_flats)}")
                else:
                    all_flats_candidates = ["面ABC", "面DEF"]
                    selected_flat, collect_flat = sample(all_flats_candidates, 2)
                    latex_problems.append(f"({problem_number}) {selected_flat}と平行な面を全て答えなさい。")
                    latex_answers.append(f"({problem_number}) {collect_flat}")
            else:
                raise ValueError(f"'selected_problem_type' is {selected_problem_type}."\
                                 "This must be 'line_and_line', 'line_and_flat' or 'flat_and_flat'.")
        return latex_answers, latex_problems

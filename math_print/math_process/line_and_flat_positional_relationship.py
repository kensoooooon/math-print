from random import choice, random, randint

import sympy as sy


class LineAndFlatPositionalRelationship:
    """直線と平面の位置関係の問題と解答を出力
    
    Attributes:
        latex_answer (str): latex形式で記述された解答
        latex_problem (str): latex形式で記述された問題
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
            self.latex_answer, self.latex_problem = self._make_quadrangular_prism_problem(problem_types)
        elif selected_solid_body == "triangular_prism":
            self.solid_body = "triangular_prism"
            self.latex_answer, self.latex_problem = self._make_triangular_prism_problem(problem_types)
        else:
            raise ValueError(f"'selected_solid_body' is {selected_solid_body}. This must be 'quadrangular_prism' or 'triangular_prism.")
    
    def _make_quadrangular_prism_problem(self, problem_types):
        """直方体を用いた直線と平面の位置関係の問題を作成

        Args:
            problem_types (list): 使用される問題(直線と直線, 直線と平面, 平面と平面)が格納されている

        Returns:
            latex_answer (str): latex形式で記述された解答
            latex_problem (str): latex形式で記述された問題
        
        Developing:
            上面左手前から反時計回りでABCD, EFGHの直方体
            答えさせる問題のタイプ
            -> ある辺に平行な直線は？
            -> ある辺と垂直な直線は？
            -->> 直線同士の位置関係
            -->> 平面同士の位置関係
            -->> 直線と平面の位置関係
        """
        latex_answer = ""
        latex_problem = ""
        for problem_number in range(1, 4):
            selected_problem_type = choice(problem_types)
            if selected_problem_type == "line_and_line":
                """
                二直線の位置関係
                -> 平行, ねじれ, 垂直に交わる, (垂直以外に交わる)
                """
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
                    latex_answer += f"({problem_number}) {remained_edges} <br>"
                    latex_problem += f"({problem_number}) {edge_used_for_problem}と平行な辺を答えなさい。<br>"
                # skew edge
                elif 0.33 <= problem_checker < 0.66:
                    """
                    # total
                    from random import choice, randint


                    all_edges = [
                        "辺AB", "辺BC", "辺CD", "辺AD",
                        "辺AE", "辺BF", "辺CG", "辺DH",
                        "辺EF", "辺FG", "辺GH", "辺EH",
                    ]
                    parallel_edges_groups = (
                        ["辺AB", "辺CD", "辺EF", "辺GH",],
                        ["辺AD", "辺BC", "辺EH", "辺FG",],
                        ["辺AE", "辺BF", "辺CG", "辺DH",],
                        )
                    edge_used_for_problem = "辺AB"
                    for parallel_edges in parallel_edges_groups:
                        if edge_used_for_problem in parallel_edges:
                            parallel_edges_with_edge_used_for_problem = parallel_edges
                    print(parallel_edges_with_edge_used_for_problem)
                    edges_without_parallel = list(set(all_edges) - set(parallel_edges_with_edge_used_for_problem))
                    print(edges_without_parallel)
                    first_alphabet = edge_used_for_problem[1]
                    second_alphabet = edge_used_for_problem[2]
                    skew_edges = [edge for edge in edges_without_parallel if (first_alphabet not in edge) and (second_alphabet not in edge)]
                    print(skew_edges)
                    vertical_edges = [edge for edge in edges_without_parallel if (first_alphabet in edge) or (second_alphabet in edge)]
                    print(vertical_edges)
                    """
                    all_edges = [
                        "辺AB", "辺BC", "辺CD", "辺AD",
                        "辺AE", "辺BF", "辺CG", "辺DH",
                        "辺EF", "辺FG", "辺GH", "辺EH",
                    ]
                    edge_used_for_problem = choice(all_edges)
                    print(f"edge_used_for_problem: {edge_used_for_problem}")
                    latex_problem += f"({problem_number}) {edge_used_for_problem}とねじれの位置にある辺を答えなさい。<br>"
                    parallel_edges_group = (
                        ["辺AB", "辺CD", "辺EF", "辺GH",],
                        ["辺AD", "辺BC", "辺EH", "辺FG",],
                        ["辺AE", "辺BF", "辺CG", "辺DH",],
                        )
                    for parallel_edges in parallel_edges_group:
                        if edge_used_for_problem in parallel_edges:
                            parallel_edges_with_edge_used_for_problem = parallel_edges
                            break
                    print(f"parallel_edges_with_edge_used_for_problem: {parallel_edges_with_edge_used_for_problem}")
                    edges_without_parallel = list(set(all_edges) - set(parallel_edges_with_edge_used_for_problem))
                    first_alphabet = edge_used_for_problem[1]
                    second_alphabet = edge_used_for_problem[2]
                    skew_edges = [edge for edge in edges_without_parallel if (first_alphabet not in edge) and (second_alphabet not in edge)]
                    latex_answer += f"({problem_number}) {', '.join(skew_edges)}"
                # vertical edge
                else:
                    all_edges = [
                        "辺AB", "辺BC", "辺CD", "辺AD",
                        "辺AE", "辺BF", "辺CG", "辺DH",
                        "辺EF", "辺FG", "辺GH", "辺EH",
                    ]
                    edge_used_for_problem = choice(all_edges)
                    latex_problem += f"({problem_number}) {edge_used_for_problem}と垂直に交わる辺を答えなさい。<br>"
                    parallel_edges_group = (
                        ["辺AB", "辺CD", "辺EF", "辺GH",],
                        ["辺AD", "辺BC", "辺EH", "辺FG",],
                        ["辺AE", "辺BF", "辺CG", "辺DH",],
                        )
                    for parallel_edges in parallel_edges_group:
                        if edge_used_for_problem in parallel_edges:
                            parallel_edges_with_edge_used_for_problem = parallel_edges
                            break
                    print(f"parallel_edges_with_edge_used_for_problem: {parallel_edges_with_edge_used_for_problem}")
                    edges_without_parallel = list(set(all_edges) - set(parallel_edges_with_edge_used_for_problem))
                    first_alphabet = edge_used_for_problem[1]
                    second_alphabet = edge_used_for_problem[2]
                    vertical_edges = [edge for edge in edges_without_parallel if (first_alphabet in edge) or (second_alphabet in edge)]
                    latex_answer += f"({problem_number}) {', '.join(vertical_edges)} <br>"
            elif selected_problem_type == "line_and_flat":
                latex_answer = "dummy answer in line_and_flat"
                latex_problem = "dummy problem in line_and_flat"
            elif selected_problem_type == "flat_and_flat":
                latex_answer = "dummy answer in flat_and_flat"
                latex_problem = "dummy problem in flat_and_flat"
            else:
                raise ValueError(f"'selected_problem_type' is {selected_problem_type}."\
                                 "This must be 'line_and_line', 'line_and_flat' or 'flat_and_flat'.")
            print("-------------------------------")
        return latex_answer, latex_problem
    
    def _make_triangular_prism_problem(self):
        """三角柱を用いた直線と平面の位置関係の問題を作成

        Returns:
            latex_answer (str): latex形式で記述された解答
            latex_problem (str): latex形式で記述された問題
        """
        latex_answer = "dummy answer in triangular problem."
        latex_problem = "dummy problem in triangular problem."
        return latex_answer, latex_problem
    
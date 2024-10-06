"""
10/4
作成開始。ガワの作成完了

10/5
htmlファイルの受け入れ開始。サンプル問題解答の出力は完了

数学処理のロジック考案開始。
    どうやら、単純な計算では指定した形にならなさそう。
    微分から逆算する方法もあるが、あまり綺麗にはならない。
    問題のタイプを絞って、手作業で計算する？
    →とりあえず(ax+b)^m(cx+d)^nをターゲットに。
    →→瞬間部分積分を利用して、全体を処理できるようにしたほうが楽そう？
    逆算＋瞬間部分積分のロジックは？
        どこまでやるべきか？がものによって異なる系
        多項式×多項式型では、微分サイドが定数に落ちるまで。eg. 3次→2, 1, 0で3回分
        微分サイドと積分サイドの決め方は、基本的に次数が低い方を微分サイドとする
        import sympy as sy

        x = sy.Symbol("x", real=True)

        f = x
        g = (x - 1) ** 5
        print(sy.degree(f, x))
        print(sy.degree(g, x))
        print("---------------------------------")
        f_minus1 = sy.diff(f, x)
        g_minus1 = sy.diff(g, x)
        print(sy.degree(f_minus1, x))
        print(sy.degree(g_minus1, x))

from random import randint
import sympy as sp

# シンボリック変数 x の定義
x = sp.Symbol("x", real=True)

def make_linear_pow_function():
    # ランダムな a, b, m の生成
    a = randint(1, 3)
    b = randint(1, 3)
    m = randint(1, 5)
    
    # 初期係数 k と初期関数
    k = 1
    functions = [k * (a * x + b) ** m]
    
    # 微分を繰り返し、関数リストに追加
    while m > 1:
        k *= m * a  # 係数の累積更新
        m = m - 1
        functions.append(k * (a * x + b) ** m)
    
    return functions

# 関数を呼び出して結果を表示
print(make_linear_pow_function())

from random import randint
import sympy as sp

# シンボリック変数 x の定義
x = sy.Symbol("x", real=True)

def make_linear_pow_function(a, b, m):   
    # 初期係数 k と初期関数
    k = 1
    functions = [k * (a * x + b) ** m]
    
    # 微分を繰り返し、関数リストに追加
    while m > 1:
        k *= m * a  # 係数の累積更新
        m = m - 1
        functions.append(k * (a * x + b) ** m)
    
    return functions

# 関数を呼び出して結果を表示
print(make_linear_pow_function(3, -4, 2))


全体を確立できるロジックが難しい状態。特に()の外れ方あたりが、そこそこに工夫しないとまずそう。因数分解の追加？
積分サイドは全く未定。おそらく、微分側から逆算して、そこから微分していくようにしてたどる形がよいと思われ？

import sympy as sy

x = sy.Symbol('x', real=True)

def make_linear_pow_function(a, b, m, target_degree):
    # 初期係数 k と初期関数
    k = 1
    functions = [k * (a * x + b) ** m]
    
    # for文を使用して、mからtarget_degreeまで微分を繰り返す
    for current_degree in range(m, target_degree, -1):
        k *= current_degree * a  # 係数の累積更新
        factored_function = sy.factor(k * (a * x + b) ** (current_degree - 1))
        functions.append(factored_function)
    
    return functions

f = 0
functions1 = make_linear_pow_function(2, 3, 3, 0)
functions2 = make_linear_pow_function(-2, 1, 4, 1)[::-1]
for f1, f2 in zip(functions1, functions2):
    print(f1)
    print(f2)
    print(f1 * f2)
    f += f1 * f2
    print("---------------")
    
display(f)

微分サイドは基本的に積分サイドより低次数であるべき
計算が楽だから。

import sympy as sy

x = sy.Symbol('x', real=True)

def make_linear_pow_function(a, b, m, target_degree):
    # 初期係数 k と初期関数
    k = 1
    functions = [k * (a * x + b) ** m]
    
    # for文を使用して、mからtarget_degreeまで微分を繰り返す
    for current_degree in range(m, target_degree, -1):
        k *= current_degree * a  # 係数の累積更新
        factored_function = sy.factor(k * (a * x + b) ** (current_degree - 1))
        functions.append(factored_function)
    
    return functions

f = 0
functions1 = make_linear_pow_function(2, -5, 2, 0)
functions2 = make_linear_pow_function(2, 3, 4, 3)[::-1]
for f1, f2 in zip(functions1, functions2):
    print(f1)
    print(f2)
    print(f1 * f2)
    f += f1 * f2
    print("---------------")
    
display(f)

次数は概ねあってきたが、次数側がズレている

10/6
係数のなんとなくのズレがある
    微分側と積分側を同じ関数で処理していることが原因っぽい？
    微分側は、順調に係数を計算していけばよいが、積分側は逆算する必要がある模様
    なんとなく、両端から微分で攻めていくというイメージは間違ってはいないと思われるが、
    →微分サイドが定数になるまでの次数を考える
    →その分特定の式の階数を先にみておいて、計算自体はあくまで微分で処理する
    
    eg. x(x-1)^5 dx 
    = x・1/6(x-1)^6 - ∫1・1/6(x-1)^7
    = x・1/6(x-1)^6 - 1・1/6・1/7(x-1)^7+C
    = 1/42(x - 1)^6 ・((1/6)/(1/42)x-(x - 1)) + C
    = 1/42(x - 1)^6(6x + 1) + C
    
    
    左辺は1次→0次
    右辺は5次→6次からの6次→7次
        つまり、逆算して、6次→5次の7次6次で計算する
        6次であることから、あらかじめ答えの積分側に1/6を置いておく必要がある
        置いておかないと、係数が少しずつ累積していく
        追加で、積分後の係数も置いておく必要がある
            係数は次数の逆数になっている？
"""
from random import choice, randint

import sympy as sy

class IntegrationByPartsProblem:
    """部分積分の問題と解答を作成し、出力
    
    Attributes:
        latex_answer (str): latex形式で記述された解答
        latex_problem (str): latex形式で記述された問題
    """
    def __init__(self, **settings):
        """初期設定
        
        Args:   
            settings (dict): 部分積分のタイプと、定積分か不定積分かの指定を含む
        
        Raises:
            ValueError: 想定していないタイプの問題が指定されたときに送出
        """
        selected_calculation_type = choice(settings["types_of_integration_by_parts"])
        selected_integral_type = choice(settings["integral_types"])
        if selected_calculation_type == "double_polynomial":
            self.latex_answer, self.latex_problem = self._make_double_polynomial_problem(selected_integral_type)
        else:
            raise ValueError(f"'selected_calculate_type' is {selected_calculation_type}. It isn't expected value.")
    
    def _make_double_polynomial_problem(self, selected_integral_type):
        """(多項式) x (多項式)型の部分積分の問題・解答を作成
        
        Args:
            selected_integral_type (str): indefinite_integral(不定積分)かdefinite_integral(定積分)のいずれかを指定
        
        Returns:
            latex_answer (str): latex形式で記述されていることを前提とした解答
            latex_problem (str): latex形式で記述されていることを前提とした問題
        """
        if selected_integral_type == "indefinite_integral":
            latex_answer = "This is dummy answer."
            latex_problem = "This is dummy problem."
        elif selected_integral_type == "definite_integral":
            latex_answer = "This is dummy answer."
            latex_problem = "This is dummy problem."
        else:
            raise ValueError(f"'selected_integral_type' must be 'indefinite_integral' or 'definite_integral'. {selected_integral_type} must be wrong.")
        return latex_answer, latex_problem

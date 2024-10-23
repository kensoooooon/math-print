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

10/19
import sympy as sy

x = sy.Symbol('x', real=True)

f = ((3 * x - 4) ** 2) * ((x - 2) ** 3)
display(f)
f_plus1 = sy.integrate(f, x)
display(f_plus1)

g = (
    ((3 * x - 4) ** 2) * (sy.Rational(1, 4) * (x - 2) ** 4) 
    - 2 * 3 * (3 * x - 4) * (sy.Rational(1, 4) * sy.Rational(1, 5) * (x - 2) ** 5) 
    + 2 * 3 * 3 * 1 * (sy.Rational(1, 4) * sy.Rational(1, 5) * sy.Rational(1, 6) * (x - 2) ** 6)
)
display(sy.expand(g))
print(g == f)

瞬間部分積分の計算的な認識はあっている

import sympy as sy

x = sy.Symbol('x', real=True)
f = (3 * x - 4) ** 2
display(f)
f_minus1 = sy.factor(sy.diff(f, x))
display(f_minus1)
f_minus2 = sy.factor(sy.diff(f_minus1, x))
display(f_minus2)

g = sy.Rational(1, 6) * sy.Rational(1, 7) * sy.Rational(1, 8) * (x - 2) ** 8
display(g)
g_minus1 = sy.diff(g, x)
display(g_minus1)
g_minus2 = sy.diff(g_minus1, x)
display(g_minus2)
g_minus3 = sy.diff(g_minus2, x)
display(g_minus3)

あとはmore, lessと関連付ける。それと、適当な手に負える程度の係数に留める必要がある

from random import choice, randint
import sympy as sy

def random_integer(a, b, including_zero=True):
    if including_zero:
        return randint(a, b)
    else:        
        if a <= 0 <= b:
            # 0を避けて範囲を分割
            return choice(list(range(a, 0)) + list(range(1, b + 1)))
        else:
            # 0が範囲に含まれていない場合
            return randint(a, b)

sy.init_printing(order='grevlex')
        
x = sy.Symbol('x', real=True)
        
less_dimension = 2
more_dimension = 5

a1 = random_integer(1, 3, including_zero=False)
b1 = random_integer(-2, 2, including_zero=False)
f = (a1 * x + b1) ** less_dimension
display(f)

for i in range(1, less_dimension + 1):
    fn = sy.diff(f, x, i)
    display(sy.factor(fn, x))

print("-------------")
a2 = random_integer(-2, 2, including_zero=False)
b2 = random_integer(-2, 2)
g = (a2 * x + b2) ** more_dimension
display(g)

for i in range(1, less_dimension + 1):



from random import choice, randint
import sympy as sy

def random_integer(a, b, including_zero=True):
    if including_zero:
        return randint(a, b)
    else:        
        if a <= 0 <= b:
            # 0を避けて範囲を分割
            return choice(list(range(a, 0)) + list(range(1, b + 1)))
        else:
            # 0が範囲に含まれていない場合
            return randint(a, b)

sy.init_printing(order='grevlex')
        
x = sy.Symbol('x', real=True)
        
less_dimension = 2
more_dimension = 5

a1 = random_integer(1, 3, including_zero=False)
b1 = random_integer(-2, 2, including_zero=False)
f = (a1 * x + b1) ** less_dimension
display(f)

for i in range(1, less_dimension + 1):
    fn = sy.diff(f, x, i)
    display(sy.factor(fn, x))

print("-------------")
a2 = random_integer(-2, 2, including_zero=False)
b2 = random_integer(-2, 2)
g = (a2 * x + b2) ** more_dimension
display(g)

for i in range(1, less_dimension + 1):

10/22
多項式×多項式のロジックを引き続き考える。
ある程度は関係性がわかってきた

# 積分の係数周り
less側+1だけ積分、つまり逆側の微分が必要になる
more側の指数+1, +2, +3, ...のように逆数を配置する必要がある
    1 / (more + (less + 1))のような係数を配置する
    分母はmore + (less + 1), more + less, more + less - 1のように、more + (less + 1)を起点として、less分だけ落とす必要がある

from random import choice, randint
import sympy as sy

sy.init_printing(order='grevlex')

def step_factorial(start, end):
    result = 1
    for i in range(start, end + 1):
        result *= i
    return result

def random_integer(a, b, including_zero=True):
    if including_zero:
        return randint(a, b)
    else:        
        if a <= 0 <= b:
            # 0を避けて範囲を分割
            return choice(list(range(a, 0)) + list(range(1, b + 1)))
        else:
            # 0が範囲に含まれていない場合
            return randint(a, b)

x = sy.Symbol('x', real=True)

less_dimension = 2
a1 = random_integer(-2, 2, including_zero=False)
b1 = random_integer(-2, 2)
f = (a1 * x + b1) ** 2
display(f)
fs = []
fs.append(f)
for i in range(1, less_dimension + 1):
    diff_f = sy.diff(f, x, i)
    display(sy.factor(diff_f))
    fs.append(diff_f)

print("-----------------")
more_dimension = 5
a2 = random_integer(-2, 2, including_zero=False)
b2 = random_integer(-2, 2)
g = (a2 * x + b2) ** more_dimension
display(g)
denom = step_factorial(more_dimension + 1, more_dimension + 1 + less_dimension)
print(denom)
g_plus = sy.Rational(1, denom) * (a2 * x + b2) ** (more_dimension + (less_dimension + 1))
display(g_plus)
gs = []
for i in range(1, less_dimension + 1):
    diff_g_plus = sy.diff(g_plus, x, i)
    display(diff_g_plus)
    gs.append(diff_g_plus)

gs.reverse()

10/23
それぞれの項を出すための計算方法は概ね定まった。

from random import choice, randint
import sympy as sy

sy.init_printing(order='grevlex')

def step_factorial(start, end):
    result = 1
    for i in range(start, end + 1):
        result *= i
    return result

def random_integer(a, b, including_zero=True):
    if including_zero:
        return randint(a, b)
    else:        
        if a <= 0 <= b:
            # 0を避けて範囲を分割
            return choice(list(range(a, 0)) + list(range(1, b + 1)))
        else:
            # 0が範囲に含まれていない場合
            return randint(a, b)

x = sy.Symbol('x', real=True)

less_dimension = 2
# a1 = random_integer(-2, 2, including_zero=False)
a1 = 3
# b1 = random_integer(-2, 2)
b1 = -4
f = (a1 * x + b1) ** 2
display(f)
fs = [f, f]
for i in range(1, less_dimension + 1):
    diff_f = sy.diff(f, x, i)
    display(sy.factor(diff_f))
    fs.append(diff_f)

print("-----------------")
more_dimension = 5
# a2 = random_integer(-2, 2, including_zero=False)
a2 = 1
# b2 = random_integer(-2, 2)
b2 = -2
g = (a2 * x + b2) ** more_dimension
display(g)
denom = step_factorial(more_dimension + 1, more_dimension + 1 + less_dimension)
g_plus = sy.Rational(1, denom) * (a2 * x + b2) ** (more_dimension + (less_dimension + 1))
display(g_plus)
gs = [g_plus]
for i in range(1, less_dimension + 1):
    diff_g_plus = sy.diff(g_plus, x, i)
    display(diff_g_plus)
    gs.append(diff_g_plus)

gs.reverse()
gs = [g] + gs

print("-------------------")
print(f"fs length: {len(fs)}")
print(fs)
print(f"gs length: {len(gs)}")
print(gs)
result = 0
for index, (left, right) in enumerate(zip(fs, gs)):
    if index % 2 == 0:
        sign = +1
    else:
        sign = -1
    result += sign * (left * right)

display(result)

あとは、表示と計算をどこまで行うか？という話になってくる
    瞬間部分積分を前提とするのであれば、+, -を順番に書いていく形でほぼ事足りる

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

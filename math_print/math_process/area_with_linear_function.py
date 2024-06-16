"""
5/30

どこに1次関数の情報をねじ込むか？
    linear_function_with_graphでは、
        self.selected_problem_type, self.graph_to_use, self.linear_functionでreturnした上で、
        "{{ information_tuple.0.selected_problem_type }}" == "with_grid_to_linear_function"や
        var left_x1 = Number({{ information_tuple.0.linear_function.x1 }});
        として渡している
    
    同じように渡せるのは渡せるが、問題は渡し方
        リストやタプルでは番号になるため、linear_function1.x1, linear_function2.y2のように、名前を変えられた方が望ましい
            とりあえずself....で渡せば、名前で呼び出せることはわかっているので、それを使う？
            何かしらを使ってよりわかりやすい構造にできないか？？というのもある
            他のものを使うか。あるいは同じにしつつも、構造だけは変えるか。
            ↑スピード重視で、そのまま使う。こっちのPythonファイルの見づらさはとりあえず目をつむる系で
    
    何を渡すか？
        with_graphでなければ、そもそも通る点を使う必要がなさそうではある
        with_graphなら当然に必須
        
        問題文や答えが必要な点も要注目
            あちらはグラフを描くことだけに絞っていたが、こちらは最低限「～～～の面積を求めよ。が必要になる。」
            同様に、解答もある程度解説する必要がありそう。
            超大作～
        
        概ね方針がお定まりした上で、どこから取り組むか？？
            テスト速度優先であれば、とりあえずグラフだけ渡して読ませるというのも一つの手段。
                そもそも3本の直線とその交点、三角形をすんなり描写できるかというのが怪しい
                手順としては、まずはこちら側でいじって、それから向こうでグラフの描写を行う
                + 問題設定にグラフの表示の有無を設定？
                    全部一律で表示するのでなければ、問題文もあわせて切り替える必要が出てくる
                    結局のところ、単純に手間が増加するのは間違いないため、それに見合うほどか？？という話になる
                        eナビもカワセミも、ざっと確認した限りはグラフありきの問題なので、それはなしでokそう
        
        というわけで、とりあえずlinear_functionを3つ分ここに用意することから始める

5/31
linear_function3つ分の用意から始める

jsのdrawLinearFunctionが悪さをしている
    そもそも、値が存在していない説？
        中で確認したら、0, 0, 0, 0だった。たまたま？
        でもなさそう。もう一つ遡って確認する
        
    
    多分self.をlinear_function1, 2, 3につけ忘れていたのが原因っぽい

6/1
linear_functionの修正から
    単純な直線だけだと、描画されている範囲に収まらない。あるは下手すると、平行な直線が出てそもそも三角形にならない場合がある
    初めに点を決めて、そこから直線を導く必要がある。
        点の決め方にも、「軸に沿う2点+1点」と「軸に沿わない3点」でチェックする必要がある
        linear_functionを分割すべきか？というチェック事項もある
            そもそも、ロジックが大幅に変わりそうな気配を感じるので、分けて置いた方が無難？
            分け方として、「機能を抽出する」という考え方が利用できるかも？？

            「軸に沿う2点+1点」

6/5
引き続き直線の扱い
    3点を定めて、そこからもう一点を定めるという方針でよさそう
    描画の方はあまり触りたくないので、linear_functionのステータス自体は触らずにいたい系
    クラス内クラスで置きかえてあげる？
    やっぱり問題ごとに点の作り方がごろっと違うので、LinearFunctionは共有しつつ、作り方はしっかりと変えたほうが良さそう
        若干不明なところはあるが、やはりわかりづらいので、とりあえず軸＋１点からぼちぼち動かしていく

6/7
まずは問題ごとに、3点を決定して扱う方法から。

それとは別件で、やはり「0以外or0も含む整数を与えるランダム関数」みたいなのは合ったほうが良いかも？

6/8
直線の作成から
    「2点を通る直線を求める」という計算は頻出しそうだから、メソッドとして作成する系
    
返すのはEqでよいのか？という疑惑がある
    文字列で

どうせ3点からの計算は必須だよね
    公式で計算できるように
    
描画が軸の存在をあまり想定していないような気がする

function drawLinearFunction(stage, x1, y1, x2, y2) {
    /*
    多分線分で直線を引くから、端っこを計算している感じ
        x = -7, 7, y=-7, 7のいずれかは必ず通るはずなので、そこを終点として計算している感じがある。
    */
    // x = -7, 7 |  y= -7, 7 check
    console.log(`x1: ${x1}`);
    console.log(`x1: ${y1}`);
    console.log(`x1: ${x2}`);
    console.log(`x1: ${y2}`);
    let linear_coefficient = (y2 - y1) / (x2 - x1)
    let intercept = -linear_coefficient * x1 + y1;
    let end_points = [];
    // x = -7 check
    let y_with_x_minus_7 = linear_coefficient * -7 + intercept;
    if (Math.abs(y_with_x_minus_7) <= 7) {
        end_points.push([-7, y_with_x_minus_7]);
    }
    // y = -7 check
    let x_with_y_minus_7 = (-7 - intercept) / linear_coefficient;
    if (Math.abs(x_with_y_minus_7) <= 7) {
        let skip = false;
        for (let point of end_points) {
            if(point.toString() == [x_with_y_minus_7, -7].toString()) {
                skip = true;
                break;
            }
        }
        if (skip == false) {
            end_points.push([x_with_y_minus_7, -7]);  
        }
    }
    // x = 7 check
    let y_with_x_plus_7 = linear_coefficient * 7 + intercept;
    if (Math.abs(y_with_x_plus_7) <= 7) {
        let skip = false;
        for (let point of end_points) {
            if(point.toString() == [7, y_with_x_plus_7].toString()) {
                skip = true;
                break;
            }
        }
        if (skip == false) {
            end_points.push([7, y_with_x_plus_7]);  
        }
    }
    // y = 7 check
    let x_with_y_plus_7 = (7 - intercept) / linear_coefficient;
    if (Math.abs(x_with_y_plus_7) <= 7) {
        let skip = false;
        for (let point of end_points) {
            if(point.toString() == [x_with_y_plus_7, 7].toString()) {
                skip = true;
                break;
            }
        }
        if (skip == false) {
            end_points.push([x_with_y_plus_7, 7]);  
        }
    }
    let end_x1, end_y1, end_x2, end_y2;
    [[end_x1, end_y1], [end_x2, end_y2]] = end_points;
    // convert x1~y2 to pixel(320, 160)
    let end_x1_p = 160 + 10 * end_x1;
    let end_y1_p = 80 + 10 * -end_y1;
    let end_x2_p = 160 + 10 * end_x2;
    let end_y2_p = 80 + 10 * -end_y2;
    drawLine(stage, end_x1_p, end_y1_p, end_x2_p, end_y2_p);
    // y = -2 x + 7, y = -3 x + 14
    // (7, -7), (7, -7)
    // three points.
    stage.update();
}


↑していない系
特に、let linear_coefficient = (y2 - y1) / (x2 - x1)
でx1 = x2であるとエラーを吐き散らかす

    両方にそれぞれx1=x2の時に挙動を変化させるようなロジックを組む。
        こちらでは、x1 = x2(y軸)であれば、式にはx=....を出力するように。（点はとくに変化させない）
        あちらでは、ifでごっそり分岐させる系？？？
            多分動作があまり頭に入っていない。クソコードみがある。
            リファクタリングまでやる？それはそれで面倒でもあるが、後々のことを考えるとなしとまでは言い切れない
            
            そもそもどのような動作をしているのかは、いずれにしろ把握必須
            
            linear_coefficient_latex = sy.latex(a),
            intercept_latex = sy.latex(b)
            が何をしているのかも地味に不明。計算だけに使っているなら、まだ条件分岐でなんとかなりそうだが…
            →おそらく表示にしか使っていない。ないなら困らない気がするし、余計なものを付けたくないので、削除
    
    LaTexのケアの場所も把握していない
        こちら側で一律ケアする必要がある
        関数作成
    
    y=0のaxis周りのやつからがnext

6/9
y=0のaxis周りがよくわからん。
とりあえず黄色いところから

6/12
続き

とりあえず直線を表示チェックするところまでは進んだ
    ・時々エラーを吐く
        点が存在していない場合があるらしい
    ・描画が面積用にカスタマイズされていない
        3点を示すのではなく、それぞれの場所に①, ②を置き描画する必要がある。
    ・点の配置がマジで面倒っぽい??
        適当にA,B,Cでいける？
            zero_coordinateの設定がないと、とても面倒そう？名前で判別可能？？
            
    ・改行周りでそこそこの面倒も
        from django.template.defaultfilters import linebreaksbr

        def my_view(request):
            problem_text = "問題のテキスト\n次の行に続きます"
            processed_text = linebreaksbr(problem_text)
            context = {'processed_text': processed_text}
            return render(request, 'my_template.html', context)
        でいけるらしい？
        
        ->linebreaksbr | safe + innerHTMLでとりあえずOK

6/13
    引き続き作業だが、そもそもhtmlファイルがかったるすぎる説がある
        全体を作成しなくても、関数の中でだけforループを回せば済むのではないか？？
        明らかに作業の遅延に直結しているため、解消できるならしておきたいところ。
        -> for_display_new.htmlで試作
        
            疑問
            ・テンプレートタグを利用したループは2回取れるのか？
                仮に取れるのであれば、どのようにすればよいのか？
                    対応としては問題1問につき、linear_functionが3つ状態
                    よくわからんので、とりあえずぶん回してみる？


6/14
    htmlファイルについてはそこそこ順調に改装が進む
    
    一方で、forループについては、二度目が空っぽになっているご様子。イテレータ的動作？

6/15
    継続作業中
        テンプレートタグのforループに関しては、単純な記述間違いと発覚
        
        次は、残りの関数の描写と、点名の描写
            近すぎて若干見えづらい感じがある。
            →点の設定がどうにもうまく行っていない感じがある
                zero_coordinateを絞ってチェック
                    randomは0に近い値も出すんだから、そりゃねといった感じになる。
                    ある程度話すためには、間じゃなくて、以上の方を確保する必要がありそう

"""
from random import choice, randint, random
from typing import Dict, NamedTuple, Optional, Tuple, Union


# views側でフィルター生成
from django.template.defaultfilters import linebreaksbr
import sympy as sy


class AreaWithLinearFunction:
    """中学2年生用の、直線で囲まれた面積の問題と解答を出力
    
    Attributes:
        latex_answer (str): LaTeX形式を前提とした解答
        latex_problem (str): LaTeX形式を前提とした問題
    """
    class Point(NamedTuple):
        x: int
        y: int
        
    class LinearFunction(NamedTuple):
        """1次関数の通る点と式を格納

        Args:
            x1, y1, x2, y2 (str): 1次関数が通る2点
            linear_function_latex (str): latex形式で記述された1次関数の式
        """
        x1: str
        y1: str
        x2: str
        y2: str
        linear_function_latex: str
    
    def __init__(self, **settings: Dict):
        sy.init_printing(order='grevlex')
        selected_problem_type = choice(settings["problem_types"])
        if selected_problem_type == "one_side_on_axis":
            self.latex_answer, self.latex_problem, self.linear_function1, self.linear_function2, self.linear_function3 = self._make_one_side_on_axis_problem()
        elif selected_problem_type == "no_side_on_axis":
            self.latex_answer, self.latex_problem, self.linear_function1, self.linear_function2, self.linear_function3 = self._make_no_side_on_axis_problem()
    
    def _make_one_side_on_axis_problem(self):
        """3点のうち、2点が軸上にある問題、解答、描画用情報の作成
        
        Developing:
            returnはタプル絡みでもうちょっとスマートにできない？？(アンパッキング)
            def sample():
                numbers = (1, 2, 3)
                return numbers

            n1, n2, n3 = sample()
            で通る→そのまますっと返してもOK
            
            中で決めるなら、decide_linear_function_statuses()でok
            
            動作抜き出し
                x,y軸のいずれかに属する2点を決定。eg. (3, 0), (-2, 0) or (0, 1), (0, 4) (0<=x<=5, 0<=y<=5)
                それ以外(y=0ならy≠0, x=0ならx≠0)でもう一点を追加
                2/3点を選びつつ、でもない
                    軸にある奴1, 2と、軸にないやつでそれぞれ直線を生成
                3つの直線を決定(一つはx or y軸)
                軸上の2点を底辺にし（絶対値の座標差）、もう一点を高さとして扱う
                面積が出る
                問題文の出力
                    (1)直線◯◯を求めよ
                    (2)
                    ↑なんかふわふわ時間してる？？軸タイプは何を与えていたっけ？？？
                    ↑2つの直線を与えている。交点を求めさせる作業を
            
            どのようまとめ方が適切？？出来る限り分割するのが良さそうではあるけども
                point_decide -> 3 points (l1, 2)
                calculate_linear_function -> 3 linear_functions (l3, 4, 5)
                    一つはx,y軸的な感じちょっと表現に怪しみを感じる。(LaTex)周り
                calculate_area -> 1 area(l6)
                
            x or y軸の存在を考えると、LinearFunctionもそのままで良いかは若干微妙な可能性を感じる？
        
        """
        def make_three_points() -> Tuple[self.Point, self.Point, self.Point]:
            """3点のうち、いずれか2点が軸上に存在する点を作成する

            Returns:
                Tuple[self.Point, self.Point, self.Point]: 条件を満たす3点
            """
            # zero_coordinate = choice(["x", "y"])
            zero_coordinate = "x"
            if zero_coordinate == "x":
                x1 = 0
                y1 = self._random_integer(min_num=-3, max_num=3, removing_zero=False)
                x2 = 0
                y2 = y1 + self._random_integer(min_num=-4, max_num=4, removing_zero=True)
                x3 = self._random_integer(min_num=-6, max_num=6, removing_zero=True)
                y3 = self._random_integer(min_num=-6, max_num=6, removing_zero=False)
            elif zero_coordinate == "y":
                x1 = self._random_integer(min_num=-3, max_num=3, removing_zero=False)
                y1 = 0
                x2 = x1 + self._random_integer(min_num=-3, max_num=3, removing_zero=True)
                y2 = 0
                x3 = self._random_integer(min_num=-6, max_num=6, removing_zero=True)
                y3 = self._random_integer(min_num=-6, max_num=6, removing_zero=True)
            p1_on_axis = self.Point(x1, y1)
            p2_on_axis = self.Point(x2, y2)
            p3_not_on_axis = self.Point(x3, y3)
            return zero_coordinate, p1_on_axis, p2_on_axis, p3_not_on_axis
        
        zero_coordinate, p1_on_axis, p2_on_axis, p3_not_on_axis = make_three_points()
        linear_function_without_axis1 = self._calculate_linear_function_by_two_points(p1_on_axis, p3_not_on_axis)
        linear_function_without_axis2 = self._calculate_linear_function_by_two_points(p2_on_axis, p3_not_on_axis)
        line_in_parallel_with_y_axis = self._calculate_linear_function_by_two_points(p1_on_axis, p2_on_axis)
        area = self._calculate_area_by_three_points(p1_on_axis, p2_on_axis, p3_not_on_axis)
        latex_problem = f"図のように、2直線{linear_function_without_axis1.linear_function_latex}…①, {linear_function_without_axis2.linear_function_latex}…②が、"
        latex_problem += f"点Aで交わっている。\n"
        if zero_coordinate == "x":
            latex_problem += f"①とy軸の交点をB, ②とy軸の交点をCとするとき、"
        elif zero_coordinate == "y":
            latex_problem += f"①とx軸の交点をB, ②とx軸の交点をCとするとき、"
        triangle_ABC = self._latex_maker("\\triangle ABC")
        latex_problem += f"{triangle_ABC}の面積を求めよ。"
        latex_answer = f"area is {area}"
        return latex_answer, latex_problem, linear_function_without_axis1, linear_function_without_axis2, line_in_parallel_with_y_axis
    
    def _make_no_side_on_axis_problem(self):
        linear_function1 = self._decide_linear_function_status()
        linear_function2 = self._decide_linear_function_status()
        linear_function3 = self._decide_linear_function_status()
        latex_answer = "dummy answer"
        latex_problem = "dummy problem"
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
        
        Developing:
            6/8
                x1 = x2のときの挙動を変化
            
            6/12
                p1.x == p2.xのときの挙動に変化が必要
                
                
        """
        x = sy.Symbol("x", real=True)
        y = sy.Symbol("y", real=True)
        if p1.x == p2.x:
            line_in_parallel_with_y_axis = sy.Eq(x, p1.x)
            line_in_parallel_with_y_axis_latex = self._latex_maker(line_in_parallel_with_y_axis)
            linear_function = self.LinearFunction(
                x1 = str(p1.x), y1 = str(p1.y),
                x2 = str(p2.x), y2 = str(p2.y),
                linear_function_latex= line_in_parallel_with_y_axis_latex
            )
        else:
            a = sy.Rational(p2.y - p1.y, p2.x - p1.x)
            right = sy.simplify(a * (x - p1.x) + p1.y)
            linear_function_equation = sy.Eq(y, right)
            linear_function_latex = self._latex_maker(linear_function_equation)
            linear_function = self.LinearFunction(
                x1 = str(p1.x), y1 = str(p1.y),
                x2 = str(p2.x), y2 = str(p2.y),
                linear_function_latex = linear_function_latex
            )
        return linear_function

    def _calculate_area_by_three_points(self, p1: Point, p2: Point, p3: Point, /) -> Union[sy.Integer, sy.Rational]:
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
    
    def _latex_maker(self, formula: Union[sy.Equality, str]) -> str:
        """与えられた式をLaTex形式にカッコ込で変形する
        
        Args:
            formula (Union[sy.Equality, str]): y = 3x - 4や、y = 0などの公式
        
        Returns:
            latex (str): LaTex形式とカッコが複合された文字列
        """
        if isinstance(formula, str):
            latex = f"\( {formula} \)"
        else:
            latex = f"\( {sy.latex(formula)} \)"
        return latex
    
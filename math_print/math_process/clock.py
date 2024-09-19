"""
時刻の読み取りや、前後の時間を考えるための問題

9/11
    作成開始
    
    まずは何につけ、「与えられた時刻の文字列からブラウザ上にそれを使って描画を行う」やり方の確率から
        そもそも何を送るか？これまでだと、ループを展開して文字列を送り、それを数値に変換してから描画していた
        →このやり方自体は同じようにできそうだが、なんか別の方法があるような気がしなくもない
        とりあえず文字列で

    次は内部でのあれこれの描写
    from chatgpt
    
    from datetime import datetime, timedelta
    from typing import NamedTuple, Optional

    class TimeInformation(NamedTuple):
        hour: int
        minute: int
        is_pm: Optional[bool] = None  # 午前・午後の情報はオプションにする

        def to_datetime(self) -> datetime:
            if self.is_pm is None:
                # AM/PMが指定されていない場合、24時間制として扱う
                return datetime(year=1900, month=1, day=1, hour=self.hour, minute=self.minute)
            else:
                # AM/PMが指定されている場合、12時間制として扱う
                hour_24 = self.hour if not self.is_pm or self.hour == 12 else self.hour + 12
                if self.is_pm and self.hour == 12:
                    hour_24 = 12  # 午後12時はそのまま12
                elif not self.is_pm and self.hour == 12:
                    hour_24 = 0  # 午前12時は0時
                return datetime(year=1900, month=1, day=1, hour=hour_24, minute=self.minute)

        def add_minutes(self, minutes: int) -> 'TimeInformation':
            # 時間に指定された分数を追加して新しいTimeInformationを返す
            new_time = self.to_datetime() + timedelta(minutes=minutes)
            if self.is_pm is None:
                return TimeInformation(hour=new_time.hour, minute=new_time.minute)
            else:
                is_pm = new_time.hour >= 12
                return TimeInformation(
                    hour=new_time.hour % 12 if new_time.hour % 12 != 0 else 12,
                    minute=new_time.minute,
                    is_pm=is_pm
                )

        def subtract_minutes(self, minutes: int) -> 'TimeInformation':
            # 時間から指定された分数を引いて新しいTimeInformationを返す
            new_time = self.to_datetime() - timedelta(minutes=minutes)
            if self.is_pm is None:
                return TimeInformation(hour=new_time.hour, minute=new_time.minute)
            else:
                is_pm = new_time.hour >= 12
                return TimeInformation(
                    hour=new_time.hour % 12 if new_time.hour % 12 != 0 else 12,
                    minute=new_time.minute,
                    is_pm=is_pm
                )

        def difference_in_minutes(self, other: 'TimeInformation') -> int:
            # 別のTimeInformationとの時間差を分で返す
            delta = self.to_datetime() - other.to_datetime()
            return int(delta.total_seconds() // 60)

        def __str__(self) -> str:
            # 可読性のための文字列フォーマット
            if self.is_pm is None:
                # AM/PMの情報がない場合は24時間制で表示
                return f"{self.hour:02d}:{self.minute:02d}"
            else:
                period = "PM" if self.is_pm else "AM"
                return f"{self.hour:02d}:{self.minute:02d} {period}"

    # 使用例
    time1 = TimeInformation(8, 30)  # 24時間制の8:30
    time2 = time1.subtract_minutes(25)  # 25分前
    print(f"8時30分の25分前は: {time2}")  # 結果: 08:05

    time3 = TimeInformation(3, 30, is_pm=True)  # 午後3:30 (15:30)
    time4 = TimeInformation(5, 20, is_pm=True)  # 午後5:20 (17:20)
    diff = time3.difference_in_minutes(time4)  # 15:30から17:20までの時間差
    print(f"15時30分から17時20分までの時間は: {diff}分")  # 結果: 110分
    
9/13
    TimeInformationのカスタマイズ
from datetime import datetime, timedelta
from typing import NamedTuple, Optional

class TimeInformation(NamedTuple):
    hour: int
    minute: int
    am_or_pm: Optional[str] = None  # 'am', 'pm', または None (24時間制)

    def to_datetime(self) -> datetime:
        # TimeInformationをdatetimeオブジェクトに変換
        if self.am_or_pm is None:
            # AM/PMの指定がない場合は24時間制
            return datetime(year=1900, month=1, day=1, hour=self.hour, minute=self.minute)
        elif self.am_or_pm.lower() == "am":
            hour_24 = self.hour if self.hour != 12 else 0  # 午前12時は0時に変換
        elif self.am_or_pm.lower() == "pm":
            hour_24 = self.hour if self.hour == 12 else self.hour + 12  # 午後12時はそのまま12時
        else:
            raise ValueError("am_or_pmは'am'または'pm'のいずれか、またはNoneである必要があります")
        
        return datetime(year=1900, month=1, day=1, hour=hour_24, minute=self.minute)

    def add_minutes(self, minutes: int) -> 'TimeInformation':
        # 時間に指定された分数を追加して新しいTimeInformationを返す
        new_time = self.to_datetime() + timedelta(minutes=minutes)
        if self.am_or_pm is None:
            return TimeInformation(hour=new_time.hour, minute=new_time.minute)
        else:
            am_or_pm = "pm" if new_time.hour >= 12 else "am"
            hour_12 = new_time.hour % 12 or 12  # 0時は12時として扱う
            return TimeInformation(hour=hour_12, minute=new_time.minute, am_or_pm=am_or_pm)

    def subtract_minutes(self, minutes: int) -> 'TimeInformation':
        # 時間から指定された分数を引いて新しいTimeInformationを返す
        new_time = self.to_datetime() - timedelta(minutes=minutes)
        if self.am_or_pm is None:
            return TimeInformation(hour=new_time.hour, minute=new_time.minute)
        else:
            am_or_pm = "pm" if new_time.hour >= 12 else "am"
            hour_12 = new_time.hour % 12 or 12
            return TimeInformation(hour=hour_12, minute=new_time.minute, am_or_pm=am_or_pm)

    def difference_in_minutes(self, other: 'TimeInformation') -> int:
        # 別のTimeInformationとの時間差を分で返す
        delta = self.to_datetime() - other.to_datetime()
        return int(delta.total_seconds() // 60)

    def __str__(self) -> str:
        # 可読性のための文字列フォーマット
        if self.am_or_pm is None:
            # AM/PMの情報がない場合は24時間制で表示
            return f"{self.hour:02d}:{self.minute:02d}"
        elif self.am_or_pm == "am":
            return f"午前{self.hour:02d}:{self.minute:02d}"
        elif self.am_or_pm == "pm":
            return f"午後{self.hour:02d}:{self.minute:02d}"
        else:
            raise ValueError(f"am_or_pm must 'None', 'am' or 'pm'. {am_or_pm} is wrong.")

# 使用例
time1 = TimeInformation(8, 30, "am")  # 午前8:30
time2 = time1.subtract_minutes(25)  # 25分前
print(f"8時30分の25分前は: {time2}")  # 結果: 08:05 AM

time3 = TimeInformation(3, 30, "pm")  # 午後3:30 (15:30)
time4 = TimeInformation(5, 20, "pm")  # 午後5:20 (17:20)
diff = time3.difference_in_minutes(time4)  # 15:30から17:20までの時間差
print(f"15時30分から17時20分までの時間は: {diff}分")  # 結果: 110分

time5 = TimeInformation(18, 45)  # 24時間制の18:45
print(f"24時間制の時間は: {time5}")  # 結果: 18:45

9/17
問題の作成
    とりあえず、午前とか午後とかはなしで。あるいは全て24時間制で？
    余計な処理のことを考えると、とりあえずは全部午前扱いで良さそう
    
9/19
差分の取り方
"""
from random import choice, randint
from datetime import datetime, timedelta
from typing import NamedTuple, Optional


class TimeInformation(NamedTuple):
    hour: int
    minute: int
    am_or_pm: Optional[str] = None  # 'am', 'pm', または None (24時間制)

    def to_datetime(self) -> datetime:
        """指定された表示に応じて、datetimeオブジェクトを生成する
        
        Returns:
            (datetime): 指定された表示に応じたdatetimeオブジェクト
        """
        if self.am_or_pm is None:
            return datetime(year=1900, month=1, day=1, hour=self.hour, minute=self.minute)
        elif self.am_or_pm == "am":
            if self.hour != 12:
                hour_24 = self.hour
            else:
                hour_24 = 0
        elif self.am_or_pm == "pm":
            if self.hour == 12:
                hour_24 = self.hour
            else:
                hour_24 = self.hour + 12
        else:
            raise ValueError(f"'am_or_pm' must be 'am', 'pm' or None. {self.am_or_pm} is wrong.")
        return datetime(year=1900, month=1, day=1, hour=hour_24, minute=self.minute)

    def add_minutes(self, minutes: int) -> 'TimeInformation':
        """指定された分数を足して、新しいTimeInformationオブジェクトを返す
        
        Attributes:
            minutes(int): 増やしたい分数
        
        Returns:
            (TimeInformation): 元の表示形式を引き継ぎつつ、指定の分数が足された
        """
        new_time = self.to_datetime() + timedelta(minutes=minutes)
        if self.am_or_pm is None:
            return TimeInformation(hour=new_time.hour, minute=new_time.minute)
        else:
            if new_time.hour >= 12:
                am_or_pm = "pm"
            else:
                am_or_pm = "am"
            hour_12 = new_time.hour % 12 or 12  # 0時は12時として扱う
            return TimeInformation(hour=hour_12, minute=new_time.minute, am_or_pm=am_or_pm)

    def subtract_minutes(self, minutes: int) -> 'TimeInformation':
        # 時間から指定された分数を引いて新しいTimeInformationを返す
        new_time = self.to_datetime() - timedelta(minutes=minutes)
        if self.am_or_pm is None:
            return TimeInformation(hour=new_time.hour, minute=new_time.minute)
        else:
            am_or_pm = "pm" if new_time.hour >= 12 else "am"
            hour_12 = new_time.hour % 12 or 12
            return TimeInformation(hour=hour_12, minute=new_time.minute, am_or_pm=am_or_pm)

    def difference_in_minutes(self, other: 'TimeInformation') -> int:
        # 別のTimeInformationとの時間差を分で返す
        delta = self.to_datetime() - other.to_datetime()
        return int(delta.total_seconds() // 60)

    def __str__(self) -> str:
        # 可読性のための文字列フォーマット
        if self.am_or_pm is None:
            # AM/PMの情報がない場合は24時間制で表示
            if self.minute == 0:
                return f"{self.hour}時"
            return f"{self.hour}時{self.minute}分"
        elif self.am_or_pm == "am":
            if self.minute == 0:
                return f"午前{self.hour}時"
            return f"午前{self.hour}時{self.minute}分"
        elif self.am_or_pm == "pm":
            if self.minute == 0:
                return f"午後{self.hour時}"
            return f"午後{self.hour}時{self.minute}分"
        else:
            raise ValueError(f"am_or_pm must 'None', 'am' or 'pm'. {self.am_or_pm} is wrong.")

# 使用例
"""
time1 = TimeInformation(8, 30)  # 24時間制の8:30
time2 = time1.subtract_minutes(25)  # 25分前
print(f"8時30分の25分前は: {time2}")  # 結果: 08:05

time3 = TimeInformation(3, 30, is_pm=True)  # 午後3:30 (15:30)
time4 = TimeInformation(5, 20, is_pm=True)  # 午後5:20 (17:20)
diff = time3.difference_in_minutes(time4)  # 15:30から17:20までの時間差
print(f"15時30分から17時20分までの時間は: {diff}分")  # 結果: 110分
"""

class ClockProblem:
    """小学2年生用の時計関連の問題と解答を出力
    
    Attributes:
        answer (str): 日本語の記述を前提とした解答
        problem (str): 日本語の記述を前提とした問題
        time_information (TimeInformation): 描画用の時間と分の情報
    """
    
    def __init__(self, **settings):
        """
        初期設定
        
        settings (dict): 各種設定を格納。この問題ではどのタイプの問題か
        """
        selected_problem_type = choice(settings["problem_types"])
        if selected_problem_type == "read_time":
            self.show_canvas = True
            self.answer, self.problem, self.time_information = self._make_read_time_problem()
        elif selected_problem_type == "time_delta_without_am_pm":
            self.show_canvas = False
            self.answer, self.problem = self._make_time_delta_without_am_pm_problem()
    
    def _make_read_time_problem(self):
        """表示された時計の画像を見て、その時間を読み取る問題の作成
        
        Returns:
            answer (str): 解答
            problem (str): 問題
            time_information (TimeInformation): 
        
        Developing:
            すべて午前扱いで
        """
        hour = randint(1, 12)
        minute = randint(0, 59)
        time_information = TimeInformation(hour, minute)
        answer = str(time_information)
        problem = "時計は何時何分ですか?"
        return answer, problem, time_information

    def _make_time_delta_without_am_pm_problem(self):
        """午前午後の入れ替えを含まない時間の経過を問う問題と回答の作成
        
        Returns:
            answer (str): 解答
            problem (str): 問題
        
        Developing:
            午前午後を跨がないようなロジックを考える必要がある
            シンプルに、ある時間をはじめに設定して、そこから12時00分と0時00分を跨がないようにランダム値を決めれ場良さそう？

            t = TimeInformation(3, 30)
            delta_from_new_day  = t.difference_in_minutes(TimeInformation(0, 0))
            print(delta_from_new_day)
            print(divmod(delta_from_new_day, 60))
            delta_to_noon = TimeInformation(12, 0).difference_in_minutes(t)
            print(delta_to_noon)
            print(divmod(delta_to_noon, 60))
                        
            210
            (3, 30)
            510
            (8, 30)
        """
        hour = randint(0, 11)
        minute = randint(0, 59)
        before_time = TimeInformation(hour, minute)
        time_from_new_day =before_time.difference_in_minute()
        
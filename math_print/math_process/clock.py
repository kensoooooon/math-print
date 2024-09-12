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

"""
from random import choice, randint
from datetime import datetime, timedelta
from typing import NamedTuple, Optional


class TimeInformation(NamedTuple):
    hour: int
    minute: int
    is_pm: Optional[bool] = None  # 午前・午後の情報はオプションにする

    def to_datetime(self) -> datetime:
        # TimeInformationをdatetimeオブジェクトに変換
        if self.is_pm is None:
            # AM/PMが指定されていない場合、24時間制として扱う
            return datetime(year=1900, month=1, day=1, hour=self.hour, minute=self.minute)
        else:
            if (not(self.is_pm)) or (self.hour == 12):
                hour_24 = self.hour
            else:
                hour_24 = self.hour + 12
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

class ClockProblem:
    """小学2年生用の時計関連の問題と解答を出力
    
    Attributes:
        answer (str): 日本語の記述を前提とした解答
        problem (str): 日本語の記述を前提とした問題
        time_information (TimeInformation): 描画用の時間と分の情報
    """
    
    class TimeInformation(NamedTuple):
        hour: int
        minute: int
    
    def __init__(self, **settings):
        """
        初期設定
        
        settings (dict): 各種設定を格納。この問題ではどのタイプの問題か
        """
        selected_problem_type = choice(settings["problem_types"])
        if selected_problem_type == "read_time":
            self.answer, self.problem, self.time_information = self._make_read_time_problem()
            
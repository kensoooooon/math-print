
from random import choice, randint
from datetime import datetime, timedelta
from typing import NamedTuple, Optional


class TimeInformation(NamedTuple):
    """時刻の計算や表示の処理を請け負う
    
    Attributes:
        hour (int): 時
        minute (int): 分
        am_or_pm (Optional[str]): 午前午後の指定。無い場合は24時間の指定だとみなす
    """
    hour: int
    minute: int
    am_or_pm: Optional[str] = None  # 'am', 'pm', または None (24時間制)

    def to_datetime(self):
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
                hour_24 = 12
            else:
                hour_24 = (self.hour % 12) + 12
        else:
            raise ValueError(f"'am_or_pm' must be 'am', 'pm' or None. {self.am_or_pm} is wrong.")
        return datetime(year=1900, month=1, day=1, hour=hour_24, minute=self.minute)

    def add_minutes(self, minutes):
        """指定された分数を足して、新しいTimeInformationオブジェクトを返す
        
        Args:
            minutes(int): 増やしたい分数
        
        Returns:
            (TimeInformation): 元の表示形式を引き継ぎつつ、指定の分数が足されたTimeInformation
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

    def subtract_minutes(self, minutes):
        """時間から指定された分数を引いて新しいTimeInformationを返す
        
        Args:
            minutes(int): 引きたい分数
            
        Returns:
            (TimeInformation): 元の表示形式を引き継ぎつつ、指定の分数が引かれたTimeInformation
        """
        new_time = self.to_datetime() - timedelta(minutes=minutes)
        if self.am_or_pm is None:
            return TimeInformation(hour=new_time.hour, minute=new_time.minute)
        else:
            am_or_pm = "pm" if new_time.hour >= 12 else "am"
            hour_12 = new_time.hour % 12 or 12
            return TimeInformation(hour=hour_12, minute=new_time.minute, am_or_pm=am_or_pm)

    def difference_in_minutes(self, other):
        """別のTimeInformationとの時間差を分で返す
        
        Args:
            other (TimeInformation): 他のTimeInformation
        
        Returns:
            (int): 分数に変換された差
        """
        delta = self.to_datetime() - other.to_datetime()
        return int(delta.total_seconds() // 60)

    def __str__(self) -> str:
        """午前午後の指定も含めた文字列フォーマット
        
        Returns:
            (str): 問題や回答の表示に利用する文字列
        """
        if self.am_or_pm is None:
            # AM/PMの情報がない場合は24時間制で表示
            if self.minute == 0:
                return f"{self.hour}時"
            return f"{self.hour}時{self.minute}分"
        elif self.am_or_pm == "am":
            # AMの場合、0時は午前12時として扱う
            hour_12 = self.hour % 12 or 12
            if self.minute == 0:
                return f"午前{hour_12}時"
            return f"午前{hour_12}時{self.minute}分"
        elif self.am_or_pm == "pm":
            # PMの場合、12時をそのまま扱い、それ以外は12を超えないよう調整
            hour_12 = self.hour % 12 or 12
            if self.minute == 0:
                return f"午後{hour_12}時"
            return f"午後{hour_12}時{self.minute}分"
        else:
            raise ValueError(f"am_or_pm must be 'None', 'am' or 'pm'. {self.am_or_pm} is wrong.")


class ClockProblem:
    """小学2年生用の時計関連の問題と解答を出力
    
    Attributes:
        show_canvas (bool): キャンバスを用意するか否かの指定
        answer (str): 日本語の記述を前提とした解答
        problem (str): 日本語の記述を前提とした問題
        time_information (TimeInformation): 描画用の時間と分の情報
    """
    def __init__(self, **settings):
        """
        初期設定
        
        settings (dict): 各種設定を格納。この問題ではどのタイプの問題か
        """
        selected_width_of_time = choice(settings["widths_of_time"])
        selected_problem_type = choice(settings["problem_types"])
        self.selected_problem_type = selected_problem_type
        if selected_problem_type == "read_time":
            self.show_canvas = True
            self.answer, self.problem, self.time_information = self._make_read_time_problem()
        elif selected_problem_type == "time_delta_without_am_pm_with_picture":
            self.show_canvas = True
            self.answer, self.problem, self.time_information = self._make_time_delta_without_am_pm_problem(selected_width_of_time)
        elif selected_problem_type  == "time_delta_without_am_pm_without_picture":
            self.show_canvas = False
            self.answer, self.problem, _ = self._make_time_delta_without_am_pm_problem(selected_width_of_time)
        elif selected_problem_type == "time_delta_with_two_clock_pictures":
            self.show_canvas = True
            self.answer, self.problem, self.time_information1, self.time_information2 = self._make_time_delta_with_two_clock_pictures(selected_width_of_time)
        elif selected_problem_type == "time_delta_with_am_pm_with_picture":
            self.show_canvas = True
            self.answer, self.problem, self.time_information = self._make_time_delta_with_am_pm_problem(selected_width_of_time)
        elif selected_problem_type  == "time_delta_with_am_pm_without_picture":
            self.show_canvas = False
            self.answer, self.problem, _ = self._make_time_delta_with_am_pm_problem(selected_width_of_time)
        elif selected_problem_type == "time_delta_with_24_hours_with_picture":
            self.show_canvas = True
            self.answer, self.problem, self.time_information = self._make_time_delta_with_24_hours_problem(selected_width_of_time)
        elif selected_problem_type  == "time_delta_with_24_hours_without_picture":
            self.show_canvas = False
            self.answer, self.problem, _ = self._make_time_delta_with_24_hours_problem(selected_width_of_time)
        else:
            raise ValueError(f"'selected_problem_type' arg is {selected_problem_type}. This isn't expected value.")

    def _make_read_time_problem(self):
        """表示された時計の画像を見て、その時間を読み取る問題の作成
        
        Returns:
            answer (str): 解答
            problem (str): 問題
            time_information (TimeInformation): 
        """
        hour = randint(1, 12)
        minute = randint(0, 59)
        time_information = TimeInformation(hour, minute)
        answer = str(time_information)
        problem = "時計は何時何分ですか?"
        return answer, problem, time_information

    def _make_time_delta_without_am_pm_problem(self, width_of_time):
        """午前午後の入れ替えを含まない時間の経過を問う問題と回答の作成
        
        Args:
            width_of_time (str): 時間の幅(less_than_one_hour or greater_than_or_equal_to_one_hour)
        
        Returns:
            answer (str): 解答
            problem (str): 問題
            time (TimeInformation): 描画用の情報
        """
        def calculate_max_minutes(time, before_or_after):
            """ランダムな計算でも午前午後、および日付の変更を跨がないような時間と分を算出
            
            Args:
                time (TimeInformation): 基準となる時間の情報
                before_or_after (str): 遡る問題なのか、進む問題なのか
                
            Returns:
                word (str): 問題文の表示に利用する表現
                max_minutes (int): 日付や午前午後を跨がない最大の分数
            """
            # 遡るので、0時を跨がないように
            if before_or_after == "before":
                word = '前'
                minutes_from_new_day = time.difference_in_minutes(TimeInformation(0, 1))
                max_minutes = minutes_from_new_day
            # 進むので、12時を跨がないように
            elif before_or_after == "after":
                word = '後'
                minutes_to_noon = TimeInformation(11, 59).difference_in_minutes(time)
                max_minutes = minutes_to_noon
            else:
                raise ValueError(f"'before_or_after' must be 'before' or 'after'. {before_or_after} is wrong assignment.")
            return word, max_minutes
        
        def make_time_information_for_answer(time, delta_hour, delta_minute, before_or_after):
            """前後の選択と、時間と分数に応じて、答えのためのTimeInformationを作成
                
            Args:
                delta_hour (int): 経過した時間数
                delta_minute (int): 経過した分数
                before_or_after (str): 前と後のいずれか
            
            Returns:
                new_time (TimeInformation): 新しい時間
            """
            minutes = delta_hour * 60 + delta_minute
            if before_or_after == "before":
                new_time = time.subtract_minutes(minutes)
            elif before_or_after == "after":
                new_time = time.add_minutes(minutes)
            else:
                raise ValueError(f"'before_or_after' must be 'before' or 'after'. {before_or_after} is wrong assignment.")
            return new_time
    
        hour = randint(1, 11)
        minute = randint(0, 59)
        time = TimeInformation(hour, minute)
        before_or_after = choice(["before", "after"])
        word, max_minutes = calculate_max_minutes(time, before_or_after)
        if width_of_time == "less_than_one_hour":
            if max_minutes == 1:
                delta_minutes = 1
            elif max_minutes < 59:
                delta_minutes = randint(0, max_minutes)
            else:
                delta_minutes = randint(0, 59)
        elif width_of_time == "greater_than_or_equal_to_one_hour":
            delta_minutes = randint(0, max_minutes)
        else:
            raise ValueError(f"'width_of_time' must be 'less_than_one_hour' or 'greater_than_or_equal_to_one_hour'. {width_of_time} is wrong assignment.")
        delta_hour, delta_minute = divmod(delta_minutes, 60)
        problem = f"{time}の"
        if delta_hour != 0:
            problem += f"{delta_hour}時間"
        if delta_minute != 0:
            problem += f"{delta_minute}分"
        problem += f"{word}は何時何分ですか。"
        new_time = make_time_information_for_answer(time, delta_hour, delta_minute, before_or_after)
        answer = str(new_time)
        return answer, problem, time

    def _make_time_delta_with_two_clock_pictures(self, width_of_time):
        """2つの時計の絵から、経過時間(前後)を求める問題の作成
        
        Args:
            width_of_time (str): 時間の幅(less_than_one_hour or greater_than_or_equal_to_one_hour)
        
        Returns:
            answer (str): 解答
            problem (str): 問題
            time1 (TimeInformation): 基準となる時間の情報
            time2 (TimeInformation): 経過後の時間の情報
        """
        
        def calculate_minutes(time, before_or_after, width_of_time):
            """ランダムな計算でも午前午後、および日付の変更を跨がないような時間と分を算出
            
            Args:
                time (TimeInformation): 基準となる時間の情報
                before_or_after (str): 遡る問題なのか、進む問題なのか
                
            Returns:
                word (str): 問題文の表示に利用する表現
                max_minutes (int): 日付や午前午後を跨がない最大の分数
            """
            # 遡るので、0時を跨がないように
            if before_or_after == "before":
                word = '前'
                minutes_from_new_day = time.difference_in_minutes(TimeInformation(0, 1))
                max_minutes = minutes_from_new_day
            # 進むので、12時を跨がないように
            elif before_or_after == "after":
                word = '後'
                minutes_to_noon = TimeInformation(11, 59).difference_in_minutes(time)
                max_minutes = minutes_to_noon
            else:
                raise ValueError(f"'before_or_after' must be 'before' or 'after'. {before_or_after} is wrong assignment.")
            if width_of_time == "less_than_one_hour":
                if max_minutes < 59:
                    delta_minutes = randint(1, max_minutes)
                else:
                    delta_minutes = randint(1, 59)
            elif width_of_time == "greater_than_or_equal_to_one_hour":
                delta_minutes = randint(1, max_minutes)
            return word, delta_minutes

        def make_time_information_for_answer(time, delta_hour, delta_minute, before_or_after):
            """前後の選択と、時間と分数に応じて、答えのためのTimeInformationを作成
                
            Args:
                delta_hour (int): 経過した時間数
                delta_minute (int): 経過した分数
                before_or_after (str): 前と後のいずれか
            
            Returns:
                new_time (TimeInformation): 新しい時間
            """
            minutes = delta_hour * 60 + delta_minute
            if before_or_after == "before":
                new_time = time.subtract_minutes(minutes)
            elif before_or_after == "after":
                new_time = time.add_minutes(minutes)
            else:
                raise ValueError(f"'before_or_after' must be 'before' or 'after'. {before_or_after} is wrong assignment.")
            return new_time

        before_or_after = choice(['before', 'after'])
        hour1 = randint(1, 11)
        minute1 = randint(0, 59)
        time1 = TimeInformation(hour1, minute1)
        word, delta_minutes = calculate_minutes(time1, before_or_after, width_of_time)
        delta_hour, delta_minute = divmod(delta_minutes, 60)
        time2 = make_time_information_for_answer(time1, delta_hour, delta_minute, before_or_after)
        problem = f"右の時計は、左の時計のどれくらい{word}ですか。"
        answer = ""
        if delta_hour != 0:
            answer += f"{delta_hour}時間"
        if delta_minute != 0:
            answer += f"{delta_minute}分"
        answer += word
        return answer, problem, time1, time2

    def _make_time_delta_with_am_pm_problem(self, width_of_time):
        """午前午後の入れ替えを含む時間の経過を問う問題と回答の作成
        
        Args:
            width_of_time (str): 時間の幅(less_than_one_hour or greater_than_or_equal_to_one_hour)
        
        Returns:
            answer (str): 解答
            problem (str): 問題
            time (TimeInformation): 描画用の情報
        """
        def calculate_max_minutes(time, before_or_after):
            """ランダムな計算でも午前午後、および日付の変更を跨がないような時間と分を算出
            
            Args:
                time (TimeInformation): 基準となる時間の情報
                before_or_after (str): 遡る問題なのか、進む問題なのか
                
            Returns:
                word (str): 問題文の表示に利用する表現
                max_minutes (int): 日付や午前午後を跨がない最大の分数
            """
            # 遡るので、0時を跨がないように
            if before_or_after == "before":
                word = '前'
                minutes_from_new_day = time.difference_in_minutes(TimeInformation(0, 1, "am"))
                max_minutes = minutes_from_new_day
            # 進むので、24時を跨がないように
            elif before_or_after == "after":
                word = '後'
                minutes_to_noon = TimeInformation(11, 59, "pm").difference_in_minutes(time)
                max_minutes = minutes_to_noon
            else:
                raise ValueError(f"'before_or_after' must be 'before' or 'after'. {before_or_after} is wrong assignment.")
            return word, max_minutes
        
        def make_time_information_for_answer(time, delta_hour, delta_minute, before_or_after):
            """前後の選択と、時間と分数に応じて、答えのためのTimeInformationを作成
                
            Args:
                delta_hour (int): 経過した時間数
                delta_minute (int): 経過した分数
                before_or_after (str): 前と後のいずれか
            
            Returns:
                new_time (TimeInformation): 新しい時間
            """
            minutes = delta_hour * 60 + delta_minute
            if before_or_after == "before":
                new_time = time.subtract_minutes(minutes)
            elif before_or_after == "after":
                new_time = time.add_minutes(minutes)
            else:
                raise ValueError(f"'before_or_after' must be 'before' or 'after'. {before_or_after} is wrong assignment.")
            return new_time
    
        # am pm 
        am_or_pm = choice(["am", "pm"])
        hour = randint(1, 11)
        minute = randint(0, 59)
        time = TimeInformation(hour, minute, am_or_pm)
        before_or_after = choice(["before", "after"])
        word, max_minutes = calculate_max_minutes(time, before_or_after)
        if width_of_time == "less_than_one_hour":
            if max_minutes < 59:
                delta_minutes = randint(0, max_minutes)
            else:
                delta_minutes = randint(0, 59)
        elif width_of_time == "greater_than_or_equal_to_one_hour":
            delta_minutes = randint(0, max_minutes)
        else:
            raise ValueError(f"'width_of_time' must be 'less_than_one_hour' or 'greater_than_or_equal_to_one_hour'. {width_of_time} is wrong assignment.")
        delta_hour, delta_minute = divmod(delta_minutes, 60)
        problem = f"{time}の"
        if delta_hour != 0:
            problem += f"{delta_hour}時間"
        if delta_minute != 0:
            problem += f"{delta_minute}分"
        problem += f"{word}は何時何分ですか。"
        new_time = make_time_information_for_answer(time, delta_hour, delta_minute, before_or_after)
        answer = str(new_time)
        return answer, problem, time

    def _make_time_delta_with_24_hours_problem(self, width_of_time):
        """24時間制の経過を問う問題と回答の作成
        
        Args:
            width_of_time (str): 時間の幅(less_than_one_hour or greater_than_or_equal_to_one_hour)
        
        Returns:
            answer (str): 解答
            problem (str): 問題
            time (TimeInformation): 描画用の情報
        """
        def calculate_max_minutes(time, before_or_after):
            """ランダムな計算でも午前午後、および日付の変更を跨がないような時間と分を算出
            
            Args:
                time (TimeInformation): 基準となる時間の情報
                before_or_after (str): 遡る問題なのか、進む問題なのか
                
            Returns:
                word (str): 問題文の表示に利用する表現
                max_minutes (int): 日付や午前午後を跨がない最大の分数
            """
            # 遡るので、0時を跨がないように
            if before_or_after == "before":
                word = '前'
                minutes_from_new_day = time.difference_in_minutes(TimeInformation(0, 1))
                max_minutes = minutes_from_new_day
            # 進むので、24時を跨がないように
            elif before_or_after == "after":
                word = '後'
                minutes_to_noon = TimeInformation(23, 59).difference_in_minutes(time)
                max_minutes = minutes_to_noon
            else:
                raise ValueError(f"'before_or_after' must be 'before' or 'after'. {before_or_after} is wrong assignment.")
            return word, max_minutes
        
        def make_time_information_for_answer(time, delta_hour, delta_minute, before_or_after):
            """前後の選択と、時間と分数に応じて、答えのためのTimeInformationを作成
                
            Args:
                delta_hour (int): 経過した時間数
                delta_minute (int): 経過した分数
                before_or_after (str): 前と後のいずれか
            
            Returns:
                new_time (TimeInformation): 新しい時間
            """
            minutes = delta_hour * 60 + delta_minute
            if before_or_after == "before":
                new_time = time.subtract_minutes(minutes)
            elif before_or_after == "after":
                new_time = time.add_minutes(minutes)
            else:
                raise ValueError(f"'before_or_after' must be 'before' or 'after'. {before_or_after} is wrong assignment.")
            return new_time
    
        hour = randint(0, 23)
        minute = randint(0, 59)
        time = TimeInformation(hour, minute)
        before_or_after = choice(["before", "after"])
        word, max_minutes = calculate_max_minutes(time, before_or_after)
        if width_of_time == "less_than_one_hour":
            if max_minutes < 59:
                delta_minutes = randint(0, max_minutes)
            else:
                delta_minutes = randint(0, 59)
        elif width_of_time == "greater_than_or_equal_to_one_hour":
            delta_minutes = randint(0, max_minutes)
        else:
            raise ValueError(f"'width_of_time' must be 'less_than_one_hour' or 'greater_than_or_equal_to_one_hour'. {width_of_time} is wrong assignment.")
        delta_hour, delta_minute = divmod(delta_minutes, 60)
        problem = f"{time}の"
        if delta_hour != 0:
            problem += f"{delta_hour}時間"
        if delta_minute != 0:
            problem += f"{delta_minute}分"
        problem += f"{word}は何時何分ですか。"
        new_time = make_time_information_for_answer(time, delta_hour, delta_minute, before_or_after)
        answer = str(new_time)
        return answer, problem, time

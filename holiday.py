import datetime as dt


def isHoliday(day):
    date = dt.date(int(day[:4]), int(day[4:6]), int(day[6:]))
    dayofweek = date.strftime('%a')
    if dayofweek == "Sat" or dayofweek == "Sun":
        return True
    # 東証営業時間・休業日一覧
    # https://www.jpx.co.jp/corporate/about-jpx/calendar/index.html
    holidays = [20210101, 2021010, 20210103, 20210111, 20210211, 20210223, 20210320, 20210429,
                20210503, 20210504, 20210505, 20210722, 20210723,
                20210808, 20210809, 20210920, 20210923, 20211103,
                20211123, 20211231]
    if day in holidays:
        return True
    return False

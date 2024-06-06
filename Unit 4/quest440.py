def gen_secs():
    for sec in range(60):
        yield sec


def gen_minutes():
    for minute in range(60):
        yield minute


def gen_hours():
    for hour in range(24):
        yield hour


def gen_time():
    for hour in gen_hours():
        for minute in gen_minutes():
            for sec in gen_secs():
                yield "%02d:%02d:%02d" % (hour, minute, sec)


def gen_years(start=2019):
    year = start
    while True:
        yield year
        year += 1


def gen_months():
    for month in range(1, 13):
        yield month


def gen_days(month, leap_year=True):
    days_in_month = {
        1: 31, 2: 29 if leap_year else 28, 3: 31, 4: 30,
        5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
    }
    for day in range(1, days_in_month[month] + 1):
        yield day


def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            return False
        return True
    return False


def gen_date(start_year=2019):
    for year in gen_years(start_year):
        leap_year = is_leap_year(year)
        for month in gen_months():
            for day in gen_days(month, leap_year):
                for time in gen_time():
                    yield "%02d/%02d/%04d %s" % (day, month, year, time)


date_gen = gen_date()
for _ in range(10):  
    print(next(date_gen))

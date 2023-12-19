from datetime import datetime
import time

new = datetime.now()


def print_date(date):
    print(date.day)
    print(date.hour)
    print(date.minute)
    print(date.second)
    print(date.year)
    print(date.month)
    print(date.timestamp())


print_date(new)

year_2024 = datetime(2024, 1, 1, 3)
print(year_2024)


# # Reloj con fecha
# while True:
#     new = datetime.now()
#     print(new.date(), new.time())
#     time.sleep(1)


from datetime import time

current_time = time(21, 6, 0)
print(current_time)
print(current_time.hour)
print(current_time.minute)
print(current_time.second)

from datetime import date
current_date = date.today()

print(current_date.year)
print(current_date.month)
print(current_date.day)

current_date = date(2022, 10, 6)

print(current_date.year)
print(current_date.month)
print(current_date.day)


#operar con duferentes fechas timedelta

from datetime import timedelta

start_timedelta = timedelta(200, 100, 100, weeks=10)
end_timedelta = timedelta(300, 100, 100, weeks=13)
print(end_timedelta - start_timedelta)
print(end_timedelta + start_timedelta)

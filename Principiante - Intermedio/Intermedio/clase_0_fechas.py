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


print_date(new)

timestamp = new.timestamp()
print(timestamp)

# Reloj con fecha
while True:
    new = datetime.now()
    print(new.date(), new.time())
    time.sleep(1)

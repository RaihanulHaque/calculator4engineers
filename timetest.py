from random import randrange
import datetime
import time

dt = datetime.datetime.now()
# tdelta = datetime.timedelta(minutes=randrange(3, 9))

for i in range(0, 100, 1):
    tdelta = datetime.timedelta(minutes=randrange(3, 9))
    dt = dt + tdelta
    print(f"{dt.date()}T{dt.hour}:{dt.minute}:{dt.second}")
    time.sleep(2)


# print(randrange(3, 9))

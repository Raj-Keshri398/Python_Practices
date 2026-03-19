# ===================== Python datetime module =====================

import datetime
#print(dir(datetime))

#output: ['MAXYEAR', 'MINYEAR', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'date', 'datetime', 'datetime_CAPI', 'sys', 'time', 'timedelta', 'timezone', 'tzinfo']


# ========================== Getting datetime Information ==========================
'''
from datetime import datetime
now = datetime.now()
print(now)                      # 2026-03-18 07:34:46.549883
day = now.day                   # 18
month = now.month               # 3
year = now.year                 # 2026
hour = now.hour                 # 20
minute = now.minute             # 38
second = now.second
timestamp = now.timestamp()
print(day, month, year, hour, minute)
print('timestamp', timestamp)
print(f'{day}/{month}/{year}, {hour}:{minute}')  # 18/3/2026, 20:08

'''
# ========================== Formatting Date Output Using strftime ==========================

'''
from datetime import datetime
new_year = datetime(2026, 1, 1)
print(new_year)      # 2026-01-01 00:00:00
day = new_year.day
month = new_year.month
year = new_year.year
hour = new_year.hour
minute = new_year.minute
second = new_year.second
print(day, month, year, hour, minute) #1 1 2026 0 0
print(f'{day}/{month}/{year}, {hour}:{minute}')  # 1/1/2026, 0:0
'''



#====================================

'''
from datetime import datetime
# current date and time
now = datetime.now()
t = now.strftime("%H:%M:%S")
print("time:", t)           # time: 20:11:58
time_one = now.strftime("%m/%d/%Y, %H:%M:%S")
# mm/dd/YY H:M:S format
print("time one:", time_one)        # time one: 03/18/2026, 20:11:58
time_two = now.strftime("%d/%m/%Y, %H:%M:%S")
# dd/mm/YY H:M:S format
print("time two:", time_two)        # time two: 18/03/2026, 20:11:58
'''


# ==================================== String to Time Using strptime ====================================

'''
from datetime import datetime
date_string = "18 March, 2026"
print("date_string =", date_string)     # date_string = 18 March, 2026
date_object = datetime.strptime(date_string, "%d %B, %Y")
print("date_object =", date_object)     # date_object = 2026-03-18 00:00:00
'''

# ============================ Using date from datetime ===========================

'''
from datetime import date
d = date(2026, 1, 1)
print(d)        # 2026-01-01
print('Current date:', d.today())    # 2026-03-18
# date object of today's date
today = date.today()
print("Current year:", today.year)   # 2026
print("Current month:", today.month) # 3
print("Current day:", today.day)     # 18
'''

# ============================ Time Objects to Represent Time ===========================

'''
from datetime import time
# time(hour = 0, minute = 0, second = 0)
a = time()
print("a =", a)     # a = 00:00:00
# time(hour, minute and second)
b = time(10, 30, 50)
print("b =", b)     # b = 10:30:50
# time(hour, minute and second)
c = time(hour=10, minute=30, second=50)
print("c =", c)     # c = 10:30:50
# time(hour, minute, second, microsecond)
d = time(10, 30, 50, 200555)
print("d =", d)     # d = 10:30:50.200555
'''

# ============================ Difference Between Two Points in Time Using ===========================

'''
from datetime import date, datetime
today = date(year=2026, month=3, day=18)
new_year = date(year=2027, month=1, day=1)
time_left_for_newyear = new_year - today
# Time left for new year:  27 days, 0:00:00
print('Time left for new - year: ', time_left_for_newyear)  # Time left for new year:  289 days, 0:00:00

t1 = datetime(year = 2026, month = 3, day = 18, hour = 0, minute = 59, second = 0)
t2 = datetime(year = 2027, month = 1, day = 1, hour = 0, minute = 0, second = 0)
diff = t2 - t1
print('Time left for new year:', diff) # Time left for new year: 288 days, 23:01:00

'''

# ============================ Difference Between Two Points in Time Using timedelta ===========================

'''
from datetime import timedelta
t1 = timedelta(weeks=12, days=10, hours=4, seconds=20)
t2 = timedelta(days=7, hours=5, minutes=3, seconds=30)
t3 = t1 - t2
print("t3 =", t3)     # t3 = 86 days, 22:56:50
'''

#  ====================== Questions ======================

# 1. Get the current day, month, year, hour, minute and timestamp from datetime module

from datetime import datetime
now = datetime.now()
day = now.day # 18
month = now.month # 3
year = now.year # 2026
hour = now.hour # 20
minute = now.minute # 11    
timestamp = now.timestamp() # 1711071118.549883
print(day, month, year, hour, minute)
print('timestamp', timestamp)


# 2. Format the current date using this format: "%m/%d/%Y, %H:%M:%S")

from datetime import datetime
now = datetime.now()
time_one = now.strftime("%m/%d/%Y, %H:%M:%S")
print("time one:", time_one)        # time one: 03/18/2026, 20:11:58

# 3. Today is 18 March, 2026. Change this time string to time.

from datetime import datetime
date_string = '27 March, 2026'
date_object = datetime.strptime(date_string, "%d %B, %Y")
print("date_object =", date_object)     # date_object = 2026-03-18 00:00:00

# 4. Calculate the time difference between now and new year.

from datetime import date, datetime
today = date(year=2026, month=3, day=18)
new_year = date(year=2028, month=1, day=1)
time_left_for_newyeat = new_year - today
print('Time left for new - year: ', time_left_for_newyeat)  # Time left for new year:  289 days, 0:00:00

# 5. Calculate the time difference between 1 January 1970 and now.

from datetime import date, datetime
today = date(year=2026, month=3, day=18)
past_date = date(year=1970, month=1, day=1)
diff = today - past_date
print('Time difference between 1 January 1970 and now:', diff) # Time difference between 1 January 1970 and now:  20549 days, 0:00:00

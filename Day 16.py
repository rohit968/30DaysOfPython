# DAY 16: 30 Days of python programming

from datetime import datetime

# 1
date_time = datetime.now()
print('Year: ',date_time.year)
print('Month: ',date_time.month)
print('Day: ',date_time.day)
print('Hour: ',date_time.hour)
print('Minute: ',date_time.minute)
print('Second: ',date_time.second)

#2
time_strftime = date_time.strftime("%m/%d/%Y, %H:%M:%S")
print(time_strftime)

#3
date_string = "05 December, 2019"
date_string_to_time = datetime.strptime(date_string, "%d %B, %Y")
print(date_string_to_time)

#4
t1 = datetime(year = 2026, month = 4, day = 13, hour = 1, minute = 0, second = 0)
t2 = datetime(year = 2027, month = 1, day = 1, hour = 0, minute = 0, second = 0)
print('Time left for new year:', t2 - t1)

#5
date_user = datetime(year = 1970, month = 1, day = 1, hour = 0, minute = 0, second = 0)
date_now = datetime.now()
print('Time between the two dates: ', date_now - date_user)

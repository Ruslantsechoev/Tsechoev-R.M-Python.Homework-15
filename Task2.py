
from datetime import datetime

# Получение текущей даты и времени
date_time_now = datetime.now()
print(date_time_now)


# Форматирование даты и времени
string_date_time = datetime.strftime(date_time_now, "%Y-%m-%d  %H:%M:%S")
print(string_date_time)


# Получение дня недели
day_of_week = date_time_now.strftime("%A")
print(day_of_week)


# Получение номера недели
num_week = date_time_now.isocalendar()[1]
print(num_week)
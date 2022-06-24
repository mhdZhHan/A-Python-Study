# Timedelta
from datetime import date


date1 = date(2021,2,1)
date2 = date(2020,2,1)

delta = date1 - date2
print(delta)
print(type(delta))
print(delta.total_seconds())
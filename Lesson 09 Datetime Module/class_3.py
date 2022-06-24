# Construct Date & Time
import datetime


new_date = datetime.datetime(2018,2,1,10,5,56,476)
print(new_date)
print(type(new_date))
print("Year:", new_date.year)
print("Month:", new_date.month)
print("Day:", new_date.day)
print("Hour:",new_date.hour)
print("Minute:",new_date.minute)
print("Second:",new_date.second)
print("Microsecond:",new_date.microsecond)
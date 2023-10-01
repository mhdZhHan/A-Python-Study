# Datetime Strptime
from datetime import datetime


# time string to datetime object

date_string = "21 June, 2018"

date_object = datetime.strptime(date_string, "%d %B, %Y")

print(date_string)
print(type(date_string))
print(date_object)
print(type(date_object))
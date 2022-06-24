import datetime

# create a coustom date
my_date = datetime.date(2018,2,1)
print(my_date)
print(type(my_date))
print("Year:", my_date.year)
print("Month:", my_date.month)
print("Day:", my_date.day)

# create a coustom time
time = datetime.time(10,5,56,476)
print(type(time))
print("Hour:",time.hour)
print("Minute:",time.minute)
print("Second:",time.second)
print("Microsecond:",time.microsecond)

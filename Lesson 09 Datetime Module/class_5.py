# Datetime Strftime
from datetime import datetime


now = datetime.now()
print(now.strftime("%Y"))

# time
time = now.strftime("%H: %M: %S")
print(time)

# day
print(now.strftime("%d"))

# month 
print(now.strftime("%m"))

# abbreviated weekday name
print(now.strftime("%a"))

# full weekday name
print(now.strftime("%A"))

# abbreviated month name
print(now.strftime("%b"))

# full month name.
print(now.strftime("%B"))

# ====== more => google it

# ========= formates ==============
print("========= formates ==============")

print(now.strftime("%c"))
print(now.strftime("%x"))
print(now.strftime("%X"))

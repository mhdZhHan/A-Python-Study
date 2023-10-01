# Exception Handling

number = input("Enter a integer: ")

try:
    print(int(number))
except:
    print("Error ❌❌")
else:
    print("Success no errors 👍")
finally:
    print("Finally block")


# =========== multiple excepts ============

n = input("Enter a integer Number: ")

try:
    print(int(n))
except SyntaxError:
    print("SyntaxError ❌❌")
except ValueError:
    print("ValueError ❌❌")
except TypeError:
    print("TypeError ❌❌")
else:
    print("Success no errors 👍")
finally:
    print("Finally block")
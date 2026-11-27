# from hello import show
# print(show("Jonathan"))

# from hello import person1
# print(person1["age"])

# import platform
# x=platform.system()
# print(x)


n = 10
try:
    res = n / 0
except ZeroDivisionError:
    print("Can't be divided by zero!")
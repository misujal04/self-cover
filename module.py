# import math #from math import pi
# print(math.sqrt(25))
# print(math.factorial(5))
# print(math.ceil(0.01))
# print(math.floor(-4.9))
# print(math.pi)

# import random
# print(random.randint(0,10))
# print(random.random())
# seq=["rock","paper","scissor"]
# print(random.choice(seq))
# random.shuffle(seq)
# print(seq)


# import datetime
# print(datetime.datetime.now())
# print(datetime.timedelta(12.001, ))
# print(datetime.date.today())
# print(datetime.time(23,59))

# a=lambda d,b,c:d*b*c
# print(a(10,20,30))

# li=[10,20,30]
# print(list(map(lambda n:n*2,li)))


# def show(x):
#     return x%2==0

# li=[10,20,30]
# print(list(map(show,li)))


# li=[10,21,30]
# print(list(filter(lambda n:n%2==0,li)))


# def show(x):
#     return x%2==0

# li=[10,21,30]
# print(list(filter(show,li)))

from functools import reduce
li=[10,20,30]
# def show(a,b):
#     return a+b
# print(reduce(show,li,100)

print(reduce(lambda a,b:a+b,li,100))

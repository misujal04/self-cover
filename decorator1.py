def outer(func):
    def inner(*args):
        print("start")
        func(*args)
        print("end")
    return inner

# @outer
# def show(a,b):
#     print( a+b)
# show(2,4)
@outer
def facto(a):
    total = 1
    for i in range(1,a+1):
        total = total * i
    print(total)

facto(5)

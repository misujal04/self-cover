def decorate(n):
    def outer(func):
        def inner(*args,**krgs):
            for i in range(n):
                print("Attempt",i+1)
                res=func(*args,**krgs)
                print("res:",res)
            return res
        return inner
    return outer
@decorate(3)
def cake(num):
    return num*num
cake(5)